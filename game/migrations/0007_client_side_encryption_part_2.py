from codeforlife.models.fields import EncryptedTextField, Sha256Field
from django.db import migrations
from django.db.models import CharField, CheckConstraint, Q, TextField

level_migrations = [
    # Name
    migrations.AlterField(
        model_name="level",
        name="_name_plain",
        field=CharField(
            max_length=100,
            db_column="name_plain",
        ),
    ),
    migrations.AlterField(
        model_name="level",
        name="_name_enc",
        field=EncryptedTextField(
            associated_data="name",
            verbose_name="name",
            db_column="name_enc",
            default=b"",
        ),
        preserve_default=False,
    ),
    migrations.AlterField(
        model_name="level",
        name="_name_hash",
        field=Sha256Field(
            editable=False,
            max_length=64,
            verbose_name="name hash",
            db_column="name_hash",
            default="",
        ),
        preserve_default=False,
    ),
    migrations.AddConstraint(
        model_name="level",
        constraint=CheckConstraint(
            condition=Q(
                Q(("_name_plain", ""), ("default", False)),
                Q(("_name_enc", b""), ("_name_hash", ""), ("default", True)),
                _connector="OR",
            ),
            name="level__name_is_plain_if_default_else_encrypted",
        ),
    ),
    # Subtitle
    migrations.AlterField(
        model_name="level",
        name="_subtitle_plain",
        field=TextField(
            max_length=100,
            blank=True,
            db_column="subtitle_plain",
        ),
    ),
    migrations.AlterField(
        model_name="level",
        name="_subtitle_enc",
        field=EncryptedTextField(
            associated_data="subtitle",
            verbose_name="subtitle",
            db_column="subtitle_enc",
            default=b"",
        ),
        preserve_default=False,
    ),
    migrations.AddConstraint(
        model_name="level",
        constraint=CheckConstraint(
            condition=Q(
                Q(("_subtitle_plain", ""), ("default", False)),
                Q(("_subtitle_enc", b""), ("default", True)),
                _connector="OR",
            ),
            name="level__subtitle_is_plain_if_default_else_encrypted",
        ),
    ),
    # Lesson
    migrations.AlterField(
        model_name="level",
        name="_lesson_plain",
        field=TextField(
            max_length=10000,
            db_column="lesson_plain",
        ),
    ),
    migrations.AlterField(
        model_name="level",
        name="_lesson_enc",
        field=EncryptedTextField(
            associated_data="lesson",
            verbose_name="lesson",
            db_column="lesson_enc",
            default=b"",
        ),
        preserve_default=False,
    ),
    migrations.AddConstraint(
        model_name="level",
        constraint=CheckConstraint(
            condition=Q(
                Q(("_lesson_plain", ""), ("default", False)),
                Q(("_lesson_enc", b""), ("default", True)),
                _connector="OR",
            ),
            name="level__lesson_is_plain_if_default_else_encrypted",
        ),
    ),
    # Hint
    migrations.AlterField(
        model_name="level",
        name="_hint_plain",
        field=TextField(
            max_length=10000,
            db_column="hint_plain",
        ),
    ),
    migrations.AlterField(
        model_name="level",
        name="_hint_enc",
        field=EncryptedTextField(
            associated_data="hint",
            verbose_name="hint",
            db_column="hint_enc",
            default=b"",
        ),
        preserve_default=False,
    ),
    migrations.AddConstraint(
        model_name="level",
        constraint=CheckConstraint(
            condition=Q(
                Q(("_hint_plain", ""), ("default", False)),
                Q(("_hint_enc", b""), ("default", True)),
                _connector="OR",
            ),
            name="level__hint_is_plain_if_default_else_encrypted",
        ),
    ),
]

workspace_migrations = [
    # Name
    migrations.RemoveField(
        model_name="workspace",
        name="_name_plain",
    ),
    migrations.AlterField(
        model_name="workspace",
        name="_name_enc",
        field=EncryptedTextField(
            associated_data="name",
            verbose_name="name",
            db_column="name_enc",
            default=b"",
        ),
        preserve_default=False,
    ),
]


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0006_client_side_encryption_part_1"),
        ("user", "0006_client_side_encryption_part_4"),
    ]

    operations = [
        *level_migrations,
        *workspace_migrations,
    ]
