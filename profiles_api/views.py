from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Use HTTP methods as function (get, post, put, patch, delete',
            'Is similiar to a traditional Django View',
            'Gives you the most control over you application logic',
            'It mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
