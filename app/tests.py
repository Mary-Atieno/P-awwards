from django.test import TestCase
import unittest
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='test', password = 'test123')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class TestProject(TestCase):

    def setUp(self):
        self.user = User.objects.create(id=1, username='mary')
        self.project = Project.objects.create(id=1, title='first post', image='https://www.entrepreneur.com/article/424106', description='circular import',owner=self.user, link='https://medium.com/@dibaekhanal101/cannot-import-name-modelname-from-partially-initialized-module-most-likely-due-to-a-circular-ee4c6ae51d7')


    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_project(self):
        self.project.save_project()
        post = Project.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_projects(self):
        self.project.save()
        posts = Project.get_projects()
        self.assertTrue(len(posts) > 0)

    def test_search_project(self):
        self.project.save()
        post = Project.search_projects('test')
        self.assertTrue(len(post) > 0)

    def test_delete_project(self):
        self.project.delete_project()
        post = Project.search_projects('test')
        self.assertTrue(len(post) < 1)

if __name__ == '__main__':
    unittest.main()