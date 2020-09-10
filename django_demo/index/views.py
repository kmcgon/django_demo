from django.http import HttpResponse
from django.template import loader

from .models import Requests

from . import utils


def index(request):
    Requests.objects.create(rtype="GET")

    latest_requests = Requests.objects.order_by("-time")[:10]
    template = loader.get_template("index.html")
    context = {
        "latest_requests": latest_requests,
        "date": utils.get_date(),
        "cpuinfo": utils.get_cpuinfo(),
    }

    return HttpResponse(template.render(context, request))
