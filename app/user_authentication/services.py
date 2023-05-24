from app.user_authentication.serializers import UserRegistrationSerializer
from app.user_authentication.models import User
from app.user_authentication.serializers import UserRegistrationSerializer
from rest_framework import status

# from django.contrib.auth.models import User

def view_users(request):   
    response={"status":status.HTTP_400_BAD_REQUEST,"message":"Fetching Users Details are  Failed"}
    all_user = User.objects.all()
    serializer = UserRegistrationSerializer(all_user, many=True)
    response["status"] = status.HTTP_200_OK
    response["message"] = " Users Details fetched successfully"
    # response["data"] = serializer.data
    return serializer.data
def user_registration(request):
    response={"status":status.HTTP_400_BAD_REQUEST,"message":"User Creation Failed"}
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response["status"] = status.HTTP_201_CREATED
        response["message"] = "Registration Successfull"
        response["data"] = serializer.data
        return Response(response)
