from django.contrib import admin
from User.models import *

admin.site.register(CustomUser)
admin.site.register(Dish)
admin.site.register(UserProfile)