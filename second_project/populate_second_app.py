import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()

import random
from second_app.models import AccessRecord, Webpage, Topic, User
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N = 5):

    for entry in range(N):
        #get the topic for the entry
        top = add_topic()

        ## create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        fake_FName = fakegen.first_name()
        fake_LName = fakegen.last_name()
        fake_Email = fakegen.email()
        # create the new webpage entry
        Webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]

        # create a fake access record for that Webpage
        acc_rec = AccessRecord.objects.get_or_create(name = Webpg, date = fake_date)[0]
        user = User.objects.get_or_create(FName = fake_FName, LName = fake_LName, Email = fake_Email)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating completely")
