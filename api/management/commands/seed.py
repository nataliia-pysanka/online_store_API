from django.core.management.base import BaseCommand
from api.models import Product, Order
import json
from faker import Faker
from random import randint
from django.utils import timezone

fake = Faker()


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_products(self):
        """
        Seeding for Product model
        """
        with open('products.json', 'r') as file:
            dump = json.loads(file.read())
            for data in dump:
                title = data['title']
                price = float(data['price'])

                product = Product(title=title, price=price)
                product.save()

    def _create_orders(self):
        """
        Seeding for Order model
        """
        with open('products.json', 'r') as file:
            dump = json.loads(file.read())
            num = len(dump)
            for i in range(1000):
                date = fake.date_between(start_date='-5y')
                prod_num = randint(1, 15)
                query_prod = []
                for q in range(prod_num):
                    rand = randint(1, num)
                    query_prod.append(rand)
                order = Order(date=date)
                order.save()
                order.products.set(query_prod)
                order.save()

    def handle(self, *args, **options):
        self._create_products()
        self._create_orders()
