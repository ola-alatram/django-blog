from audioop import reverse
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category (models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.category}"
    

class Blog (models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(default="", null=False, db_index=True)
    content = models.TextField()
    image = models.ImageField(upload_to="images")
    category = models.ManyToManyField(Category, related_name="blogs", blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
    
    def save (self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog-page", kwargs={"pk": self.pk})


