from django.core.management import BaseCommand

from ..bot.run import SocialNetworkBot


class Command(BaseCommand):
    help = 'Object of this bot demonstrate functionalities of the system according to defined ​ rules. ' \
           'This bot should read rules from a config file (inany format chosen by the ​ candidate),' \
           '​ but should have following fields (all integers, candidate can rename as they see fit): \n' \
           '•number_of_users \n' \
           '•max_posts_per_user \n' \
           '•max_likes_per_user'

    def handle(self, *args, **options):
        try:
            social_network_bot = SocialNetworkBot()
            social_network_bot.run()
            self.stdout.write(
                self.style.SUCCESS('BOT FINISH HIS ACTIVITY! LET\'S GO CHECK IT AT http://localhost:8000/')
            )
        except Exception as e:
            print(e)
