from django.contrib.admin import utils
from django.http import Http404
from django.template import loader
from rest_framework import status, viewsets
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes, renderer_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import mixins

from . import utils
from .models import Requests
from .serializers import RequestSerializer


class RequestViewSet(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,):
    """REST API definition for 'Requests'.
    
    This will be all http methods on the 'api/' route.
    """
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Requests.objects.all().order_by("id")
    serializer_class = RequestSerializer
    lookup_field = "id"
        

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
        return Response(status=status.HTTP_200_OK)


 
@api_view(['get'])
@renderer_classes([TemplateHTMLRenderer])
@authentication_classes([BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def index(request):
    """Return the index page on GET request to the main page."""
    Requests.objects.create(rtype="GET")

    latest_requests = Requests.objects.order_by("-time")[:10]

    context = {
        "latest_requests": latest_requests,
        "date": utils.get_date(),
        "cpuinfo": utils.get_cpuinfo(),
    }

    return Response(template_name="index.html", data=context )
