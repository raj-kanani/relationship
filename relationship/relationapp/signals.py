from .models import Page
from django.db.models.signals import post_delete
from django.dispatch import receiver

# @receiver(post_delete, sender=page)
# def delete_user(sender, instance, **kwargs):
#     print("page post delete.........")
#     instance.user.delete()