from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model): # the name of the database 
    user = models.ForeignKey(User,on_delete=models.CASCADE) # the rows in the database
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images',default='blank-profile-picture.png')
    location = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username
