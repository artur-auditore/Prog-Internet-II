from django.shortcuts import render
import json

# Create your views here.
from rest_framework import generics
from app.models import *

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        pass

class ImportData(generics.GenericAPIView):
    name = 'import_data'

    def get(self, request, *args, **kwargs):
        self.import_data()


    def import_data(self):

        data = json.load(open('db.json'))

        for user in data['users']:
            ad = user['address']
            address = Address(street=ad['street'], city=ad['city'], suite=ad['suite'], zipcode=ad['zipcode'])

            address.save()

            name = user['name']
            email = user['email']
            Profile.objects.create(name=name, email=email, address=address)

        for post in data['posts']:
            profile = Profile.objects.get(id=post['userId'])
            Post.objects.create(title=post['title'],
                                body=post['profile'],
                                profile=profile)

        for comment in data['comments']:
            post = Post.objects.get(id=comment['postId'])
            Comment.objects.create(id=comment['id'],
                                             name=comment['name'],
                                             email=comment['email'],
                                             body=comment['body'],
                                             post=post)