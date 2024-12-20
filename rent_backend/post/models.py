from django.db import models
from myaccount.models import User

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    address = models.TextField()
    image_url = models.URLField(null=True, blank=True)
    owner = models.ForeignKey(User, related_name="listings", on_delete=models.CASCADE)
    available_from = models.DateTimeField()
    available_to = models.DateTimeField()
    is_booked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
