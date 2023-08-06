from django.db import models

# Create your models here.

class CreateTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
       abstract = True

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    def __str__(self):
        return self.title
    class Meta: 
        verbose_name_plural = "Categories" 


class Post(CreateTime):
    ACTIVE = 'active'
    DRAFT='Draft'
    CHOISES=(
        (ACTIVE,'Active'),(DRAFT,'Draft')
        )

    title = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=CHOISES, default=ACTIVE)
    slug =  models.SlugField(max_length=255)
    intro = models.TextField()
    body =models.TextField()
    image= models.ImageField(upload_to='uploads/', blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='posts')
   

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        

class Comment(CreateTime):

    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.name
    


    
