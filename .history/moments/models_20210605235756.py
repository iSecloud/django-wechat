from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WeChatUser(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    motto = models.CharField(max_length=100, null=True, blank=True)
    pic = models.CharField(max_length=50, null=True, blank=True)
    region = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Status(models.Model):
    user = models.ForeignKey(WeChatUser, models.CASCADE)
    text = models.CharField(max_length=280)
    pic = models.CharField(max_length=100, null=True, blank=True)
    pub_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
    class Meta:
        ordering = ['-id']

#定义回复和点赞的数据表
class Reply(models.Model):
    status = models.ForeignKey(Status, models.CASCADE)
    author = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=[("0", "like"), ("1", "comment")])
    text = models.CharField(max_length=300, null=True, blank=True) #允许空评论
    at_person = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        at_person_name = ""
        if self.at_person:
            at_person_name = "@{}".format(self.at_person)
        return "{}{} says {}".format(self.author, at_person_name, self.text)
