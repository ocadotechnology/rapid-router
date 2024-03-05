import datetime
import logging
import re

import pytz
from django.apps.registry import Apps
from django.db import migrations

LOGGER = logging.getLogger(__name__)


def add_missing_model_solutions(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    model_solutions = {
        "80": "[5]",
        "81": "[10]",
        "82": "[11]",
        "83": "[5]",
        "84": "[5]",
        "85": "[3]",
        "86": "[8]",
        "87": "[8]",
        "88": "[11]",
        "89": "[11]",
        "90": "[15]",
        "91": "[15]",
    }

    for level_name, model_solution in model_solutions.items():
        count = Level.objects.filter(
            default=True, episode__isnull=False, name=level_name
        ).update(model_solution=model_solution, disable_algorithm_score=False)
        assert count == 1

    Attempt = apps.get_model("game", "Attempt")

    attempts = Attempt.objects.filter(
        level__default=True,
        level__episode__isnull=False,
        level__name__in=[
            "80",
            "81",
            "82",
            "83",
            "84",
            "85",
            "86",
            "87",
            "88",
            "89",
            "90",
            "91",
        ],
        score=10,
        finish_time__gte=datetime.datetime(2023, 3, 1, 00, 00, tzinfo=pytz.UTC),
    ).select_related("level")

    LOGGER.info(f"Retrieved {attempts.count()} attempts.")

    processed_count = 0

    for attempt in attempts.iterator(chunk_size=1000):
        workspace = attempt.workspace

        # Get number of blocks from solution - 1 to discount Start block
        number_of_blocks = len(re.findall("<block", workspace)) - 1

        model_solution = model_solutions[attempt.level.name]

        ideal_number_of_blocks = int(
            model_solution.replace("[", "").replace("]", "")
        )

        if number_of_blocks == ideal_number_of_blocks:
            attempt.score = 20
        else:
            difference = abs(number_of_blocks - ideal_number_of_blocks)

            if difference < 10:
                attempt.score += 10 - difference

        attempt.save()

        processed_count += 1

        if processed_count % 1000 == 0:
            LOGGER.info(f"Processed {processed_count} attempts.")


def remove_new_model_solutions(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    Level.objects.filter(
        default=True,
        episode__isnull=False,
        name__in=[
            "80",
            "81",
            "82",
            "83",
            "84",
            "85",
            "86",
            "87",
            "88",
            "89",
            "90",
            "91",
        ],
    ).update(model_solution="[]", disable_algorithm_score=True)

    Attempt = apps.get_model("game", "Attempt")

    Attempt.objects.filter(
        level__default=True,
        level__episode__isnull=False,
        level__name__in=[
            "80",
            "81",
            "82",
            "83",
            "84",
            "85",
            "86",
            "87",
            "88",
            "89",
            "90",
            "91",
        ],
        score__gt=10,
        finish_time__gte=datetime.datetime(2023, 3, 1, 00, 00, tzinfo=pytz.UTC),
    ).select_related("level").update(score=10)


class Migration(migrations.Migration):
    dependencies = [("game", "0089_episodes_in_development")]
    operations = [
        migrations.RunPython(
            add_missing_model_solutions,
            reverse_code=remove_new_model_solutions,
        )
    ]
