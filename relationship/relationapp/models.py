from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# one to one relationship
class Page(models.Model):
    # user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff': True})
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    page_name = models.CharField(max_length=40)
    page_cat = models.CharField(max_length=80)
    date = models.DateField()

class Like(Page):
    page = models.OneToOneField(Page, on_delete=models.CASCADE, primary_key=True, parent_link=True)
    likes = models.IntegerField()


# many to one relationship
class Post(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User,  related_name='user', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=150)
    cat = models.CharField(max_length=150)
    date = models.DateField()

# many to many relationship..
class Song(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=150)
    duration = models.IntegerField()
##### show admin panel in singer name and multiple name
    def written(self):
        return ", ".join([str(p) for p in self.user.all()])