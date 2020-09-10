from django.urls import include, path

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"", views.RequestViewSet)

urlpatterns = [path(r"<id>/", include(router.urls))]
