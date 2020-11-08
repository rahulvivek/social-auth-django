from rest_framework import serializers

from .utils import register_social_user
from . import facebook

class FacebookSocialAuthSerializer(serializers.Serializer):
    """Handles serialization of facebook related data"""
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = facebook.Facebook.validate(auth_token)
        print(user_data)

        try:
            user_id = user_data['id']
            email = user_data.get('email')
            name = user_data['name']
            provider = 'facebook'
            if not email:
                email = "{}{}@{}.com".format(name.replace(" ", "").lower(), user_id, provider)
            return register_social_user(
                provider=provider,
                user_id=user_id,
                email=email,
                name=name
            )
        except Exception as identifier:
            raise serializers.ValidationError(
                'The token  is invalid or expired. Please login again.'
            )