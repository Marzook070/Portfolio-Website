from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Projects(models.Model):
    project_name = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to=f'images/',null=True, blank=True,default='images/default.jpg')
    description = RichTextField(blank=True, null=True ,default='Description of the project')
    website_link = models.URLField(default='https://www.google.com')

    def __str__(self):  
        return self.project_name    


