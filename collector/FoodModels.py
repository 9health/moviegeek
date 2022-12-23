from django.db import models


class Log(models.Model):
    created = models.DateTimeField('date happened')
    user_id = models.CharField(max_length=16)
    content_id = models.CharField(max_length=16)
    event = models.CharField(max_length=200)
    session_id = models.CharField(max_length=128)
    id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    totaltime = models.BigIntegerField()
    ingrename = models.CharField(max_length=128)
    ingreid = models.BigIntegerField()
    totalliked = models.BigIntegerField()
    avgrating = models.BigIntegerField()
    detailurl = models.CharField(max_length=200)
    //"id"    "bigint"
    //"name"  "character varying"
    //"totaltime" "bigint"
    //"ingrename" "character varying"
    //"ingreid"   "bigint"
    //"totalliked"    "bigint"
    //"avgrating" "bigint"
    //"detailurl" "character varying"

    def __str__(self):
        return "user_id: {}, content_id: {}, event: {}".format(self.user_id,
                                                               str(self.content_id),
                                                               self.event)
