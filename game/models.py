import typing as t
from builtins import str

from common.models import Class, Student, UserProfile
from django.contrib.auth.models import User
from django.db import models
from django.db.models.query import QuerySet


def theme_choices():
    from game.theme import get_all_themes

    return [(theme.name, theme.name) for theme in get_all_themes()]


def character_choices():
    from game.character import get_all_character

    return [(character.name, character.name) for character in get_all_character()]


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


class LevelManager(models.Manager):
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


class Level(models.Model):
    after_worksheet: t.Optional["Worksheet"]

    name = models.CharField(max_length=100)
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
    shared_with = models.ManyToManyField(User, related_name="shared", blank=True)
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
    subtitle = models.TextField(max_length=100, blank=True, null=True)
    lesson = models.TextField(
        max_length=10000, default="Can you find the shortest route?"
    )
    hint = models.TextField(
        max_length=10000,
        default="Think back to earlier levels. What did you learn?",
    )
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
    objects = LevelManager()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~models.Q(
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


class LevelBlock(models.Model):
    type = models.ForeignKey(Block, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=None, null=True)


class LevelDecor(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    decor_name = models.CharField(max_length=100, default="tree1")


class Workspace(models.Model):
    name = models.CharField(max_length=200)
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


class Attempt(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    level = models.ForeignKey(Level, related_name="attempts", on_delete=models.CASCADE)
    student = models.ForeignKey(
        Student,
        related_name="attempts",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    finish_time = models.DateTimeField(null=True, blank=True)
    score = models.FloatField(default=0, null=True)
    workspace = models.TextField(default="")
    night_mode = models.BooleanField(default=False)
    python_workspace = models.TextField(default="")
    is_best_attempt = models.BooleanField(db_index=True, default=False)

    def elapsed_time(self):
        return self.finish_time - self.start_time


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
    slides_link = models.CharField(max_length=500, null=True, blank=True, default=None)
    student_worksheet_link = models.CharField(
        max_length=500, null=True, blank=True, default=None
    )
    indy_worksheet_link = models.CharField(
        max_length=500, null=True, blank=True, default=None
    )
    video_link = models.CharField(max_length=500, null=True, blank=True, default=None)
    locked_classes = models.ManyToManyField(
        Class, blank=True, related_name="locked_worksheets"
    )
