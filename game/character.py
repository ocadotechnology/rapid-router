"""
    Character data
"""

from builtins import object
from rest_framework.reverse import reverse


class Character(object):
    def __init__(self, pk, name, en_face, top_down, width, height):
        self.id = self.pk = pk
        self.name = name
        self.en_face = en_face
        self.top_down = top_down
        self.width = width
        self.height = height


CHARACTER_DATA = {
    "Van": Character(
        pk=1,
        name="Van",
        # FUTURE: add external branding option
        en_face="characters/front_view/Van.svg",
        top_down="characters/top_view/Van.svg",
        height="20",
        width="40",
    ),
    "Dee": Character(
        pk=2,
        name="Dee",
        # FUTURE: add external branding option
        en_face="characters/front_view/Dee.svg",
        top_down="characters/top_view/Dee.svg",
        height="28",
        width="52",
    ),
    "Nigel": Character(
        pk=3,
        name="Nigel",
        en_face="characters/front_view/Nigel.svg",
        top_down="characters/top_view/Nigel.svg",
        height="32",
        width="56",
    ),
    "Kirsty": Character(
        pk=4,
        name="Kirsty",
        en_face="characters/front_view/Kirsty.svg",
        top_down="characters/top_view/Kirsty.svg",
        height="32",
        width="60",
    ),
    "Wes": Character(
        pk=5,
        name="Wes",
        en_face="characters/front_view/Wes.svg",
        top_down="characters/top_view/Wes.svg",
        height="20",
        width="40",
    ),
    "Phil": Character(
        pk=6,
        name="Phil",
        en_face="characters/front_view/Phil.svg",
        top_down="characters/top_view/Phil.svg",
        height="40",
        width="40",
    ),
    "Electric van": Character(
        pk=7,
        name="Electric van",
        en_face="characters/front_view/Electric_van.svg",
        top_down="characters/top_view/Electric_van.svg",
        height="20",
        width="40"
    ),
}


def get_character(name):
    """Helper method to get a character."""
    return CHARACTER_DATA[name]


def get_all_character():
    return list(CHARACTER_DATA.values())


def get_character_by_pk(pk):
    for character in list(CHARACTER_DATA.values()):
        if character.pk == int(pk):
            return character
    raise KeyError


def get_characters_url(pk, request):
    return reverse("character-detail", args={pk}, request=request)
