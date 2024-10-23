from django.urls import path

from javerly.apps import JaverlyConfig
from django.views.decorators.cache import cache_page
from javerly.views import JaverlyView

app_name = JaverlyConfig.name

urlpatterns = [
    path('', JaverlyView.as_view(), name='home'),
]
