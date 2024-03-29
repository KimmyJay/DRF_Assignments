from django.contrib import admin
from User.models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    list_display = ('realname', 'username') # 사용자 목록에 보여질 필드 지정
    list_display_links = ('realname', 'username') # 상세 페이지 눌러서 들어갈 필드 지정
    list_filter = ('realname', 'username')
    search_fields = ('realname','username', )
    readonly_fields = ('join_date', )
    fieldsets = (
        ("info", {'fields': ('username', 'password', 'email', 'realname', 'join_date')}),
        ('permissions', {'fields': ('is_admin', 'is_active', )}),
    )
   
    filter_horizontal = []

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Dish)
admin.site.register(UserProfile)