from django.db import models

# create Movie model
class Movie(models.Model):
    title = models.CharField(max_length=250)
    released_date = models.DateField()
    production_company = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)    # When it was create
    updated_at = models.DateTimeField(auto_now=True)        # when it was update

    def __str__(self):
        return self.title
