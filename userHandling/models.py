from django.db import models
from django.contrib.auth.models import User



#Create model for user profile and what fields will be associated with the user.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)


    #Other aspects of user profile (user profile page and profile pic)

    profile_pic = models.ImageField(upload_to='profile_pics', blank='True')
    #Beaches Visited
    #Reviews
    #Pictures


    def __str__(self):
        return self.user.username
