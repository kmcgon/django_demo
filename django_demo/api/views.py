from django.contrib.admin import utils
from django.http import Http404, HttpResponse
from django.template import loader

from rest_framework import viewsets
from rest_framework.viewsets import mixins
from rest_framework.response import Response
from rest_framework import status

from .serializers import RequestSerializer
from .models import Requests
from . import utils


class RequestViewSet(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Requests.objects.all().order_by("id")
    serializer_class = RequestSerializer
    http_method_names = ["post", "delete", "get"]

    def list(self, request, *args, **kwargs):
        Requests.objects.create(rtype="GET")

        latest_requests = self.queryset.order_by("-time")[:10]
        template = loader.get_template("index.html")
        context = {
            "latest_requests": latest_requests,
            "date": utils.get_date(),
            "cpuinfo": utils.get_cpuinfo(),
        }

        return HttpResponse(template.render(context, request))

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
