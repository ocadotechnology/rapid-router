from codeforlife.models.fields import (
    EncryptedTextField,
    Sha256Field,
)
from django.db import migrations

level_migrations = [
    # Name
    migrations.RemoveField(
        model_name="level",
        name="_name_plain",
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
    # Subtitle
    migrations.RemoveField(
        model_name="level",
        name="_subtitle_plain",
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
    # Lesson
    migrations.RemoveField(
        model_name="level",
        name="_lesson_plain",
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
    # Hint
    migrations.RemoveField(
        model_name="level",
        name="_hint_plain",
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
