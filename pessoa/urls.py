from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from pessoa.views import PessoaViewSet

router = DefaultRouter()
router.register(r'', PessoaViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]