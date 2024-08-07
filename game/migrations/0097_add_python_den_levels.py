import json

from django.apps.registry import Apps
from django.db import migrations, models
from game.level_management import set_decor_inner, set_blocks_inner

def add_python_den_levels(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    Episode = apps.get_model("game", "Episode")

    episode20 = Episode.objects.get(pk=20)
    episode21 = Episode.objects.get(pk=21)
    episode22 = Episode.objects.get(pk=22)
    episode25 = Episode.objects.get(pk=25)
    episode26 = Episode.objects.get(pk=26)

    level1 = Level.objects.get(name="110", default=True)
    level1.name = "1001"
    level1.episode = episode20

    level2 = Level.objects.get(name="111", default=True)
    level2.name = "1002"
    level2.episode = episode20

    level3 = Level.objects.get(name="112", default=True)
    level3.name = "1003"
    level3.episode = episode20

    level4 = Level.objects.get(name="113", default=True)
    level4.name = "1004"
    level4.episode = episode20

    level5 = Level.objects.get(name="114", default=True)
    level5.name = "1005"
    level5.episode = episode20

    level6 = Level.objects.get(name="115", default=True)
    level6.name = "1006"
    level6.episode = episode20

    level7 = Level.objects.get(name="116", default=True)
    level7.name = "1007"
    level7.episode = episode20

    level8 = Level.objects.get(name="117", default=True)
    level8.name = "1008"
    level8.episode = episode20

    level9 = Level.objects.get(name="118", default=True)
    level9.name = "1009"
    level9.episode = episode20

    level10 = Level.objects.get(name="119", default=True)
    level10.name = "1010"
    level10.episode = episode20

    level11 = Level.objects.get(name="120", default=True)
    level11.name = "1011"
    level11.episode = episode20

    level12 = Level.objects.get(name="121", default=True)
    level12.name = "1012"
    level12.episode = episode20

    level13 = Level.objects.get(name="122", default=True)
    level13.name = "1013"
    level13.episode = episode20

    level14 = Level(
        name="1014",
        episode=episode21,
        anonymous=False,
        blocklyEnabled=True,
        character_name="Van",
        default=True,
        destinations="[[9,4]]",
        disable_algorithm_score=True,
        direct_drive=False,
        fuel_gauge=True,
        max_fuel=50,
        model_solution="[10]",
        origin='{"coordinate":[0,4],"direction":"E"}',
        path='[{"coordinate":[0,4],"connectedNodes":[1]},{"coordinate":[1,4],"connectedNodes":[0,2]},{"coordinate":[2,4],"connectedNodes":[1,3]},{"coordinate":[3,4],"connectedNodes":[2,4]},{"coordinate":[4,4],"connectedNodes":[3,5]},{"coordinate":[5,4],"connectedNodes":[4,6]},{"coordinate":[6,4],"connectedNodes":[5,7]},{"coordinate":[7,4],"connectedNodes":[6,8]},{"coordinate":[8,4],"connectedNodes":[7,9]},{"coordinate":[9,4],"connectedNodes":[8]}]',
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="farm",
        threads=1,
        traffic_lights="[]",
        cows='[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":2,"y":4},{"x":5,"y":4},{"x":7,"y":4}],"type":"WHITE"}]',
        lesson="This is a nice long straight road, but there are cows about!",
        hint="Make sure you sound the horn to get the cows off the road."
    )

    level15 = Level(
        name="1015",
        episode=episode21,
        path='[{"coordinate":[5,0],"connectedNodes":[1]},{"coordinate":[5,1],"connectedNodes":[2,0]},{"coordinate":[4,1],"connectedNodes":[3,1]},{"coordinate":[4,2],"connectedNodes":[4,2]},{"coordinate":[4,3],"connectedNodes":[5,3]},{"coordinate":[4,4],"connectedNodes":[6,4]},{"coordinate":[3,4],"connectedNodes":[7,5]},{"coordinate":[3,5],"connectedNodes":[8,6]},{"coordinate":[3,6],"connectedNodes":[9,7]},{"coordinate":[3,7],"connectedNodes":[8]}]',
        traffic_lights="[]",
        cows="[]",
        origin='{"coordinate":[5,0],"direction":"N"}',
        destinations="[[3,7]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[11]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=True,
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="farm",
        character_name="Van",
        lesson="There are some bends in this road. Be careful!",
        hint="What do you need to count, how many times you move or how many times you move forwards?",
        anonymous=False
    )

    level16 = Level(
        name="1016",
        episode=episode21,
        path='[{"coordinate":[1,1],"connectedNodes":[1]},{"coordinate":[1,2],"connectedNodes":[2,0]},{"coordinate":[2,2],"connectedNodes":[1,3]},{"coordinate":[2,3],"connectedNodes":[4,2]},{"coordinate":[3,3],"connectedNodes":[3,5]},{"coordinate":[3,4],"connectedNodes":[6,4]},{"coordinate":[4,4],"connectedNodes":[5,7]},{"coordinate":[4,5],"connectedNodes":[8,6]},{"coordinate":[5,5],"connectedNodes":[7,9]},{"coordinate":[5,6],"connectedNodes":[10,8]},{"coordinate":[6,6],"connectedNodes":[9,11]},{"coordinate":[6,7],"connectedNodes":[12,10]},{"coordinate":[7,7],"connectedNodes":[11]}]',
        traffic_lights="[]",
        cows='[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":3,"y":3},{"x":5,"y":5},{"x":4,"y":4}],"type":"WHITE"}]',
        origin='{"coordinate":[1,1],"direction":"N"}',
        destinations="[[7,7]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=False,
        pythonEnabled=True,
        pythonViewEnabled=False,
        theme_name="farm",
        character_name="Van",
        lesson="Oh no! The farmer seems to have let their cows out again. Be careful.",
        hint="Look for a pattern here...",
        anonymous=False
    )

    level17 = Level(
        name="1017",
        episode=episode21,
        path='[{"coordinate":[7,0],"connectedNodes":[1]},{"coordinate":[7,1],"connectedNodes":[2,0]},{"coordinate":[6,1],"connectedNodes":[3,1]},{"coordinate":[6,2],"connectedNodes":[4,2]},{"coordinate":[6,3],"connectedNodes":[5,3]},{"coordinate":[6,4],"connectedNodes":[6,4]},{"coordinate":[5,4],"connectedNodes":[7,5]},{"coordinate":[5,5],"connectedNodes":[8,6]},{"coordinate":[5,6],"connectedNodes":[7]}]',
        traffic_lights="[]",
        cows="[]",
        origin='{"coordinate":[7,0],"direction":"N"}',
        destinations="[[5,6]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=False,
        pythonEnabled=True,
        pythonViewEnabled=False,
        theme_name="grass",
        character_name="Van",
        lesson="Keep going, you're getting the hang of the Python code.",
        hint="So you are going forward unless...?",
        anonymous=False
    )

    level18 = Level(
        name="1018",
        episode=episode21,
        path='[{"coordinate":[7,1],"connectedNodes":[1]},{"coordinate":[7,2],"connectedNodes":[2,0]},{"coordinate":[7,3],"connectedNodes":[3,1]},{"coordinate":[7,4],"connectedNodes":[4,2]},{"coordinate":[7,5],"connectedNodes":[5,3]},{"coordinate":[6,5],"connectedNodes":[6,4]},{"coordinate":[5,5],"connectedNodes":[7,5]},{"coordinate":[4,5],"connectedNodes":[8,6]},{"coordinate":[3,5],"connectedNodes":[9,7]},{"coordinate":[2,5],"connectedNodes":[8,10]},{"coordinate":[2,4],"connectedNodes":[9,11]},{"coordinate":[2,3],"connectedNodes":[10,12]},{"coordinate":[2,2],"connectedNodes":[11,13]},{"coordinate":[2,1],"connectedNodes":[12,14]},{"coordinate":[3,1],"connectedNodes":[13,15]},{"coordinate":[4,1],"connectedNodes":[14,16]},{"coordinate":[5,1],"connectedNodes":[15,17]},{"coordinate":[6,1],"connectedNodes":[16,18]},{"coordinate":[6,2],"connectedNodes":[19,17]},{"coordinate":[6,3],"connectedNodes":[20,18]},{"coordinate":[6,4],"connectedNodes":[21,19]},{"coordinate":[5,4],"connectedNodes":[22,20]},{"coordinate":[4,4],"connectedNodes":[23,21]},{"coordinate":[3,4],"connectedNodes":[22,24]},{"coordinate":[3,3],"connectedNodes":[23,25]},{"coordinate":[3,2],"connectedNodes":[24,26]},{"coordinate":[4,2],"connectedNodes":[25,27]},{"coordinate":[5,2],"connectedNodes":[26]}]',
        traffic_lights="[]",
        cows="[]",
        origin='{"coordinate":[7,1],"direction":"N"}',
        destinations="[[5,2]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[10]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=False,
        pythonEnabled=True,
        pythonViewEnabled=False,
        theme_name="snow",
        character_name="Van",
        lesson="Oh dear, you might get a bit dizzy!",
        hint="What are you counting here, straight roads or bends?",
        anonymous=False
    )

    level19 = Level(
        name="1019",
        episode=episode21,
        path='[{"coordinate":[9,3],"connectedNodes":[1]},{"coordinate":[8,3],"connectedNodes":[2,0]},{"coordinate":[7,3],"connectedNodes":[3,1,15]},{"coordinate":[7,4],"connectedNodes":[4,2]},{"coordinate":[6,4],"connectedNodes":[5,3]},{"coordinate":[5,4],"connectedNodes":[6,4,12]},{"coordinate":[4,4],"connectedNodes":[7,5]},{"coordinate":[3,4],"connectedNodes":[8,6]},{"coordinate":[3,5],"connectedNodes":[9,7]},{"coordinate":[2,5],"connectedNodes":[10,8,17]},{"coordinate":[1,5],"connectedNodes":[11,9]},{"coordinate":[0,5],"connectedNodes":[10]},{"coordinate":[5,3],"connectedNodes":[5,13]},{"coordinate":[5,2],"connectedNodes":[21,12,14]},{"coordinate":[6,2],"connectedNodes":[13,15]},{"coordinate":[7,2],"connectedNodes":[14,2,16]},{"coordinate":[7,1],"connectedNodes":[15]},{"coordinate":[2,4],"connectedNodes":[9,18]},{"coordinate":[2,3],"connectedNodes":[17,19]},{"coordinate":[2,2],"connectedNodes":[18,20]},{"coordinate":[3,2],"connectedNodes":[19,21]},{"coordinate":[4,2],"connectedNodes":[20,13]}]',
        traffic_lights="[]",
        cows="[]",
        origin='{"coordinate":[9,3],"direction":"W"}',
        destinations="[[0,5]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[11]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=True,
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="grass",
        character_name="Van",
        lesson="Have you noticed that there are more roads ahead than turns? Try checking if there is a road ahead and then otherwise making the turns you need...",
        hint="Remember to use if..else",
        anonymous=False
    )

    level20 = Level(
        name="1020",
        episode=episode21,
        path='[{"coordinate":[2,2],"connectedNodes":[1]},{"coordinate":[3,2],"connectedNodes":[0,2,19]},{"coordinate":[3,3],"connectedNodes":[10,3,1]},{"coordinate":[4,3],"connectedNodes":[2,4]},{"coordinate":[4,4],"connectedNodes":[5,3]},{"coordinate":[5,4],"connectedNodes":[4,6,17]},{"coordinate":[5,5],"connectedNodes":[7,5]},{"coordinate":[6,5],"connectedNodes":[6,8]},{"coordinate":[6,6],"connectedNodes":[9,7]},{"coordinate":[7,6],"connectedNodes":[8]},{"coordinate":[3,4],"connectedNodes":[11,2]},{"coordinate":[3,5],"connectedNodes":[12,10]},{"coordinate":[3,6],"connectedNodes":[13,11]},{"coordinate":[3,7],"connectedNodes":[14,12]},{"coordinate":[4,7],"connectedNodes":[13,15]},{"coordinate":[5,7],"connectedNodes":[14,16]},{"coordinate":[6,7],"connectedNodes":[15]},{"coordinate":[5,3],"connectedNodes":[5,18]},{"coordinate":[5,2],"connectedNodes":[19,17]},{"coordinate":[4,2],"connectedNodes":[1,18]}]',
        traffic_lights="[]",
        cows="[]",
        origin='{"coordinate":[2,2],"direction":"E"}',
        destinations="[[7,6]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=False,
        pythonEnabled=True,
        pythonViewEnabled=False,
        theme_name="snow",
        character_name="Van",
        lesson="Use if..else in Python for this level",
        hint="Don't get distracted by the other roads. Look for a pattern you can repeat.",
        anonymous=False
    )

    level21 = Level(
        name="1021",
        episode=episode21,
        path='[{"coordinate":[4,0],"connectedNodes":[1]},{"coordinate":[4,1],"connectedNodes":[2,0]},{"coordinate":[3,1],"connectedNodes":[3,1]},{"coordinate":[3,2],"connectedNodes":[4,2]},{"coordinate":[3,3],"connectedNodes":[5,3]},{"coordinate":[3,4],"connectedNodes":[6,4]},{"coordinate":[2,4],"connectedNodes":[7,5]},{"coordinate":[2,5],"connectedNodes":[8,6]},{"coordinate":[2,6],"connectedNodes":[9,7]},{"coordinate":[1,6],"connectedNodes":[10,8]},{"coordinate":[1,7],"connectedNodes":[9]}]',
        traffic_lights="[]",
        cows="[]",
        origin='{"coordinate":[4,0],"direction":"N"}',
        destinations="[[3,1],[2,4],[1,6],[1,7]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=False,
        pythonEnabled=True,
        pythonViewEnabled=False,
        theme_name="grass",
        character_name="Van",
        lesson="This is a really busy road. Make sure that you don't miss any of the houses.",
        hint="Did you get the last house? Think about what value the loop counter will have at that point in your code...",
        anonymous=False
    )

    level22 = Level(
        name="1022",
        episode=episode21,
        path='[{"coordinate":[2,3],"connectedNodes":[1]},{"coordinate":[2,2],"connectedNodes":[0,2,16]},{"coordinate":[3,2],"connectedNodes":[1,3]},{"coordinate":[3,1],"connectedNodes":[2,4,14]},{"coordinate":[4,1],"connectedNodes":[3,5]},{"coordinate":[5,1],"connectedNodes":[4,6,22]},{"coordinate":[5,2],"connectedNodes":[7,5]},{"coordinate":[6,2],"connectedNodes":[6,8]},{"coordinate":[6,3],"connectedNodes":[9,17,7]},{"coordinate":[6,4],"connectedNodes":[10,8]},{"coordinate":[5,4],"connectedNodes":[11,9]},{"coordinate":[5,5],"connectedNodes":[12,10]},{"coordinate":[4,5],"connectedNodes":[13,11]},{"coordinate":[3,5],"connectedNodes":[12]},{"coordinate":[3,0],"connectedNodes":[15,3]},{"coordinate":[2,0],"connectedNodes":[16,14]},{"coordinate":[2,1],"connectedNodes":[1,15]},{"coordinate":[7,3],"connectedNodes":[8,18]},{"coordinate":[8,3],"connectedNodes":[17,19]},{"coordinate":[8,2],"connectedNodes":[18,20]},{"coordinate":[8,1],"connectedNodes":[21,19]},{"coordinate":[7,1],"connectedNodes":[22,20]},{"coordinate":[6,1],"connectedNodes":[5,21]}]',
        traffic_lights="[]",
        cows="[]",
        origin='{"coordinate":[2,3],"direction":"S"}',
        destinations="[[3,5]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[12]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=True,
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="grass",
        character_name="Van",
        lesson="There are lots of turns here, don't get distracted.",
        hint="Think about the order of the questions you ask using your if and elif statements.",
        anonymous=False
    )

    level23 = Level(
        name="1023",
        episode=episode21,
        path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[1,28,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,3],"connectedNodes":[3,5]},{"coordinate":[2,2],"connectedNodes":[4,6]},{"coordinate":[2,1],"connectedNodes":[5,7]},{"coordinate":[3,1],"connectedNodes":[6,8]},{"coordinate":[4,1],"connectedNodes":[7,9]},{"coordinate":[5,1],"connectedNodes":[8,10]},{"coordinate":[6,1],"connectedNodes":[9,11]},{"coordinate":[7,1],"connectedNodes":[10,12]},{"coordinate":[8,1],"connectedNodes":[11,13]},{"coordinate":[9,1],"connectedNodes":[12,14]},{"coordinate":[9,2],"connectedNodes":[15,13]},{"coordinate":[9,3],"connectedNodes":[16,14]},{"coordinate":[9,4],"connectedNodes":[17,15]},{"coordinate":[9,5],"connectedNodes":[18,16]},{"coordinate":[9,6],"connectedNodes":[19,17]},{"coordinate":[8,6],"connectedNodes":[20,18]},{"coordinate":[7,6],"connectedNodes":[21,19]},{"coordinate":[6,6],"connectedNodes":[22,20]},{"coordinate":[5,6],"connectedNodes":[23,21]},{"coordinate":[4,6],"connectedNodes":[22,24]},{"coordinate":[4,5],"connectedNodes":[28,23,25]},{"coordinate":[4,4],"connectedNodes":[24,26]},{"coordinate":[4,3],"connectedNodes":[25,27]},{"coordinate":[4,2],"connectedNodes":[26]},{"coordinate":[3,5],"connectedNodes":[2,24]}]',
        traffic_lights="[]",
        cows="[]",
        origin='{"coordinate":[2,7],"direction":"S"}',
        destinations="[[4,2]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[12]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=True,
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="farm",
        character_name="Van",
        lesson="Don't go the long way around!",
        hint="Think carefully about the order in which you ask questions in your if..else if block",
        anonymous=False
    )

    level24 = Level(
        name="1024",
        episode=episode21,
        path='[{"coordinate":[7,0],"connectedNodes":[1]},{"coordinate":[7,1],"connectedNodes":[10,2,0]},{"coordinate":[7,2],"connectedNodes":[3,24,1]},{"coordinate":[7,3],"connectedNodes":[4,2]},{"coordinate":[6,3],"connectedNodes":[5,3]},{"coordinate":[6,4],"connectedNodes":[23,6,33,4]},{"coordinate":[6,5],"connectedNodes":[7,5]},{"coordinate":[6,6],"connectedNodes":[8,6]},{"coordinate":[5,6],"connectedNodes":[9,7]},{"coordinate":[5,7],"connectedNodes":[8]},{"coordinate":[6,1],"connectedNodes":[11,1]},{"coordinate":[5,1],"connectedNodes":[12,10]},{"coordinate":[4,1],"connectedNodes":[13,11]},{"coordinate":[3,1],"connectedNodes":[14,12]},{"coordinate":[2,1],"connectedNodes":[15,13]},{"coordinate":[1,1],"connectedNodes":[16,17,14]},{"coordinate":[0,1],"connectedNodes":[15]},{"coordinate":[1,2],"connectedNodes":[18,15]},{"coordinate":[1,3],"connectedNodes":[19,17]},{"coordinate":[1,4],"connectedNodes":[20,18]},{"coordinate":[2,4],"connectedNodes":[19,21]},{"coordinate":[3,4],"connectedNodes":[20,22]},{"coordinate":[4,4],"connectedNodes":[21,23]},{"coordinate":[5,4],"connectedNodes":[22,5]},{"coordinate":[8,2],"connectedNodes":[2,25]},{"coordinate":[9,2],"connectedNodes":[24,26]},{"coordinate":[9,3],"connectedNodes":[27,25]},{"coordinate":[9,4],"connectedNodes":[28,26]},{"coordinate":[9,5],"connectedNodes":[29,27]},{"coordinate":[9,6],"connectedNodes":[30,28]},{"coordinate":[8,6],"connectedNodes":[29,31]},{"coordinate":[8,5],"connectedNodes":[30,32]},{"coordinate":[8,4],"connectedNodes":[33,31]},{"coordinate":[7,4],"connectedNodes":[5,32]}]',
        traffic_lights="[]",
        cows="[]",
        origin='{"coordinate":[7,0],"direction":"N"}',
        destinations="[[5,7]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=False,
        pythonEnabled=True,
        pythonViewEnabled=False,
        theme_name="farm",
        character_name="Van",
        lesson="Look carefully for the shortest route.",
        hint="Think carefully about the order in which you ask questions in your if..elif statements.",
        anonymous=False
    )

    level25 = Level(
        name="1025",
        episode=episode21,
        path='[{"coordinate":[8,0],"connectedNodes":[1]},{"coordinate":[8,1],"connectedNodes":[2,0]},{"coordinate":[8,2],"connectedNodes":[3,1]},{"coordinate":[7,2],"connectedNodes":[4,2]},{"coordinate":[6,2],"connectedNodes":[12,5,3]},{"coordinate":[6,3],"connectedNodes":[25,4]},{"coordinate":[4,5],"connectedNodes":[7,19]},{"coordinate":[3,5],"connectedNodes":[8,6]},{"coordinate":[2,5],"connectedNodes":[9,7]},{"coordinate":[1,5],"connectedNodes":[10,8,18]},{"coordinate":[1,6],"connectedNodes":[11,9]},{"coordinate":[1,7],"connectedNodes":[10]},{"coordinate":[5,2],"connectedNodes":[13,4]},{"coordinate":[4,2],"connectedNodes":[14,12]},{"coordinate":[3,2],"connectedNodes":[15,13]},{"coordinate":[2,2],"connectedNodes":[16,14]},{"coordinate":[1,2],"connectedNodes":[17,15]},{"coordinate":[1,3],"connectedNodes":[18,16]},{"coordinate":[1,4],"connectedNodes":[9,17]},{"coordinate":[5,5],"connectedNodes":[6,20]},{"coordinate":[6,5],"connectedNodes":[19,21]},{"coordinate":[7,5],"connectedNodes":[20,22]},{"coordinate":[8,5],"connectedNodes":[21,23]},{"coordinate":[8,4],"connectedNodes":[24,22]},{"coordinate":[7,4],"connectedNodes":[25,23]},{"coordinate":[6,4],"connectedNodes":[24,5]}]',
        traffic_lights='[{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":5},"direction":"W","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":1,"y":5},"direction":"N","startTime":0,"startingState":"RED"}]',
        cows="[]",
        origin='{"coordinate":[8,0],"direction":"N"}',
        destinations="[[1,7]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=False,
        pythonEnabled=True,
        pythonViewEnabled=False,
        theme_name="grass",
        character_name="Van",
        lesson="Look carefully for the shortest route.",
        hint="Think carefully about the order in which you ask questions in your if..elif statements. Don't forget the traffic lights.",
        anonymous=False
    )

    level26 = Level.objects.get(name="85", default=True)
    level26.name = "1026"
    level26.episode=episode22

    level27 = Level(
        name="1027",
        episode=episode22,
        path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3,5]},{"coordinate":[5,3],"connectedNodes":[4,6]},{"coordinate":[6,3],"connectedNodes":[5,7]},{"coordinate":[7,3],"connectedNodes":[6,8]},{"coordinate":[8,3],"connectedNodes":[7]}]',
        traffic_lights="[]",
        cows="[]",
        origin='{"coordinate":[0,3],"direction":"E"}',
        destinations="[[8,3]]",
        default=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[4]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=True,
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="grass",
        character_name="Van",
        lesson="Just keep going until you get there...",
        hint="You might find that the solution to this level is quite familiar...",
        anonymous=False
    )

    level28 = Level(
        name="1028",
        episode=episode22,
        path='[{"coordinate":[2,2],"connectedNodes":[1]},{"coordinate":[3,2],"connectedNodes":[0,2]},{"coordinate":[3,3],"connectedNodes":[3,1]},{"coordinate":[4,3],"connectedNodes":[2,4]},{"coordinate":[4,4],"connectedNodes":[5,3]},{"coordinate":[5,4],"connectedNodes":[4,6]},{"coordinate":[5,5],"connectedNodes":[7,5]},{"coordinate":[6,5],"connectedNodes":[6,8]},{"coordinate":[6,6],"connectedNodes":[9,7]},{"coordinate":[7,6],"connectedNodes":[8]}]',
        traffic_lights='[]',
        cows='[]',
        origin='{"coordinate":[2,2],"direction":"E"}',
        destinations="[[7,6]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[5]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=True,
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="grass",
        character_name="Van",
        lesson="Well done, you did it! Now have a go at using the <b>Repeat until</b> block on a road with lots of turns.",
        hint="This is another route you have seen before. Last time you counted how many times your instructions were repeated. This time, your program is going to repeat your commands until you reach the destination. What do you need to repeat?",
        anonymous=False
    )

    level29 = Level.objects.get(name="119", default=True)
    level29.pk = None
    level29._state.adding = True
    level29.name = "1029"
    level29.blocklyEnabled = True
    level29.pythonEnabled = False
    level29.pythonViewEnabled = True
    level29.model_solution = "[7]"
    level29.episode=episode22

    level30 = Level.objects.get(name="84", default=True)
    level30.pk = None
    level30._state.adding = True
    level30.name = "1030"
    level30.blocklyEnabled = False
    level30.pythonEnabled = True
    level30.pythonViewEnabled = False
    level30.model_solution = "[]"
    level30.episode=episode22

    level31 = Level.objects.get(name="34", default=True)
    level31.pk = None
    level31._state.adding = True
    level31.name = "1031"
    level31.blocklyEnabled = True
    level31.pythonEnabled = False
    level31.pythonViewEnabled = True
    level31.model_solution = "[7]"
    level31.episode=episode22

    level32 = Level(
        name="1032",
        episode=episode22,
        path='[{"coordinate":[5,0],"connectedNodes":[1]},{"coordinate":[5,1],"connectedNodes":[2,0]},{"coordinate":[5,2],"connectedNodes":[3,23,1]},{"coordinate":[5,3],"connectedNodes":[4,2]},{"coordinate":[5,4],"connectedNodes":[17,3]},{"coordinate":[4,5],"connectedNodes":[6,17]},{"coordinate":[3,5],"connectedNodes":[7,5]},{"coordinate":[2,5],"connectedNodes":[24,6,8]},{"coordinate":[2,4],"connectedNodes":[7,9]},{"coordinate":[2,3],"connectedNodes":[8,10]},{"coordinate":[2,2],"connectedNodes":[9,11]},{"coordinate":[2,1],"connectedNodes":[10,12]},{"coordinate":[3,1],"connectedNodes":[11,13]},{"coordinate":[4,1],"connectedNodes":[12,14]},{"coordinate":[4,2],"connectedNodes":[15,13]},{"coordinate":[4,3],"connectedNodes":[16,14]},{"coordinate":[4,4],"connectedNodes":[15]},{"coordinate":[5,5],"connectedNodes":[5,29,18,4]},{"coordinate":[6,5],"connectedNodes":[17,19]},{"coordinate":[7,5],"connectedNodes":[18,20]},{"coordinate":[7,4],"connectedNodes":[19,21]},{"coordinate":[7,3],"connectedNodes":[20,22]},{"coordinate":[7,2],"connectedNodes":[23,21,36]},{"coordinate":[6,2],"connectedNodes":[2,22]},{"coordinate":[1,5],"connectedNodes":[25,7]},{"coordinate":[1,6],"connectedNodes":[26,24]},{"coordinate":[2,6],"connectedNodes":[25,27]},{"coordinate":[3,6],"connectedNodes":[26,28]},{"coordinate":[4,6],"connectedNodes":[27,29]},{"coordinate":[5,6],"connectedNodes":[28,30,17]},{"coordinate":[6,6],"connectedNodes":[29,31]},{"coordinate":[7,6],"connectedNodes":[30,32]},{"coordinate":[8,6],"connectedNodes":[31,33]},{"coordinate":[8,5],"connectedNodes":[32,34]},{"coordinate":[8,4],"connectedNodes":[33,35]},{"coordinate":[8,3],"connectedNodes":[34,36]},{"coordinate":[8,2],"connectedNodes":[22,35]}]',
        traffic_lights='[]',
        cows='[]',
        origin='{"coordinate":[5,0],"direction":"N"}',
        destinations="[[4,4]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[7]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=True,
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="grass",
        character_name="Van",
        lesson="You don't have a right turn block here, so plan your route carefully.",
        hint="Think carefully about the order in which you ask questions in your if-statement here...",
        anonymous=False
    )

    level33 = Level(
        name="1033",
        episode=episode22,
        path='[{"coordinate":[7,1],"connectedNodes":[1]},{"coordinate":[7,2],"connectedNodes":[2,0]},{"coordinate":[6,2],"connectedNodes":[3,1]},{"coordinate":[6,3],"connectedNodes":[4,13,2]},{"coordinate":[5,3],"connectedNodes":[5,3]},{"coordinate":[5,4],"connectedNodes":[6,16,15,4]},{"coordinate":[4,4],"connectedNodes":[7,5]},{"coordinate":[4,5],"connectedNodes":[8,16,6]},{"coordinate":[3,5],"connectedNodes":[9,7]},{"coordinate":[3,6],"connectedNodes":[10,8]},{"coordinate":[2,6],"connectedNodes":[11,9]},{"coordinate":[2,7],"connectedNodes":[12,17,10]},{"coordinate":[1,7],"connectedNodes":[11]},{"coordinate":[7,3],"connectedNodes":[3,14]},{"coordinate":[7,4],"connectedNodes":[15,13]},{"coordinate":[6,4],"connectedNodes":[5,22,14]},{"coordinate":[5,5],"connectedNodes":[7,5]},{"coordinate":[3,7],"connectedNodes":[11,18]},{"coordinate":[4,7],"connectedNodes":[17,19]},{"coordinate":[5,7],"connectedNodes":[18,20]},{"coordinate":[6,7],"connectedNodes":[19,21]},{"coordinate":[6,6],"connectedNodes":[20,22]},{"coordinate":[6,5],"connectedNodes":[21,15]}]',
        traffic_lights="[]",
        cows="[]",
        origin='{"coordinate":[7,1],"direction":"N"}',
        destinations="[[1,7]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=False,
        pythonEnabled=True,
        pythonViewEnabled=False,
        theme_name="grass",
        character_name="Van",
        lesson="Can you find the shortest route?",
        hint="In this level, you want to check for a left turn first. If there is no left turn, turn right. Notice what that looks like in Python.",
        anonymous=False
    )

    level34 = Level(
        name="1034",
        episode=episode22,
        path='[{"coordinate":[0,6],"connectedNodes":[1]},{"coordinate":[1,6],"connectedNodes":[0,2]},{"coordinate":[2,6],"connectedNodes":[1,3]},{"coordinate":[3,6],"connectedNodes":[2,4]},{"coordinate":[4,6],"connectedNodes":[3,5]},{"coordinate":[5,6],"connectedNodes":[4,6]},{"coordinate":[5,5],"connectedNodes":[5,23,7]},{"coordinate":[5,4],"connectedNodes":[6,8]},{"coordinate":[5,3],"connectedNodes":[7,29,9]},{"coordinate":[5,2],"connectedNodes":[8,10]},{"coordinate":[5,1],"connectedNodes":[11,9]},{"coordinate":[4,1],"connectedNodes":[12,10]},{"coordinate":[3,1],"connectedNodes":[13,11]},{"coordinate":[2,1],"connectedNodes":[14,12]},{"coordinate":[1,1],"connectedNodes":[15,13]},{"coordinate":[1,2],"connectedNodes":[34,16,14]},{"coordinate":[1,3],"connectedNodes":[17,15]},{"coordinate":[1,4],"connectedNodes":[30,16]},{"coordinate":[2,5],"connectedNodes":[30,19]},{"coordinate":[3,5],"connectedNodes":[18,20]},{"coordinate":[3,4],"connectedNodes":[19,21]},{"coordinate":[3,3],"connectedNodes":[20,22]},{"coordinate":[3,2],"connectedNodes":[21]},{"coordinate":[6,5],"connectedNodes":[6,24]},{"coordinate":[7,5],"connectedNodes":[23,25]},{"coordinate":[8,5],"connectedNodes":[24,26]},{"coordinate":[8,4],"connectedNodes":[25,27]},{"coordinate":[8,3],"connectedNodes":[28,26]},{"coordinate":[7,3],"connectedNodes":[29,27]},{"coordinate":[6,3],"connectedNodes":[8,28]},{"coordinate":[1,5],"connectedNodes":[31,18,17]},{"coordinate":[0,5],"connectedNodes":[30,32]},{"coordinate":[0,4],"connectedNodes":[31,33]},{"coordinate":[0,3],"connectedNodes":[32,34]},{"coordinate":[0,2],"connectedNodes":[33,15]}]',
        traffic_lights="[]",
        cows="[]",
        origin='{"coordinate":[0,6],"direction":"E"}',
        destinations="[[3,2]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=False,
        pythonEnabled=True,
        pythonViewEnabled=False,
        theme_name="grass",
        character_name="Van",
        lesson="Can you find the shortest route? Don't take the scenic route.",
        hint="Just look for the simplest route to the house.",
        anonymous=False
    )

    level35 = Level.objects.get(name="99", default=True)
    level35.name = "1035"
    level35.blocklyEnabled = True
    level35.pythonEnabled = False
    level35.pythonViewEnabled = True
    level35.episode=episode22

    level36 = Level.objects.get(name="38", default=True)
    level36.pk = None
    level36._state.adding = True
    level36.name = "1036"
    level36.pythonViewEnabled = True
    level36.model_solution = "[11]"
    level36.episode=episode22

    level37 = Level.objects.get(name="100", default=True)
    level37.name = "1037"
    level37.episode=episode22

    level38 = Level.objects.get(name="39", default=True)
    level38.pk = None
    level38._state.adding = True
    level38.name = "1038"
    level38.blocklyEnabled = False
    level38.pythonEnabled = True
    level38.model_solution = "[]"
    level38.episode=episode22

    level39 = Level.objects.get(name="47", default=True)
    level39.pk = None
    level39._state.adding = True
    level39.name = "1039"
    level39.blocklyEnabled = False
    level39.pythonEnabled = True
    level39.model_solution = "[]"
    level39.episode=episode22

    level40 = Level.objects.get(name="48", default=True)
    level40.pk = None
    level40._state.adding = True
    level40.name = "1040"
    level40.blocklyEnabled = False
    level40.pythonEnabled = True
    level40.model_solution = "[]"
    level40.episode=episode22

    level41 = Level.objects.get(name="83", default=True)
    level41.name = "1041"
    level41.episode = episode25

    level42 = Level.objects.get(name="95", default=True)
    level42.name = "1042"
    level42.episode = episode25

    level43 = Level.objects.get(name="96", default=True)
    level43.name = "1043"
    level43.episode = episode25

    level44 = Level.objects.get(name="84", default=True)
    level44.name = "1044"
    level44.episode = episode25

    level45 = Level.objects.get(name="97", default=True)
    level45.name = "1045"
    level45.episode = episode25

    level46 = Level.objects.get(name="106", default=True)
    level46.name = "1046"
    level46.episode = episode25

    level47 = Level.objects.get(name="107", default=True)
    level47.name = "1047"
    level47.episode = episode25

    level48 = Level.objects.get(name="108", default=True)
    level48.name = "1048"
    level48.episode = episode25

    level49 = Level.objects.get(name="109", default=True)
    level49.name = "1049"
    level49.episode = episode25

    level50 = Level.objects.get(name="61", default=True)
    level50.pk = None
    level50._state.adding = True
    level50.name = "1050"
    level50.pythonViewEnabled = True
    level50.episode = episode26

    level51 = Level.objects.get(name="62", default=True)
    level51.pk = None
    level51._state.adding = True
    level51.name = "1051"
    level51.pythonViewEnabled = True
    level51.episode = episode26

    level52 = Level.objects.get(name="63", default=True)
    level52.pk = None
    level52._state.adding = True
    level52.name = "1052"
    level52.blocklyEnabled = False
    level52.pythonEnabled = True
    level52.model_solution = "[]"
    level52.episode = episode26

    level53 = Level.objects.get(name="64", default=True)
    level53.pk = None
    level53._state.adding = True
    level53.name = "1053"
    level53.blocklyEnabled = False
    level53.pythonEnabled = True
    level53.model_solution = "[]"
    level53.episode = episode26

    level54 = Level.objects.get(name="65", default=True)
    level54.pk = None
    level54._state.adding = True
    level54.name = "1054"
    level54.blocklyEnabled = False
    level54.pythonEnabled = True
    level54.model_solution = "[]"
    level54.episode = episode26

    level55 = Level.objects.get(name="66", default=True)
    level55.pk = None
    level55._state.adding = True
    level55.name = "1055"
    level55.blocklyEnabled = False
    level55.pythonEnabled = True
    level55.model_solution = "[]"
    level55.episode = episode26

    level56 = Level.objects.get(name="67", default=True)
    level56.pk = None
    level56._state.adding = True
    level56.name = "1056"
    level56.blocklyEnabled = False
    level56.pythonEnabled = True
    level56.model_solution = "[]"
    level56.episode = episode26

    level57 = Level.objects.get(name="90", default=True)
    level57.name = "1057"
    level57.blocklyEnabled = False
    level57.pythonViewEnabled = False
    level57.pythonEnabled = True
    level57.episode = episode26

    level58 = Level.objects.get(name="91", default=True)
    level58.name = "1058"
    level58.blocklyEnabled = False
    level58.pythonViewEnabled = False
    level58.pythonEnabled = True
    level58.episode = episode26

    level59 = Level.objects.get(name="101", default=True)
    level59.name = "1059"
    level59.episode = episode26

    level60 = Level.objects.get(name="102", default=True)
    level60.name = "1060"
    level60.episode = episode26

    def save_all_levels():
        level1.save()
        level2.save()
        level3.save()
        level4.save()
        level5.save()
        level6.save()
        level7.save()
        level8.save()
        level9.save()
        level10.save()
        level11.save()
        level12.save()
        level13.save()
        level14.save()
        level15.save()
        level16.save()
        level17.save()
        level18.save()
        level19.save()
        level20.save()
        level21.save()
        level22.save()
        level23.save()
        level24.save()
        level25.save()
        level26.save()
        level27.save()
        level28.save()
        level29.save()
        level30.save()
        level31.save()
        level32.save()
        level33.save()
        level34.save()
        level35.save()
        level36.save()
        level37.save()
        level38.save()
        level39.save()
        level40.save()
        level41.save()
        level42.save()
        level43.save()
        level44.save()
        level45.save()
        level46.save()
        level47.save()
        level48.save()
        level49.save()
        level50.save()
        level51.save()
        level52.save()
        level53.save()
        level54.save()
        level55.save()
        level56.save()
        level57.save()
        level58.save()
        level59.save()
        level60.save()

    save_all_levels()

    level1.next_level = level2
    level2.next_level = level3
    level3.next_level = level4
    level4.next_level = level5
    level5.next_level = level6
    level6.next_level = level7
    level7.next_level = level8
    level8.next_level = level9
    level9.next_level = level10
    level10.next_level = level11
    level11.next_level = level12
    level12.next_level = level13
    level13.next_level = level14
    level14.next_level = level15
    level15.next_level = level16
    level16.next_level = level17
    level17.next_level = level18
    level18.next_level = level19
    level19.next_level = level20
    level20.next_level = level21
    level21.next_level = level22
    level22.next_level = level23
    level23.next_level = level24
    level24.next_level = level25
    level25.next_level = level26
    level26.next_level = level27
    level27.next_level = level28
    level28.next_level = level29
    level29.next_level = level30
    level30.next_level = level31
    level31.next_level = level32
    level32.next_level = level33
    level33.next_level = level34
    level34.next_level = level35
    level35.next_level = level36
    level36.next_level = level37
    level37.next_level = level38
    level38.next_level = level39
    level39.next_level = level40
    level40.next_level = level41
    level41.next_level = level42
    level42.next_level = level43
    level43.next_level = level44
    level44.next_level = level45
    level45.next_level = level46
    level46.next_level = level47
    level47.next_level = level48
    level48.next_level = level49
    level49.next_level = level50
    level50.next_level = level51
    level51.next_level = level52
    level52.next_level = level53
    level53.next_level = level54
    level54.next_level = level55
    level55.next_level = level56
    level56.next_level = level57
    level57.next_level = level58
    level58.next_level = level59
    level59.next_level = level60

    save_all_levels()


def add_python_den_blocks(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    LevelBlock = apps.get_model("game", "LevelBlock")
    Block = apps.get_model("game", "Block")

    def set_blocks(level, blocks):
        set_blocks_inner(level, blocks, LevelBlock, Block)

    level14 = Level.objects.get(name="1014", default=True)
    level15 = Level.objects.get(name="1015", default=True)
    level19 = Level.objects.get(name="1019", default=True)
    level22 = Level.objects.get(name="1022", default=True)
    level23 = Level.objects.get(name="1023", default=True)
    level27 = Level.objects.get(name="1027", default=True)
    level28 = Level.objects.get(name="1028", default=True)
    level29 = Level.objects.get(name="1029", default=True)
    level31 = Level.objects.get(name="1031", default=True)
    level32 = Level.objects.get(name="1032", default=True)
    level35 = Level.objects.get(name="1035", default=True)
    level36 = Level.objects.get(name="1036", default=True)
    level50 = Level.objects.get(name="1050", default=True)
    level51 = Level.objects.get(name="1051", default=True)

    set_blocks(
        level14,
        json.loads(
            '[{"type": "variables_numeric_set"},'
            + '{"type": "controls_repeat_while"},'
            + '{"type": "variables_get"},'
            + '{"type": "math_number"},'
            + '{"type": "logic_compare"},'
            + '{"type": "controls_if"},'
            + '{"type": "cow_crossing"},'
            + '{"type": "sound_horn"},'
            + '{"type": "move_forwards"},'
            + '{"type": "variables_increment"}]'
        )
    )

    set_blocks(
        level15,
        json.loads(
            '[{"type": "variables_numeric_set"},'
            + '{"type": "controls_repeat_while"},'
            + '{"type": "variables_get"},'
            + '{"type": "math_number"},'
            + '{"type": "logic_compare"},'
            + '{"type": "controls_if"},'
            + '{"type": "road_exists"},'
            + '{"type": "turn_left"},'
            + '{"type": "turn_right"},'
            + '{"type": "move_forwards"},'
            + '{"type": "variables_increment"}]'
        )
    )

    set_blocks(
        level19,
        json.loads(
            '[{"type": "variables_numeric_set"},'
            + '{"type": "controls_repeat_while"},'
            + '{"type": "variables_get"},'
            + '{"type": "math_number"},'
            + '{"type": "logic_compare"},'
            + '{"type": "controls_if"},'
            + '{"type": "road_exists"},'
            + '{"type": "turn_left"},'
            + '{"type": "turn_right"},'
            + '{"type": "move_forwards"},'
            + '{"type": "variables_increment"}]'
        )
    )

    set_blocks(
        level22,
        json.loads(
            '[{"type": "variables_numeric_set"},'
            + '{"type": "controls_repeat_while"},'
            + '{"type": "variables_get"},'
            + '{"type": "math_number"},'
            + '{"type": "logic_compare"},'
            + '{"type": "controls_if"},'
            + '{"type": "road_exists"},'
            + '{"type": "turn_left"},'
            + '{"type": "turn_right"},'
            + '{"type": "move_forwards"},'
            + '{"type": "variables_increment"}]'
        )
    )

    set_blocks(
        level23,
        json.loads(
            '[{"type": "variables_numeric_set"},'
            + '{"type": "controls_repeat_while"},'
            + '{"type": "variables_get"},'
            + '{"type": "math_number"},'
            + '{"type": "logic_compare"},'
            + '{"type": "controls_if"},'
            + '{"type": "road_exists"},'
            + '{"type": "turn_left"},'
            + '{"type": "turn_right"},'
            + '{"type": "move_forwards"},'
            + '{"type": "variables_increment"}]'
        )
    )

    set_blocks(
        level27,
        json.loads(
            '[{"type": "controls_repeat_while"},'
            + '{"type": "logic_negate"},'
            + '{"type": "at_destination"},'
            + '{"type": "move_forwards"}]'
        )
    )

    set_blocks(
        level28,
        json.loads(
            '[{"type": "controls_repeat_while"},'
            + '{"type": "logic_negate"},'
            + '{"type": "at_destination"},'
            + '{"type": "turn_left"},'
            + '{"type": "turn_right"}]'
        )
    )

    set_blocks(
        level29,
        json.loads(
            '[{"type": "controls_repeat_while"},'
            + '{"type": "logic_negate"},'
            + '{"type": "at_destination"},'
            + '{"type": "turn_left"},'
            + '{"type": "turn_right"},'
            + '{"type": "move_forwards"}]'
        )
    )

    set_blocks(
        level31,
        json.loads(
            '[{"type": "controls_repeat_while"},'
            + '{"type": "logic_negate"},'
            + '{"type": "at_destination"},'
            + '{"type": "controls_if"},'
            + '{"type": "road_exists"},'
            + '{"type": "turn_left"},'
            + '{"type": "move_forwards"}]'
        )
    )

    set_blocks(
        level32,
        json.loads(
            '[{"type": "controls_repeat_while"},'
            + '{"type": "logic_negate"},'
            + '{"type": "at_destination"},'
            + '{"type": "controls_if"},'
            + '{"type": "road_exists"},'
            + '{"type": "turn_left"},'
            + '{"type": "move_forwards"}]'
        )
    )

    set_blocks(
        level35,
        json.loads(
            '[{"type": "controls_repeat_while"},'
            + '{"type": "logic_negate"},'
            + '{"type": "at_destination"},'
            + '{"type": "controls_if"},'
            + '{"type": "road_exists"},'
            + '{"type": "move_forwards"},'
            + '{"type": "turn_left"},'
            + '{"type": "turn_right"}]'
        )
    )

    set_blocks(
        level36,
        json.loads(
            '[{"type": "controls_repeat_while"},'
            + '{"type": "logic_negate"},'
            + '{"type": "at_destination"},'
            + '{"type": "controls_if"},'
            + '{"type": "cow_crossing"},'
            + '{"type": "road_exists"},'
            + '{"type": "move_forwards"},'
            + '{"type": "turn_left"},'
            + '{"type": "turn_right"}]'
        )
    )

    set_blocks(
        level50,
        json.loads(
            '[{"type": "call_proc"},'
            + '{"type": "declare_proc"},'
            + '{"type": "move_forwards"},'
            + '{"type": "turn_left"},'
            + '{"type": "turn_right"},'
            + '{"type": "controls_repeat"}]'
        )
    )

    set_blocks(
        level51,
        json.loads(
            '[{"type": "call_proc"},'
            + '{"type": "declare_proc"},'
            + '{"type": "move_forwards"},'
            + '{"type": "turn_right"},'
            + '{"type": "wait"},'
            + '{"type": "controls_repeat_until"},'
            + '{"type": "traffic_light"}]'
        )
    )


def add_python_den_decor(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    LevelDecor = apps.get_model("game", "LevelDecor")

    def set_decor(level, decor):
        set_decor_inner(level, decor, LevelDecor)

    def bulk_copy_decor(new_level_name, old_level_name):
        old_level = Level.objects.get(name=old_level_name, default=True)
        decor_to_copy = LevelDecor.objects.filter(level_id=old_level.id).values()
        new_level = Level.objects.get(name=new_level_name, default=True)

        new_level_decor = []
        for decor in decor_to_copy:
            new_level_decor.append(
                LevelDecor(
                    level_id = new_level.pk, x = decor["x"], y = decor["y"], decorName = decor["decorName"]
                )
            )
        LevelDecor.objects.bulk_create(new_level_decor)

    level14 = Level.objects.get(name="1014", default=True)
    level15 = Level.objects.get(name="1015", default=True)
    level16 = Level.objects.get(name="1016", default=True)
    level17 = Level.objects.get(name="1017", default=True)
    level18 = Level.objects.get(name="1018", default=True)
    level20 = Level.objects.get(name="1020", default=True)
    level21 = Level.objects.get(name="1021", default=True)
    level22 = Level.objects.get(name="1022", default=True)
    level23 = Level.objects.get(name="1023", default=True)
    level24 = Level.objects.get(name="1024", default=True)
    level27 = Level.objects.get(name="1027", default=True)
    level28 = Level.objects.get(name="1028", default=True)
    level33 = Level.objects.get(name="1033", default=True)
    level34 = Level.objects.get(name="1034", default=True)

    set_decor(
        level14,
        json.loads(
            '[{"x": 149, "y": 299, "decorName": "pond"},'
            + '{"x": 398, "y": 354, "decorName": "bush"},'
            + '{"x": 399, "y": 318, "decorName": "bush"},'
            + '{"x": 311, "y": 309, "decorName": "tree2"},'
            + '{"x": 568, "y": 516, "decorName": "tree1"},'
            + '{"x": 654, "y": 512, "decorName": "tree1"}]'
        )
    )

    set_decor(
        level15,
        json.loads(
            '[{"x": 404, "y": 602, "decorName": "pond"},'
            + '{"x": 563, "y": 600, "decorName": "pond"},'
            + '{"x": 501, "y": 503, "decorName": "pond"},'
            + '{"x": 254, "y": 655, "decorName": "bush"},'
            + '{"x": 253, "y": 617, "decorName": "bush"},'
            + '{"x": 407, "y": 512, "decorName": "tree2"},'
            + '{"x": 494, "y": 391, "decorName": "tree1"},'
            + '{"x": 486, "y": 318, "decorName": "tree1"},'
            + '{"x": 286, "y": 327, "decorName": "tree1"},'
            + '{"x": 252, "y": 256, "decorName": "tree1"}]'
        )
    )

    set_decor(
        level16,
        json.loads(
            '[{"x": 699, "y": 499, "decorName": "pond"},'
            + '{"x": 700, "y": 402, "decorName": "pond"},'
            + '{"x": 611, "y": 469, "decorName": "bush"},'
            + '{"x": 610, "y": 427, "decorName": "bush"},'
            + '{"x": 613, "y": 505, "decorName": "tree2"}]'
        )
    )

    set_decor(
        level17,
        json.loads(
            '[{"x": 461, "y": 314, "decorName": "pond"},'
            + '{"x": 428, "y": 371, "decorName": "tree1"},'
            + '{"x": 500, "y": 179, "decorName": "tree1"}]'
        )
    )

    set_decor(
        level18,
        json.loads(
            '[{"x": 301, "y": 594, "decorName": "tree1"},'
            + '{"x": 421, "y": 598, "decorName": "tree1"},'
            + '{"x": 529, "y": 600, "decorName": "tree1"},'
            + '{"x": 120, "y": 415, "decorName": "tree2"},'
            + '{"x": 93, "y": 300, "decorName": "tree2"}]'
        )
    )

    set_decor(
        level20,
        json.loads(
            '[{"x": 443, "y": 578, "decorName": "pond"},'
            + '{"x": 640, "y": 434, "decorName": "tree2"},'
            + '{"x": 623, "y": 362, "decorName": "tree1"},'
            + '{"x": 647, "y": 292, "decorName": "tree2"},'
            + '{"x": 694, "y": 341, "decorName": "tree1"},'
            + '{"x": 516, "y": 651, "decorName": "tree2"},'
            + '{"x": 412, "y": 648, "decorName": "tree1"}]'
        )
    )

    set_decor(
        level21,
        json.loads(
            '[{"x": 149, "y": 292, "decorName": "pond"},'
            + '{"x": 300, "y": 507, "decorName": "tree1"},'
            + '{"x": 308, "y": 583, "decorName": "tree1"}]'
        )
    )

    set_decor(
        level22,
        json.loads(
            '[{"x": 663, "y": 191, "decorName": "pond"},'
            + '{"x": 364, "y": 395, "decorName": "tree1"},'
            + '{"x": 463, "y": 317, "decorName": "tree2"},'
            + '{"x": 367, "y": 237, "decorName": "tree1"},'
            + '{"x": 250, "y": 391, "decorName": "tree2"}]'
        )
    )

    set_decor(
        level23,
        json.loads(
            '[{"x": 599, "y": 310, "decorName": "pond"},'
            + '{"x": 599, "y": 208, "decorName": "pond"},'
            + '{"x": 754, "y": 337, "decorName": "bush"},'
            + '{"x": 755, "y": 370, "decorName": "bush"},'
            + '{"x": 754, "y": 302, "decorName": "bush"},'
            + '{"x": 809, "y": 370, "decorName": "bush"},'
            + '{"x": 810, "y": 334, "decorName": "bush"},'
            + '{"x": 810, "y": 298, "decorName": "bush"},'
            + '{"x": 602, "y": 418, "decorName": "tree2"},'
            + '{"x": 646, "y": 483, "decorName": "tree1"},'
            + '{"x": 678, "y": 426, "decorName": "tree1"}]'
        )
    )

    set_decor(
        level24,
        json.loads(
            '[{"x": 316, "y": 302, "decorName": "pond"},'
            + '{"x": 207, "y": 198, "decorName": "pond"},'
            + '{"x": 371, "y": 198, "decorName": "pond"},'
            + '{"x": 533, "y": 195, "decorName": "pond"},'
            + '{"x": 491, "y": 367, "decorName": "bush"},'
            + '{"x": 498, "y": 330, "decorName": "bush"},'
            + '{"x": 553, "y": 354, "decorName": "bush"},'
            + '{"x": 546, "y": 318, "decorName": "bush"},'
            + '{"x": 230, "y": 317, "decorName": "tree2"}]'
        )
    )

    set_decor(
        level27,
        json.loads(
            '[{"x": 147, "y": 214, "decorName": "pond"},'
            + '{"x": 434, "y": 255, "decorName": "bush"},'
            + '{"x": 489, "y": 259, "decorName": "bush"},'
            + '{"x": 298, "y": 188, "decorName": "tree2"},'
            + '{"x": 158, "y": 398, "decorName": "tree2"},'
            + '{"x": 220, "y": 410, "decorName": "tree1"},'
            + '{"x": 548, "y": 411, "decorName": "tree1"},'
            + '{"x": 617, "y": 407, "decorName": "tree2"},'
            + '{"x": 669, "y": 199, "decorName": "tree2"}]'
        )
    )

    set_decor(
        level28,
        json.loads(
            '[{"x": 443, "y": 578, "decorName": "pond"},'
            + '{"x": 640, "y": 434, "decorName": "tree2"},'
            + '{"x": 623, "y": 362, "decorName": "tree1"},'
            + '{"x": 647, "y": 292, "decorName": "tree2"},'
            + '{"x": 694, "y": 341, "decorName": "tree1"},'
            + '{"x": 516, "y": 651, "decorName": "tree2"},'
            + '{"x": 412, "y": 648, "decorName": "tree1"}]'
        )
    )

    set_decor(
        level33,
        json.loads(
            '[{"x": 459, "y": 602, "decorName": "pond"},'
            + '{"x": 381, "y": 606, "decorName": "tree2"},'
            + '{"x": 692, "y": 688, "decorName": "tree1"},'
            + '{"x": 717, "y": 620, "decorName": "tree1"},'
            + '{"x": 686, "y": 530, "decorName": "tree2"}]'
        )
    )

    set_decor(
        level34,
        json.loads(
            '[{"x": 625, "y": 408, "decorName": "pond"},'
            + '{"x": 201, "y": 411, "decorName": "tree2"},'
            + '{"x": 200, "y": 342, "decorName": "tree1"},'
            + '{"x": 405, "y": 443, "decorName": "tree2"},'
            + '{"x": 400, "y": 514, "decorName": "tree1"}]'
        )
    )

    bulk_copy_decor("1010", "1029")
    bulk_copy_decor("1044", "1030")
    bulk_copy_decor("34", "1031")
    bulk_copy_decor("38", "1036")
    bulk_copy_decor("39", "1038")
    bulk_copy_decor("47", "1039")
    bulk_copy_decor("48", "1040")
    bulk_copy_decor("61", "1050")
    bulk_copy_decor("62", "1051")
    bulk_copy_decor("63", "1052")
    bulk_copy_decor("64", "1053")
    bulk_copy_decor("65", "1054")
    bulk_copy_decor("66", "1055")
    bulk_copy_decor("67", "1056")


def create_python_den_episodes(apps, schema_editor):
    Episode = apps.get_model("game", "Episode")

    episode16 = Episode.objects.create(
        pk=16,
        name="Output, Operators, and Data",
    )

    episode17 = Episode.objects.create(
        pk=17,
        name="Variables, Input, and Casting",
    )

    episode18 = Episode.objects.create(
        pk=18,
        name="Selection",
    )

    episode19 = Episode.objects.create(
        pk=19,
        name="Complex Selection",
    )

    episode20 = Episode.objects.create(
        pk=20,
        name="Counted Loops Using While",
    )

    episode21 = Episode.objects.create(
        pk=21,
        name="Selection in a Loop",
    )

    episode22 = Episode.objects.create(
        pk=22,
        name="Indeterminate Loops",
    )

    episode23 = Episode.objects.create(
        pk=23,
        name="String Manipulation",
    )

    episode24 = Episode.objects.create(
        pk=24,
        name="Lists",
    )

    episode25 = Episode.objects.create(
        pk=25,
        name="For Loops",
    )

    episode26 = Episode.objects.create(
        pk=26,
        name="Procedures",
    )

    episode15 = Episode.objects.get(pk=15)
    episode15.next_episode = episode16
    episode16.next_episode = episode17
    episode17.next_episode = episode18
    episode18.next_episode = episode19
    episode19.next_episode = episode20
    episode20.next_episode = episode21
    episode21.next_episode = episode22
    episode22.next_episode = episode23
    episode23.next_episode = episode24
    episode24.next_episode = episode25
    episode25.next_episode = episode26


class Migration(migrations.Migration):
    dependencies = [
        ('game', '0096_alter_level_commands')
    ]

    operations = [
        migrations.RunPython(code=create_python_den_episodes),
        migrations.RunPython(code=add_python_den_levels),
        migrations.RunPython(code=add_python_den_blocks),
        migrations.RunPython(code=add_python_den_decor)
    ]
