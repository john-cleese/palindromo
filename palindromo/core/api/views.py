from rest_framework.response import Response
from rest_framework.views import APIView


class CheckPalindromeAPIView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    permission_classes = []

    def get(self, request, format=None):

        return Response({"mensagem": "OK"})
