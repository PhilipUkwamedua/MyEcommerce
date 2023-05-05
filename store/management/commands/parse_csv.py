import csv
import os
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth.models import User
from store.models import *
from faker import Faker


class Command(BaseCommand):
    help = 'Import data from csv file'

    def handle(self, *args, **options):

        # drop all data from tables
        User.objects.all().delete()
        Product.objects.all().delete()
        Customer.objects.all().delete()
        Order.objects.all().delete()
        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/store/data/electronics_data.csv', newline='') as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)  # skip the header line
            number=100000
            num=1
            for row in reader:
                if len(row) < 7:
                    next(reader)
                elif row[2]=='' or row[4]=='' or row[5]=='' or row[6]=='': 
                    next(reader)
                else:
                    print(row)
                    product = Product.objects.create(
                        id = str(number),
                        name = row[4],
                        brand = row[5],
                        price = float(row[6]),   
                    )
                    product.save()

                    fake = Faker()

                    username=fake.name()+str(num)
                    num=num+1
                    email=fake.free_email()

                    user = User.objects.create_user(username=username,
                                                    email=email,
                                                    password='password')
                    user.is_active = True
                    user.save()

                    customer = user.customer
                    #     user=user,
                    # )
                    # customer.save()
                    for _ in range(1,4):
                        order = Order.objects.create(
                            transaction_id=str(number),
                            customer=customer,
                        )
                        number+=1
                        order.save()