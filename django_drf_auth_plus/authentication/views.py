from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = self.serializer_class(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()

        user_data = user.data
        user = User.object.get(email=user_data["email"])

        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relative_link = reverse("email-verify")
        abs_url = "http://" + current_site + relative_link + "?token=" + str(token)
        email_body = "Hi " + user.username + ", Use link bellow to verify your emai \n" + abs_url
        data = {"email_body": email_body, "to": user.email, "email_subject": "Verify your account", "domain": current_site}

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(GenericAPIView):

    def get(self):
        pass
