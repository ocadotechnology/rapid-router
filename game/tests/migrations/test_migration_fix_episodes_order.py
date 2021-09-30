import pytest


@pytest.mark.django_db
def test_episodes_renamed_properly(migrator):
    old_state = migrator.apply_initial_migration(("game", "0067_level_score_27"))
    new_state = migrator.apply_tested_migration(
        ("game", "0069_remove_user_levels_from_episodes")
    )

    Episode = new_state.apps.get_model("game", "Episode")
    episode7 = Episode.objects.get(id=7)
    episode8 = Episode.objects.get(id=8)

    assert episode7.name == "Limited Blocks"
    assert episode8.name == "Procedures"


@pytest.mark.django_db
def test_episodes_reordered_properly(migrator):
    old_state = migrator.apply_initial_migration(("game", "0067_level_score_27"))
    new_state = migrator.apply_tested_migration(
        ("game", "0069_remove_user_levels_from_episodes")
    )

    Episode = new_state.apps.get_model("game", "Episode")
    episode6 = Episode.objects.get(id=6)
    episode7 = Episode.objects.get(id=7)
    episode8 = Episode.objects.get(id=8)
    episode9 = Episode.objects.get(id=9)

    assert episode7.next_episode == episode8
    assert episode8.next_episode == episode9
    assert episode6.next_episode == episode7
