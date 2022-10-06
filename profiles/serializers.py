from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile serializer.
    Providing readability to profile data in API.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Associates User to User Profile.
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """
        Lists of Profile model fields to display.
        """
        model = Profile
        fields = [
            'id',
            'owner',
            'created_on',
            'modified_on',
            'first_name',
            'last_name',
            'country',
            'username',
            'description',
            'image',
            'is_owner',
        ]