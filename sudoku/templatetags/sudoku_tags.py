# https://docs.djangoproject.com/en/5.1/howto/custom-template-tags/
# to use this tag, add:
# {% load sudoku_tags %}
# to the template
# and

from django import template
import requests

register = template.Library()

@register.simple_tag()
def get_game(difficulty):
    body = {
        "difficulty": difficulty,  # "easy", "medium", or "hard" (defaults to "easy")
        "solution": True,  # True or False (defaults to True)
        "array": False  # True or False (defaults to False)
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post("https://youdosudoku.com/api/", json=body, headers=headers)
    response_json = response.json()
    response_json['http_status'] = response.status_code
    return response_json


