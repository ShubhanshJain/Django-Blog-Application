from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.post = Post.objects.create(title="Test Post", content="Content", author=self.user)

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.author.username, "testuser")

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.post = Post.objects.create(title="Test Post", content="Content", author=self.user)
        self.comment = Comment.objects.create(post=self.post, author=self.user, text="Nice post!")

    def test_comment_creation(self):
        self.assertEqual(self.comment.text, "Nice post!")
        self.assertEqual(self.comment.post.title, "Test Post")
