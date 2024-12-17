from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('Tenant', 'Tenant'),
        ('Landlord', 'Landlord'),
        ('Admin', 'Admin'),
        ('Super Admin', 'Super Admin'),
        ('Staff', 'Staff'),
        ('Agent', 'Agent'),
    ]
    
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Store hashed password
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    profile_picture = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
