from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView


class LoginAccount(APIView):

    def post(self, request, *args, **kwargs):

        if {'username', 'password'}.issubset(request.data):
            user = authenticate(username=request.data['username'], password=request.data['password'])
            token, _ = Token.objects.get_or_create(user=user)

            return Response({'Status': True, 'Token': token.key})

        return Response({'Status': False, 'Errors': 'Not all required arguments are specified'})
