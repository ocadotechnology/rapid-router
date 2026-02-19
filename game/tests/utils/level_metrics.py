from game.models import LevelMetrics


def create_level_metrics(student, level, score):
    level_metrics = LevelMetrics(level=level, student=student, top_score=score)
    level_metrics.save()

    return level_metrics
