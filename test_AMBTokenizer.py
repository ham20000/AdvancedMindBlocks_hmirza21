import AMBTokenizer

def test_is_token_number():
    assert AMBTokenizer.isTokenNumber('1111')
    assert not AMBTokenizer.isTokenNumber('hello')
    assert AMBTokenizer.isTokenNumber('-1111')
    assert not AMBTokenizer.isTokenNumber('---1111')
    assert not AMBTokenizer.isTokenNumber('11-11')

def test_is_token_character_string():
    assert AMBTokenizer.isTokenCharacterString('""')
    assert AMBTokenizer.isTokenCharacterString('"hello"')
    assert not AMBTokenizer.isTokenCharacterString('" " " ')
    assert not AMBTokenizer.isTokenCharacterString('asdf')