from rest_framework import serializers
from accounts.models import User, Profile

# class UserSerializer(serializers.Serializer):
#     first_name = serializers.CharField()


class ProfileSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        field = "dob", "address", "contact_no"


 class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerailizer()

    class Meta:
        model = User
        fields = "first_name", "last_name", "email", "username", "profile"

     def create(self, validate_data):
        profile = validate_data.pop("profile")
        raw_password = validate_data.pop("password")
        validate_data
        pass


 """{
     "first_name": "prajeet", 
     "last_name": "agrawal", 
     "profile": {
         "dob": 1983/03/14, 
         "address": "ktm"
     }
 }"""