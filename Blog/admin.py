from django.contrib import admin
from Blog.models import *

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)

