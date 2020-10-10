from django.db import models
from django.contrib.auth import models as mod
# Create your models here.


class blog(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(default=None, null=True, blank=True)
    body = models.TextField()
    day = models.DateField(auto_now_add=True, blank=True)
    owner = models.ForeignKey(mod.User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class breed(models.Model):
    predBreed = models.CharField(max_length=50)
    img= models.ImageField(default=None,null = True, blank=True)
    owner = models.ForeignKey(mod.User,on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.predBreed
