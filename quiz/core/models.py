from django.db import models

class Response(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    user_name = models.CharField(max_length=100)
    favorite_game = models.CharField(max_length=50)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name}'s response"
