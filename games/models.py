from django.db import models
from django.db import reverse
from django.utils.text import slugify


class Game(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(blank=True)
    img = models.CharField()
    slug = models.SlugField(blank=True, unique=True)
    genre = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        path_components = {'slug': self.slug}
        return reverse('wiki-details-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)


        return super(Game, self).save(*args, **kwargs)

