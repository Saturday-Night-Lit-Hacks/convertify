from django.db import models

# Create your models here.
class UserInput(models.Model):
    article_url = models.URLField(max_length=250, null=True, blank=True)
    has_url = models.BooleanField(default=False)
    text = models.TextField(blank=True, null=True)

    # top freq_num of words
    freq_num = models.IntegerField(default=3)
    rand_video = models.BooleanField(default=False)
