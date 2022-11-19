# Create your tests here.
import pytest

from palindromo.core.utils import check_palindrome


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
