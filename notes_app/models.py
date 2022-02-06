from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    date_posted = models.DateField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title