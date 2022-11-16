from rest_framework.response import Response
from rest_framework.views import APIView

from palindromo.core.utils import check_palindrome


class CheckPalindromeAPIView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    permission_classes = []

    def get(self, request, format=None):
        check_result = check_palindrome(request.GET.get("sentence"))

        return Response({"mensagem": check_result})
