from django.http import Http404

from rest_framework import viewsets
from rest_framework.viewsets import mixins
from rest_framework.response import Response
from rest_framework import status

from .serializers import RequestSerializer
from ..models import Requests


class RequestViewSet(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Requests.objects.all().order_by("id")
    serializer_class = RequestSerializer
    http_method_names = ["post", "delete", "get"]

    def create(self, request, *args, **kwargs):
        request_id = request.data.get("id")
        request_record = None

        if request_id:
            request_record = Requests.objects.filter(pk=request_id).first()
        if request_record:
            request_record.add_comment(request.data.get("comment"))
            request_record.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """Delete a Request table record.

        Override method from DestroyModelMixin, so that we can force a 200 status code on success,
        and 400 on failure.
        """
        try:
            instance = self.get_object()
        except Http404:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
