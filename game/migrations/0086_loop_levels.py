from django.apps.registry import Apps
from django.db import migrations


def add_loop_levels(apps: Apps, *args):
    Level = apps.get_model("game", "Level")
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
        path="",
    )
    level_152 = Level.objects.create(
        name="152",
        episode=episode_15,
        path="",
        next_level=level_153,
    )
    level_151 = Level.objects.create(
        name="151",
        episode=episode_15,
        path="",
        next_level=level_152,
    )
    level_150 = Level.objects.create(
        name="150",
        episode=episode_15,
        path="",
        next_level=level_151,
    )
    level_149 = Level.objects.create(
        name="149",
        episode=episode_15,
        path="",
        next_level=level_150,
    )

    # Episode 14, Levels 141 - 148
    level_148 = Level.objects.create(
        name="148",
        episode=episode_14,
        path="",
        next_level=level_149,
    )
    level_147 = Level.objects.create(
        name="147",
        episode=episode_14,
        path="",
        next_level=level_148,
    )
    level_146 = Level.objects.create(
        name="146",
        episode=episode_14,
        path="",
        next_level=level_147,
    )
    level_145 = Level.objects.create(
        name="145",
        episode=episode_14,
        path="",
        next_level=level_146,
    )
    level_144 = Level.objects.create(
        name="144",
        episode=episode_14,
        path="",
        next_level=level_145,
    )
    level_143 = Level.objects.create(
        name="143",
        episode=episode_14,
        path="",
        next_level=level_144,
    )
    level_142 = Level.objects.create(
        name="142",
        episode=episode_14,
        path="",
        next_level=level_143,
    )
    level_141 = Level.objects.create(
        name="141",
        episode=episode_14,
        path="",
        next_level=level_142,
    )

    # Episode 13, Levels 123 - 140
    level_140 = Level.objects.create(
        name="140",
        episode=episode_13,
        path="",
        next_level=level_141,
    )
    level_139 = Level.objects.create(
        name="139",
        episode=episode_13,
        path="",
        next_level=level_140,
    )
    level_138 = Level.objects.create(
        name="138",
        episode=episode_13,
        path="",
        next_level=level_139,
    )
    level_137 = Level.objects.create(
        name="137",
        episode=episode_13,
        path="",
        next_level=level_138,
    )
    level_136 = Level.objects.create(
        name="136",
        episode=episode_13,
        path="",
        next_level=level_137,
    )
    level_135 = Level.objects.create(
        name="135",
        episode=episode_13,
        path="",
        next_level=level_136,
    )
    level_134 = Level.objects.create(
        name="134",
        episode=episode_13,
        path="",
        next_level=level_135,
    )
    level_133 = Level.objects.create(
        name="133",
        episode=episode_13,
        path="",
        next_level=level_134,
    )
    level_132 = Level.objects.create(
        name="132",
        episode=episode_13,
        path="",
        next_level=level_133,
    )
    level_131 = Level.objects.create(
        name="131",
        episode=episode_13,
        path="",
        next_level=level_132,
    )
    level_130 = Level.objects.create(
        name="130",
        episode=episode_13,
        path="",
        next_level=level_131,
    )
    level_129 = Level.objects.create(
        name="129",
        episode=episode_13,
        path="",
        next_level=level_130,
    )
    level_128 = Level.objects.create(
        name="128",
        episode=episode_13,
        path="",
        next_level=level_129,
    )
    level_127 = Level.objects.create(
        name="127",
        episode=episode_13,
        path="",
        next_level=level_128,
    )
    level_126 = Level.objects.create(
        name="126",
        episode=episode_13,
        path="",
        next_level=level_127,
    )
    level_125 = Level.objects.create(
        name="125",
        episode=episode_13,
        path="",
        next_level=level_126,
    )
    level_124 = Level.objects.create(
        name="124",
        episode=episode_13,
        path="",
        next_level=level_125,
    )
    level_123 = Level.objects.create(
        name="123",
        episode=episode_13,
        path="",
        next_level=level_124,
    )

    # Episode 12, Levels 110 - 122
    level_122 = Level.objects.create(
        name="122",
        episode=episode_12,
        path="",
        # next_level=level_123, TODO: connect them when the next levels are enabled.
    )
    level_121 = Level.objects.create(
        name="121",
        episode=episode_12,
        path="",
        next_level=level_122,
    )
    level_120 = Level.objects.create(
        name="120",
        episode=episode_12,
        path="",
        next_level=level_121,
    )
    level_119 = Level.objects.create(
        name="119",
        episode=episode_12,
        path="",
        next_level=level_120,
    )
    level_118 = Level.objects.create(
        name="118",
        episode=episode_12,
        path="",
        next_level=level_119,
    )
    level_117 = Level.objects.create(
        name="117",
        episode=episode_12,
        path="",
        next_level=level_118,
    )
    level_116 = Level.objects.create(
        name="116",
        episode=episode_12,
        path="",
        next_level=level_117,
    )
    level_115 = Level.objects.create(
        name="115",
        episode=episode_12,
        path="",
        next_level=level_116,
    )
    level_114 = Level.objects.create(
        name="114",
        episode=episode_12,
        path="",
        next_level=level_115,
    )
    level_113 = Level.objects.create(
        name="113",
        episode=episode_12,
        path="",
        next_level=level_114,
    )
    level_112 = Level.objects.create(
        name="112",
        episode=episode_12,
        path="",
        next_level=level_113,
    )
    level_111 = Level.objects.create(
        name="111",
        episode=episode_12,
        path="",
        next_level=level_112,
    )
    level_110 = Level.objects.create(
        name="110",
        episode=episode_12,
        path="",
        next_level=level_111,
    )

    level_109 = Level.objects.get(name="109")
    level_109.next_level = level_110
    level_109.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0085_add_new_blocks")]
    operations = [
        migrations.RunPython(
            add_loop_levels,
            reverse_code=migrations.RunPython.noop,
        )
    ]
