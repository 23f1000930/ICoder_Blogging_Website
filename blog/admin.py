from django.contrib import admin
from blog.models import Post,BlogComment
# Register your models here.

admin.site.register((BlogComment))

@admin.register(Post) #decorator , register as well as change in model

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)