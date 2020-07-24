from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField(max_length = 100, blank = False, null = False,help_text = "Email")
    first_name = models.CharField(max_length = 100, blank = False, null = False,help_text = "First Name")
    last_name = models.CharField(max_length = 100, blank = False, null = False,help_text = "Last Name")

    def __str__(self):
        return str(self.first_name +" " + self.last_name)

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"