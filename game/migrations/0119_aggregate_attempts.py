from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0118_dailyactivity_levelmetrics_clean_attempt"),
    ]

    def delete_attempts_with_invalid_score(apps, *args):
        Attempt = apps.get_model("game", "Attempt")

        Attempt.objects.filter(score__lt=0, score__gt=20).delete()

    FALSIFY_INVALID_BEST_ATTEMPTS_SQL = """
WITH ranked_attempts AS (
    SELECT
        id AS sub_id,
        ROW_NUMBER() OVER (
        PARTITION BY student_id, level_id 
        ORDER BY score DESC, start_time DESC
        ) AS rank
    FROM game_attempt
    WHERE is_best_attempt = TRUE
)
UPDATE game_attempt
SET is_best_attempt = 0
FROM ranked_attempts
WHERE id = ranked_attempts.sub_id
AND ranked_attempts.rank > 1;
"""

    ATTEMPT_COUNT_AND_TIME_PER_LEVEL_SQL = """
INSERT INTO game_levelmetrics (student_id, level_id, attempt_count, time_spent)
SELECT
   student_id,
   level_id,
   COUNT(*) AS attempt_count,
   SUM(UNIXEPOCH(finish_time) - UNIXEPOCH(start_time)) AS elapsed_time
FROM game_attempt
WHERE finish_time IS NOT NULL
GROUP BY student_id, level_id;
"""

    ATTEMPT_TOP_SCORE_PER_LEVEL_SQL = """
UPDATE game_levelmetrics
SET top_score = CAST(best_attempt.score AS INT64)
FROM (
    SELECT
        level_id AS sub_level_id,
        student_id AS sub_student_id,
        score
    FROM game_attempt
    WHERE finish_time IS NOT NULL
    AND start_time IS NOT NULL
    AND score IS NOT NULL
    AND score > 0
    AND is_best_attempt = TRUE
) AS best_attempt
WHERE level_id = best_attempt.sub_level_id
AND student_id = best_attempt.sub_student_id;    
"""

    ATTEMPT_COUNT_PER_DAY_SQL = """
SELECT
    DATE(finish_time),
    level_id,
    COUNT(*) AS attempts_per_day
FROM game_attempt
WHERE finish_time IS NOT NULL
GROUP BY DATE(finish_time), student_id, level_id
"""

    operations = [
        migrations.RunPython(
            code=delete_attempts_with_invalid_score,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.RunSQL(FALSIFY_INVALID_BEST_ATTEMPTS_SQL),
        migrations.RunSQL(ATTEMPT_COUNT_AND_TIME_PER_LEVEL_SQL),
        migrations.RunSQL(ATTEMPT_TOP_SCORE_PER_LEVEL_SQL),
        migrations.RunSQL(ATTEMPT_COUNT_PER_DAY_SQL),
    ]
