from random import randint
from uuid import uuid4

from posts.models import Post, User
from social_network.settings import NUMBER_OF_USERS, MAX_POST_PER_USER, MAX_LIKES_PER_USER


class SocialNetworkBot:
    def __init__(self):
        self.number_of_users = NUMBER_OF_USERS
        self.max_post_per_user = MAX_POST_PER_USER
        self.max_likes_per_user = MAX_LIKES_PER_USER
        self.user_list = []
        self.post_list = []

    def create_users(self):
        for _ in range(self.number_of_users):
            user_obj = User()
            user_obj.username = str(uuid4())[:6]
            self.user_list.append(user_obj)
            User.save(user_obj)

    def create_posts(self):
        for user in self.user_list:
            for i in range(self.max_post_per_user):
                post_obj = Post()
                post_obj.title = f"{user.username} created {i} posts"
                post_obj.content = 'test test test'
                post_obj.author = user
                Post.save(post_obj)
                self.post_list.append(post_obj)

    def like_posts(self):
        for post in self.post_list:
            for user in self.user_list:
                for _ in range(randint(0, self.max_likes_per_user)):
                    post.like(user)

    def run(self):
        self.create_users()
        self.create_posts()
        self.like_posts()
