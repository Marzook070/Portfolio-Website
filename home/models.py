from django.db import models

# Create your models here.
class Projects(models.Model):
    project_name = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to=f'images/',null=True, blank=True)
    description = models.TextField(default='Description of the project')
    website_link = models.URLField(default='#')

    def __str__(self):  
        return self.project_name    


