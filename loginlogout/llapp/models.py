from django.db import models

# Create your models here.

# class User(models.Model):
#     username = models.CharField(max_length=30)
#     password = models.CharField(max_length=50)

#     def __str__(self):
#         return self.username
# Create your models here.

class Master(models.Model):
    mmusername = models.CharField(max_length=20)
    mmpassword = models.CharField(max_length=20)
    mmrole = models.CharField(max_length=20,default="")
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)

# class UserLogin(models.Model):
#     ticket_id = models.ForeignKey(Master,on_delete=models.CASCADE)
#     userusername = models.CharField(max_length=20,default="")
#     userpassword = models.CharField(max_length=20,default="")
#     userserverdetails = models.CharField(max_length=100)
#     usersenddate = models.DateTimeField('created at',auto_now_add=True)
#     userlicenseno = models.CharField(max_length=25)
#     userfile = models.FileField()
    
#     def __str__(self):
#         return self.userusername

# class AdminLogin(models.Model):
#     ticket_id = models.ForeignKey(Master,on_delete=models.CASCADE)
#     adminusername = models.CharField(max_length=20)
#     adminpassword = models.CharField(max_length=20)
    
#     def __str__(self):
#         return self.adminusername