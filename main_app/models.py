from django.db import models
from django.urls import reverse

# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.

class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id })

# Add new Feeding model below Finch model
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        # add the choices field
        choices = MEALS,
        # set a default value for the meal to be 'B'
        default = MEALS[0][0]
    )
    # add finch foreign key reference
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        # this method is coming from django
        # produced like this: get_<name_of_field>_display()
        return f"{self.get_meal_display()} on {self.date}"