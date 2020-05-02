from django.db.models.fields import CharField
import importlib
import os

class LanguageField(CharField):
    """
    A language field for Django models.
    """
    def __init__(self, *args, **kwargs):
        # Local import so the languages aren't loaded unless they are needed.
        #from .languages import LANGUAGES
        if 'size' in kwargs:
            size_option='_'+kwargs['size']
        else:
            size_option=''
        languages = importlib.import_module('languages.languages' + size_option , os.path.dirname(__file__))
        LANGUAGES = languages.LANGUAGES

        kwargs.setdefault('max_length', 4)
        kwargs.setdefault('choices', LANGUAGES)
        kwargs.pop('size', "")
        super(CharField, self).__init__(*args, **kwargs)
