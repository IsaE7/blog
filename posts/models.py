from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title


