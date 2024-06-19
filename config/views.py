from django.http.response import HttpResponse, JsonResponse
from django.views.generic import TemplateView, View
from django.shortcuts import render
import random
# from django.contrib.auth import logout
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def hello_world(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def hello_world_json(request):
    return JsonResponse({"message": "Hello, World!"})

class RandomNumberTemplateView(TemplateView):
    template_name = "random.html"
    
class RandomNumberView(View):
    def get(self, request):
        random_number = random.randint(1, 100)
        return render(request, "random.html", {"random": random_number})

class LogoutView(APIView):
    def post(self, request):
        try:
            token = request.auth
            token.delete()
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except (AttributeError, Token.DoesNotExist):
            return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)

# class LogoutView(APIView):
#     def post(self, request):
#         logout(request)
#         return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
