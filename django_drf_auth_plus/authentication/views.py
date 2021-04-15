from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = self.serializer_class(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()

        user_data = user.data
        return Response(user_data, status=status.HTTP_201_CREATED)
