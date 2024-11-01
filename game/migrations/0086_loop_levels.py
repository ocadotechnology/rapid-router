import json

from django.apps.registry import Apps
from django.db import migrations

from game.level_management import set_blocks_inner


def add_loop_levels(apps: Apps, *args):
    Level = apps.get_model("game", "Level")
    LevelBlock = apps.get_model("game", "LevelBlock")
    Block = apps.get_model("game", "Block")
    LevelDecor = apps.get_model("game", "LevelDecor")
    Episode = apps.get_model("game", "Episode")

    episode_15 = Episode.objects.create(
        pk=15,
        name="For Loops - coming soon",
    )
    episode_14 = Episode.objects.create(
        pk=14,
        next_episode=episode_15,
        name="Selection in a Loop - coming soon",
    )
    episode_13 = Episode.objects.create(
        pk=13,
        next_episode=episode_14,
        name="Indeterminate WHILE Loops - coming soon",
    )
    episode_12 = Episode.objects.create(
        pk=12,
        next_episode=episode_13,
        name="Sequencing and Counted Loops",
    )

    episode_11 = Episode.objects.get(pk=11)
    episode_11.next_episode = episode_12
    episode_11.save()

    # Episode 15, Levels 149 - 153
    level_153 = Level.objects.create(
        name="153",
        episode=episode_15,
    )
    level_152 = Level.objects.create(
        name="152",
        episode=episode_15,
        next_level=level_153,
    )
    level_151 = Level.objects.create(
        name="151",
        episode=episode_15,
        next_level=level_152,
    )
    level_150 = Level.objects.create(
        name="150",
        episode=episode_15,
        next_level=level_151,
    )
    level_149 = Level.objects.create(
        name="149",
        episode=episode_15,
        next_level=level_150,
    )

    # Episode 14, Levels 141 - 148
    level_148 = Level.objects.create(
        name="148",
        episode=episode_14,
        next_level=level_149,
    )
    level_147 = Level.objects.create(
        name="147",
        episode=episode_14,
        next_level=level_148,
    )
    level_146 = Level.objects.create(
        name="146",
        episode=episode_14,
        next_level=level_147,
    )
    level_145 = Level.objects.create(
        name="145",
        episode=episode_14,
        next_level=level_146,
    )
    level_144 = Level.objects.create(
        name="144",
        episode=episode_14,
        next_level=level_145,
    )
    level_143 = Level.objects.create(
        name="143",
        episode=episode_14,
        next_level=level_144,
    )
    level_142 = Level.objects.create(
        name="142",
        episode=episode_14,
        next_level=level_143,
    )
    level_141 = Level.objects.create(
        name="141",
        episode=episode_14,
        next_level=level_142,
    )

    # Episode 13, Levels 123 - 140
    level_140 = Level.objects.create(
        name="140",
        episode=episode_13,
        next_level=level_141,
    )
    level_139 = Level.objects.create(
        name="139",
        episode=episode_13,
        next_level=level_140,
    )
    level_138 = Level.objects.create(
        name="138",
        episode=episode_13,
        next_level=level_139,
    )
    level_137 = Level.objects.create(
        name="137",
        episode=episode_13,
        next_level=level_138,
    )
    level_136 = Level.objects.create(
        name="136",
        episode=episode_13,
        next_level=level_137,
    )
    level_135 = Level.objects.create(
        name="135",
        episode=episode_13,
        next_level=level_136,
    )
    level_134 = Level.objects.create(
        name="134",
        episode=episode_13,
        next_level=level_135,
    )
    level_133 = Level.objects.create(
        name="133",
        episode=episode_13,
        next_level=level_134,
    )
    level_132 = Level.objects.create(
        name="132",
        episode=episode_13,
        next_level=level_133,
    )
    level_131 = Level.objects.create(
        name="131",
        episode=episode_13,
        next_level=level_132,
    )
    level_130 = Level.objects.create(
        name="130",
        episode=episode_13,
        next_level=level_131,
    )
    level_129 = Level.objects.create(
        name="129",
        episode=episode_13,
        next_level=level_130,
    )
    level_128 = Level.objects.create(
        name="128",
        episode=episode_13,
        next_level=level_129,
    )
    level_127 = Level.objects.create(
        name="127",
        episode=episode_13,
        next_level=level_128,
    )
    level_126 = Level.objects.create(
        name="126",
        episode=episode_13,
        next_level=level_127,
    )
    level_125 = Level.objects.create(
        name="125",
        episode=episode_13,
        next_level=level_126,
    )
    level_124 = Level.objects.create(
        name="124",
        episode=episode_13,
        next_level=level_125,
    )
    level_123 = Level.objects.create(
        name="123",
        episode=episode_13,
        next_level=level_124,
    )

    # Episode 12, Levels 110 - 122
    level_122 = Level.objects.create(
        name="122",
        episode=episode_12,
        # next_level=level_123, TODO: connect them when the next levels are enabled.
        path='[{"coordinate":[1,5],"connectedNodes":[1]},{"coordinate":[1,4],"connectedNodes":[0,2]},{"coordinate":[2,4],"connectedNodes":[1,3]},{"coordinate":[2,5],"connectedNodes":[4,2]},{"coordinate":[3,5],"connectedNodes":[3,5]},{"coordinate":[3,4],"connectedNodes":[4,6]},{"coordinate":[4,4],"connectedNodes":[5,7]},{"coordinate":[4,5],"connectedNodes":[8,6]},{"coordinate":[5,5],"connectedNodes":[7,9]},{"coordinate":[5,4],"connectedNodes":[8,10]},{"coordinate":[6,4],"connectedNodes":[9,11]},{"coordinate":[6,5],"connectedNodes":[12,10]},{"coordinate":[7,5],"connectedNodes":[11,13]},{"coordinate":[7,4],"connectedNodes":[12,14]},{"coordinate":[7,3],"connectedNodes":[13,15]},{"coordinate":[7,2],"connectedNodes":[14,16]},{"coordinate":[7,1],"connectedNodes":[17,15]},{"coordinate":[6,1],"connectedNodes":[18,16]},{"coordinate":[6,2],"connectedNodes":[19,17]},{"coordinate":[5,2],"connectedNodes":[18,20]},{"coordinate":[5,1],"connectedNodes":[21,19]},{"coordinate":[4,1],"connectedNodes":[22,20]},{"coordinate":[4,2],"connectedNodes":[23,21]},{"coordinate":[3,2],"connectedNodes":[22,24]},{"coordinate":[3,1],"connectedNodes":[25,23]},{"coordinate":[2,1],"connectedNodes":[26,24]},{"coordinate":[2,2],"connectedNodes":[27,25]},{"coordinate":[1,2],"connectedNodes":[26,28]},{"coordinate":[1,1],"connectedNodes":[27]}]',
        origin='{"coordinate":[1,5],"direction":"S"}',
        destinations="[[1,1]]",
        default=True,
        blocklyEnabled=False,
        theme_name="grass",
        character_name="Van",
    )
    level_121 = Level.objects.create(
        name="121",
        episode=episode_12,
        next_level=level_122,
        path='[{"coordinate":[1,7],"connectedNodes":[1]},{"coordinate":[1,6],"connectedNodes":[0,2,13]},{"coordinate":[2,6],"connectedNodes":[1,25,3]},{"coordinate":[2,5],"connectedNodes":[2,4]},{"coordinate":[3,5],"connectedNodes":[3,5]},{"coordinate":[3,4],"connectedNodes":[4,6]},{"coordinate":[4,4],"connectedNodes":[5,7]},{"coordinate":[4,3],"connectedNodes":[23,6,8]},{"coordinate":[5,3],"connectedNodes":[7,9]},{"coordinate":[5,2],"connectedNodes":[8,10]},{"coordinate":[6,2],"connectedNodes":[9,31,11]},{"coordinate":[6,1],"connectedNodes":[21,10,12]},{"coordinate":[7,1],"connectedNodes":[11,32]},{"coordinate":[1,5],"connectedNodes":[1,14]},{"coordinate":[1,4],"connectedNodes":[13,15]},{"coordinate":[1,3],"connectedNodes":[14,22,16]},{"coordinate":[1,2],"connectedNodes":[15,17]},{"coordinate":[1,1],"connectedNodes":[16,18]},{"coordinate":[2,1],"connectedNodes":[17,19]},{"coordinate":[3,1],"connectedNodes":[18,24,20]},{"coordinate":[4,1],"connectedNodes":[19,21]},{"coordinate":[5,1],"connectedNodes":[20,11]},{"coordinate":[2,3],"connectedNodes":[15,23]},{"coordinate":[3,3],"connectedNodes":[22,7,24]},{"coordinate":[3,2],"connectedNodes":[23,19]},{"coordinate":[3,6],"connectedNodes":[2,26]},{"coordinate":[4,6],"connectedNodes":[25,27]},{"coordinate":[5,6],"connectedNodes":[26,28]},{"coordinate":[6,6],"connectedNodes":[27,29]},{"coordinate":[6,5],"connectedNodes":[28,30]},{"coordinate":[6,4],"connectedNodes":[29,31]},{"coordinate":[6,3],"connectedNodes":[30,10]},{"coordinate":[7,0],"connectedNodes":[12]}]',
        origin='{"coordinate":[1,7],"direction":"S"}',
        destinations="[[7,0]]",
        default=True,
        blocklyEnabled=False,
        theme_name="farm",
        character_name="Van",
    )
    level_120 = Level.objects.create(
        name="120",
        episode=episode_12,
        next_level=level_121,
        path='[{"coordinate":[9,5],"connectedNodes":[1]},{"coordinate":[8,5],"connectedNodes":[2,0]},{"coordinate":[7,5],"connectedNodes":[1,3]},{"coordinate":[7,4],"connectedNodes":[4,2,20]},{"coordinate":[6,4],"connectedNodes":[5,3]},{"coordinate":[5,4],"connectedNodes":[13,4,6]},{"coordinate":[5,3],"connectedNodes":[7,5]},{"coordinate":[4,3],"connectedNodes":[8,6]},{"coordinate":[3,3],"connectedNodes":[7,9]},{"coordinate":[3,2],"connectedNodes":[10,8,24]},{"coordinate":[2,2],"connectedNodes":[11,9]},{"coordinate":[1,2],"connectedNodes":[19,10,12]},{"coordinate":[1,1],"connectedNodes":[25,11]},{"coordinate":[5,5],"connectedNodes":[14,5]},{"coordinate":[4,5],"connectedNodes":[15,13]},{"coordinate":[3,5],"connectedNodes":[16,14]},{"coordinate":[2,5],"connectedNodes":[17,15]},{"coordinate":[1,5],"connectedNodes":[16,18]},{"coordinate":[1,4],"connectedNodes":[17,19]},{"coordinate":[1,3],"connectedNodes":[18,11]},{"coordinate":[7,3],"connectedNodes":[3,21]},{"coordinate":[7,2],"connectedNodes":[22,20]},{"coordinate":[6,2],"connectedNodes":[23,21]},{"coordinate":[5,2],"connectedNodes":[24,22]},{"coordinate":[4,2],"connectedNodes":[9,23]},{"coordinate":[0,1],"connectedNodes":[12]}]',
        origin='{"coordinate":[9,5],"direction":"W"}',
        destinations="[[0,1]]",
        default=True,
        blocklyEnabled=False,
        theme_name="grass",
        character_name="Van",
    )
    level_119 = Level.objects.create(
        name="119",
        episode=episode_12,
        next_level=level_120,
        path='[{"coordinate":[2,3],"connectedNodes":[1]},{"coordinate":[2,2],"connectedNodes":[0,2]},{"coordinate":[3,2],"connectedNodes":[1,3]},{"coordinate":[3,1],"connectedNodes":[2,4]},{"coordinate":[4,1],"connectedNodes":[3,5]},{"coordinate":[5,1],"connectedNodes":[4,6]},{"coordinate":[5,2],"connectedNodes":[7,5]},{"coordinate":[6,2],"connectedNodes":[6,8]},{"coordinate":[6,3],"connectedNodes":[9,7]},{"coordinate":[6,4],"connectedNodes":[10,8]},{"coordinate":[5,4],"connectedNodes":[11,9]},{"coordinate":[5,5],"connectedNodes":[12,10]},{"coordinate":[4,5],"connectedNodes":[13,11]},{"coordinate":[3,5],"connectedNodes":[12]}]',
        origin='{"coordinate":[2,3],"direction":"S"}',
        destinations="[[3,5]]",
        default=True,
        blocklyEnabled=False,
        theme_name="grass",
        character_name="Van",
    )
    level_118 = Level.objects.create(
        name="118",
        episode=episode_12,
        next_level=level_119,
        path='[{"coordinate":[1,3],"connectedNodes":[1]},{"coordinate":[2,3],"connectedNodes":[0,2]},{"coordinate":[3,3],"connectedNodes":[1,3]},{"coordinate":[3,4],"connectedNodes":[4,2]},{"coordinate":[4,4],"connectedNodes":[3,5]},{"coordinate":[4,5],"connectedNodes":[6,4]},{"coordinate":[5,5],"connectedNodes":[5,7]},{"coordinate":[5,6],"connectedNodes":[8,6]},{"coordinate":[6,6],"connectedNodes":[7,9]},{"coordinate":[7,6],"connectedNodes":[8,10]},{"coordinate":[8,6],"connectedNodes":[9]}]',
        origin='{"coordinate":[1,3],"direction":"E"}',
        destinations="[[8,6]]",
        default=True,
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="snow",
        character_name="Van",
        model_solution="[11]",
    )
    level_117 = Level.objects.create(
        name="117",
        episode=episode_12,
        next_level=level_118,
        path='[{"coordinate":[2,2],"connectedNodes":[1]},{"coordinate":[3,2],"connectedNodes":[0,2]},{"coordinate":[3,3],"connectedNodes":[3,1]},{"coordinate":[4,3],"connectedNodes":[2,4]},{"coordinate":[4,4],"connectedNodes":[5,3]},{"coordinate":[5,4],"connectedNodes":[4,6]},{"coordinate":[5,5],"connectedNodes":[7,5]},{"coordinate":[6,5],"connectedNodes":[6,8]},{"coordinate":[6,6],"connectedNodes":[9,7]},{"coordinate":[7,6],"connectedNodes":[8]}]',
        origin='{"coordinate":[2,2],"direction":"E"}',
        destinations="[[7,6]]",
        default=True,
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="snow",
        character_name="Van",
        model_solution="[8]",
    )
    level_116 = Level.objects.create(
        name="116",
        episode=episode_12,
        next_level=level_117,
        path='[{"coordinate":[1,4],"connectedNodes":[1]},{"coordinate":[2,4],"connectedNodes":[0,2]},{"coordinate":[3,4],"connectedNodes":[1,3]},{"coordinate":[4,4],"connectedNodes":[2,4]},{"coordinate":[5,4],"connectedNodes":[3,5]},{"coordinate":[6,4],"connectedNodes":[4]}]',
        origin='{"coordinate":[1,4],"direction":"E"}',
        destinations="[[6,4]]",
        default=True,
        pythonEnabled=False,
        theme_name="grass",
        character_name="Van",
        model_solution="[7]",
    )
    level_115 = Level.objects.create(
        name="115",
        episode=episode_12,
        next_level=level_116,
        path='[{"coordinate":[9,2],"connectedNodes":[1]},{"coordinate":[8,2],"connectedNodes":[26,0,2]},{"coordinate":[8,1],"connectedNodes":[3,1]},{"coordinate":[7,1],"connectedNodes":[4,2]},{"coordinate":[6,1],"connectedNodes":[5,20,3]},{"coordinate":[5,1],"connectedNodes":[6,4]},{"coordinate":[4,1],"connectedNodes":[7,5]},{"coordinate":[3,1],"connectedNodes":[8,6]},{"coordinate":[3,2],"connectedNodes":[9,7]},{"coordinate":[4,2],"connectedNodes":[8,10]},{"coordinate":[4,3],"connectedNodes":[11,9]},{"coordinate":[3,3],"connectedNodes":[12,10]},{"coordinate":[3,4],"connectedNodes":[13,11]},{"coordinate":[3,5],"connectedNodes":[14,12]},{"coordinate":[4,5],"connectedNodes":[13,15]},{"coordinate":[5,5],"connectedNodes":[14,16,17]},{"coordinate":[5,6],"connectedNodes":[21,15]},{"coordinate":[5,4],"connectedNodes":[15,18]},{"coordinate":[6,4],"connectedNodes":[17,19]},{"coordinate":[6,3],"connectedNodes":[18,27,20]},{"coordinate":[6,2],"connectedNodes":[19,4]},{"coordinate":[6,6],"connectedNodes":[16,22]},{"coordinate":[7,6],"connectedNodes":[21,23]},{"coordinate":[8,6],"connectedNodes":[22,24]},{"coordinate":[8,5],"connectedNodes":[23,25]},{"coordinate":[8,4],"connectedNodes":[24,26]},{"coordinate":[8,3],"connectedNodes":[27,25,1]},{"coordinate":[7,3],"connectedNodes":[19,26]}]',
        origin='{"coordinate":[9,2],"direction":"W"}',
        destinations="[[4,5]]",
        default=True,
        blocklyEnabled=False,
        theme_name="grass",
        character_name="Van",
    )
    level_114 = Level.objects.create(
        name="114",
        episode=episode_12,
        next_level=level_115,
        path='[{"coordinate":[0,2],"connectedNodes":[1]},{"coordinate":[1,2],"connectedNodes":[0,2]},{"coordinate":[1,3],"connectedNodes":[3,1]},{"coordinate":[1,4],"connectedNodes":[4,2]},{"coordinate":[1,5],"connectedNodes":[5,3]},{"coordinate":[2,5],"connectedNodes":[4,6]},{"coordinate":[2,4],"connectedNodes":[5,7]},{"coordinate":[3,4],"connectedNodes":[6,8]},{"coordinate":[3,3],"connectedNodes":[7,9]},{"coordinate":[3,2],"connectedNodes":[8,10]},{"coordinate":[3,1],"connectedNodes":[9,11]},{"coordinate":[4,1],"connectedNodes":[10,12]},{"coordinate":[4,2],"connectedNodes":[13,11]},{"coordinate":[5,2],"connectedNodes":[12]}]',
        origin='{"coordinate":[0,2],"direction":"E"}',
        destinations="[[5,2]]",
        default=True,
        blocklyEnabled=False,
        theme_name="grass",
        character_name="Van",
    )
    level_113 = Level.objects.create(
        name="113",
        episode=episode_12,
        next_level=level_114,
        path='[{"coordinate":[4,7],"connectedNodes":[1]},{"coordinate":[4,6],"connectedNodes":[0,2]},{"coordinate":[4,5],"connectedNodes":[3,1]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[3,4],"connectedNodes":[3,5]},{"coordinate":[3,3],"connectedNodes":[4]}]',
        origin='{"coordinate":[4,7],"direction":"S"}',
        destinations="[[3,3]]",
        default=True,
        blocklyEnabled=False,
        theme_name="farm",
        character_name="Van",
    )
    level_112 = Level.objects.create(
        name="112",
        episode=episode_12,
        next_level=level_113,
        path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[3,6],"connectedNodes":[1,3,17]},{"coordinate":[4,6],"connectedNodes":[2,4]},{"coordinate":[5,6],"connectedNodes":[3,5]},{"coordinate":[6,6],"connectedNodes":[4,6]},{"coordinate":[6,5],"connectedNodes":[5,7]},{"coordinate":[6,4],"connectedNodes":[20,6,8]},{"coordinate":[6,3],"connectedNodes":[7,9]},{"coordinate":[6,2],"connectedNodes":[8,10]},{"coordinate":[6,1],"connectedNodes":[11,9]},{"coordinate":[5,1],"connectedNodes":[12,10]},{"coordinate":[4,1],"connectedNodes":[13,22,11]},{"coordinate":[3,1],"connectedNodes":[14,12]},{"coordinate":[2,1],"connectedNodes":[15,13]},{"coordinate":[1,1],"connectedNodes":[16,14]},{"coordinate":[0,1],"connectedNodes":[15]},{"coordinate":[3,5],"connectedNodes":[2,18]},{"coordinate":[3,4],"connectedNodes":[17,19]},{"coordinate":[4,4],"connectedNodes":[18,20,21]},{"coordinate":[5,4],"connectedNodes":[19,7]},{"coordinate":[4,3],"connectedNodes":[19,22]},{"coordinate":[4,2],"connectedNodes":[21,12]}]',
        origin='{"coordinate":[2,7],"direction":"S"}',
        destinations="[[0,1]]",
        default=True,
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="grass",
        character_name="Van",
        model_solution="[11]",
    )
    level_111 = Level.objects.create(
        name="111",
        episode=episode_12,
        next_level=level_112,
        path='[{"coordinate":[0,5],"connectedNodes":[1]},{"coordinate":[1,5],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[1,3]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[3,6],"connectedNodes":[5,3]},{"coordinate":[4,6],"connectedNodes":[4,6]},{"coordinate":[5,6],"connectedNodes":[5,7]},{"coordinate":[5,5],"connectedNodes":[6,8]},{"coordinate":[5,4],"connectedNodes":[7,9]},{"coordinate":[5,3],"connectedNodes":[8,10]},{"coordinate":[5,2],"connectedNodes":[9,11]},{"coordinate":[6,2],"connectedNodes":[10]}]',
        origin='{"coordinate":[0,5],"direction":"E"}',
        destinations="[[6,2]]",
        default=True,
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="grass",
        character_name="Van",
    )
    level_110 = Level.objects.create(
        name="110",
        episode=episode_12,
        next_level=level_111,
        path='[{"coordinate":[0,2],"connectedNodes":[2]},{"coordinate":[2,2],"connectedNodes":[2,3]},{"coordinate":[1,2],"connectedNodes":[0,1]},{"coordinate":[2,3],"connectedNodes":[4,1]},{"coordinate":[2,4],"connectedNodes":[5,3]},{"coordinate":[3,4],"connectedNodes":[4,6]},{"coordinate":[4,4],"connectedNodes":[5]}]',
        origin='{"coordinate":[0,2],"direction":"E"}',
        destinations="[[4,4]]",
        default=True,
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="farm",
        character_name="Van",
    )

    def set_decor(level, decor):
        """Helper method creating LevelDecor objects given a list of decor in dictionary form."""
        LevelDecor.objects.filter(level=level).delete()

        level_decors = []
        for data in decor:
            level_decors.append(
                LevelDecor(
                    level_id=level.id, x=data["x"], y=data["y"], decorName=data[
                        "decorName"]
                )
            )
        LevelDecor.objects.bulk_create(level_decors)

    set_decor(
        level_110,
        json.loads('[{"x":503,"y":409,"decorName":"tree2"},{"x":384,"y":503,"decorName":"bush"},{"x":355,"y":549,"decorName":"bush"},{"x":320,"y":503,"decorName":"bush"},{"x":399,"y":200,"decorName":"pond"},{"x":400,"y":299,"decorName":"pond"}]')
    )
    set_decor(
        level_111,
        json.loads('[{"x":611,"y":568,"decorName":"tree2"},{"x":595,"y":648,"decorName":"tree1"},{"x":714,"y":454,"decorName":"tree2"},{"x":652,"y":328,"decorName":"tree2"},{"x":600,"y":447,"decorName":"tree2"},{"x":651,"y":498,"decorName":"tree1"},{"x":366,"y":286,"decorName":"tree2"},{"x":285,"y":257,"decorName":"tree2"},{"x":206,"y":283,"decorName":"tree1"},{"x":82,"y":385,"decorName":"tree1"},{"x":46,"y":324,"decorName":"tree1"},{"x":233,"y":355,"decorName":"tree1"},{"x":637,"y":400,"decorName":"tree1"},{"x":87,"y":258,"decorName":"tree2"},{"x":291,"y":321,"decorName":"tree1"},{"x":164,"y":388,"decorName":"tree2"},{"x":129,"y":334,"decorName":"tree1"},{"x":128,"y":593,"decorName":"tree2"},{"x":235,"y":685,"decorName":"tree2"},{"x":103,"y":688,"decorName":"tree2"},{"x":181,"y":635,"decorName":"tree1"},{"x":70,"y":625,"decorName":"tree1"}]')
    )
    set_decor(
        level_112,
        json.loads('[{"x":50,"y":625,"decorName":"tree1"},{"x":50,"y":207,"decorName":"tree1"},{"x":50,"y":321,"decorName":"tree1"},{"x":50,"y":426,"decorName":"tree1"},{"x":50,"y":529,"decorName":"tree1"},{"x":398,"y":485,"decorName":"tree2"},{"x":500,"y":513,"decorName":"tree2"},{"x":500,"y":198,"decorName":"bush"},{"x":500,"y":274,"decorName":"bush"},{"x":500,"y":352,"decorName":"bush"}]')
    )
    set_decor(
        level_113,
        json.loads('[{"x":404,"y":415,"decorName":"tree2"},{"x":251,"y":420,"decorName":"bush"},{"x":187,"y":420,"decorName":"bush"},{"x":128,"y":420,"decorName":"bush"},{"x":221,"y":460,"decorName":"bush"},{"x":153,"y":460,"decorName":"bush"},{"x":183,"y":500,"decorName":"bush"},{"x":203,"y":596,"decorName":"pond"},{"x":203,"y":696,"decorName":"pond"}]')
    )
    set_decor(
        level_114,
        json.loads('[{"x":2,"y":438,"decorName":"tree1"},{"x":2,"y":543,"decorName":"tree1"},{"x":2,"y":329,"decorName":"tree1"},{"x":548,"y":556,"decorName":"tree1"},{"x":563,"y":469,"decorName":"tree1"},{"x":475,"y":549,"decorName":"tree2"},{"x":419,"y":514,"decorName":"tree1"},{"x":488,"y":434,"decorName":"tree2"}]')
    )
    set_decor(
        level_115,
        json.loads('[{"x":885,"y":343,"decorName":"tree1"},{"x":885,"y":440,"decorName":"tree1"},{"x":406,"y":383,"decorName":"tree2"},{"x":498,"y":306,"decorName":"tree2"},{"x":484,"y":190,"decorName":"tree2"}]')
    )
    set_decor(
        level_116,
        json.loads('[{"x":220,"y":305,"decorName":"pond"},{"x":539,"y":569,"decorName":"tree2"},{"x":569,"y":516,"decorName":"tree1"},{"x":498,"y":497,"decorName":"tree2"},{"x":182,"y":165,"decorName":"tree2"},{"x":225,"y":228,"decorName":"tree1"},{"x":159,"y":245,"decorName":"tree1"},{"x":312,"y":254,"decorName":"tree2"}]')
    )
    set_decor(
        level_117,
        json.loads('[{"x":443,"y":578,"decorName":"pond"},{"x":412,"y":648,"decorName":"tree1"},{"x":516,"y":651,"decorName":"tree2"},{"x":694,"y":341,"decorName":"tree1"},{"x":647,"y":292,"decorName":"tree2"},{"x":623,"y":362,"decorName":"tree1"},{"x":640,"y":434,"decorName":"tree2"}]')
    )
    set_decor(
        level_118,
        json.loads('[{"x":711,"y":507,"decorName":"tree2"},{"x":605,"y":508,"decorName":"tree2"},{"x":193,"y":396,"decorName":"bush"},{"x":250,"y":398,"decorName":"bush"}]')
    )
    set_decor(
        level_119,
        json.loads('[{"x":250,"y":391,"decorName":"tree2"},{"x":367,"y":237,"decorName":"tree1"},{"x":463,"y":317,"decorName":"tree2"},{"x":364,"y":395,"decorName":"tree1"}]')
    )
    set_decor(
        level_120,
        json.loads('[{"x":189,"y":337,"decorName":"pond"},{"x":793,"y":368,"decorName":"tree1"},{"x":814,"y":285,"decorName":"tree2"},{"x":869,"y":389,"decorName":"tree2"},{"x":334,"y":413,"decorName":"tree1"},{"x":403,"y":402,"decorName":"tree2"},{"x":192,"y":410,"decorName":"tree1"}]')
    )
    set_decor(
        level_121,
        json.loads('[{"x":383,"y":500,"decorName":"pond"},{"x":700,"y":500,"decorName":"pond"},{"x":700,"y":400,"decorName":"pond"},{"x":700,"y":300,"decorName":"pond"},{"x":550,"y":433,"decorName":"bush"},{"x":549,"y":467,"decorName":"bush"},{"x":550,"y":395,"decorName":"bush"},{"x":186,"y":431,"decorName":"tree1"},{"x":196,"y":387,"decorName":"tree1"},{"x":541,"y":501,"decorName":"tree2"}]')
    )
    set_decor(
        level_122,
        json.loads('[{"x":150,"y":320,"decorName":"bush"},{"x":350,"y":320,"decorName":"bush"},{"x":550,"y":320,"decorName":"bush"}]')
    )

    def set_blocks(level, blocks):
        set_blocks_inner(level, blocks, LevelBlock, Block)

    set_blocks(
        level_110,
        json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"}]'),
    )
    set_blocks(
        level_111,
        json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"}]'),
    )
    set_blocks(
        level_112,
        json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"}]'),
    )
    set_blocks(
        level_116,
        json.loads('[{"type":"move_forwards"},{"type":"controls_repeat_while"},{"type":"variables_numeric_set"},{"type":"variables_increment"},{"type":"variables_get"},{"type":"math_number"},{"type":"logic_compare"}]'),
    )
    set_blocks(
        level_117,
        json.loads('[{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat_while"},{"type":"variables_numeric_set"},{"type":"variables_increment"},{"type":"variables_get"},{"type":"math_number"},{"type":"logic_compare"}]'),
    )
    set_blocks(
        level_118,
        json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat_while"},{"type":"variables_numeric_set"},{"type":"variables_increment"},{"type":"variables_get"},{"type":"math_number"},{"type":"logic_compare"}]'),
    )

    level_109 = Level.objects.get(name="109")
    level_109.next_level = level_110
    level_109.save()


def delete_loop_levels(apps: Apps, *args):
    Level = apps.get_model("game", "Level")
    Episode = apps.get_model("game", "Episode")

    Level.objects.filter(episode__pk__in=range(12, 16)).delete()
    Episode.objects.filter(pk__in=range(12, 16)).delete()


class Migration(migrations.Migration):
    dependencies = [("game", "0085_add_new_blocks")]
    operations = [
        migrations.RunPython(
            add_loop_levels,
            reverse_code=delete_loop_levels,
        )
    ]
