from game.models import Attempt


def create_attempt(student, level, score):
    attempt = Attempt(level=level, student=student, score=score)
    attempt.save()

    return attempt
