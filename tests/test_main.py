from src.assignment_14.main import check_if_anagrams


def test_check_if_anagrams_not_ignore_case():
    str1 = 'listen'
    str2 = 'SiLenT'
    result = check_if_anagrams(str1, str2, ignore_case=False)
    assert result == False


def test_check_if_anagrams_ignore_case():
    str1 = 'listen'
    str2 = 'SiLenT'
    result = check_if_anagrams(str1, str2, ignore_case=True)
    assert result == True


def test_check_if_anagrams_not_anagrams():
    str1 = 'apple'
    str2 = 'appeal'
    result = check_if_anagrams(str1, str2)
    assert result == False


def test_check_if_anagrams_empty_strings():
    str1 = ''
    str2 = ''
    result = check_if_anagrams(str1, str2)
    assert result == True


def test_check_if_anagrams_unequal_length_strings():
    str1 = 'das'
    str2 = 'sd'
    result = check_if_anagrams(str1, str2)
    assert result == False