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

def test_is_token_label():
    assert AMBTokenizer.isTokenLabel('h')
    assert not AMBTokenizer.isTokenLabel('1')
    assert AMBTokenizer.isTokenLabel('H')
    assert AMBTokenizer.isTokenLabel('hello')
    assert AMBTokenizer.isTokenLabel('hello123')
    assert not AMBTokenizer.isTokenLabel('hello#$%$')

def test_tokenizer():
    data = open('AMB_Sample.txt', 'r')
    # print(data.read())
    tokens = AMBTokenizer.tokenize(data.read())