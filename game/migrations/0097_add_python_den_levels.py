import json

from django.db import migrations

from game.level_management import set_blocks_inner


def add_python_den_levels(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    Episode = apps.get_model("game", "Episode")

    episode13 = Episode.objects.get(pk=13)
    episode14 = Episode.objects.get(pk=14)
    episode15 = Episode.objects.get(pk=15)
    episode22 = Episode.objects.get(pk=22)

    level1014 = Level(
        name="1014",
        episode=episode13,
        character_name="Van",
        default=True,
        destinations="[[9,4]]",
        model_solution="[10]",
        origin='{"coordinate":[0,4],"direction":"E"}',
        path='[{"coordinate":[0,4],"connectedNodes":[1]},{"coordinate":[1,4],"connectedNodes":[0,2]},{"coordinate":[2,4],"connectedNodes":[1,3]},{"coordinate":[3,4],"connectedNodes":[2,4]},{"coordinate":[4,4],"connectedNodes":[3,5]},{"coordinate":[5,4],"connectedNodes":[4,6]},{"coordinate":[6,4],"connectedNodes":[5,7]},{"coordinate":[7,4],"connectedNodes":[6,8]},{"coordinate":[8,4],"connectedNodes":[7,9]},{"coordinate":[9,4],"connectedNodes":[8]}]',
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="farm",
        cows='[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":2,"y":4},{"x":5,"y":4},{"x":7,"y":4}],"type":"WHITE"}]',
        lesson="This is a nice long straight road, but there are cows about!",
        hint="Make sure you sound the horn to get the cows off the road.",
    )

    level1015 = Level(
        name="1015",
        episode=episode13,
        path='[{"coordinate":[5,0],"connectedNodes":[1]},{"coordinate":[5,1],"connectedNodes":[2,0]},{"coordinate":[4,1],"connectedNodes":[3,1]},{"coordinate":[4,2],"connectedNodes":[4,2]},{"coordinate":[4,3],"connectedNodes":[5,3]},{"coordinate":[4,4],"connectedNodes":[6,4]},{"coordinate":[3,4],"connectedNodes":[7,5]},{"coordinate":[3,5],"connectedNodes":[8,6]},{"coordinate":[3,6],"connectedNodes":[9,7]},{"coordinate":[3,7],"connectedNodes":[8]}]',
        origin='{"coordinate":[5,0],"direction":"N"}',
        destinations="[[3,7]]",
        default=True,
        model_solution="[11]",
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="farm",
        character_name="Van",
        lesson="There are some bends in this road. Be careful!",
        hint="What do you need to count, how many times you move or how many times you move forwards?",
    )

    level1016 = Level(
        name="1016",
        episode=episode13,
        path='[{"coordinate":[1,1],"connectedNodes":[1]},{"coordinate":[1,2],"connectedNodes":[2,0]},{"coordinate":[2,2],"connectedNodes":[1,3]},{"coordinate":[2,3],"connectedNodes":[4,2]},{"coordinate":[3,3],"connectedNodes":[3,5]},{"coordinate":[3,4],"connectedNodes":[6,4]},{"coordinate":[4,4],"connectedNodes":[5,7]},{"coordinate":[4,5],"connectedNodes":[8,6]},{"coordinate":[5,5],"connectedNodes":[7,9]},{"coordinate":[5,6],"connectedNodes":[10,8]},{"coordinate":[6,6],"connectedNodes":[9,11]},{"coordinate":[6,7],"connectedNodes":[12,10]},{"coordinate":[7,7],"connectedNodes":[11]}]',
        cows='[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":3,"y":3},{"x":5,"y":5},{"x":4,"y":4}],"type":"WHITE"}]',
        origin='{"coordinate":[1,1],"direction":"N"}',
        destinations="[[7,7]]",
        default=True,
        disable_algorithm_score=True,
        blocklyEnabled=False,
        theme_name="farm",
        character_name="Van",
        lesson="Oh no! The farmer seems to have let their cows out again. Be careful.",
        hint="Look for a pattern here...",
    )

    level1017 = Level(
        name="1017",
        episode=episode13,
        path='[{"coordinate":[7,0],"connectedNodes":[1]},{"coordinate":[7,1],"connectedNodes":[2,0]},{"coordinate":[6,1],"connectedNodes":[3,1]},{"coordinate":[6,2],"connectedNodes":[4,2]},{"coordinate":[6,3],"connectedNodes":[5,3]},{"coordinate":[6,4],"connectedNodes":[6,4]},{"coordinate":[5,4],"connectedNodes":[7,5]},{"coordinate":[5,5],"connectedNodes":[8,6]},{"coordinate":[5,6],"connectedNodes":[7]}]',
        origin='{"coordinate":[7,0],"direction":"N"}',
        destinations="[[5,6]]",
        default=True,
        disable_algorithm_score=True,
        blocklyEnabled=False,
        theme_name="grass",
        character_name="Van",
        lesson="Keep going, you're getting the hang of the Python code.",
        hint="So you are going forward unless...?",
    )

    level1018 = Level(
        name="1018",
        episode=episode13,
        path='[{"coordinate":[7,1],"connectedNodes":[1]},{"coordinate":[7,2],"connectedNodes":[2,0]},{"coordinate":[7,3],"connectedNodes":[3,1]},{"coordinate":[7,4],"connectedNodes":[4,2]},{"coordinate":[7,5],"connectedNodes":[5,3]},{"coordinate":[6,5],"connectedNodes":[6,4]},{"coordinate":[5,5],"connectedNodes":[7,5]},{"coordinate":[4,5],"connectedNodes":[8,6]},{"coordinate":[3,5],"connectedNodes":[9,7]},{"coordinate":[2,5],"connectedNodes":[8,10]},{"coordinate":[2,4],"connectedNodes":[9,11]},{"coordinate":[2,3],"connectedNodes":[10,12]},{"coordinate":[2,2],"connectedNodes":[11,13]},{"coordinate":[2,1],"connectedNodes":[12,14]},{"coordinate":[3,1],"connectedNodes":[13,15]},{"coordinate":[4,1],"connectedNodes":[14,16]},{"coordinate":[5,1],"connectedNodes":[15,17]},{"coordinate":[6,1],"connectedNodes":[16,18]},{"coordinate":[6,2],"connectedNodes":[19,17]},{"coordinate":[6,3],"connectedNodes":[20,18]},{"coordinate":[6,4],"connectedNodes":[21,19]},{"coordinate":[5,4],"connectedNodes":[22,20]},{"coordinate":[4,4],"connectedNodes":[23,21]},{"coordinate":[3,4],"connectedNodes":[22,24]},{"coordinate":[3,3],"connectedNodes":[23,25]},{"coordinate":[3,2],"connectedNodes":[24,26]},{"coordinate":[4,2],"connectedNodes":[25,27]},{"coordinate":[5,2],"connectedNodes":[26]}]',
        origin='{"coordinate":[7,1],"direction":"N"}',
        destinations="[[5,2]]",
        default=True,
        disable_algorithm_score=True,
        blocklyEnabled=False,
        theme_name="snow",
        character_name="Van",
        lesson="Oh dear, you might get a bit dizzy!",
        hint="What are you counting here, straight roads or bends?",
    )

    level1019 = Level(
        name="1019",
        episode=episode13,
        path='[{"coordinate":[9,3],"connectedNodes":[1]},{"coordinate":[8,3],"connectedNodes":[2,0]},{"coordinate":[7,3],"connectedNodes":[3,1,15]},{"coordinate":[7,4],"connectedNodes":[4,2]},{"coordinate":[6,4],"connectedNodes":[5,3]},{"coordinate":[5,4],"connectedNodes":[6,4,12]},{"coordinate":[4,4],"connectedNodes":[7,5]},{"coordinate":[3,4],"connectedNodes":[8,6]},{"coordinate":[3,5],"connectedNodes":[9,7]},{"coordinate":[2,5],"connectedNodes":[10,8,17]},{"coordinate":[1,5],"connectedNodes":[11,9]},{"coordinate":[0,5],"connectedNodes":[10]},{"coordinate":[5,3],"connectedNodes":[5,13]},{"coordinate":[5,2],"connectedNodes":[21,12,14]},{"coordinate":[6,2],"connectedNodes":[13,15]},{"coordinate":[7,2],"connectedNodes":[14,2,16]},{"coordinate":[7,1],"connectedNodes":[15]},{"coordinate":[2,4],"connectedNodes":[9,18]},{"coordinate":[2,3],"connectedNodes":[17,19]},{"coordinate":[2,2],"connectedNodes":[18,20]},{"coordinate":[3,2],"connectedNodes":[19,21]},{"coordinate":[4,2],"connectedNodes":[20,13]}]',
        origin='{"coordinate":[9,3],"direction":"W"}',
        destinations="[[0,5]]",
        default=True,
        model_solution="[11]",
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="grass",
        character_name="Van",
        lesson="Have you noticed that there are more roads ahead than turns? Try checking if there is a road ahead and then otherwise making the turns you need...",
        hint="Remember to use if..else",
    )

    level1020 = Level(
        name="1020",
        episode=episode13,
        path='[{"coordinate":[2,2],"connectedNodes":[1]},{"coordinate":[3,2],"connectedNodes":[0,2,19]},{"coordinate":[3,3],"connectedNodes":[10,3,1]},{"coordinate":[4,3],"connectedNodes":[2,4]},{"coordinate":[4,4],"connectedNodes":[5,3]},{"coordinate":[5,4],"connectedNodes":[4,6,17]},{"coordinate":[5,5],"connectedNodes":[7,5]},{"coordinate":[6,5],"connectedNodes":[6,8]},{"coordinate":[6,6],"connectedNodes":[9,7]},{"coordinate":[7,6],"connectedNodes":[8]},{"coordinate":[3,4],"connectedNodes":[11,2]},{"coordinate":[3,5],"connectedNodes":[12,10]},{"coordinate":[3,6],"connectedNodes":[13,11]},{"coordinate":[3,7],"connectedNodes":[14,12]},{"coordinate":[4,7],"connectedNodes":[13,15]},{"coordinate":[5,7],"connectedNodes":[14,16]},{"coordinate":[6,7],"connectedNodes":[15]},{"coordinate":[5,3],"connectedNodes":[5,18]},{"coordinate":[5,2],"connectedNodes":[19,17]},{"coordinate":[4,2],"connectedNodes":[1,18]}]',
        origin='{"coordinate":[2,2],"direction":"E"}',
        destinations="[[7,6]]",
        default=True,
        disable_algorithm_score=True,
        blocklyEnabled=False,
        theme_name="snow",
        character_name="Van",
        lesson="Use if..else in Python for this level",
        hint="Don't get distracted by the other roads. Look for a pattern you can repeat.",
    )

    level1021 = Level(
        name="1021",
        episode=episode13,
        path='[{"coordinate":[4,0],"connectedNodes":[1]},{"coordinate":[4,1],"connectedNodes":[2,0]},{"coordinate":[3,1],"connectedNodes":[3,1]},{"coordinate":[3,2],"connectedNodes":[4,2]},{"coordinate":[3,3],"connectedNodes":[5,3]},{"coordinate":[3,4],"connectedNodes":[6,4]},{"coordinate":[2,4],"connectedNodes":[7,5]},{"coordinate":[2,5],"connectedNodes":[8,6]},{"coordinate":[2,6],"connectedNodes":[9,7]},{"coordinate":[1,6],"connectedNodes":[10,8]},{"coordinate":[1,7],"connectedNodes":[9]}]',
        origin='{"coordinate":[4,0],"direction":"N"}',
        destinations="[[3,1],[2,4],[1,6],[1,7]]",
        default=True,
        disable_algorithm_score=True,
        blocklyEnabled=False,
        theme_name="grass",
        character_name="Van",
        lesson="This is a really busy road. Make sure that you don't miss any of the houses.",
        hint="Did you get the last house? Think about what value the loop counter will have at that point in your code...",
    )

    level1022 = Level(
        name="1022",
        episode=episode13,
        path='[{"coordinate":[2,3],"connectedNodes":[1]},{"coordinate":[2,2],"connectedNodes":[0,2,16]},{"coordinate":[3,2],"connectedNodes":[1,3]},{"coordinate":[3,1],"connectedNodes":[2,4,14]},{"coordinate":[4,1],"connectedNodes":[3,5]},{"coordinate":[5,1],"connectedNodes":[4,6,22]},{"coordinate":[5,2],"connectedNodes":[7,5]},{"coordinate":[6,2],"connectedNodes":[6,8]},{"coordinate":[6,3],"connectedNodes":[9,17,7]},{"coordinate":[6,4],"connectedNodes":[10,8]},{"coordinate":[5,4],"connectedNodes":[11,9]},{"coordinate":[5,5],"connectedNodes":[12,10]},{"coordinate":[4,5],"connectedNodes":[13,11]},{"coordinate":[3,5],"connectedNodes":[12]},{"coordinate":[3,0],"connectedNodes":[15,3]},{"coordinate":[2,0],"connectedNodes":[16,14]},{"coordinate":[2,1],"connectedNodes":[1,15]},{"coordinate":[7,3],"connectedNodes":[8,18]},{"coordinate":[8,3],"connectedNodes":[17,19]},{"coordinate":[8,2],"connectedNodes":[18,20]},{"coordinate":[8,1],"connectedNodes":[21,19]},{"coordinate":[7,1],"connectedNodes":[22,20]},{"coordinate":[6,1],"connectedNodes":[5,21]}]',
        origin='{"coordinate":[2,3],"direction":"S"}',
        destinations="[[3,5]]",
        default=True,
        model_solution="[12]",
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="grass",
        character_name="Van",
        lesson="There are lots of turns here, don't get distracted.",
        hint="Think about the order of the questions you ask using your if and elif statements.",
    )

    level1023 = Level(
        name="1023",
        episode=episode13,
        path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[1,28,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,3],"connectedNodes":[3,5]},{"coordinate":[2,2],"connectedNodes":[4,6]},{"coordinate":[2,1],"connectedNodes":[5,7]},{"coordinate":[3,1],"connectedNodes":[6,8]},{"coordinate":[4,1],"connectedNodes":[7,9]},{"coordinate":[5,1],"connectedNodes":[8,10]},{"coordinate":[6,1],"connectedNodes":[9,11]},{"coordinate":[7,1],"connectedNodes":[10,12]},{"coordinate":[8,1],"connectedNodes":[11,13]},{"coordinate":[9,1],"connectedNodes":[12,14]},{"coordinate":[9,2],"connectedNodes":[15,13]},{"coordinate":[9,3],"connectedNodes":[16,14]},{"coordinate":[9,4],"connectedNodes":[17,15]},{"coordinate":[9,5],"connectedNodes":[18,16]},{"coordinate":[9,6],"connectedNodes":[19,17]},{"coordinate":[8,6],"connectedNodes":[20,18]},{"coordinate":[7,6],"connectedNodes":[21,19]},{"coordinate":[6,6],"connectedNodes":[22,20]},{"coordinate":[5,6],"connectedNodes":[23,21]},{"coordinate":[4,6],"connectedNodes":[22,24]},{"coordinate":[4,5],"connectedNodes":[28,23,25]},{"coordinate":[4,4],"connectedNodes":[24,26]},{"coordinate":[4,3],"connectedNodes":[25,27]},{"coordinate":[4,2],"connectedNodes":[26]},{"coordinate":[3,5],"connectedNodes":[2,24]}]',
        origin='{"coordinate":[2,7],"direction":"S"}',
        destinations="[[4,2]]",
        default=True,
        model_solution="[12]",
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="farm",
        character_name="Van",
        lesson="Don't go the long way around!",
        hint="Think carefully about the order in which you ask questions in your if..else if block",
    )

    level1024 = Level(
        name="1024",
        episode=episode13,
        path='[{"coordinate":[7,0],"connectedNodes":[1]},{"coordinate":[7,1],"connectedNodes":[10,2,0]},{"coordinate":[7,2],"connectedNodes":[3,24,1]},{"coordinate":[7,3],"connectedNodes":[4,2]},{"coordinate":[6,3],"connectedNodes":[5,3]},{"coordinate":[6,4],"connectedNodes":[23,6,33,4]},{"coordinate":[6,5],"connectedNodes":[7,5]},{"coordinate":[6,6],"connectedNodes":[8,6]},{"coordinate":[5,6],"connectedNodes":[9,7]},{"coordinate":[5,7],"connectedNodes":[8]},{"coordinate":[6,1],"connectedNodes":[11,1]},{"coordinate":[5,1],"connectedNodes":[12,10]},{"coordinate":[4,1],"connectedNodes":[13,11]},{"coordinate":[3,1],"connectedNodes":[14,12]},{"coordinate":[2,1],"connectedNodes":[15,13]},{"coordinate":[1,1],"connectedNodes":[16,17,14]},{"coordinate":[0,1],"connectedNodes":[15]},{"coordinate":[1,2],"connectedNodes":[18,15]},{"coordinate":[1,3],"connectedNodes":[19,17]},{"coordinate":[1,4],"connectedNodes":[20,18]},{"coordinate":[2,4],"connectedNodes":[19,21]},{"coordinate":[3,4],"connectedNodes":[20,22]},{"coordinate":[4,4],"connectedNodes":[21,23]},{"coordinate":[5,4],"connectedNodes":[22,5]},{"coordinate":[8,2],"connectedNodes":[2,25]},{"coordinate":[9,2],"connectedNodes":[24,26]},{"coordinate":[9,3],"connectedNodes":[27,25]},{"coordinate":[9,4],"connectedNodes":[28,26]},{"coordinate":[9,5],"connectedNodes":[29,27]},{"coordinate":[9,6],"connectedNodes":[30,28]},{"coordinate":[8,6],"connectedNodes":[29,31]},{"coordinate":[8,5],"connectedNodes":[30,32]},{"coordinate":[8,4],"connectedNodes":[33,31]},{"coordinate":[7,4],"connectedNodes":[5,32]}]',
        origin='{"coordinate":[7,0],"direction":"N"}',
        destinations="[[5,7]]",
        default=True,
        disable_algorithm_score=True,
        blocklyEnabled=False,
        theme_name="farm",
        character_name="Van",
        lesson="Look carefully for the shortest route.",
        hint="Think carefully about the order in which you ask questions in your if..elif statements.",
    )

    level1025 = Level(
        name="1025",
        episode=episode13,
        path='[{"coordinate":[8,0],"connectedNodes":[1]},{"coordinate":[8,1],"connectedNodes":[2,0]},{"coordinate":[8,2],"connectedNodes":[3,1]},{"coordinate":[7,2],"connectedNodes":[4,2]},{"coordinate":[6,2],"connectedNodes":[12,5,3]},{"coordinate":[6,3],"connectedNodes":[25,4]},{"coordinate":[4,5],"connectedNodes":[7,19]},{"coordinate":[3,5],"connectedNodes":[8,6]},{"coordinate":[2,5],"connectedNodes":[9,7]},{"coordinate":[1,5],"connectedNodes":[10,8,18]},{"coordinate":[1,6],"connectedNodes":[11,9]},{"coordinate":[1,7],"connectedNodes":[10]},{"coordinate":[5,2],"connectedNodes":[13,4]},{"coordinate":[4,2],"connectedNodes":[14,12]},{"coordinate":[3,2],"connectedNodes":[15,13]},{"coordinate":[2,2],"connectedNodes":[16,14]},{"coordinate":[1,2],"connectedNodes":[17,15]},{"coordinate":[1,3],"connectedNodes":[18,16]},{"coordinate":[1,4],"connectedNodes":[9,17]},{"coordinate":[5,5],"connectedNodes":[6,20]},{"coordinate":[6,5],"connectedNodes":[19,21]},{"coordinate":[7,5],"connectedNodes":[20,22]},{"coordinate":[8,5],"connectedNodes":[21,23]},{"coordinate":[8,4],"connectedNodes":[24,22]},{"coordinate":[7,4],"connectedNodes":[25,23]},{"coordinate":[6,4],"connectedNodes":[24,5]}]',
        traffic_lights='[{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":5},"direction":"W","startTime":0,"startingState":"RED"},{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":1,"y":5},"direction":"N","startTime":0,"startingState":"RED"}]',
        origin='{"coordinate":[8,0],"direction":"N"}',
        destinations="[[1,7]]",
        default=True,
        disable_algorithm_score=True,
        blocklyEnabled=False,
        theme_name="grass",
        character_name="Van",
        lesson="Look carefully for the shortest route.",
        hint="Think carefully about the order in which you ask questions in your if..elif statements. Don't forget the traffic lights.",
    )

    level1026 = Level.objects.get(name="85", default=True)
    level1026.pk = None
    level1026._state.adding = True
    level1026.name = "1026"
    level1026.model_solution = "[4]"
    level1026.disable_algorithm_score = False
    level1026.episode = episode14

    level1027 = Level(
        name="1027",
        episode=episode14,
        path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3,5]},{"coordinate":[5,3],"connectedNodes":[4,6]},{"coordinate":[6,3],"connectedNodes":[5,7]},{"coordinate":[7,3],"connectedNodes":[6,8]},{"coordinate":[8,3],"connectedNodes":[7]}]',
        origin='{"coordinate":[0,3],"direction":"E"}',
        destinations="[[8,3]]",
        default=True,
        model_solution="[4]",
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="grass",
        character_name="Van",
        lesson="Just keep going until you get there...",
        hint="You might find that the solution to this level is quite familiar...",
    )

    level1028 = Level(
        name="1028",
        episode=episode14,
        path='[{"coordinate":[2,2],"connectedNodes":[1]},{"coordinate":[3,2],"connectedNodes":[0,2]},{"coordinate":[3,3],"connectedNodes":[3,1]},{"coordinate":[4,3],"connectedNodes":[2,4]},{"coordinate":[4,4],"connectedNodes":[5,3]},{"coordinate":[5,4],"connectedNodes":[4,6]},{"coordinate":[5,5],"connectedNodes":[7,5]},{"coordinate":[6,5],"connectedNodes":[6,8]},{"coordinate":[6,6],"connectedNodes":[9,7]},{"coordinate":[7,6],"connectedNodes":[8]}]',
        origin='{"coordinate":[2,2],"direction":"E"}',
        destinations="[[7,6]]",
        default=True,
        model_solution="[5]",
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="grass",
        character_name="Van",
        lesson="Well done, you did it! Now have a go at using the <b>Repeat until</b> block on a road with lots of turns.",
        hint="This is another route you have seen before. Last time you counted how many times your instructions were repeated. This time, your program is going to repeat your commands until you reach the destination. What do you need to repeat?",
    )

    level1029 = Level.objects.get(name="119", default=True)
    level1029.pk = None
    level1029._state.adding = True
    level1029.name = "1029"
    level1029.blocklyEnabled = True
    level1029.pythonEnabled = False
    level1029.pythonViewEnabled = True
    level1029.model_solution = "[7]"
    level1029.disable_algorithm_score = False
    level1029.episode = episode14

    level1030 = Level.objects.get(name="84", default=True)
    level1030.pk = None
    level1030._state.adding = True
    level1030.name = "1030"
    level1030.blocklyEnabled = False
    level1030.pythonEnabled = True
    level1030.pythonViewEnabled = False
    level1030.model_solution = "[]"
    level1030.disable_algorithm_score = True
    level1030.episode = episode14

    level1031 = Level.objects.get(name="34", default=True)
    level1031.pk = None
    level1031._state.adding = True
    level1031.name = "1031"
    level1031.blocklyEnabled = True
    level1031.pythonEnabled = False
    level1031.pythonViewEnabled = True
    level1031.model_solution = "[7]"
    level1031.disable_algorithm_score = False
    level1031.episode = episode14

    level1032 = Level(
        name="1032",
        episode=episode14,
        path='[{"coordinate":[5,0],"connectedNodes":[1]},{"coordinate":[5,1],"connectedNodes":[2,0]},{"coordinate":[5,2],"connectedNodes":[3,23,1]},{"coordinate":[5,3],"connectedNodes":[4,2]},{"coordinate":[5,4],"connectedNodes":[17,3]},{"coordinate":[4,5],"connectedNodes":[6,17]},{"coordinate":[3,5],"connectedNodes":[7,5]},{"coordinate":[2,5],"connectedNodes":[24,6,8]},{"coordinate":[2,4],"connectedNodes":[7,9]},{"coordinate":[2,3],"connectedNodes":[8,10]},{"coordinate":[2,2],"connectedNodes":[9,11]},{"coordinate":[2,1],"connectedNodes":[10,12]},{"coordinate":[3,1],"connectedNodes":[11,13]},{"coordinate":[4,1],"connectedNodes":[12,14]},{"coordinate":[4,2],"connectedNodes":[15,13]},{"coordinate":[4,3],"connectedNodes":[16,14]},{"coordinate":[4,4],"connectedNodes":[15]},{"coordinate":[5,5],"connectedNodes":[5,29,18,4]},{"coordinate":[6,5],"connectedNodes":[17,19]},{"coordinate":[7,5],"connectedNodes":[18,20]},{"coordinate":[7,4],"connectedNodes":[19,21]},{"coordinate":[7,3],"connectedNodes":[20,22]},{"coordinate":[7,2],"connectedNodes":[23,21,36]},{"coordinate":[6,2],"connectedNodes":[2,22]},{"coordinate":[1,5],"connectedNodes":[25,7]},{"coordinate":[1,6],"connectedNodes":[26,24]},{"coordinate":[2,6],"connectedNodes":[25,27]},{"coordinate":[3,6],"connectedNodes":[26,28]},{"coordinate":[4,6],"connectedNodes":[27,29]},{"coordinate":[5,6],"connectedNodes":[28,30,17]},{"coordinate":[6,6],"connectedNodes":[29,31]},{"coordinate":[7,6],"connectedNodes":[30,32]},{"coordinate":[8,6],"connectedNodes":[31,33]},{"coordinate":[8,5],"connectedNodes":[32,34]},{"coordinate":[8,4],"connectedNodes":[33,35]},{"coordinate":[8,3],"connectedNodes":[34,36]},{"coordinate":[8,2],"connectedNodes":[22,35]}]',
        origin='{"coordinate":[5,0],"direction":"N"}',
        destinations="[[4,4]]",
        default=True,
        model_solution="[7]",
        pythonEnabled=False,
        pythonViewEnabled=True,
        theme_name="grass",
        character_name="Van",
        lesson="You don't have a right turn block here, so plan your route carefully.",
        hint="Think carefully about the order in which you ask questions in your if-statement here...",
    )

    level1033 = Level(
        name="1033",
        episode=episode14,
        path='[{"coordinate":[7,1],"connectedNodes":[1]},{"coordinate":[7,2],"connectedNodes":[2,0]},{"coordinate":[6,2],"connectedNodes":[3,1]},{"coordinate":[6,3],"connectedNodes":[4,13,2]},{"coordinate":[5,3],"connectedNodes":[5,3]},{"coordinate":[5,4],"connectedNodes":[6,16,15,4]},{"coordinate":[4,4],"connectedNodes":[7,5]},{"coordinate":[4,5],"connectedNodes":[8,16,6]},{"coordinate":[3,5],"connectedNodes":[9,7]},{"coordinate":[3,6],"connectedNodes":[10,8]},{"coordinate":[2,6],"connectedNodes":[11,9]},{"coordinate":[2,7],"connectedNodes":[12,17,10]},{"coordinate":[1,7],"connectedNodes":[11]},{"coordinate":[7,3],"connectedNodes":[3,14]},{"coordinate":[7,4],"connectedNodes":[15,13]},{"coordinate":[6,4],"connectedNodes":[5,22,14]},{"coordinate":[5,5],"connectedNodes":[7,5]},{"coordinate":[3,7],"connectedNodes":[11,18]},{"coordinate":[4,7],"connectedNodes":[17,19]},{"coordinate":[5,7],"connectedNodes":[18,20]},{"coordinate":[6,7],"connectedNodes":[19,21]},{"coordinate":[6,6],"connectedNodes":[20,22]},{"coordinate":[6,5],"connectedNodes":[21,15]}]',
        origin='{"coordinate":[7,1],"direction":"N"}',
        destinations="[[1,7]]",
        default=True,
        disable_algorithm_score=True,
        blocklyEnabled=False,
        theme_name="snow",
        character_name="Van",
        lesson="Can you find the shortest route?",
        hint="In this level, you want to check for a left turn first. If there is no left turn, turn right. Keep in mind what that looks like in Python.",
    )

    level1034 = Level(
        name="1034",
        episode=episode14,
        path='[{"coordinate":[0,6],"connectedNodes":[1]},{"coordinate":[1,6],"connectedNodes":[0,2]},{"coordinate":[2,6],"connectedNodes":[1,3]},{"coordinate":[3,6],"connectedNodes":[2,4]},{"coordinate":[4,6],"connectedNodes":[3,5]},{"coordinate":[5,6],"connectedNodes":[4,6]},{"coordinate":[5,5],"connectedNodes":[5,23,7]},{"coordinate":[5,4],"connectedNodes":[6,8]},{"coordinate":[5,3],"connectedNodes":[7,29,9]},{"coordinate":[5,2],"connectedNodes":[8,10]},{"coordinate":[5,1],"connectedNodes":[11,9]},{"coordinate":[4,1],"connectedNodes":[12,10]},{"coordinate":[3,1],"connectedNodes":[13,11]},{"coordinate":[2,1],"connectedNodes":[14,12]},{"coordinate":[1,1],"connectedNodes":[15,13]},{"coordinate":[1,2],"connectedNodes":[34,16,14]},{"coordinate":[1,3],"connectedNodes":[17,15]},{"coordinate":[1,4],"connectedNodes":[30,16]},{"coordinate":[2,5],"connectedNodes":[30,19]},{"coordinate":[3,5],"connectedNodes":[18,20]},{"coordinate":[3,4],"connectedNodes":[19,21]},{"coordinate":[3,3],"connectedNodes":[20,22]},{"coordinate":[3,2],"connectedNodes":[21]},{"coordinate":[6,5],"connectedNodes":[6,24]},{"coordinate":[7,5],"connectedNodes":[23,25]},{"coordinate":[8,5],"connectedNodes":[24,26]},{"coordinate":[8,4],"connectedNodes":[25,27]},{"coordinate":[8,3],"connectedNodes":[28,26]},{"coordinate":[7,3],"connectedNodes":[29,27]},{"coordinate":[6,3],"connectedNodes":[8,28]},{"coordinate":[1,5],"connectedNodes":[31,18,17]},{"coordinate":[0,5],"connectedNodes":[30,32]},{"coordinate":[0,4],"connectedNodes":[31,33]},{"coordinate":[0,3],"connectedNodes":[32,34]},{"coordinate":[0,2],"connectedNodes":[33,15]}]',
        origin='{"coordinate":[0,6],"direction":"E"}',
        destinations="[[3,2]]",
        default=True,
        disable_algorithm_score=True,
        blocklyEnabled=False,
        theme_name="grass",
        character_name="Van",
        lesson="Can you find the shortest route? Don't take the scenic route.",
        hint="Just look for the simplest route to the house.",
    )

    level1035 = Level.objects.get(name="99", default=True)
    level1035.pk = None
    level1035._state.adding = True
    level1035.name = "1035"
    level1035.blocklyEnabled = True
    level1035.pythonEnabled = False
    level1035.pythonViewEnabled = True
    level1035.model_solution = "[9]"
    level1035.disable_algorithm_score = False
    level1035.episode = episode14

    level1036 = Level.objects.get(name="38", default=True)
    level1036.pk = None
    level1036._state.adding = True
    level1036.name = "1036"
    level1036.pythonViewEnabled = True
    level1036.model_solution = "[11]"
    level1036.disable_algorithm_score = False
    level1036.episode = episode14

    level1037 = Level.objects.get(name="100", default=True)
    level1037.pk = None
    level1037._state.adding = True
    level1037.name = "1037"
    level1037.episode = episode14

    level1038 = Level.objects.get(name="39", default=True)
    level1038.pk = None
    level1038._state.adding = True
    level1038.name = "1038"
    level1038.blocklyEnabled = False
    level1038.pythonEnabled = True
    level1038.model_solution = "[]"
    level1038.disable_route_score = False
    level1038.disable_algorithm_score = True
    level1038.episode = episode14

    level1039 = Level.objects.get(name="47", default=True)
    level1039.pk = None
    level1039._state.adding = True
    level1039.name = "1039"
    level1039.blocklyEnabled = False
    level1039.pythonEnabled = True
    level1039.model_solution = "[]"
    level1039.disable_algorithm_score = True
    level1039.episode = episode14

    level1040 = Level.objects.get(name="48", default=True)
    level1040.pk = None
    level1040._state.adding = True
    level1040.name = "1040"
    level1040.blocklyEnabled = False
    level1040.pythonEnabled = True
    level1040.model_solution = "[]"
    level1040.disable_algorithm_score = True
    level1040.episode = episode14

    level1041 = Level.objects.get(name="83", default=True)
    level1041.pk = None
    level1041._state.adding = True
    level1041.name = "1041"
    level1041.disable_algorithm_score = False
    level1041.episode = episode15

    level1042 = Level.objects.get(name="95", default=True)
    level1042.pk = None
    level1042._state.adding = True
    level1042.name = "1042"
    level1042.episode = episode15

    level1043 = Level.objects.get(name="96", default=True)
    level1043.pk = None
    level1043._state.adding = True
    level1043.name = "1043"
    level1043.episode = episode15

    level1044 = Level.objects.get(name="84", default=True)
    level1044.pk = None
    level1044._state.adding = True
    level1044.name = "1044"
    level1044.disable_algorithm_score = False
    level1044.episode = episode15

    level1045 = Level.objects.get(name="97", default=True)
    level1045.pk = None
    level1045._state.adding = True
    level1045.name = "1045"
    level1045.episode = episode15

    level1046 = Level.objects.get(name="106", default=True)
    level1046.pk = None
    level1046._state.adding = True
    level1046.name = "1046"
    level1046.episode = episode15

    level1047 = Level.objects.get(name="107", default=True)
    level1047.pk = None
    level1047._state.adding = True
    level1047.name = "1047"
    level1047.episode = episode15

    level1048 = Level.objects.get(name="108", default=True)
    level1048.pk = None
    level1048._state.adding = True
    level1048.name = "1048"
    level1048.episode = episode15

    level1049 = Level.objects.get(name="109", default=True)
    level1049.pk = None
    level1049._state.adding = True
    level1049.name = "1049"
    level1049.next_level = None
    level1049.episode = episode15

    level1050 = Level.objects.get(name="61", default=True)
    level1050.pk = None
    level1050._state.adding = True
    level1050.name = "1050"
    level1050.pythonViewEnabled = True
    level1050.disable_algorithm_score = False
    level1050.episode = episode22

    level1051 = Level.objects.get(name="62", default=True)
    level1051.pk = None
    level1051._state.adding = True
    level1051.name = "1051"
    level1051.pythonViewEnabled = True
    level1051.disable_algorithm_score = False
    level1051.episode = episode22

    level1052 = Level.objects.get(name="63", default=True)
    level1052.pk = None
    level1052._state.adding = True
    level1052.name = "1052"
    level1052.blocklyEnabled = False
    level1052.pythonEnabled = True
    level1052.model_solution = "[]"
    level1052.disable_algorithm_score = True
    level1052.episode = episode22

    level1053 = Level.objects.get(name="64", default=True)
    level1053.pk = None
    level1053._state.adding = True
    level1053.name = "1053"
    level1053.blocklyEnabled = False
    level1053.pythonEnabled = True
    level1053.model_solution = "[]"
    level1053.disable_algorithm_score = True
    level1053.episode = episode22

    level1054 = Level.objects.get(name="65", default=True)
    level1054.pk = None
    level1054._state.adding = True
    level1054.name = "1054"
    level1054.blocklyEnabled = False
    level1054.pythonEnabled = True
    level1054.model_solution = "[]"
    level1054.disable_algorithm_score = True
    level1054.episode = episode22

    level1055 = Level.objects.get(name="66", default=True)
    level1055.pk = None
    level1055._state.adding = True
    level1055.name = "1055"
    level1055.blocklyEnabled = False
    level1055.pythonEnabled = True
    level1055.model_solution = "[]"
    level1055.disable_algorithm_score = True
    level1055.episode = episode22

    level1056 = Level.objects.get(name="67", default=True)
    level1056.pk = None
    level1056._state.adding = True
    level1056.name = "1056"
    level1056.blocklyEnabled = False
    level1056.pythonEnabled = True
    level1056.model_solution = "[]"
    level1056.disable_algorithm_score = True
    level1056.episode = episode22

    level1057 = Level.objects.get(name="90", default=True)
    level1057.pk = None
    level1057._state.adding = True
    level1057.name = "1057"
    level1057.blocklyEnabled = False
    level1057.pythonViewEnabled = False
    level1057.pythonEnabled = True
    level1057.disable_algorithm_score = True
    level1057.episode = episode22

    level1058 = Level.objects.get(name="91", default=True)
    level1058.pk = None
    level1058._state.adding = True
    level1058.name = "1058"
    level1058.blocklyEnabled = False
    level1058.pythonViewEnabled = False
    level1058.pythonEnabled = True
    level1058.disable_algorithm_score = True
    level1058.episode = episode22

    level1059 = Level.objects.get(name="101", default=True)
    level1059.pk = None
    level1059._state.adding = True
    level1059.name = "1059"
    level1059.episode = episode22

    level1060 = Level.objects.get(name="102", default=True)
    level1060.pk = None
    level1060._state.adding = True
    level1060.name = "1060"
    level1060.episode = episode22

    def save_all_levels():
        level1014.save()
        level1015.save()
        level1016.save()
        level1017.save()
        level1018.save()
        level1019.save()
        level1020.save()
        level1021.save()
        level1022.save()
        level1023.save()
        level1024.save()
        level1025.save()
        level1026.save()
        level1027.save()
        level1028.save()
        level1029.save()
        level1030.save()
        level1031.save()
        level1032.save()
        level1033.save()
        level1034.save()
        level1035.save()
        level1036.save()
        level1037.save()
        level1038.save()
        level1039.save()
        level1040.save()
        level1041.save()
        level1042.save()
        level1043.save()
        level1044.save()
        level1045.save()
        level1046.save()
        level1047.save()
        level1048.save()
        level1049.save()
        level1050.save()
        level1051.save()
        level1052.save()
        level1053.save()
        level1054.save()
        level1055.save()
        level1056.save()
        level1057.save()
        level1058.save()
        level1059.save()
        level1060.save()

    save_all_levels()
    level1014.next_level = level1015
    level1015.next_level = level1016
    level1016.next_level = level1017
    level1017.next_level = level1018
    level1018.next_level = level1019
    level1019.next_level = level1020
    level1020.next_level = level1021
    level1021.next_level = level1022
    level1022.next_level = level1023
    level1023.next_level = level1024
    level1024.next_level = level1025
    level1025.next_level = level1026
    level1026.next_level = level1027
    level1027.next_level = level1028
    level1028.next_level = level1029
    level1029.next_level = level1030
    level1030.next_level = level1031
    level1031.next_level = level1032
    level1032.next_level = level1033
    level1033.next_level = level1034
    level1034.next_level = level1035
    level1035.next_level = level1036
    level1036.next_level = level1037
    level1037.next_level = level1038
    level1038.next_level = level1039
    level1039.next_level = level1040
    level1040.next_level = level1041
    level1041.next_level = level1042
    level1042.next_level = level1043
    level1043.next_level = level1044
    level1044.next_level = level1045
    level1045.next_level = level1046
    level1046.next_level = level1047
    level1047.next_level = level1048
    level1048.next_level = level1049
    level1050.next_level = level1051
    level1051.next_level = level1052
    level1052.next_level = level1053
    level1053.next_level = level1054
    level1054.next_level = level1055
    level1055.next_level = level1056
    level1056.next_level = level1057
    level1057.next_level = level1058
    level1058.next_level = level1059
    level1059.next_level = level1060
    level1060.next_level = None

    save_all_levels()


def delete_python_den_levels(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    Level.objects.filter(name__in=range(1014, 1061)).delete()


def add_python_den_blocks(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    LevelBlock = apps.get_model("game", "LevelBlock")
    Block = apps.get_model("game", "Block")

    def set_blocks(level, blocks):
        set_blocks_inner(level, blocks, LevelBlock, Block)

    level1014 = Level.objects.get(name="1014", default=True)
    level1015 = Level.objects.get(name="1015", default=True)
    level1019 = Level.objects.get(name="1019", default=True)
    level1022 = Level.objects.get(name="1022", default=True)
    level1023 = Level.objects.get(name="1023", default=True)
    level1026 = Level.objects.get(name="1026", default=True)
    level1027 = Level.objects.get(name="1027", default=True)
    level1028 = Level.objects.get(name="1028", default=True)
    level1029 = Level.objects.get(name="1029", default=True)
    level1031 = Level.objects.get(name="1031", default=True)
    level1032 = Level.objects.get(name="1032", default=True)
    level1035 = Level.objects.get(name="1035", default=True)
    level1036 = Level.objects.get(name="1036", default=True)
    level1041 = Level.objects.get(name="1041", default=True)
    level1044 = Level.objects.get(name="1044", default=True)
    level1050 = Level.objects.get(name="1050", default=True)
    level1051 = Level.objects.get(name="1051", default=True)
    level1057 = Level.objects.get(name="1057", default=True)
    level1058 = Level.objects.get(name="1058", default=True)

    set_blocks(
        level1014,
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
        ),
    )

    set_blocks(
        level1015,
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
        ),
    )

    set_blocks(
        level1019,
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
        ),
    )

    set_blocks(
        level1022,
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
        ),
    )

    set_blocks(
        level1023,
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
        ),
    )

    set_blocks(
        level1026,
        json.loads(
            '[{"type": "move_forwards"},'
            + '{"type": "turn_left"},'
            + '{"type": "turn_right"},'
            + '{"type": "at_destination"},'
            + '{"type": "logic_negate"},'
            + '{"type": "controls_repeat_while"}]'
        ),
    )

    set_blocks(
        level1027,
        json.loads(
            '[{"type": "controls_repeat_while"},'
            + '{"type": "logic_negate"},'
            + '{"type": "at_destination"},'
            + '{"type": "move_forwards"}]'
        ),
    )

    set_blocks(
        level1028,
        json.loads(
            '[{"type": "controls_repeat_while"},'
            + '{"type": "logic_negate"},'
            + '{"type": "at_destination"},'
            + '{"type": "turn_left"},'
            + '{"type": "turn_right"}]'
        ),
    )

    set_blocks(
        level1029,
        json.loads(
            '[{"type": "controls_repeat_while"},'
            + '{"type": "logic_negate"},'
            + '{"type": "at_destination"},'
            + '{"type": "turn_left"},'
            + '{"type": "turn_right"},'
            + '{"type": "move_forwards"}]'
        ),
    )

    set_blocks(
        level1031,
        json.loads(
            '[{"type": "controls_repeat_while"},'
            + '{"type": "logic_negate"},'
            + '{"type": "at_destination"},'
            + '{"type": "controls_if"},'
            + '{"type": "road_exists"},'
            + '{"type": "turn_left"},'
            + '{"type": "move_forwards"}]'
        ),
    )

    set_blocks(
        level1032,
        json.loads(
            '[{"type": "controls_repeat_while"},'
            + '{"type": "logic_negate"},'
            + '{"type": "at_destination"},'
            + '{"type": "controls_if"},'
            + '{"type": "road_exists"},'
            + '{"type": "turn_left"},'
            + '{"type": "move_forwards"}]'
        ),
    )

    set_blocks(
        level1035,
        json.loads(
            '[{"type": "controls_repeat_while"},'
            + '{"type": "logic_negate"},'
            + '{"type": "at_destination"},'
            + '{"type": "controls_if"},'
            + '{"type": "road_exists"},'
            + '{"type": "move_forwards"},'
            + '{"type": "turn_left"},'
            + '{"type": "turn_right"}]'
        ),
    )

    set_blocks(
        level1036,
        json.loads(
            '[{"type": "controls_repeat_while"},'
            + '{"type": "logic_negate"},'
            + '{"type": "at_destination"},'
            + '{"type": "controls_if"},'
            + '{"type": "cow_crossing"},'
            + '{"type": "sound_horn"},'
            + '{"type": "road_exists"},'
            + '{"type": "move_forwards"},'
            + '{"type": "turn_left"},'
            + '{"type": "turn_right"}]'
        ),
    )

    set_blocks(
        level1041,
        json.loads(
            '[{"type": "move_forwards"},'
            + '{"type": "turn_left"},'
            + '{"type": "turn_right"},'
            + '{"type": "controls_repeat"}]'
        ),
    )

    set_blocks(
        level1044,
        json.loads(
            '[{"type": "move_forwards"},'
            + '{"type": "turn_left"},'
            + '{"type": "turn_right"},'
            + '{"type": "controls_repeat"}]'
        ),
    )

    set_blocks(
        level1050,
        json.loads(
            '[{"type": "call_proc"},'
            + '{"type": "declare_proc"},'
            + '{"type": "move_forwards"},'
            + '{"type": "turn_left"},'
            + '{"type": "turn_right"},'
            + '{"type": "controls_repeat"}]'
        ),
    )

    set_blocks(
        level1051,
        json.loads(
            '[{"type": "call_proc"},'
            + '{"type": "declare_proc"},'
            + '{"type": "move_forwards"},'
            + '{"type": "turn_right"},'
            + '{"type": "wait"},'
            + '{"type": "controls_repeat_until"},'
            + '{"type": "traffic_light"}]'
        ),
    )

    set_blocks(
        level1057,
        json.loads(
            '[{"type":"move_forwards"},'
            + '{"type":"turn_left"},'
            + '{"type":"turn_right"},'
            + '{"type":"controls_repeat"},'
            + '{"type":"call_proc"},'
            + '{"type":"declare_proc"}]'
        ),
    )

    set_blocks(
        level1058,
        json.loads(
            '[{"type":"move_forwards"},'
            + '{"type":"turn_left"},'
            + '{"type":"turn_right"},'
            + '{"type":"controls_repeat"},'
            + '{"type":"call_proc"},'
            + '{"type":"declare_proc"}]'
        ),
    )


def delete_python_den_blocks(apps, schema_editor):
    LevelBlock = apps.get_model("game", "LevelBlock")
    LevelBlock.objects.filter(level_id__in=range(1014, 1061)).delete()


def add_python_den_decor(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    LevelDecor = apps.get_model("game", "LevelDecor")

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

    def bulk_copy_decor(old_level_name, new_level_name):
        old_level = Level.objects.get(name=old_level_name, default=True)
        decor_to_copy = LevelDecor.objects.filter(level_id=old_level.id).values()
        new_level = Level.objects.get(name=new_level_name, default=True)

        new_level_decor = []
        for decor in decor_to_copy:
            new_level_decor.append(
                LevelDecor(
                    level_id=new_level.pk,
                    x=decor["x"],
                    y=decor["y"],
                    decorName=decor["decorName"],
                )
            )
        LevelDecor.objects.bulk_create(new_level_decor)

    level1014 = Level.objects.get(name="1014", default=True)
    level1015 = Level.objects.get(name="1015", default=True)
    level1016 = Level.objects.get(name="1016", default=True)
    level1017 = Level.objects.get(name="1017", default=True)
    level1018 = Level.objects.get(name="1018", default=True)
    level1019 = Level.objects.get(name="1019", default=True)
    level1020 = Level.objects.get(name="1020", default=True)
    level1021 = Level.objects.get(name="1021", default=True)
    level1022 = Level.objects.get(name="1022", default=True)
    level1023 = Level.objects.get(name="1023", default=True)
    level1024 = Level.objects.get(name="1024", default=True)
    level1027 = Level.objects.get(name="1027", default=True)
    level1028 = Level.objects.get(name="1028", default=True)
    level1033 = Level.objects.get(name="1033", default=True)
    level1034 = Level.objects.get(name="1034", default=True)

    set_decor(
        level1014,
        json.loads(
            '[{"x": 149, "y": 299, "decorName": "pond"},'
            + '{"x": 398, "y": 354, "decorName": "bush"},'
            + '{"x": 399, "y": 318, "decorName": "bush"},'
            + '{"x": 311, "y": 309, "decorName": "tree2"},'
            + '{"x": 568, "y": 516, "decorName": "tree1"},'
            + '{"x": 654, "y": 512, "decorName": "tree1"}]'
        ),
    )

    set_decor(
        level1015,
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
        ),
    )

    set_decor(
        level1016,
        json.loads(
            '[{"x": 699, "y": 499, "decorName": "pond"},'
            + '{"x": 700, "y": 402, "decorName": "pond"},'
            + '{"x": 611, "y": 469, "decorName": "bush"},'
            + '{"x": 610, "y": 427, "decorName": "bush"},'
            + '{"x": 613, "y": 505, "decorName": "tree2"}]'
        ),
    )

    set_decor(
        level1017,
        json.loads(
            '[{"x": 461, "y": 314, "decorName": "pond"},'
            + '{"x": 428, "y": 371, "decorName": "tree1"},'
            + '{"x": 500, "y": 179, "decorName": "tree1"}]'
        ),
    )

    set_decor(
        level1018,
        json.loads(
            '[{"x": 301, "y": 594, "decorName": "tree1"},'
            + '{"x": 421, "y": 598, "decorName": "tree1"},'
            + '{"x": 529, "y": 600, "decorName": "tree1"},'
            + '{"x": 120, "y": 415, "decorName": "tree2"},'
            + '{"x": 93, "y": 300, "decorName": "tree2"}]'
        ),
    )

    set_decor(
        level1019,
        json.loads(
            '[{"x": 562, "y": 42, "decorName": "pond"},'
            + '{"x": 551, "y": 501, "decorName": "bush"},'
            + '{"x": 551, "y": 562, "decorName": "bush"},'
            + '{"x": 602, "y": 299, "decorName": "tree2"},'
            + '{"x": 618, "y": 500, "decorName": "tree1"},'
            + '{"x": 460, "y": 495, "decorName": "tree1"},'
            + '{"x": 145, "y": 364, "decorName": "tree1"},'
            + '{"x": 145, "y": 269, "decorName": "tree1"}]'
        ),
    )

    set_decor(
        level1020,
        json.loads(
            '[{"x": 443, "y": 578, "decorName": "pond"},'
            + '{"x": 640, "y": 434, "decorName": "tree2"},'
            + '{"x": 623, "y": 362, "decorName": "tree1"},'
            + '{"x": 647, "y": 292, "decorName": "tree2"},'
            + '{"x": 694, "y": 341, "decorName": "tree1"},'
            + '{"x": 516, "y": 651, "decorName": "tree2"},'
            + '{"x": 412, "y": 648, "decorName": "tree1"}]'
        ),
    )

    set_decor(
        level1021,
        json.loads(
            '[{"x": 149, "y": 292, "decorName": "pond"},'
            + '{"x": 300, "y": 507, "decorName": "tree1"},'
            + '{"x": 308, "y": 583, "decorName": "tree1"}]'
        ),
    )

    set_decor(
        level1022,
        json.loads(
            '[{"x": 663, "y": 191, "decorName": "pond"},'
            + '{"x": 364, "y": 395, "decorName": "tree1"},'
            + '{"x": 463, "y": 317, "decorName": "tree2"},'
            + '{"x": 367, "y": 237, "decorName": "tree1"},'
            + '{"x": 250, "y": 391, "decorName": "tree2"}]'
        ),
    )

    set_decor(
        level1023,
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
        ),
    )

    set_decor(
        level1024,
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
        ),
    )

    set_decor(
        level1027,
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
        ),
    )

    set_decor(
        level1028,
        json.loads(
            '[{"x": 443, "y": 578, "decorName": "pond"},'
            + '{"x": 640, "y": 434, "decorName": "tree2"},'
            + '{"x": 623, "y": 362, "decorName": "tree1"},'
            + '{"x": 647, "y": 292, "decorName": "tree2"},'
            + '{"x": 694, "y": 341, "decorName": "tree1"},'
            + '{"x": 516, "y": 651, "decorName": "tree2"},'
            + '{"x": 412, "y": 648, "decorName": "tree1"}]'
        ),
    )

    set_decor(
        level1033,
        json.loads(
            '[{"x": 459, "y": 602, "decorName": "pond"},'
            + '{"x": 381, "y": 606, "decorName": "tree2"},'
            + '{"x": 692, "y": 688, "decorName": "tree1"},'
            + '{"x": 717, "y": 620, "decorName": "tree1"},'
            + '{"x": 686, "y": 530, "decorName": "tree2"}]'
        ),
    )

    set_decor(
        level1034,
        json.loads(
            '[{"x": 625, "y": 408, "decorName": "pond"},'
            + '{"x": 201, "y": 411, "decorName": "tree2"},'
            + '{"x": 200, "y": 342, "decorName": "tree1"},'
            + '{"x": 405, "y": 443, "decorName": "tree2"},'
            + '{"x": 400, "y": 514, "decorName": "tree1"}]'
        ),
    )

    bulk_copy_decor("85", "1026")
    bulk_copy_decor("119", "1029")
    bulk_copy_decor("84", "1030")
    bulk_copy_decor("34", "1031")
    bulk_copy_decor("99", "1035")
    bulk_copy_decor("38", "1036")
    bulk_copy_decor("100", "1037")
    bulk_copy_decor("39", "1038")
    bulk_copy_decor("47", "1039")
    bulk_copy_decor("48", "1040")
    bulk_copy_decor("83", "1041")
    bulk_copy_decor("95", "1042")
    bulk_copy_decor("96", "1043")
    bulk_copy_decor("84", "1044")
    bulk_copy_decor("97", "1045")
    bulk_copy_decor("106", "1046")
    bulk_copy_decor("107", "1047")
    bulk_copy_decor("108", "1048")
    bulk_copy_decor("109", "1049")
    bulk_copy_decor("61", "1050")
    bulk_copy_decor("62", "1051")
    bulk_copy_decor("63", "1052")
    bulk_copy_decor("64", "1053")
    bulk_copy_decor("65", "1054")
    bulk_copy_decor("66", "1055")
    bulk_copy_decor("67", "1056")
    bulk_copy_decor("90", "1057")
    bulk_copy_decor("91", "1058")
    bulk_copy_decor("101", "1059")
    bulk_copy_decor("102", "1060")


def delete_python_den_decor(apps, schema_editor):
    LevelDecor = apps.get_model("game", "LevelDecor")
    LevelDecor.objects.filter(level_id__in=range(1014, 1061)).delete()


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
        name="String Manipulation",
    )

    episode21 = Episode.objects.create(
        pk=21,
        name="Lists",
    )

    Episode.objects.create(
        pk=22,
        name="Procedures",
    )

    episode12 = Episode.objects.get(pk=12)
    episode13 = Episode.objects.get(pk=13)
    episode14 = Episode.objects.get(pk=14)
    episode15 = Episode.objects.get(pk=15)
    episode16.next_episode = episode17
    episode17.next_episode = episode18
    episode18.next_episode = episode19
    episode19.next_episode = episode12
    episode12.next_episode = episode13
    episode13.next_episode = episode14
    episode14.next_episode = episode20
    episode20.next_episode = episode21
    episode21.next_episode = episode15

    episode12.save()
    episode13.save()
    episode14.save()
    episode16.save()
    episode17.save()
    episode18.save()
    episode19.save()
    episode20.save()
    episode21.save()


def delete_python_den_episodes(apps, schema_editor):
    Episode = apps.get_model("game", "Episode")
    Episode.objects.filter(pk__in=range(16, 23)).delete()

    episode14 = Episode.objects.get(pk=14)
    episode15 = Episode.objects.get(pk=15)
    episode14.next_episode = episode15

    episode14.save()


def set_first_and_last_levels(apps, schema_editor):
    Episode = apps.get_model("game", "Episode")
    Level = apps.get_model("game", "Level")

    episode13 = Episode.objects.get(pk=13)
    episode13.first_level = Level.objects.get(name="1014", default=True)
    episode13.save()

    episode14 = Episode.objects.get(pk=14)
    episode14.first_level = Level.objects.get(name="1026", default=True)
    episode14.save()

    episode15 = Episode.objects.get(pk=15)
    episode15.first_level = Level.objects.get(name="1041", default=True)
    episode15.save()

    episode22 = Episode.objects.get(pk=22)
    episode22.first_level = Level.objects.get(name="1050", default=True)
    episode22.save()


def reset_first_and_last_levels(apps, schema_editor):
    Episode = apps.get_model("game", "Episode")

    episode13 = Episode.objects.get(pk=13)
    episode13.first_level = None
    episode13.save()

    episode14 = Episode.objects.get(pk=14)
    episode14.first_level = None
    episode14.save()

    episode15 = Episode.objects.get(pk=15)
    episode15.first_level = None
    episode15.save()

    episode22 = Episode.objects.get(pk=22)
    episode22.first_level = None
    episode22.save()


def delete_old_loop_levels(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    Level.objects.filter(name__in=range(123, 154)).delete()


def recreate_old_loop_levels(apps, schema_editor):
    Episode = apps.get_model("game", "Episode")
    Level = apps.get_model("game", "Level")

    episode_15 = Episode.objects.get(pk=15)
    episode_14 = Episode.objects.get(pk=14)
    episode_13 = Episode.objects.get(pk=13)

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
    Level.objects.create(
        name="123",
        episode=episode_13,
        next_level=level_124,
    )


class Migration(migrations.Migration):
    dependencies = [("game", "0096_alter_level_commands")]

    operations = [
        migrations.RunPython(
            code=delete_old_loop_levels, reverse_code=recreate_old_loop_levels
        ),
        migrations.RunPython(
            code=create_python_den_episodes, reverse_code=delete_python_den_episodes
        ),
        migrations.RunPython(
            code=add_python_den_levels, reverse_code=delete_python_den_levels
        ),
        migrations.RunPython(
            code=add_python_den_blocks, reverse_code=delete_python_den_blocks
        ),
        migrations.RunPython(
            code=add_python_den_decor, reverse_code=delete_python_den_decor
        ),
        migrations.RunPython(
            code=set_first_and_last_levels, reverse_code=reset_first_and_last_levels
        ),
    ]
