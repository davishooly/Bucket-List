from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

from ..models import BucketList

from django.urls import reverse
# Create your tests here.


class ModelTestCase(TestCase):
    """ This class defines testsuite for the backetlist appliction """

    def setUp(self):
        """ This method defines testclient and other test variables """
        self.backetlist_name = "kimame here"
        self.bucketlist = BucketList(name=self.backetlist_name)

    def test_model_can_create_a_bucket_list(self):
        """ create a bucketlist """
        old_count = BucketList.objects.create()
        self.bucketlist.save()
        new_count = BucketList.objects.create()
        self.assertNotEqual(old_count, new_count)


# Testing our views

class ViewTestCase(TestCase):
    """ defines test suite fr api views """

    def setUp(self):

        self.client = APIClient()
        self.bucketlist_data = {
            "name": "kimame"
        }
        self.response = self.client.post(
            reverse("create"),
            self.bucketlist_data,
            format="json"
        )

    def test_api_create_bucketlist(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
