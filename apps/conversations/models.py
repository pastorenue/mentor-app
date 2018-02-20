from django.db import models


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sending_user')
    receiver = models.ForeignKey(User, related_name='receiving_user')
    subject = models.CharField(max_length=100, null=True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s-->%s".format(self.sender,self.receiver)

    class Meta:
        ordering = ("-date_created",)