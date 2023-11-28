from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class AppDevClubReviewsView(APIView):
    def get(self, request):
        reviews = [
            'app dev is great',
            'you should join',
            'hello world',
            'add more react workshops'
        ]
        return Response({'reviews': reviews})
