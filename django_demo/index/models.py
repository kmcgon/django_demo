from django.db import models


class RequestType(models.TextChoices):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class Requests(models.Model):
    rtype = models.CharField(choices=RequestType.choices, max_length=7)
    time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(default=None, blank=True, null=True)

    def add_comment(self, data):
        self.comment = str(data)
