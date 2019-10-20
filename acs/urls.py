from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from views import AcsViewSet

router = DefaultRouter()
router.register(r'', AcsViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]