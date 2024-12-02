from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    referrals = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['phone_number', 'invite_code', 'activated_invite', 'referrals']

    def get_referrals(self, obj):
        return [user.phone_number for user in obj.referrals.all()]
