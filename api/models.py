from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from decouple import config

# Create your models here.

class Cake(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    discount=models.IntegerField()
    rating=models.FloatField()
    weight=models.FloatField()
    eggless=models.BooleanField()
    description=models.TextField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True,upload_to='cakes/')
    created_date=models.DateTimeField(null=True,blank=True)
    updated_date=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    cakeid=models.ForeignKey(Cake,on_delete=models.CASCADE)
    def __str__(self):
        return self.userid

class Orders(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    cakeid=models.ManyToManyField(Cake)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=255)    
    city=models.CharField(max_length=50)
    pincode=models.PositiveIntegerField()
    phone=models.BigIntegerField()
    orderdate= models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.name



@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    print(reset_password_token.user.email)
    email_plaintext_message = " copy this token------->token={}".format(reset_password_token.key)
    send_mail(
        # title:
        "Password Reset for {title}".format(title="udaycakeshop.herokuapp.com"),
        # message:
        email_plaintext_message,
        # from:        
        config('FROM_EMAIL'),
        # to:
        [reset_password_token.user.email])
