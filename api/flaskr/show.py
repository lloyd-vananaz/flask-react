from flask import (
    Blueprint
)
from flask_cors.decorator import cross_origin


bp = Blueprint('show', __name__, url_prefix='/show')


# Dummy Data
my_shows = [
    {
        'id': 0,
        'title': 'The Avengers',
        'director': 'Joss Whedon',
        'cast': ['Robert Downey Jr.', 'Chris Evans', 'Chris Hemsworth'],
        'type': 'Movie'
    },
    {
        'id': 1,
        'title': 'Rurouni Kenshin Part I: Origins',
        'director': 'Keishi Ohtomo',
        'cast': ['Takeru Satoh', 'Emi Takei'],
        'type': 'Movie'
    },
    {
        'id': 2,
        'title': 'Modern Family',
        'director': '',
        'cast': ['Ed O\'Neill', 'Sofía Vergara', 'Julie Bowen' ,'Ty Burrell'],
        'type': 'Series'
    },
    {
        'id': 3,
        'title': 'Community',
        'director': 'Dan Harmon',
        'cast': ['Joel McHale', 'Gillian Jacobs', 'Danny Pudi' ,'Alison Brie', 'Donald Glover', 'Ken Jeong'],
        'type': 'Series'
    },
    {
        'id': 4,
        'title': 'The Hangover',
        'director': 'Todd Phillips',
        'cast': ['Bradley Cooper', 'Ed Helms', 'Zach Galifianakis' ,'Justin Bartha', 'Ken Jeong'],
        'type': 'Movie'
    }
]


# API to get all shows
@bp.route('/', methods=('GET',))
@cross_origin()
def index():
    return { 'data': my_shows }


# API to get details of one show using ID
@bp.route('/<int:id>', methods=('GET',))
@cross_origin()
def get_by_id(id):
    result = {}

    for show in my_shows:
        if(id == show['id']):
            result = show

    return result


# API to search shows using a keyword
@bp.route('/search/<string:keyword>', methods=('GET',))
@cross_origin()
def search(keyword):
    result = []
    for index, show in enumerate(my_shows):
        show_info = list(show.values())
        if keyword in show_info or keyword in show['cast']:
            result.append(my_shows[index])

    return { 'data': result }