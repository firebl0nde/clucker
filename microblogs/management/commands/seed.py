from django.core.management.base import BaseCommand, CommandError
from faker import Faker 
from microblogs.models import User

class Command ( BaseCommand ):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')


    def handle(self, *args, **options):
        print ("WARNING: the SEED command has not been implemented yet.")

        for _ in range(100):
            person = User.objects.create_user(
                    username = '@' + self.faker.profile( fields = ['username'])['username'], 
                    first_name = self.faker.first_name(),
                    last_name = self.faker.last_name(), 
                    email = self.faker.email(), 
                    password = self.faker.password(),
                    bio = self.faker.paragraph(nb_sentences = 2)
                    )

