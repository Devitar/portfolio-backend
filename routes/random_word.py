from flask import Blueprint, jsonify
import requests
from wonderwords import RandomWord

bp = Blueprint("random_word", __name__)

random_word_generator = RandomWord()
dictionary_api_endpoint = "https://api.dictionaryapi.dev/api/v2/entries/en/"


@bp.route("/random_word")
def random_word():
    word = random_word_generator.word(include_parts_of_speech=["nouns", "adjectives"])
    response = requests.get(dictionary_api_endpoint + word)

    if response.status_code == 200:
        data = response.json()
        try:
            definition = data[0]["meanings"][0]["definitions"][0]["definition"]
        except (KeyError, IndexError, TypeError):
            definition = None
    else:
        definition = None

    return jsonify({
        "definition": definition,
        "word": word,
    })
