from django.contrib import admin
# import the class you created in models.py
from .models import Post

admin.site.register(Post)
# Register your models here.
