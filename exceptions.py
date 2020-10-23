class MixedLanguages(Exception):
    def __init__(self):
        self.msg = "You probably mixed languages please use one"


class LanguageDoseNotSupported(Exception):
    def __init__(self):
        self.msg = "The Morse Translator dose not support this language"


class UnsupportedLetter(Exception):
    def __init__(self):
        self.msg = "You probably type unsupported letter"
