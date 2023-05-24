from app.user_authentication.serializers import UserRegistrationSerializer
from app.user_authentication.models import User
from app.user_authentication.serializers import *
from rest_framework import status
from customer_management.constants import messages

# from django.contrib.auth.models import User

def view_users(request):   
    response = {"status":status.HTTP_400_BAD_REQUEST,"message":messages.USER_DETAILS_FAILED}
    all_user = User.objects.all()
    serializer = UserRegistrationSerializer(all_user, many=True)
    response = {"status":status.HTTP_200_OK,"message":messages.USER_DETAILS_SUCESS,"data":serializer.data}
    return response


def user_registration(request):
    response = {"status":status.HTTP_400_BAD_REQUEST,"message":messages.USER_REGISTRATION_FAILED}
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        response = {"status":status.HTTP_201_CREATED,"message":messages.USER_REGISTRATION_SUCESS,"data":serializer.data}
        return response

