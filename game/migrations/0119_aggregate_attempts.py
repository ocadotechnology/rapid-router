from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0118_dailyactivity_levelmetrics_clean_attempt"),
    ]

    def delete_attempts_with_invalid_score(apps, *args):
        Attempt = apps.get_model("game", "Attempt")

        Attempt.objects.filter(score__lt=0, score__gt=20).delete()

    FALSIFY_INVALID_BEST_ATTEMPTS_SQL = """
UPDATE attempt
SET is_best_attempt = FALSE
FROM (
    SELECT *
    FROM attempt
    WHERE is_best_attempt = TRUE
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY student_id, level_id 
        ORDER BY score DESC, start_time DESC
    ) != 1
) AS invalid_attempt
WHERE attempt.id = invalid_attempt.id;
"""

    ATTEMPT_COUNT_AND_TIME_PER_LEVEL_SQL = """
INSERT INTO level_metrics (student_id, level_id, attempt_count, time_spent)
SELECT
   student_id,
   level_id,
   COUNT(*) as attempt_count,
   SUM(TIMESTAMP_DIFF(finish_time, start_time, SECOND)) AS elapsed_time,
FROM attempt
WHERE finish_time IS NOT NULL
GROUP BY student_id, level_id;
"""

    ATTEMPT_TOP_SCORE_PER_LEVEL_SQL = """
UPDATE level_metrics
SET top_score = CAST(best_attempt.score AS INT64)
FROM (
    SELECT *,
    FROM attempt
    WHERE finish_time IS NOT NULL
    AND start_time IS NOT NULL
    AND score IS NOT NULL
    AND score > 0
    AND is_best_attempt = TRUE
) AS best_attempt
WHERE level_metrics.level_id = best_attempt.level_id
AND level_metrics.student_id = best_attempt.student_id;    
"""

    ATTEMPT_COUNT_PER_DAY_SQL = """
SELECT
    DATE(finish_time),
    level_id,
    COUNT(*) AS attempts_per_day
FROM attempt
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
