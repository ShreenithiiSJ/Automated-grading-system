#models

# gradingapp/models.py

from django.db import models

class GradingData(models.Model):
    Paper_id = models.IntegerField(primary_key=True)
    Paper_content = models.TextField()
    Marks_obtained = models.IntegerField()
    Automated_Marks = models.IntegerField()
    Correctly_Graded = models.BooleanField()