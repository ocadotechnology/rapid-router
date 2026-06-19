from codeforlife.models.fields import EncryptedTextField, Sha256Field
from django.db import migrations

level_migrations = [
    # Name
    migrations.RenameField(
        model_name="level",
        old_name="name",
        new_name="_name_plain",
    ),
    migrations.AddField(
        model_name="level",
        name="_name_enc",
        field=EncryptedTextField(
            associated_data="name",
            null=True,
            verbose_name="name",
            db_column="name_enc",
        ),
    ),
    migrations.AddField(
        model_name="level",
        name="_name_hash",
        field=Sha256Field(
            null=True,
            editable=False,
            max_length=64,
            verbose_name="name hash",
            db_column="name_hash",
        ),
    ),
    # Subtitle
    migrations.RenameField(
        model_name="level",
        old_name="subtitle",
        new_name="_subtitle_plain",
    ),
    migrations.AddField(
        model_name="level",
        name="_subtitle_enc",
        field=EncryptedTextField(
            associated_data="subtitle",
            null=True,
            verbose_name="subtitle",
            db_column="subtitle_enc",
        ),
    ),
    # Lesson
    migrations.RenameField(
        model_name="level",
        old_name="lesson",
        new_name="_lesson_plain",
    ),
    migrations.AddField(
        model_name="level",
        name="_lesson_enc",
        field=EncryptedTextField(
            associated_data="lesson",
            null=True,
            verbose_name="lesson",
            db_column="lesson_enc",
        ),
    ),
    # Hint
    migrations.RenameField(
        model_name="level",
        old_name="hint",
        new_name="_hint_plain",
    ),
    migrations.AddField(
        model_name="level",
        name="_hint_enc",
        field=EncryptedTextField(
            associated_data="hint",
            null=True,
            verbose_name="hint",
            db_column="hint_enc",
        ),
    ),
]

workspace_migrations = [
    # Name
    migrations.RenameField(
        model_name="workspace",
        old_name="name",
        new_name="_name_plain",
    ),
    migrations.AddField(
        model_name="workspace",
        name="_name_enc",
        field=EncryptedTextField(
            associated_data="name",
            null=True,
            verbose_name="name",
            db_column="name_enc",
        ),
    ),
]


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0005_alter_dailyactivity_unique_together_and_more"),
        ("user", "0003_client_side_encryption_part_1"),
    ]

    operations = [
        *level_migrations,
        *workspace_migrations,
    ]
