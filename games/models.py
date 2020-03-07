from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User


# class GamesList(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gamelist", null=True)
#     name = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.name

class Game(models.Model):

    title = models.CharField(max_length=100)
    price = models.IntegerField(blank=True)
    img = models.CharField(max_length=1000)
    slug = models.CharField(max_length=10, blank=True, editable=False)
    

    # def get_absolute_url(self):
    #     path_components = {'slug': self.slug}
    #     return reverse('game-detail-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)


        return super(Game, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

