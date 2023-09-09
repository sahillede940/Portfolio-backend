from django.db import models
import os


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="portfolio/projects/", blank=True, null=True)
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        # Remove the associated image file before deleting the book instance
        if self.image:
            # Get the file path of the image
            image_path = self.image.path

            # Check if the file exists, then delete it
            if os.path.exists(image_path):
                os.remove(image_path)

        super(Project, self).delete(*args, **kwargs)
    
    def delete_old_image(self):
        if self.pk:
            try:
                old_instance = Project.objects.get(pk=self.pk)
                if old_instance.image:
                    # Delete the old image file
                    old_image_path = old_instance.image.path
                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)
            except Project.DoesNotExist:
                pass

    def save(self, *args, **kwargs):
        self.delete_old_image()        
        super(Project, self).save(*args, **kwargs)


class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="portfolio/skills/", blank=True, null=True)
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        # Remove the associated image file before deleting the book instance
        if self.image:
            # Get the file path of the image
            image_path = self.image.path

            # Check if the file exists, then delete it
            if os.path.exists(image_path):
                os.remove(image_path)

        super(Skill, self).delete(*args, **kwargs)
    
    def delete_old_image(self):
        if self.pk:
            try:
                old_instance = Skill.objects.get(pk=self.pk)
                if old_instance.image:
                    # Delete the old image file
                    old_image_path = old_instance.image.path
                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)
            except Skill.DoesNotExist:
                pass

    def save(self, *args, **kwargs):
        self.delete_old_image()        
        super(Skill, self).save(*args, **kwargs)

