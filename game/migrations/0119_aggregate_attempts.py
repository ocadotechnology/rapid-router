from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0118_dailyactivity_levelmetrics_clean_attempt"),
    ]

    def delete_attempts_with_invalid_score(apps, *args):
        Attempt = apps.get_model("game", "Attempt")

        Attempt.objects.filter(models.Q(score__lt=0) | models.Q(score__gt=20)).delete()

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
SET is_best_attempt = FALSE
FROM ranked_attempts
WHERE id = ranked_attempts.sub_id
AND ranked_attempts.rank > 1;
"""

    ATTEMPT_COUNT_AND_TIME_PER_LEVEL_SQL = """
INSERT INTO game_levelmetrics (student_id, level_id, attempt_count, time_spent, top_score)
SELECT
    student_id,
    level_id,
    COUNT(*) AS attempt_count,
    SUM(EXTRACT(EPOCH FROM finish_time) - EXTRACT(EPOCH FROM start_time)) AS elapsed_time,
    0 AS top_score
FROM game_attempt
WHERE finish_time IS NOT NULL
GROUP BY student_id, level_id;
"""

    DELETE_LEVEL_METRICS_SQL = """
DELETE FROM game_levelmetrics
WHERE TRUE;
"""

    ATTEMPT_TOP_SCORE_PER_LEVEL_SQL = """
UPDATE game_levelmetrics
SET top_score = CAST(best_attempt.score AS BIGINT)
FROM (
    SELECT
        level_id AS sub_level_id,
        student_id AS sub_student_id,
        score
    FROM game_attempt
    WHERE finish_time IS NOT NULL
    AND start_time IS NOT NULL
    AND score IS NOT NULL
    AND is_best_attempt = TRUE
) AS best_attempt
WHERE level_id = best_attempt.sub_level_id
AND student_id = best_attempt.sub_student_id;    
"""

    ATTEMPT_COUNT_PER_DAY_SQL = """
INSERT INTO game_dailyactivity (date, level_id, count)
SELECT
    DATE(finish_time),
    level_id,
    COUNT(*) AS count
FROM game_attempt
WHERE finish_time IS NOT NULL
GROUP BY DATE(finish_time), level_id
"""

    DELETE_DAILY_ACTIVITY_SQL = """
DELETE FROM game_dailyactivity
WHERE TRUE;
"""

    operations = [
        migrations.RunPython(
            code=delete_attempts_with_invalid_score,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.RunSQL(sql=FALSIFY_INVALID_BEST_ATTEMPTS_SQL, reverse_sql=migrations.RunSQL.noop),
        migrations.RunSQL(sql=ATTEMPT_COUNT_AND_TIME_PER_LEVEL_SQL, reverse_sql=DELETE_LEVEL_METRICS_SQL),
        migrations.RunSQL(sql=ATTEMPT_TOP_SCORE_PER_LEVEL_SQL, reverse_sql=migrations.RunSQL.noop),
        migrations.RunSQL(sql=ATTEMPT_COUNT_PER_DAY_SQL, reverse_sql=DELETE_DAILY_ACTIVITY_SQL),
    ]
