from game.models import LevelMetrics


def create_level_metrics(student, level, score):
    level_metrics = LevelMetrics.objects.create(
        level=level, student=student, top_score=score
    )

    return level_metrics
