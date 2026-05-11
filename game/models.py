import typing as t
from builtins import str

from codeforlife.models import EncryptedModel
from codeforlife.models.fields import EncryptedTextField, Sha256Field
from codeforlife.legacy.models import Class, Student, UserProfile
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()


def theme_choices():
    from game.theme import get_all_themes

    return [(theme.name, theme.name) for theme in get_all_themes()]


def character_choices():
    from game.character import get_all_character

    return [
        (character.name, character.name) for character in get_all_character()
    ]


class Block(models.Model):
    type = models.CharField(max_length=200)
    block_type = models.IntegerField(
        choices=[
            (0, "Start"),
            (1, "Action"),
            (2, "Condition"),
            (3, "Procedure"),
            (4, "ControlFlow"),
            (5, "Variable"),
            (6, "Math"),
        ]
    )

    def __str__(self):
        return self.type

    class Meta:
        ordering = ["block_type", "pk"]


class Episode(models.Model):
    """Variables prefixed with r_ signify they are parameters for random level generation"""

    worksheets: QuerySet["Worksheet"]

    name = models.CharField(max_length=200)
    next_episode = models.ForeignKey(
        "self", null=True, blank=True, default=None, on_delete=models.SET_NULL
    )
    in_development = models.BooleanField(default=False)

    r_random_levels_enabled = models.BooleanField(default=False)
    r_branchiness = models.FloatField(default=0, null=True)
    r_loopiness = models.FloatField(default=0, null=True)
    r_curviness = models.FloatField(default=0, null=True)
    r_num_tiles = models.IntegerField(default=5, null=True)
    r_blocks = models.ManyToManyField(Block, related_name="episodes")
    r_blockly_enabled = models.BooleanField(default=True)
    r_python_enabled = models.BooleanField(default=False)
    r_traffic_lights = models.BooleanField(default=False)
    r_cows = models.BooleanField(default=False)

    @property
    def first_level(self):
        return self.levels[0]

    @property
    def levels(self):
        """Sorts the levels by integer conversion of "name" which should equate to the correct play order"""

        return sorted(self.level_set.all(), key=lambda level: int(level.name))

    @property
    def difficulty(self):
        """
        Maps the Episode's id to a difficulty level, used later on to map to CSS classes and different background
        colours
        """
        difficulty_map = {
            1: "easy",
            2: "easy",
            3: "easy",
            4: "easy",
            5: "medium",
            6: "medium",
            7: "medium-hard",
            8: "medium-hard",
            9: "brainteasers",
            10: "early-python",
            11: "early-python",
            12: "late-python",
            13: "late-python",
            14: "late-python",
            15: "late-python",
            16: "early-python",
            17: "early-python",
            18: "early-python",
            19: "early-python",
            20: "late-python",
            21: "late-python",
            22: "late-python",
            23: "late-python",
            24: "late-python",
            25: "late-python",
            26: "late-python",
        }

        return difficulty_map.get(self.id, "easy")

    def __str__(self):
        return f"Episode: {self.name}"


class LevelManager(EncryptedModel.Manager["Level"]):
    def sorted_levels(self):
        # Sorts all the levels by integer conversion of "name" which should equate to the correct play order
        # Custom levels do not have an episode

        return sort_levels(
            self.model.objects.filter(episode__isnull=False).exclude(
                episode__name__icontains="coming soon"
            )
        )


def sort_levels(levels):
    return sorted(levels, key=lambda level: int(level.name))


class Level(EncryptedModel):
    associated_data = "level"
    field_aliases = {
        "name": {"_name_plain", "_name_enc", "_name_hash"},
        "subtitle": {"_subtitle_plain", "_subtitle_enc"},
        "lesson": {"_lesson_plain", "_lesson_enc"},
        "hint": {"_hint_plain", "_hint_enc"},
    }

    after_worksheet: t.Optional["Worksheet"]

    # --------------------------------------------------------------------------
    # Name
    # --------------------------------------------------------------------------

    _name_hash = Sha256Field(
        verbose_name=_("name hash"), db_column="name_hash", null=True
    )
    _name_plain = models.CharField(max_length=100)
    _name_enc = EncryptedTextField(
        associated_data="name",
        db_column="name_enc",
        null=True,
        verbose_name=_("name"),
    )

    @property
    def name(self):
        """The level's name."""
        if not self.default and self._name_enc is not None:
            return EncryptedTextField.get(self, "_name_enc")
        return self._name_plain

    @name.setter
    def name(self, value: str):
        """Set the level's name."""
        if self.default:
            self._name_plain = value
        else:
            self._name_plain = value  # TODO: remove when all are encrypted.
            EncryptedTextField.set(self, value, "_name_enc")
            Sha256Field.set(self, value, "_name_hash")

    # --------------------------------------------------------------------------

    episode = models.ForeignKey(
        Episode, blank=True, null=True, default=None, on_delete=models.PROTECT
    )
    path = models.TextField(max_length=10000)
    traffic_lights = models.TextField(max_length=10000, default="[]")
    cows = models.TextField(max_length=10000, default="[]")
    origin = models.CharField(max_length=50, default="[]")
    destinations = models.CharField(max_length=50, default="[[]]")
    default = models.BooleanField(default=False)
    owner = models.ForeignKey(
        UserProfile,
        related_name="levels",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    fuel_gauge = models.BooleanField(default=True)
    max_fuel = models.IntegerField(default=50)
    next_level = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name="prev_level",
    )
    shared_with = models.ManyToManyField(
        User, related_name="shared", blank=True
    )
    model_solution = models.CharField(blank=True, max_length=20, default="[]")
    disable_route_score = models.BooleanField(default=False)
    disable_algorithm_score = models.BooleanField(default=False)
    threads = models.IntegerField(blank=False, default=1)
    blockly_enabled = models.BooleanField(default=True)
    python_enabled = models.BooleanField(default=True)
    python_view_enabled = models.BooleanField(default=False)
    theme_name = models.CharField(
        max_length=10,
        choices=theme_choices(),
        blank=True,
        null=True,
        default=None,
    )
    character_name = models.CharField(
        max_length=20,
        choices=character_choices(),
        blank=True,
        null=True,
        default=None,
    )

    # --------------------------------------------------------------------------
    # Subtitle
    # --------------------------------------------------------------------------

    _subtitle_plain = models.TextField(max_length=100, blank=True, null=True)
    _subtitle_enc = EncryptedTextField(
        associated_data="subtitle",
        db_column="subtitle_enc",
        null=True,
        verbose_name=_("subtitle"),
    )

    @property
    def subtitle(self):
        """The level's subtitle."""
        if not self.default and self._subtitle_enc is not None:
            return EncryptedTextField.get(self, "_subtitle_enc")
        return self._subtitle_plain

    @subtitle.setter
    def subtitle(self, value: t.Optional[str]):
        """Set the level's subtitle."""
        if self.default:
            self._subtitle_plain = value
        else:
            self._subtitle_plain = value  # TODO: remove when all are encrypted.
            EncryptedTextField.set(self, value, "_subtitle_enc")

    # --------------------------------------------------------------------------
    # Lesson
    # --------------------------------------------------------------------------

    _lesson_plain = models.TextField(
        max_length=10000, default="Can you find the shortest route?"
    )
    _lesson_enc = EncryptedTextField(
        associated_data="lesson",
        db_column="lesson_enc",
        null=True,
        verbose_name=_("lesson"),
    )

    @property
    def lesson(self):
        """The level's description."""
        if not self.default and self._lesson_enc is not None:
            return EncryptedTextField.get(self, "_lesson_enc")
        return self._lesson_plain

    @lesson.setter
    def lesson(self, value: str):
        """Set the level's description."""
        if self.default:
            self._lesson_plain = value
        else:
            self._lesson_plain = value  # TODO: remove when all are encrypted.
            EncryptedTextField.set(self, value, "_lesson_enc")

    # --------------------------------------------------------------------------
    # Hint
    # --------------------------------------------------------------------------

    _hint_plain = models.TextField(
        max_length=10000,
        default="Think back to earlier levels. What did you learn?",
    )
    _hint_enc = EncryptedTextField(
        associated_data="hint",
        db_column="hint_enc",
        null=True,
        verbose_name=_("hint"),
    )

    @property
    def hint(self):
        """The level's hint."""
        if not self.default and self._hint_enc is not None:
            return EncryptedTextField.get(self, "_hint_enc")
        return self._hint_plain

    @hint.setter
    def hint(self, value: str):
        """Set the level's hint."""
        if self.default:
            self._hint_plain = value
        else:
            self._hint_plain = value  # TODO: remove when all are encrypted.
            EncryptedTextField.set(self, value, "_hint_enc")

    # --------------------------------------------------------------------------

    commands = models.TextField(
        max_length=10000,
        default='<div class="row">'
        + '<div class="large-4 columns">'
        + "<p><b>Movement</b>"
        + "<br>my_van.move_forwards()"
        + "<br>my_van.turn_around()"
        + "<br>my_van.turn_left()"
        + "<br>my_van.turn_right()"
        + "<br>my_van.wait()<p></div>"
        + '<div class="large-4 columns">'
        + "<p><b>Position</b>"
        + "<br>my_van.at_dead_end()"
        + "<br>my_van.at_destination()"
        + "<br>my_van.at_red_traffic_light()"
        + "<br>my_van.at_green_traffic_light()"
        + "<br>my_van.at_traffic_light(c)"
        + "<br><i>where c is 'RED' or 'GREEN'</i></p></div>"
        + '<div class="large-4 columns">'
        + "<p><br>my_van.is_road_right()"
        + "<br>my_van.is_road_left()"
        + "<br>my_van.is_road_forward()"
        + "<br>my_van.is_road(d)"
        + "<br><i>where d is 'FORWARD', 'LEFT', or 'RIGHT'</i></p></div>"
        + "</div>"
        + '<div class="row">'
        + '<div class="large-4 columns">'
        + "<p><b>Animals</b>"
        + "<br>my_van.is_animal_crossing()"
        + "<br>my_van.sound_horn()</div>"
        + "</div>",
    )
    anonymous = models.BooleanField(default=False)
    locked_for_class = models.ManyToManyField(
        Class, blank=True, related_name="locked_levels"
    )
    needs_approval = models.BooleanField(default=True)

    objects: LevelManager = LevelManager()

    class Meta:
        constraints = [
            # TODO: add these checks once all data is encrypted.
            # models.CheckConstraint(
            #     condition=~Q(
            #         default=True,
            #         _name_enc__isnull=False,
            #     ),
            #     name="level__default_name_is_not_encrypted",
            # ),
            # models.CheckConstraint(
            #     condition=~Q(
            #         default=True,
            #         _name_hash__isnull=False,
            #     ),
            #     name="level__default_name_is_not_hashed",
            # ),
            # models.CheckConstraint(
            #     condition=~Q(
            #         default=False,
            #         _name_plain__isnull=False,
            #     ),
            #     name="level__non_default_name_is_not_plain",
            # ),
            models.CheckConstraint(
                condition=~Q(
                    default=True,
                    needs_approval=True,
                ),
                name="level__default_does_not_need_approval",
            ),
        ]

    def __str__(self):
        return f"Level {self.name}"

    @property
    def theme(self):
        from game.theme import get_theme

        try:
            return get_theme(self.theme_name)
        except KeyError:
            return None

    @theme.setter
    def theme(self, val):
        from game.theme import get_theme_by_pk

        self.theme_name = get_theme_by_pk(val.pk).name

    @property
    def character(self):
        from game.character import get_character

        try:
            return get_character(self.character_name)
        except KeyError:
            return None

    @character.setter
    def character(self, val):
        from game.character import get_character_by_pk

        self.character_name = get_character_by_pk(val.pk).name

    @property
    def difficulty(self):
        return self.episode.difficulty if self.episode else "easy"

    @property
    def dek_aead(self):
        if self.owner is None:
            raise ValueError("Level must have an owner to access dek_aead.")

        return self.owner.user.dek_aead


class LevelBlock(models.Model):
    type = models.ForeignKey(Block, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=None, null=True)


class LevelDecor(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    decor_name = models.CharField(max_length=100, default="tree1")


class Workspace(EncryptedModel):
    associated_data = "workspace"
    field_aliases = {
        "name": {"_name_plain", "_name_enc"},
    }

    # --------------------------------------------------------------------------
    # Name
    # --------------------------------------------------------------------------

    _name_plain = models.CharField(max_length=200)
    _name_enc = EncryptedTextField(
        associated_data="name",
        db_column="name_enc",
        null=True,
        verbose_name=_("name"),
    )

    @property
    def name(self):
        """The level's name."""
        if self._name_enc is not None:
            return EncryptedTextField.get(self, "_name_enc")
        return self._name_plain

    @name.setter
    def name(self, value: str):
        """Set the level's name."""
        self._name_plain = value
        EncryptedTextField.set(self, value, "_name_enc")

    # --------------------------------------------------------------------------

    owner = models.ForeignKey(
        UserProfile,
        related_name="workspaces",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    contents = models.TextField(default="")
    python_contents = models.TextField(default="")
    blockly_enabled = models.BooleanField(default=False)
    python_enabled = models.BooleanField(default=False)
    python_view_enabled = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    @property
    def dek_aead(self):
        if self.owner is None:
            raise ValueError("Workspace must have an owner to access dek_aead.")

        return self.owner.user.dek_aead


class LevelMetrics(models.Model):
    time_spent = models.PositiveBigIntegerField(default=0)
    level = models.ForeignKey(
        Level, related_name="metrics", on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        Student,
        related_name="level_metrics",
        on_delete=models.CASCADE,
    )
    top_score = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(20)]
    )
    attempt_count = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("student", "level")
        verbose_name_plural = "Levels metrics"


class Worksheet(models.Model):
    episode = models.ForeignKey(
        Episode,
        blank=True,
        null=True,
        default=None,
        on_delete=models.PROTECT,
        related_name="worksheets",
    )
    before_level = models.OneToOneField(
        Level,
        blank=True,
        null=True,
        default=None,
        on_delete=models.PROTECT,
        related_name="after_worksheet",
    )
    lesson_plan_link = models.CharField(
        max_length=500, null=True, blank=True, default=None
    )
    slides_link = models.CharField(
        max_length=500, null=True, blank=True, default=None
    )
    student_worksheet_link = models.CharField(
        max_length=500, null=True, blank=True, default=None
    )
    indy_worksheet_link = models.CharField(
        max_length=500, null=True, blank=True, default=None
    )
    video_link = models.CharField(
        max_length=500, null=True, blank=True, default=None
    )
    locked_classes = models.ManyToManyField(
        Class, blank=True, related_name="locked_worksheets"
    )


class DailyActivity(models.Model):
    """
    A model to record attempt count per level per day.
    """

    date = models.DateField(default=timezone.now)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    count = models.PositiveBigIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["date", "level"],
                condition=~Q(level=None),
                name="unique_date_level_pair",
            )
        ]
        verbose_name_plural = "Daily activities"

    def __repr__(self):
        return f"On {self.date}, level {self.level} was played {self.count} time(s)."
