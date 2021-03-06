# TO RUN in Windows
# Run the following in the terminal without the hash sign:
# venv\Scripts\activate
# $env:FLASK_APP = "shows"
# $env:FLASK_ENV = "development"
# flask run -h localhost -p 3030

# TO RUN in MacOS/Linux
# Run the following in the terminal without the hash sign:
# . venv/bin/activate
# export FLASK_APP=shows
# export FLASK_ENV=development
# flask run -h localhost -p 3030

from flask import Flask


# Flask Instance
app = Flask(__name__)


# Dummy Data (List of Shows)
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
@app.route('/api/show/', methods=('GET',)) # Endpoint and the HTTP Request Method
def index():
    return { 'data': my_shows }


# API to get details of one show using ID
@app.route('/api/show/<int:id>', methods=('GET',)) # Endpoint passing the 'id' argument to the function below
def get_by_id(id):
    result = {}

    for show in my_shows:
        if(id == show['id']):
            result = show

    return result