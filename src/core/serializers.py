from djoser.serializers import UserSerializer


class CoreUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('balance',)
