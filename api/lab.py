from typing import List


my_shows = [
    {
        'id': 0,
        'title': 'The Avengers',
        'director': 'Joss Whedon',
        'cast': ['Robert Downey Jr.', 'Chris Evans', 'Chris Hemsworth'],
        'type': 'movie'
    },
    {
        'id': 1,
        'title': 'Rurouni Kenshin Part I: Origins',
        'director': 'Keishi Ohtomo',
        'cast': ['Takeru Satoh', 'Emi Takei'],
        'type': 'movie'
    },
    {
        'id': 2,
        'title': 'Modern Family',
        'director': '',
        'cast': ['Ed O\'Neill', 'Sofía Vergara', 'Julie Bowen' ,'Ty Burrell'],
        'type': 'series'
    },
    {
        'id': 3,
        'title': 'Community',
        'director': 'Dan Harmon',
        'cast': ['Joel McHale', 'Gillian Jacobs', 'Danny Pudi' ,'Alison Brie', 'Donald Glover', 'Ken Jeong'],
        'type': 'series'
    },
    {
        'id': 4,
        'title': 'The Hangover',
        'director': 'Todd Phillips',
        'cast': ['Bradley Cooper', 'Ed Helms', 'Zach Galifianakis' ,'Justin Bartha', 'Ken Jeong'],
        'type': 'movie'
    }
]

# print(my_shows[1])
for show in my_shows:
    if(1 == show['id']):
        print(show)

# print(my_shows)
keyword ='Julie Bowen'
result = []
for index, show in enumerate(my_shows):
    show_info = list(show.values())
    if keyword in show_info or keyword in show['cast']:
        result.append(my_shows[index])

print(result)