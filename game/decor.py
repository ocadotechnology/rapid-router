"""
    Decor data
"""

from builtins import object

from rest_framework.reverse import reverse

from game.theme import get_theme, get_all_themes


class Decor(object):
    def __init__(self, pk, name, url, xmas_url, width, height, theme, z_index):
        self.id = self.pk = pk
        self.name = name
        self.url = url
        self.xmas_url = xmas_url
        self.width = width
        self.height = height
        self.theme = theme
        self.z_index = z_index


DECOR_DATA = {
    ("tree1", "grass"): Decor(
        z_index=4,
        name="tree1",
        url="decor/grass/tree1.svg",
        xmas_url="decor/snow/tree1.svg",
        height=100,
        width=100,
        theme=get_theme("grass"),
        pk=1,
    ),
    ("tree2", "grass"): Decor(
        z_index=4,
        name="tree2",
        url="decor/grass/tree2.svg",
        xmas_url="decor/snow/tree2.svg",
        height=100,
        width=100,
        theme=get_theme("grass"),
        pk=2,
    ),
    ("bush", "grass"): Decor(
        z_index=3,
        name="bush",
        url="decor/grass/bush.svg",
        xmas_url="decor/snow/bush.svg",
        height=50,
        width=50,
        theme=get_theme("grass"),
        pk=3,
    ),
    ("house", "grass"): Decor(
        z_index=1,
        name="house",
        url="decor/grass/house.svg",
        xmas_url="decor/snow/house.svg",
        height=50,
        width=50,
        theme=get_theme("grass"),
        pk=4,
    ),
    ("cfc", "grass"): Decor(
        z_index=1,
        name="cfc",
        # FUTURE: add external branding option
        url="decor/grass/cfc.svg",
        xmas_url="decor/snow/cfc.svg",
        height=107,
        width=100,
        theme=get_theme("grass"),
        pk=5,
    ),
    ("pond", "grass"): Decor(
        z_index=2,
        name="pond",
        url="decor/grass/pond.svg",
        xmas_url="decor/snow/pond.svg",
        height=100,
        width=150,
        theme=get_theme("grass"),
        pk=6,
    ),
    ("tree1", "snow"): Decor(
        z_index=4,
        name="tree1",
        url="decor/snow/tree1.svg",
        xmas_url="decor/snow/tree1.svg",
        height=100,
        width=100,
        theme=get_theme("snow"),
        pk=7,
    ),
    ("tree2", "snow"): Decor(
        z_index=4,
        name="tree2",
        url="decor/snow/tree2.svg",
        xmas_url="decor/snow/tree2.svg",
        height=100,
        width=100,
        theme=get_theme("snow"),
        pk=8,
    ),
    ("bush", "snow"): Decor(
        z_index=3,
        name="bush",
        url="decor/snow/bush.svg",
        xmas_url="decor/snow/bush.svg",
        height=50,
        width=50,
        theme=get_theme("snow"),
        pk=9,
    ),
    ("house", "snow"): Decor(
        z_index=1,
        name="house",
        url="decor/snow/house.svg",
        xmas_url="decor/snow/house.svg",
        height=50,
        width=50,
        theme=get_theme("snow"),
        pk=10,
    ),
    ("cfc", "snow"): Decor(
        z_index=1,
        name="cfc",
        # FUTURE: add external branding option
        url="decor/snow/cfc.svg",
        xmas_url="decor/snow/cfc.svg",
        height=107,
        width=100,
        theme=get_theme("snow"),
        pk=11,
    ),
    ("pond", "snow"): Decor(
        z_index=2,
        name="pond",
        url="decor/snow/pond.svg",
        xmas_url="decor/snow/pond.svg",
        height=100,
        width=150,
        theme=get_theme("snow"),
        pk=12,
    ),
    ("tile1", "grass"): Decor(
        z_index=0,
        name="tile1",
        url="decor/grass/tile1.svg",
        xmas_url="decor/snow/tile1.svg",
        height=100,
        width=100,
        theme=get_theme("grass"),
        pk=13,
    ),
    ("tile1", "snow"): Decor(
        z_index=0,
        name="tile1",
        url="decor/snow/tile1.svg",
        xmas_url="decor/snow/tile1.svg",
        height=100,
        width=100,
        theme=get_theme("snow"),
        pk=14,
    ),
    ("tile2", "snow"): Decor(
        z_index=0,
        name="tile2",
        url="decor/snow/tile2.svg",
        xmas_url="decor/snow/tile2.svg",
        height=100,
        width=100,
        theme=get_theme("snow"),
        pk=15,
    ),
    ("house", "farm"): Decor(
        z_index=1,
        name="house",
        url="decor/farm/house1.svg",
        xmas_url="decor/snow/house1.svg",
        height=224,
        width=184,
        theme=get_theme("farm"),
        pk=16,
    ),
    ("cfc", "farm"): Decor(
        z_index=1,
        name="cfc",
        url="decor/farm/cfc.svg",
        xmas_url="decor/snow/barn.svg",
        height=301,
        width=332,
        theme=get_theme("farm"),
        pk=17,
    ),
    ("bush", "farm"): Decor(
        z_index=3,
        name="bush",
        url="decor/farm/bush.svg",
        xmas_url="decor/snow/bush.svg",
        height=30,
        width=50,
        theme=get_theme("farm"),
        pk=18,
    ),
    ("tree1", "farm"): Decor(
        z_index=4,
        name="tree1",
        url="decor/farm/tree1.svg",
        xmas_url="decor/snow/tree1.svg",
        height=100,
        width=100,
        theme=get_theme("farm"),
        pk=19,
    ),
    ("tree2", "farm"): Decor(
        z_index=4,
        name="tree2",
        url="decor/farm/house2.svg",
        xmas_url="decor/snow/house.svg",
        height=88,
        width=65,
        theme=get_theme("farm"),
        pk=20,
    ),
    ("pond", "farm"): Decor(
        z_index=2,
        name="pond",
        url="decor/farm/crops.svg",
        xmas_url="decor/snow/crops.svg",
        height=100,
        width=150,
        theme=get_theme("farm"),
        pk=21,
    ),
    ("tile1", "farm"): Decor(
        z_index=0,
        name="tile1",
        url="decor/farm/tile1.svg",
        xmas_url="decor/snow/tile1.svg",
        height=337,
        width=194,
        theme=get_theme("farm"),
        pk=22,
    ),
    ("tile1", "city"): Decor(
        z_index=0,
        name="tile1",
        url="decor/city/pavementTile.png",
        xmas_url="decor/snow/tile1.svg",
        height=100,
        width=100,
        theme=get_theme("city"),
        pk=23,
    ),
    ("house", "city"): Decor(
        z_index=1,
        name="house",
        url="decor/city/house.svg",
        xmas_url="decor/snow/house2.svg",
        height=50,
        width=50,
        theme=get_theme("city"),
        pk=24,
    ),
    ("bush", "city"): Decor(
        z_index=3,
        name="bush",
        url="decor/city/bush.svg",
        xmas_url="decor/snow/bush.svg",
        height=50,
        width=50,
        theme=get_theme("city"),
        pk=25,
    ),
    ("tree1", "city"): Decor(
        z_index=4,
        name="tree1",
        url="decor/city/shop.svg",
        xmas_url="decor/snow/shop.svg",
        height=70,
        width=70,
        theme=get_theme("city"),
        pk=26,
    ),
    ("tree2", "city"): Decor(
        z_index=4,
        name="tree2",
        url="decor/city/school.svg",
        xmas_url="decor/snow/school.svg",
        height=100,
        width=100,
        theme=get_theme("city"),
        pk=27,
    ),
    ("pond", "city"): Decor(
        z_index=2,
        name="pond",
        url="decor/city/hospital.svg",
        xmas_url="decor/snow/hospital.svg",
        height=157,
        width=140,
        theme=get_theme("city"),
        pk=28,
    ),
    ("cfc", "city"): Decor(
        z_index=1,
        name="cfc",
        # FUTURE: add external branding option
        url="decor/grass/cfc.svg",
        xmas_url="decor/snow/cfc.svg",
        height=107,
        width=100,
        theme=get_theme("city"),
        pk=29,
    ),
    ("tile2", "grass"): Decor(
        z_index=0,
        name="tile2",
        url="decor/snow/tile2.svg",
        xmas_url="decor/snow/tile2.svg",
        height=100,
        width=100,
        theme=get_theme("grass"),
        pk=30,
    ),
    ("tile2", "farm"): Decor(
        z_index=0,
        name="tile2",
        url="decor/snow/tile2.svg",
        xmas_url="decor/snow/tile2.svg",
        height=100,
        width=100,
        theme=get_theme("farm"),
        pk=31,
    ),
    ("tile2", "city"): Decor(
        z_index=0,
        name="tile2",
        url="decor/snow/tile2.svg",
        xmas_url="decor/snow/tile2.svg",
        height=100,
        width=100,
        theme=get_theme("city"),
        pk=32,
    ),
    ("solar_panel", "grass"): Decor(
        z_index=4,
        name="solar_panel",
        url="decor/grass/solar_panel.svg",
        xmas_url="decor/snow/tree1.svg",
        height=100,
        width=100,
        theme=get_theme("grass"),
        pk=33
    ),
    ("solar_panel", "farm"): Decor(
        z_index=4,
        name="solar_panel",
        url="decor/farm/solar_panel.svg",
        xmas_url="decor/snow/tree1.svg",
        height=100,
        width=100,
        theme=get_theme("farm"),
        pk=34
    ),
    ("solar_panel", "snow"): Decor(
        z_index=4,
        name="solar_panel",
        url="decor/snow/solar_panel.svg",
        xmas_url="decor/snow/solar_panel.svg",
        height=100,
        width=100,
        theme=get_theme("snow"),
        pk=35
    ),
    ("solar_panel", "city"): Decor(
        z_index=4,
        name="solar_panel",
        url="decor/city/solar_panel.svg",
        xmas_url="decor/snow/solar_panel.svg",
        height=100,
        width=100,
        theme=get_theme("city"),
        pk=36
    )
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
