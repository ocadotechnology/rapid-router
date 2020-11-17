import pytest
from common.models import Teacher
from common.tests.utils.teacher import signup_teacher_directly
from django.db.models.deletion import ProtectedError
from django.test import TestCase

from game.models import Level, Episode
from .utils.episode import create_episode
from .utils.level import create_save_level


class TestModels(TestCase):
    def test_level_next_level_on_delete(self):
        """
        Given two levels level1 and level2 where level2 is level1's next level,
        When level2 is deleted,
        Then level1's next_level field is set to null.
        """
        teacher_email, teacher_password = signup_teacher_directly()

        teacher = Teacher.objects.get(new_user__email=teacher_email)

        level1_id = create_save_level(teacher)
        level2_id = create_save_level(teacher)

        level1 = Level.objects.get(id=level1_id)
        level2 = Level.objects.get(id=level2_id)

        assert level1.next_level is None
        assert level2.next_level is None

        level1.next_level = level2
        level1.save()

        level2.delete()

        level1 = Level.objects.get(id=level1_id)

        assert level1.next_level is None

    def test_episode_next_episode_on_delete(self):
        """
        Given two episodes episode1 and episode2 where episode2 is episode1's next episode,
        When episode2 is deleted,
        Then episode1's next_episode field is set to null.
        """
        episode1_id = create_episode()
        episode2_id = create_episode()

        episode1 = Episode.objects.get(id=episode1_id)
        episode2 = Episode.objects.get(id=episode2_id)

        assert episode1.next_episode is None
        assert episode1.next_episode is None

        episode1.next_episode = episode2
        episode2.save()

        episode2.delete()

        episode1 = Episode.objects.get(id=episode1_id)

        assert episode1.next_episode is None

    def test_level_episode_on_delete(self):
        """
        Given a level and an episode where the level is in the episode,
        When anyone tries to delete the episode,
        Then a ProtectedError is raised and the episode isn't deleted.
        """
        teacher_email, teacher_password = signup_teacher_directly()
        teacher = Teacher.objects.get(new_user__email=teacher_email)

        level_id = create_save_level(teacher)
        level = Level.objects.get(id=level_id)

        episode_id = create_episode()
        episode = Episode.objects.get(id=episode_id)

        assert level.episode is None
        assert len(episode.levels) == 0

        level.episode = episode
        level.save()

        assert len(episode.levels) == 1

        with pytest.raises(ProtectedError):
            episode.delete()
