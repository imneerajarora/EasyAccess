# Create your models heref
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# class category(models.Model):
#     name = models.CharField( max_length=50)

#     def __str__(self):
#         return self.name
class HomeData(models.Model):
    image = models.ImageField(upload_to='home-page/',height_field=None,width_field=None,max_length=None)


class category(models.Model):
    name = models.CharField( max_length=50)
    slug = models.SlugField(unique=True,blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class documentation(models.Model):
    icon = models.ImageField( upload_to='images-Ai/', height_field=None, width_field=None, max_length=None)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    link = models.URLField( max_length=200)
    slug = models.SlugField(unique=True,blank=True,null=True)
    category = models.ForeignKey('category',on_delete=models.CASCADE,related_name='documentations',blank=True,null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(documentation, self).save(*args, **kwargs)
    # category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='doCategory',blank=None,null=None)

    def __str__(self):
        return self.title
    

class AITool(models.Model):
    icon = models.ImageField( upload_to='AITOol-images/', height_field=None, width_field=None, max_length=None)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    link = models.URLField( max_length=200)
    slug = models.SlugField(unique=True,blank=True,null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(AITool, self).save(*args, **kwargs)


    def __str__(self):
        return self.title


class history(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title_name = models.CharField( max_length=50,null=True)
    title_link = models.URLField( max_length=500,null=True)
    accessed_at = models.DateTimeField( auto_now_add=True)


    def __str__(self):
        return f"{self.user.username}-{self.title_name} at {self.accessed_at}"


   
        
class DataFeedback(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.feedback_text} by {self.user_name} ({self.created_at})"


    


    







