import logging
from typing import Dict, List

from exceptions import LanguageDoseNotSupported, MixedLanguages, UnsupportedLetter
from morse_tables import get_table_by_text, MORSE_TABLES
import requests
from validators import check_is_alpha, check_is_morse, check_unsupported_letters

# Get logger
app_logger = logging.getLogger('morse_logger')


def _get_unique_letters(text: str) -> str:
    """
    Get one instance of the letters in the text
    :param text: message from user
    :return: one instance of each letter in string
    """
    return ''.join(set(text))


def translate(text: str) -> str:
    """
    Translate the text from user to morse/normal text
    :param text: Message from user
    :return: The translated message
    """
    try:
        is_alpha = check_is_alpha(text)
        is_morse = check_is_morse(text)
        is_unsupported_letter = check_unsupported_letters(text)

        if is_alpha and is_morse:
            raise MixedLanguages
        elif is_unsupported_letter:
            raise UnsupportedLetter
        elif is_alpha:
            try:
                morse_table_code = get_table_by_text(text)
            except LanguageDoseNotSupported as err:
                app_logger.error(err.msg)
                return err.msg
            except Exception as err:
                app_logger.error(err)
            else:
                return _encocde(text, morse_table_code)
        elif is_morse:
            return _decode(text)
        else:
            return text
    except MixedLanguages as err:
        app_logger.error(err.msg)
        return err.msg
    except UnsupportedLetter as err:
        app_logger.error(err.msg)
        return err.msg


def _encocde(text: str, morse_table: Dict[str, str]) -> str:
    """
    Encode the message from normal text to morse
    :param text: Message from user
    :param morse_table: Morse table to convert the message by it
    :return: Message encoded
    """
    unique_letters_in_text = _get_unique_letters(text)

    for letter in unique_letters_in_text:
        translated_letter = morse_table.get(letter.upper())
        if translated_letter is None:
            raise UnsupportedLetter

        if letter != '\n' and letter != ' ':
            translated_letter += ' '

        text = text.replace(letter, translated_letter)
    return text


def _decode(text: str) -> str:
    """
    Decode the morse code to normal text
    using API - www.morsecode-api.de of Morsecode As A Service by repat
    link to - https://repat.github.io/morsecode-api/
    :param text: Message from user
    :return: Message decoded
    """
    try:
        text = text.replace('\n', ' ')
        text = text.replace('\r', ' ')
        API = f'http://www.morsecode-api.de/decode?string={text}'
        normal_text = requests.get(API)
        return normal_text.json()['plaintext']
    except Exception as err:
        app_logger.fatal(err)


def show_morse_table() -> List[Dict[str, str]]:
    """
    Get all morse tables
    :return: Morse tables
    """
    return MORSE_TABLES
