from django.urls import include, path
from rest_framework import routers

from .views import RequestViewSet, index

# views for the 'list' route for api. Ex: GET - http://localhost:8000/api
list_views = RequestViewSet.as_view({'get': 'list'})
# view for the 'detail' routes. Ex: POST - http://localhost:8000/api/4
detail_views = RequestViewSet.as_view({'get': 'retrieve', "delete": "destroy", "post": 'partial_update'})

urlpatterns = [
    path("", index),
    path("api/", list_views),
    path("api/<id>/", detail_views),
]
