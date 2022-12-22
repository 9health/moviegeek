from django.db import models


class Log(models.Model):
    created = models.DateTimeField('date happened')
    user_id = models.CharField(max_length=16)
    content_id = models.CharField(max_length=16)
    event = models.CharField(max_length=200)
    session_id = models.CharField(max_length=128)
    id = models.BigIntegerField()
    Name = models.CharField(max_length=200)
    TotalTime = models.BigIntegerField()
    IngreName = models.CharField(max_length=200)
    IngreID = models.BigIntegerField()
    TotalLiked = models.BigIntegerField()
    AvgRating = models.BigIntegerField()
    DetailUrl = models.CharField(max_length=200)

    def __str__(self):
        return "user_id: {}, content_id: {}, event: {}".format(self.user_id,
                                                               str(self.content_id),
                                                               self.event)
