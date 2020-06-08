import pytest
from mixer.backend.django import mixer

from workstation_app.models import Workstation, list_class_models

pytestmark = pytest.mark.django_db


@pytest.fixture(params=list_class_models)
def list_models_fixture(request):
    return request.param


class TestModels:

    def test_models(self, list_models_fixture):
        instance = mixer.blend(list_models_fixture)
        assert instance
        assert instance.pk
