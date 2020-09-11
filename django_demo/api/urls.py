from django.urls import include, path

from rest_framework import routers


from .views import RequestViewSet

router = routers.DefaultRouter()
router.register(r"", RequestViewSet)


urlpatterns = [
    path("<id>/", include(router.urls)),
]
