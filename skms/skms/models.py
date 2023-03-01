from django.db import models

class UserAccount(models.Model):
    

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices= (('Active','Active'), ('Inactive','Inactive')), default='Active')
    type = models.CharField(max_length=255, choices= (('User','User'), ('Expert','Expert')), default='User')
    userimage = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.username

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

class Report(models.Model):
    reporter_comments = models.TextField()
    reporter_name = models.CharField(max_length=300, choices= (('Current User','Current User'), ('Anonymous','Anonymous')), default='Anonymous')
    report_date = models.DateTimeField(auto_now_add=True)
    contact_preference = models.CharField(max_length = 3, choices= (('N','No'), ('Y','Yes')), default='N')
    report_anonymously = models.CharField(max_length = 3, choices= (('N','No'), ('Y','Yes')), default='Y')
    submitter = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.reporter_comments

class Voice(models.Model):
    voice_comments = models.TextField()
    voice_user = models.CharField(max_length=300, choices= (('Current User','Current User'), ('Anonymous','Anonymous')), default='Anonymous')
    voice_date = models.DateTimeField(auto_now_add=True)
    contact_preference = models.CharField(max_length = 3, choices= (('N','No'), ('Y','Yes')), default='N')
    voice_anonymously = models.CharField(max_length = 3, choices= (('N','No'), ('Y','Yes')), default='Y')
    submitter = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.voice_comments