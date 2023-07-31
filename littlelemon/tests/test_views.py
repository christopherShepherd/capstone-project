from django.test import TestCase
from django.contrib.auth.models import User
from restaurant.models import Menu, Booking
from decimal import Decimal


class MenuViewTest(TestCase):

    def setUp(self):
        num_of_items = 5

        for i in range(num_of_items):
            Menu.objects.create(title=f'item{i}',
                                price=Decimal('1.00'),
                                inventory=10)
        
        # create test user
        test_user = User.objects.create_user(username='test_user', password='generic1')
        test_user.save()

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)
        item = dict(response.data[0])
        expected_item = Menu.objects.create(title='item0', price='1.00', inventory=10)
        self.assertEqual(item['title'], expected_item.title)
        self.assertEqual(item['price'], expected_item.price)
        self.assertEqual(item['inventory'], expected_item.inventory)

    def test_create(self):
        new_item = {"title":"test", "price":"1.00", "inventory":1}
        response = self.client.post('/restaurant/menu/', new_item, format='json')
        self.assertEqual(response.status_code, 401)

        login = self.client.post('/auth/token/login/', {"username":'test_user', "password":'generic1'})
        token =  login.data['auth_token']
        header = {"Authorization":"Token " + token}
        response2 = self.client.post('/restaurant/menu/', new_item, format='json', headers=header)
        self.assertEqual(response2.status_code, 201)


class BookingViewTest(TestCase):

    def setUp(self):
         # create test user
        test_user = User.objects.create_user(username='test_user', password='generic1')
        test_user.save()

        Booking.objects.create(name='user0', no_of_guests=3, booking_date='2024-01-01T12:00:00Z')

   
    def test_get_all(self):
        response = self.client.get('/restaurant/booking/tables/')
        self.assertEqual(response.status_code, 401)

        login = self.client.post('/auth/token/login/', {"username":'test_user', "password":'generic1'})
        token =  login.data['auth_token']
        header = {"Authorization":"Token " + token}
        response2 = self.client.get('/restaurant/booking/tables/', headers=header)
        self.assertEqual(response2.status_code, 200)
        booking = dict(response2.data[0])
        self.assertEqual(booking['name'], 'user0')

    def test_create(self):
        new_item = {"name":"testbooking", "no_of_guests":2, "booking_date":"2023-12-12T12:00:00Z"}
        response = self.client.post('/restaurant/booking/tables/', new_item, format='json')
        self.assertEqual(response.status_code, 401)

        login = self.client.post('/auth/token/login/', {"username":'test_user', "password":'generic1'})
        token =  login.data['auth_token']
        header = {"Authorization":"Token " + token}
        response2 = self.client.post('/restaurant/booking/tables/', new_item, format='json', headers=header)
        self.assertEqual(response2.status_code, 201)

    def test_retrieve_delete(self):
        test_book = Booking.objects.create(name='user1', no_of_guests=4, booking_date='2024-02-02T12:00:00Z')
        test_book.save()
        id = test_book.id
        login = self.client.post('/auth/token/login/', {"username":'test_user', "password":'generic1'})
        token =  login.data['auth_token']
        header = {"Authorization":"Token " + token}
        endpoint = f'/restaurant/booking/tables/{id}/'
        response = self.client.get(endpoint, headers=header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], id)
        removed = self.client.delete(endpoint, headers=header)
        self.assertEqual(removed.status_code, 204)
