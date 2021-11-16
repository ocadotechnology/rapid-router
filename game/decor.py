"""
    Decor data
"""

from builtins import object
from rest_framework.reverse import reverse
from game.theme import get_theme, get_all_themes


class Decor(object):
    def __init__(self, pk, name, url, width, height, theme, z_index):
        self.id = self.pk = pk
        self.name = name
        self.url = url
        self.width = width
        self.height = height
        self.theme = theme
        self.z_index = z_index


DECOR_DATA = {
    (u"tree1", u"grass"): Decor(
        z_index=4,
        name=u"tree1",
        url=u"decor/grass/tree1.svg",
        height=100,
        width=100,
        theme=get_theme("grass"),
        pk=1,
    ),
    (u"tree2", u"grass"): Decor(
        z_index=4,
        name=u"tree2",
        url=u"decor/grass/tree2.svg",
        height=100,
        width=100,
        theme=get_theme("grass"),
        pk=2,
    ),
    (u"bush", u"grass"): Decor(
        z_index=3,
        name=u"bush",
        url=u"decor/grass/bush.svg",
        height=50,
        width=50,
        theme=get_theme("grass"),
        pk=3,
    ),
    (u"house", u"grass"): Decor(
        z_index=1,
        name=u"house",
        url=u"decor/grass/house.svg",
        height=50,
        width=50,
        theme=get_theme("grass"),
        pk=4,
    ),
    (u"cfc", u"grass"): Decor(
        z_index=1,
        name=u"cfc",
        # FUTURE: add external branding option
        url=u"decor/grass/cfc.svg",
        height=107,
        width=100,
        theme=get_theme("grass"),
        pk=5,
    ),
    (u"pond", u"grass"): Decor(
        z_index=2,
        name=u"pond",
        url=u"decor/grass/pond.svg",
        height=100,
        width=150,
        theme=get_theme("grass"),
        pk=6,
    ),
    (u"tree1", u"snow"): Decor(
        z_index=4,
        name=u"tree1",
        url=u"decor/snow/tree1.svg",
        height=100,
        width=100,
        theme=get_theme("snow"),
        pk=7,
    ),
    (u"tree2", u"snow"): Decor(
        z_index=4,
        name=u"tree2",
        url=u"decor/snow/tree2.svg",
        height=100,
        width=100,
        theme=get_theme("snow"),
        pk=8,
    ),
    (u"bush", u"snow"): Decor(
        z_index=3,
        name=u"bush",
        url=u"decor/snow/bush.svg",
        height=50,
        width=50,
        theme=get_theme("snow"),
        pk=9,
    ),
    (u"house", u"snow"): Decor(
        z_index=1,
        name=u"house",
        url=u"decor/snow/house.svg",
        height=50,
        width=50,
        theme=get_theme("snow"),
        pk=10,
    ),
    (u"cfc", u"snow"): Decor(
        z_index=1,
        name=u"cfc",
        # FUTURE: add external branding option
        url=u"decor/snow/cfc.svg",
        height=107,
        width=100,
        theme=get_theme("snow"),
        pk=11,
    ),
    (u"pond", u"snow"): Decor(
        z_index=2,
        name=u"pond",
        url=u"decor/snow/pond.svg",
        height=100,
        width=150,
        theme=get_theme("snow"),
        pk=12,
    ),
    (u"tile1", u"grass"): Decor(
        z_index=0,
        name=u"tile1",
        url=u"decor/grass/tile1.svg",
        height=100,
        width=100,
        theme=get_theme("grass"),
        pk=13,
    ),
    (u"tile1", u"snow"): Decor(
        z_index=0,
        name=u"tile1",
        url=u"decor/snow/tile1.svg",
        height=100,
        width=100,
        theme=get_theme("snow"),
        pk=14,
    ),
    (u"tile2", u"snow"): Decor(
        z_index=0,
        name=u"tile2",
        url=u"decor/snow/tile2.svg",
        height=100,
        width=100,
        theme=get_theme("snow"),
        pk=15,
    ),
    (u"house", u"farm"): Decor(
        z_index=1,
        name=u"house",
        url=u"decor/farm/house1.svg",
        height=224,
        width=184,
        theme=get_theme("farm"),
        pk=16,
    ),
    (u"cfc", u"farm"): Decor(
        z_index=1,
        name=u"cfc",
        url=u"decor/farm/cfc.svg",
        height=301,
        width=332,
        theme=get_theme("farm"),
        pk=17,
    ),
    (u"bush", u"farm"): Decor(
        z_index=3,
        name=u"bush",
        url=u"decor/farm/bush.svg",
        height=30,
        width=50,
        theme=get_theme("farm"),
        pk=18,
    ),
    (u"tree1", u"farm"): Decor(
        z_index=4,
        name=u"tree1",
        url=u"decor/farm/tree1.svg",
        height=100,
        width=100,
        theme=get_theme("farm"),
        pk=19,
    ),
    (u"tree2", u"farm"): Decor(
        z_index=4,
        name=u"tree2",
        url=u"decor/farm/house2.svg",
        height=88,
        width=65,
        theme=get_theme("farm"),
        pk=20,
    ),
    (u"pond", u"farm"): Decor(
        z_index=2,
        name=u"pond",
        url=u"decor/farm/crops.svg",
        height=100,
        width=150,
        theme=get_theme("farm"),
        pk=21,
    ),
    (u"tile1", u"farm"): Decor(
        z_index=0,
        name=u"tile1",
        url=u"decor/farm/tile1.svg",
        height=337,
        width=194,
        theme=get_theme("farm"),
        pk=22,
    ),
    (u"tile1", u"city"): Decor(
        z_index=0,
        name=u"tile1",
        url=u"decor/city/pavementTile.png",
        height=100,
        width=100,
        theme=get_theme("city"),
        pk=23,
    ),
    (u"house", u"city"): Decor(
        z_index=1,
        name=u"house",
        url=u"decor/city/house.svg",
        height=50,
        width=50,
        theme=get_theme("city"),
        pk=24,
    ),
    (u"bush", u"city"): Decor(
        z_index=3,
        name=u"bush",
        url=u"decor/city/bush.svg",
        height=50,
        width=50,
        theme=get_theme("city"),
        pk=25,
    ),
    (u"tree1", u"city"): Decor(
        z_index=4,
        name=u"tree1",
        url=u"decor/city/shop.svg",
        height=70,
        width=70,
        theme=get_theme("city"),
        pk=26,
    ),
    (u"tree2", u"city"): Decor(
        z_index=4,
        name=u"tree2",
        url=u"decor/city/school.svg",
        height=100,
        width=100,
        theme=get_theme("city"),
        pk=27,
    ),
    (u"pond", u"city"): Decor(
        z_index=2,
        name=u"pond",
        url=u"decor/city/hospital.svg",
        height=157,
        width=140,
        theme=get_theme("city"),
        pk=28,
    ),
    (u"cfc", u"city"): Decor(
        z_index=1,
        name=u"cfc",
        # FUTURE: add external branding option
        url=u"decor/grass/cfc.svg",
        height=107,
        width=100,
        theme=get_theme("city"),
        pk=29,
    ),
    (u"tile2", u"grass"): Decor(
        z_index=0,
        name=u"tile2",
        url=u"decor/snow/tile2.svg",
        height=100,
        width=100,
        theme=get_theme("grass"),
        pk=30,
    ),
    (u"tile2", u"farm"): Decor(
        z_index=0,
        name=u"tile2",
        url=u"decor/snow/tile2.svg",
        height=100,
        width=100,
        theme=get_theme("farm"),
        pk=31,
    ),
    (u"tile2", u"city"): Decor(
        z_index=0,
        name=u"tile2",
        url=u"decor/snow/tile2.svg",
        height=100,
        width=100,
        theme=get_theme("city"),
        pk=32,
    ),
}


def get_decor_element(name, theme):
    """Helper method to get a decor element corresponding to the theme or a default one."""
    try:
        return DECOR_DATA[(name, theme.name)]
    except KeyError:
        for theme_object in get_all_themes():
            try:
                return DECOR_DATA[(name, theme_object.name)]
            except KeyError:
                pass
    raise KeyError


def get_all_decor():
    return list(DECOR_DATA.values())


def get_decor_element_by_pk(pk):
    for decor in list(DECOR_DATA.values()):
        if decor.pk == int(pk):
            return decor
    raise KeyError


def get_decors_url(pk, request):
    return reverse("decor-detail", args={pk}, request=request)
