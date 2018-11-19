from django.db import models

# Create your models here.


class BucketList(models.Model):
    """ This class represnts the bucketlist model """
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ returns a human readable representation of the model """
        return "{}".format(self.name)
