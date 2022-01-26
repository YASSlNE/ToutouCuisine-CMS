from faker import Faker
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CMS.settings')
import django
django.setup()
from accounts.models import Clients

fake=Faker()
# c=Clients()
for i in range(1,50):
    name=fake.unique.name()
    phone=fake.unique.phone_number()
    email=fake.unique.email()
    c=Clients(name=name,phone=phone,profile_link=email)
    c.save()