from django.contrib.auth.models import User
from django.db import models

MARKS_CHOICES = [
    ('like', 'Like'),
    ('dislike', 'Dislike'),
]


class Mark(models.Model):
    user = models.ForeignKey(User, related_name="marks", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", related_name="marks", on_delete=models.CASCADE)
    mark_type = models.CharField(max_length=10, choices=MARKS_CHOICES, default='like')


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users_liked = models.ManyToManyField(User, blank=True)

    @property
    def marks_count(self):
        return self.marks.count()

    @property
    def likes(self):
        return self.marks.filter(mark_type='like')

    @property
    def dislikes(self):
        return self.marks.filter(mark_type='dislike')

    def like(self, user):
        mark = Mark.objects.create(user=user, post=self, mark_type='like')
        mark.save()

    def dislike(self, user):
        mark = Mark.objects.create(user=user, post=self, mark_type='dislike')
        mark.save()
