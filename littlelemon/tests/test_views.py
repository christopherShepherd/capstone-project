from django.test import TestCase
from restaurant.models import Menu
from decimal import Decimal

class MenuViewTest(TestCase):

    def setUp(self):
        num_of_items = 5

        for i in range(num_of_items):
            Menu.objects.create(title=f'item{i}',
                                price=Decimal('1.00'),
                                inventory=10)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)
        item = dict(response.data[0])
        expected_item = Menu.objects.create(title='item0', price='1.00', inventory=10)
        self.assertEqual(item['title'], expected_item.title)
        self.assertEqual(item['price'], expected_item.price)
        self.assertEqual(item['inventory'], expected_item.inventory)



