from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Skill(models.Model):
    name = models.CharField(max_length=100)
    bonus = models.TextField()

    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="skills",
    )


class Guild(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="players",
    )

    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        related_name="players",
    )
