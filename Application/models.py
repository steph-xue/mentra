from django.contrib.auth.models import AbstractUser
from django.db import models

# Model for user database (username, email, password)
class User(AbstractUser):
    pass

# Model for category of responses given by AI
class Category(models.Model):
    category_name = models.CharField(max_length=30, default="")
    category_description = models.CharField(max_length=1000, default="")
    icon_url = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.category_name

# Model for 
class JournalLog(models.Model):
    input = models.CharField(max_length=1000)
    output = models.CharField(max_length=3000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="log_category")
    date_time = models.DateTimeField()

    def __str__(self):
        return self.input
