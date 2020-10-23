from morse_tables import get_table_by_text, MORSE_TABLES
from validators import check_is_alpha, check_is_morse, check_unsupported_letters
import requests

from exceptions import LanguageDoseNotSupported, MixedLanguages, UnsupportedLetter
import logging

app_logger = logging.getLogger('morse_logger')


def _get_unique_letters(text):
    return ''.join(set(text))


def translate(text):
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


def _encocde(text, morse_table):
    unique_letters_in_text = _get_unique_letters(text)

    for letter in unique_letters_in_text:
        translated_letter = morse_table.get(letter.upper())
        if translated_letter is None:
            translated_letter = _get_key_by_value(morse_table, letter)

        if letter != '\n' and letter != ' ':
            translated_letter += ' '

        text = text.replace(letter, translated_letter)
    return text


def _decode(text):
    try:
        text = text.replace('\n', ' ')
        text = text.replace('\r', ' ')
        API = f'http://www.morsecode-api.de/decode?string={text}'
        normal_text = requests.get(API)
        return normal_text.json()['plaintext']
    except Exception as err:
        app_logger.fatal(err)


def show_morse_table():
    return MORSE_TABLES


def _get_key_by_value(dict_in, value_in):
    for key, value in dict_in.items():
        if value == value_in:
            return key
