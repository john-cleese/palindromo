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


class CounterPalindromeAPIView(APIView):
    """
    View responsavel por conta caracteres de um palindromo.
    """

    permission_classes = []

    def get(self, request, format=None):
        sentence = request.GET.get("sentence")
        if not check_palindrome(sentence):
            return Response({"mensagem": "Frase informada não é um palindromo!"})

        counter = len(sentence)

        return Response({"quantidade": counter})
