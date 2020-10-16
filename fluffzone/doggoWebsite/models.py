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

class adoptPost(models.Model):
    ADOPTION_CHOICES = (
    ('yes','YES'),
    ('no', 'NO'),
    )

    name = models.CharField(max_length=50, blank = False)
    breedName = models.CharField(max_length=50, blank = True, null = True)
    img = models.ImageField(default=None, null=True, blank=True)
    health = models.CharField(max_length=50, blank = True, null = True)
    gender = models.CharField(max_length=50, blank = True, null = True)
    ageYears = models.IntegerField()
    location = models.CharField(max_length=50, blank=False)
    addr = models.TextField(blank=False)
    phone = models.CharField(max_length=15, blank=False, unique=True)
    upForAdoption = models.CharField(max_length=6, choices=ADOPTION_CHOICES, default='yes')
    details = models.TextField()

    def __str__(self):
        return self.name + " the " + self.breedName


