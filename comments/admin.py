from django.contrib import admin
from .models import Post, Thread 

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=["user","name","image","exclamation_text","created_at","posted"]
    
@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display=["user","post","comment","parent","comment_written_time"]