from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from reviews.models import Review

# Create your views here.
class AppDevClubReviewsView(APIView):
    def get(self, request):
        reviews = []
        for review in Review.objects.filter():
            reviews.append(review.review_text)
        return Response({'reviews': reviews})

class CreateAppDevClubReview(APIView):
    def post(self, request):
        review = request.data['review']
        person = request.data['personName']
        email = request.data['email']
        phone_number = request.data['phoneNumber']
        if review != '':
            new_database_entry = Review(review_text=review, person=person, email=email, phone_number=phone_number)
            new_database_entry.save()
            return Response({'message': 'success'})
        else:
            return Response({'message': 'failure'})
