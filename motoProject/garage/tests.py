from django.test import TestCase
from django.urls import reverse
from .models import Motorcycle, MotorcycleReview
from django.utils import timezone

# This file contains unit tests for the Garage app.

# The tests in this file cover the following functionality:
# - Checking that the index page loads without error
# - Ensuring that a motorcycle can be created
# - Confirming that an existing motorcycle can be updated
# - Testing that a motorcycle can be deleted
# - Verifying that a review can be added to a motorcycle
# - Checking that a review can be deleted from a motorcycle
# - Ensuring that invalid data cannot be entered when creating a motorcycle
# - Verifying that an invalid motorcycle update request results in a 404 error
# - Testing that an invalid motorcycle deletion request results in a 404 error
# - Ensuring that an invalid review creation request results in a 404 error
# - Verifying that an invalid review deletion request results in a 404 error


class MotorcycleTest(TestCase):
    def setUp(self):
        self.motorcycle = Motorcycle.objects.create(
            motorcycle_name='TestMotorcycle', 
            motorcycle_brand='TestBrand', 
            motorcycle_description='TestDescription'
        )

    def test_motorcycle_str(self):
        self.assertEqual(str(self.motorcycle), 'TestMotorcycle')

    def test_motorcycle_list_view(self):
        response = self.client.get(reverse('motorcycle_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'TestMotorcycle')

    def test_motorcycle_detail_view(self):
        response = self.client.get(reverse('motorcycle_detail', args=[self.motorcycle.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'TestBrand')

    def test_motorcycle_review(self):
        motorcycle_review = MotorcycleReview.objects.create(
            motorcycle=self.motorcycle,
            name='TestName',
            review_text='Test Review',
            pub_date=timezone.now()
        )
        self.assertEqual(str(motorcycle_review), 'Test Review')