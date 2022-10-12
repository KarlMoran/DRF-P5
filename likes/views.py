from rest_framework import generics, permissions
from drf_p5.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """ 
    List all likes. Create a like if authenticated.
    The perform_create method associates the like with the logged in user. 
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeDetail(generics.RetrieveDestroyAPIView):
    """ 
    Retrieve a like. 
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

