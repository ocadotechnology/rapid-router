from game.models import Episode


def create_episode():
    episode = Episode()
    episode.name = "Test Episode"
    episode.save()

    return episode.id
