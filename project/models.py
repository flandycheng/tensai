from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

@python_2_unicode_compatible
class Project(models.Model):
    PROJECT_TYPES = (
        ('P','Product'),
        ('C','Consult'),
    )
    project_id = models.CharField(max_length=30,primary_key=True)
    project_name = models.CharField(max_length=30)
    project_type = models.CharField(max_length=1,choices=PROJECT_TYPES)
    owner = models.IntegerField()
    update_date = models.DateField()
    create_date = models.DateField()

    def __str__(self):
        return ("%s:%s" % (self.project_id, self.project_name))
