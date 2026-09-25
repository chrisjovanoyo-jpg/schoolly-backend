from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)

    university = models.ForeignKey(
        "Academic.University",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    program = models.ForeignKey(
        "Academic.Program",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username
    



class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s profile"