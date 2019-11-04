from django.shortcuts import render, redirect
import json

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import *

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'address-list'

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name = 'address-detail'

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'profiles': reverse(ProfileList.name, request=request),
            'address': reverse(AddressList.name, request=request)
        })




def import_data():

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
        Post.objects.create(title=post['title'], body=post['body'], profile=profile)

    for comment in data['comments']:
        post = Post.objects.get(id=comment['postId'])
        Comment.objects.create(id=comment['id'],
                               name=comment['name'],
                               email=comment['email'],
                               body=comment['body'],
                               post=post)