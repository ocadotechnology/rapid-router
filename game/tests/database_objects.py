from game.models import Block, Decor, Episode, Level, LevelDecor, Theme


def setup_themes():
    Theme.objects.create(name='grass', background='a0c53a', border='#70961f', selected='#bce369')
    Theme.objects.create(name='snow', background='#eef7ff', border='#83c9fe', selected='#b3deff')
    Theme.objects.create(name='farm', background='#a0c53a', border='#70961f', selected='#bce369')
    Theme.objects.create(name='city', background='#969696', border='#686868', selected='#C1C1C1')


def setup_blocks():
    Block.objects.create(type='move_forwards')
    Block.objects.create(type='turn_left')
    Block.objects.create(type='turn_right')
    Block.objects.create(type='turn_around')
    Block.objects.create(type='wait')
    Block.objects.create(type='deliver')
    Block.objects.create(type='controls_repeat')
    Block.objects.create(type='controls_repeat_while')
    Block.objects.create(type='controls_repeat_until')
    Block.objects.create(type='controls_if')
    Block.objects.create(type='logic_negate')
    Block.objects.create(type='at_destination')
    Block.objects.create(type='road_exists')
    Block.objects.create(type='dead_end')
    Block.objects.create(type='traffic_light')
    Block.objects.create(type='call_proc')
    Block.objects.create(type='declare_proc')


def setup_decor():
    grass = Theme.objects.get(name='grass')
    snow = Theme.objects.get(name='snow')
    farm = Theme.objects.get(name='farm')
    city = Theme.objects.get(name='city')

    Decor.objects.create(name='tree1', theme=grass, url='decor/grass/tree1.svg', height=100,
                         width=100)
    Decor.objects.create(name='tree2', theme=grass, url='decor/grass/tree2.svg', height=100,
                         width=100)
    Decor.objects.create(name='bush', theme=grass, url='decor/grass/bush.svg', height=50,
                         width=50)
    Decor.objects.create(name='house', theme=grass, url='decor/grass/house.svg', height=50,
                         width=50)
    Decor.objects.create(name='cfc', theme=grass, url='decor/grass/cfc.svg', height=107,
                         width=100)
    Decor.objects.create(name='pond', theme=grass, url='decor/grass/pond.svg', height=100,
                         width=150)
    Decor.objects.create(name='tree1', theme=snow, url='decor/snow/tree1.svg', height=100,
                         width=100)
    Decor.objects.create(name='tree2', theme=snow, url='decor/snow/tree2.svg', height=100,
                         width=100)
    Decor.objects.create(name='bush', theme=snow, url='decor/snow/bush.svg', height=50,
                         width=50)
    Decor.objects.create(name='house', theme=snow, url='decor/snow/house.svg', height=50,
                         width=50)
    Decor.objects.create(name='cfc', theme=snow, url='decor/snow/cfc.svg', height=107,
                         width=100)
    Decor.objects.create(name='pond', theme=snow, url='decor/snow/pond.svg', height=100,
                         width=150)
    Decor.objects.create(name='tile1', theme=grass, url='decor/grass/tile1.svg', height=100,
                         width=100)
    Decor.objects.create(name='tile1', theme=snow, url='decor/snow/tile1.svg', height=100,
                         width=100)
    Decor.objects.create(name='tile2', theme=snow, url='decor/snow/tile2.svg', height=100,
                         width=100)
    Decor.objects.create(name='house', theme=farm, url='decor/farm/house1.svg', height=224,
                         width=184)
    Decor.objects.create(name='cfc', theme=farm, url='decor/farm/cfc.svg', height=301,
                         width=332)
    Decor.objects.create(name='bush', theme=farm, url='decor/farm/bush.svg', height=30,
                         width=50)
    Decor.objects.create(name='tree1', theme=farm, url='decor/farm/tree1.svg', height=100,
                         width=100)
    Decor.objects.create(name='tree2', theme=farm, url='decor/farm/house2.svg', height=88,
                         width=65)
    Decor.objects.create(name='pond', theme=farm, url='decor/farm/crops.svg', height=100,
                         width=150)
    Decor.objects.create(name='tile1', theme=farm, url='decor/farm/tile1.svg', height=337,
                         width=194)
    Decor.objects.create(name='tile1', theme=city, url='decor/city/pavementTile.png', height=100,
                         width=100)
    Decor.objects.create(name='house', theme=city, url='decor/city/house.svg', height=50,
                         width=50)
    Decor.objects.create(name='bush', theme=city, url='decor/city/bush.svg', height=50,
                         width=50)
    Decor.objects.create(name='tree1', theme=city, url='decor/city/shop.svg', height=70,
                         width=70)
    Decor.objects.create(name='tree2', theme=city, url='decor/city/school.svg', height=100,
                         width=100)
    Decor.objects.create(name='pond', theme=city, url='decor/city/hospital.svg', height=157,
                         width=140)
    