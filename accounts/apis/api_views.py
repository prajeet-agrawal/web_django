from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny


class UserRegistrationAPIView(CreateAPIView):
    permission_classes = [AllowAny]