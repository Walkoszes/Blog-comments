from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def add_comment(self, comment_text, author):
        return Comment.objects.create(post=self, text=comment_text, author=author)

class Comment(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"