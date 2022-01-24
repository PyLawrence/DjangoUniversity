from django.db import models


class djangoClasses(models.Model):
    title = models.CharField(max_length=50)
    # make unique course number so there is no confusion, even if the pks are the same
    courseNumber = models.IntegerField(unique=True)
    instructorName = models.CharField(max_length=60)
    duration = models.DecimalField(max_digits=10, decimal_places=2)

    # this is defined by default, but this allows us to select the name when referring to this
    classes = models.Manager()

    # instead of getting some code, we get a readable name
    def __str__(self):
        return self.title

