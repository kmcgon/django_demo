from django.db import models


class RequestType(models.TextChoices):
    """Valid http request method choices for the rtype column of Requests.
    
    Most methods are missing because based on the functional requirments,
    GET will be the only valid value for the request method type.
    """
    GET = "GET"


class Requests(models.Model):
    """Model for the Requests table."""
    rtype = models.CharField(choices=RequestType.choices, max_length=7)
    time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(default=None, blank=True, null=True)

    def add_comment(self, data):
        self.comment = str(data)
