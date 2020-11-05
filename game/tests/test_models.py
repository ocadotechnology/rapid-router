from django.apps import apps
from django.db import models
from django.test import TestCase


class TestModels(TestCase):
    def test_models_on_delete(self):
        game_models = apps.get_app_config("game").get_models()

        for model in game_models:
            remote_fields = self._get_model_remote_fields(model)

            for field in remote_fields:
                if (
                    model.__name__ == "Level"
                    and field.name == "next_level"
                    or model.__name__ == "Episode"
                    and field.name == "next_episode"
                ):
                    assert field.remote_field.on_delete == models.SET_NULL
                elif model.__name__ == "Level" and field.name == "episode":
                    assert field.remote_field.on_delete == models.PROTECT
                else:
                    assert field.remote_field.on_delete == models.CASCADE

    def _get_model_remote_fields(self, model):
        return [
            field
            for field in model._meta.get_fields()
            if isinstance(field, models.ForeignKey)
            or isinstance(field, models.OneToOneField)
        ]
