import pytest
from rest_framework.test import APIClient

from palindromo.core.utils import check_palindrome
from palindromo.django_assertions import assert_contains

pytestmark = [pytest.mark.django_db, pytest.mark.palindrome]


@pytest.mark.parametrize(
    "sentence, output",
    [
        # Casos para teste com return True.
        ("Socorram-me, subi no ônibus em Marrocos", True),
        ("Rir, o breve verbo rir.", True),
        ("A mãe te ama.", True),
        ("Oto come mocotó.", True),
        ("A cara rajada da jararaca.", True),
        ("Até time demite, tá?", True),
        ("Seco de raiva, coloco no colo caviar e doces.", True),
        ("Amo Omã. Se Roma me tem amores, amo Omã!", True),
        ("Me vê se a panela da moça é de aço, Madalena Paes, e vem.", True),
        (
            "Luza Rocelina, a namorada do Manuel, leu na moda da Romana: anil é cor azul.",
            True,
        ),
        (
            "O duplo pó do trote torpe de potro meu que morto pede protetor todo polpudo.",
            True,
        ),
        ("O romano acata amores a damas amadas e Roma ataca o namoro.", True),
        # Casos para teste com return False.
        ("Rir, o breve verbo rir. Não palindromo.", False),
        ("A mãe te ama. Não palindromo", False),
        ("Oto come mocotó. Não palindromo", False),
        ("A cara rajada da jararaca. Não palindromo", False),
        ("Até time demite, tá? Não palindromo", False),
    ],
)
def test_check_palindrome(sentence, output):
    assert check_palindrome(sentence) == output


class TestPalindromeEndpoints:
    endpoint = "/api/"
    client = APIClient()

    @pytest.mark.parametrize(
        "sentence, output",
        [
            # Casos para teste com return True.
            ("Socorram-me, subi no ônibus em Marrocos", 39),
            ("Oto", 3),
            ("Rir, o breve verbo rir.", 23),
        ],
    )
    def test_count(self, sentence, output):
        expected_json = {"quantidade": output}
        url = f"{self.endpoint}count/?sentence={sentence}"
        response = self.client.get(url)
        assert_contains(response, expected_json["quantidade"])

    @pytest.mark.parametrize(
        "sentence",
        [
            # Casos para teste com return False.
            "Oto come mocotó. Não palindromo",
            "A cara rajada da jararaca. Não palindromo",
            "Até time demite, tá. Não palindromo",
        ],
    )
    def test_counter_not_palindrome(self, sentence):
        expected_json = {"mensagem": "não é um palindromo"}
        url = f"{self.endpoint}count/?sentence={sentence}"
        response = self.client.get(url)
        print("###############################################################")
        print(sentence)
        print(response.data)
        assert_contains(response, expected_json["mensagem"])
