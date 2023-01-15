from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from imma_chore_app.models import Parent, Kid, Chore, Kid_Chore

class HomeViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.parent = Parent.objects.create(name='John Doe')
        self.kid = Kid.objects.create(parent=self.parent, name='Jane Doe')
        self.chore = Chore.objects.create(parent=self.parent, name='Do the dishes', description='Wash the dishes', payout=5)
        self.kid_chore = Kid_Chore.objects.create(kid=self.kid, parent=self.parent, chore=self.chore, day_of_the_week='Monday', is_complete=False)

    def test_home_view_get(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')
        self.assertContains(response, 'Jane Doe')

    def test_home_view_post_create(self):
        response = self.client.post(reverse('home'), {'name': 'Jane Smith', 'create': 'create'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/parent/2/1/1')

    def test_home_view_post_selected_parent(self):
        response = self.client.post(reverse('home'), {'selected_parent': '1'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/parent/1/1/1')

    def test_home_view_post_selected_kid(self):
        response = self.client.post(reverse('home'), {'selected_kid': '1'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/kid/1')

class ParentViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.parent = Parent.objects.create(name='John Doe')
        self.kid = Kid.objects.create(parent=self.parent, name='Jane Doe')
        self.chore = Chore.objects.create(parent=self.parent, name='Do the dishes', description='Wash the dishes', payout=5)
        self.kid_chore = Kid_Chore.objects.create(kid=self.kid, parent=self.parent, chore=self.chore, day_of_the_week='Monday', is_complete=False)

    def test_parent_view_get(self):
        response = self.client.get(reverse('parent', args=[1,1,1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')
        self.assertContains(response, 'Jane Doe')
        self.assertCont