from django.contrib import admin
from blog.models import Post, BlogComment

admin.site.register((BlogComment))
# Register your models here.
# admin.site.register((Post, BlogComment))



# This is Tiny Rich Text Editor ScriptInject

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)
        

