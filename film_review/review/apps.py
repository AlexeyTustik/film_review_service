import joblib
import re

from django.apps import AppConfig
from django.conf import settings
from nltk.stem.porter import PorterStemmer


class ReviewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'review'
    model = joblib.load(settings.MODEL)
    stemmer = PorterStemmer()

    def stem_text(text):
        words = re.sub('[^a-zA-Z]', ' ', text).lower().split()
        words_stemmed = [ReviewConfig.stemmer.stem(word) for word in words]
        return ' '.join(words_stemmed)
