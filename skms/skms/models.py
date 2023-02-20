from django.db import models

# Create your models here.

class Post(models.Model):
    #likes, comments, title, content, userUploaded, date, time, subject, subscriptions
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    subject = models.CharField(max_length=100)
    subscriptions = models.ManyToManyField('auth.User', related_name='subscribed_posts')
    comments = models.ManyToManyField('Comment', related_name='post_comments')
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} - {self.content}'
