from morse_tables import MORSE_EN_CODE_DICT, UNSUPPORTED_LETEERS


def check_is_morse(text: str) -> bool:
    """
    Check if the text is morse code
    :param text: Message from user
    :return: True if it is morse , false if not
    """
    for code in text.split(' '):
        if code in MORSE_EN_CODE_DICT.values() and code != '':
            return True
    return False


def check_is_alpha(text: str) -> bool:
    """
    Check if the text is alphabet
    :param text: Message from user
    :return: True if it is alphabet , false if not
    """
    for letter in text:
        if letter.isalpha() or letter.isalnum():
            return True
    return False


def check_unsupported_letters(text: str) -> bool:
    """
    Check if the text include unsupported signs
    :param text: Message from user
    :return: True if it is unsupported letter , false if not
    """
    for letter in text:
        if letter in UNSUPPORTED_LETEERS:
            return True
    return False
