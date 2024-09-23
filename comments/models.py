from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User=get_user_model() 

#model for posting something with exclamation (reactiion) and image
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='posts/images/',null=True,blank=True)
    exclamation_text=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} "
    
    @property
    def posted(self):
        day_difference=(timezone.now()-self.created_at).days
        
        if day_difference<1:
            return "Today's Post"
        
        elif day_difference>=1 and day_difference <2:
            return "Yesterday's Post"
        
        else:
            return f"Posted {day_difference} days ago"
        
#Model for nested comments (threads)
class Thread(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='commenting_user')
    parent=models.ForeignKey("self",related_name='replies',on_delete=models.CASCADE,null=True,blank=True)
    comment=models.TextField()
    commented_at=models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.comment} on {self.post}"
    @property
    def comment_written_time(self):
        
            day_difference=(timezone.now()-self.commented_at).days
        
            if day_difference<1:
                return "Today's Commment"
        
            elif day_difference>=1 and day_difference <2:
                return "Yesterday's Comment"
        
            else:
                return f"Written {day_difference} days ago"
    
