from django.db import models



# title, description, and technology_used
class Project(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    technology_used = models.CharField(max_length=250)
    project_image = models.ImageField(null=True)
    
    
    def __str__(self):
        return self.title