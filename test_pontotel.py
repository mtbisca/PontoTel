import pontotel
class TestPontoTel:
    def test_one:
        url = "https://docs.pytest.org/en/latest/goodpractices.html#test-discovery"
        key_word = "files"
        answer = '{{"{0}": "{1}"}}'.format("Occurrences", "11")
        assert get_occurrences(url, key_word) == answer

    def test_two:
        url =
        key_word =
        answer =
        assert get_occurrences(url, key_word) == answer

    def test_three:
        url =
        key_word =
        answer =
        assert get_occurrences(url, key_word, case_sensitive=False) == answer

    def test_four:
        url =
        key_word =
        answer =
        assert get_occurrences(url, key_word) == answer
    def test_five:
        url =
        key_word =
        answer =
        assert get_occurrences(url, key_word) == answer
