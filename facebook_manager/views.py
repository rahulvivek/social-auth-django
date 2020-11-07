import json
import facebook
import requests 

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import permissions


class FacebookGetPagesAPIView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body)
        try:
            graph = facebook.GraphAPI(access_token=data["auth_token"])
            profile = graph.request('/me?fields=accounts')
            pages = []
            for account in profile["accounts"]["data"]:
                print(account)
                page_details = graph.request('/{}?fields=about,name,description,phone,general_info,website'.format(account["id"]))
                page_details["access_token"] = account["access_token"]
                pages.append(page_details)
            return Response({
                "pages": pages
            })

        except:
            return Response({
                "error": "The token is invalid or expired."
            }, 400)

class FacebookPageUpdateAPIView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        data = json.loads(request.body)
        data.pop("auth_token")
        data.pop("name")
        id = data.pop("id")
        if True:
            graph = facebook.GraphAPI()
            response = requests.post("https://graph.facebook.com/v8.0/{}".format(id), params=data)
            # page_details = graph.request("post", url, data
            # page_details = graph.request('/{}?fields=about,name,description,phone,general_info,website'.format(account["id"]))
            
            return Response({
                "page": {
                    "id": id,
                    "about": data["about"]
                }
            })

    


