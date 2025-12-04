from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView

from accounts.models import Profile
from accounts.serializers.profile import ProfileSerializer


class ProfileDetailAPIView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileUpdateAPIView(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDeleteAPIView(DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer