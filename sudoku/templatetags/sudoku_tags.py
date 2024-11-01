# https://docs.djangoproject.com/en/5.1/howto/custom-template-tags/
# to use this tag, add:
# {% load sudoku_tags %}
# to the template
# and

from django import template
import requests

register = template.Library()

@register.inclusion_tag("game.html")
def get_game():
    # query API here
    body = {
        # TODO change difficulty
        "difficulty": "easy",  # "easy", "medium", or "hard" (defaults to "easy")
        "solution": True,  # True or False (defaults to True)
        "array": False  # True or False (defaults to False)
    }
    # headers = {"Content-Type": "application/json"}
    # response = requests.post("https://youdosudoku.com/api/", json=body, headers=headers)
    # return { "game" : response }

    response = requests.get("https://youdosudoku.com/api/")

    return { "json" : response.json(), "error" : response.status_code }