def add_python_den_levels(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    Theme = apps.get_model("game", "Theme")
    Character = apps.get_model("game", "Character")

    grass = Theme.objects.get(name="grass")
    snow = Theme.objects.get(name="snow")
    farm = Theme.objects.get(name="farm")
    city = Theme.objects.get(name="city")

    van = Character.objects.get(name="Van")
    dee = Character.objects.get(name="Dee")

    level14 = Level(
        name="python_14",
        anonymous=False,
        blocklyEnabled=True,
        character=van,
        default=True,
        destinations="[[9,4]]",
        disable_algorithm_score=True,
        direct_drive=False,
        fuel_gauge=True,
        max_fuel=50,
        model_solution="[]",
        origin='{"coordinate":[0,4],"direction":"E"}',
        path='[{"coordinate":[0,4],"connectedNodes":[1]},{"coordinate":[1,4],"connectedNodes":[0,2]},{"coordinate":[2,4],"connectedNodes":[1,3]},{"coordinate":[3,4],"connectedNodes":[2,4]},{"coordinate":[4,4],"connectedNodes":[3,5]},{"coordinate":[5,4],"connectedNodes":[4,6]},{"coordinate":[6,4],"connectedNodes":[5,7]},{"coordinate":[7,4],"connectedNodes":[6,8]},{"coordinate":[8,4],"connectedNodes":[7,9]},{"coordinate":[9,4],"connectedNodes":[8]}]',
        pythonEnabled=False,
        pythonVieWEnabled=True,
        ideEnabled=False,
        theme=farm,
        threads=1,
        traffic_lights="[]",
        cows='[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":2,"y":4},{"x":5,"y":4},{"x":7,"y":4}],"type":"WHITE"}]',
        lesson="This is a nice long straight road, but there are cows about!",
        hint="Make sure you sound the horn to get the cows off the road."
    )

    level15 = Level(
        name="python_15",
        path='[{"coordinate":[5,0],"connectedNodes":[1]},{"coordinate":[5,1],"connectedNodes":[2,0]},{"coordinate":[4,1],"connectedNodes":[3,1]},{"coordinate":[4,2],"connectedNodes":[4,2]},{"coordinate":[4,3],"connectedNodes":[5,3]},{"coordinate":[4,4],"connectedNodes":[6,4]},{"coordinate":[3,4],"connectedNodes":[7,5]},{"coordinate":[3,5],"connectedNodes":[8,6]},{"coordinate":[3,6],"connectedNodes":[9,7]},{"coordinate":[3,7],"connectedNodes":[8]}]',
        traffic_lights="[]",
        cows="[]",
        origin='{"coordinate":[5,0],"direction":"N"}',
        destinations="[[3,7]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=True,
        pythonEnabled=False,
        pythonViewEnabled=True,
        ideEnabled=False,
        theme=farm,
        character=van,
        lesson="There are some bends in this road. Be careful!",
        hint="What do you need to count, how many times you move or how many times you move forwards?",
        anonymous=False
    )

    level16 = Level(
        name="python_16",
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
        ideEnabled=False,
        theme=farm,
        character=van,
        lesson="Oh no! The farmer seems to have let their cows out again. Be careful.",
        hint="Look for a pattern here...",
        anonymous=False
    )

    level17 = Level(
        name="python_17",
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
        pythonVieWEnabled=False,
        ideEnabled=False,
        theme=grass,
        character=van,
        lesson="Keep going, you're getting the hang of the Python code.",
        hint="So you are going forward unless...?",
        anonymous=False
    )

    level18 = Level(
        name="python_18",
        path='[{"coordinate":[7,1],"connectedNodes":[1]},{"coordinate":[7,2],"connectedNodes":[2,0]},{"coordinate":[7,3],"connectedNodes":[3,1]},{"coordinate":[7,4],"connectedNodes":[4,2]},{"coordinate":[7,5],"connectedNodes":[5,3]},{"coordinate":[6,5],"connectedNodes":[6,4]},{"coordinate":[5,5],"connectedNodes":[7,5]},{"coordinate":[4,5],"connectedNodes":[8,6]},{"coordinate":[3,5],"connectedNodes":[9,7]},{"coordinate":[2,5],"connectedNodes":[8,10]},{"coordinate":[2,4],"connectedNodes":[9,11]},{"coordinate":[2,3],"connectedNodes":[10,12]},{"coordinate":[2,2],"connectedNodes":[11,13]},{"coordinate":[2,1],"connectedNodes":[12,14]},{"coordinate":[3,1],"connectedNodes":[13,15]},{"coordinate":[4,1],"connectedNodes":[14,16]},{"coordinate":[5,1],"connectedNodes":[15,17]},{"coordinate":[6,1],"connectedNodes":[16,18]},{"coordinate":[6,2],"connectedNodes":[19,17]},{"coordinate":[6,3],"connectedNodes":[20,18]},{"coordinate":[6,4],"connectedNodes":[21,19]},{"coordinate":[5,4],"connectedNodes":[22,20]},{"coordinate":[4,4],"connectedNodes":[23,21]},{"coordinate":[3,4],"connectedNodes":[22,24]},{"coordinate":[3,3],"connectedNodes":[23,25]},{"coordinate":[3,2],"connectedNodes":[24,26]},{"coordinate":[4,2],"connectedNodes":[25,27]},{"coordinate":[5,2],"connectedNodes":[26]}]',
        traffic_lights="[]",
        cows="[]",
        origin='{"coordinate":[7,1],"direction":"N"}',
        destinations="[[5,2]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=True,
        pythonEnabled=False,
        pythonVieWEnabled=True,
        ideEnabled=False,
        theme=snow,
        character=van,
        lesson="Oh dear, you might get a bit dizzy!",
        hint="What are you counting here, straight roads or bends?",
        anonymous=False
    )

    level19 = Level(
        name="python_19",
        path='[{"coordinate":[9,3],"connectedNodes":[1]},{"coordinate":[8,3],"connectedNodes":[2,0]},{"coordinate":[7,3],"connectedNodes":[3,1,15]},{"coordinate":[7,4],"connectedNodes":[4,2]},{"coordinate":[6,4],"connectedNodes":[5,3]},{"coordinate":[5,4],"connectedNodes":[6,4,12]},{"coordinate":[4,4],"connectedNodes":[7,5]},{"coordinate":[3,4],"connectedNodes":[8,6]},{"coordinate":[3,5],"connectedNodes":[9,7]},{"coordinate":[2,5],"connectedNodes":[10,8,17]},{"coordinate":[1,5],"connectedNodes":[11,9]},{"coordinate":[0,5],"connectedNodes":[10]},{"coordinate":[5,3],"connectedNodes":[5,13]},{"coordinate":[5,2],"connectedNodes":[21,12,14]},{"coordinate":[6,2],"connectedNodes":[13,15]},{"coordinate":[7,2],"connectedNodes":[14,2,16]},{"coordinate":[7,1],"connectedNodes":[15]},{"coordinate":[2,4],"connectedNodes":[9,18]},{"coordinate":[2,3],"connectedNodes":[17,19]},{"coordinate":[2,2],"connectedNodes":[18,20]},{"coordinate":[3,2],"connectedNodes":[19,21]},{"coordinate":[4,2],"connectedNodes":[20,13]}]',
        traffic_lights="[]",
        cows="[]",
        origin='{"coordinate":[9,3],"direction":"W"}',
        destinations="[[0,5]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=True,
        pythonEnabled=False,
        pythonVieWEnabled=True,
        ideEnabled=False,
        theme=grass,
        character=van,
        lesson="Have you noticed that there are more roads ahead than turns? Try checking if there is a road ahead and then otherwise making the turns you need...",
        hint="Remember to use if..else"
        anonymous=False
    )

    level20 = Level(
        name="python_20",
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
        pythonVieWEnabled=False,
        ideEnabled=False,
        theme=snow,
        character=van,
        lesson="Use if..else in Python for this level",
        hint="Don't get distracted by the other roads. Look for a pattern you can repeat.",
        anonymous=False
    )

    level21 = Level(
        name="python_21",
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
        pythonVieWEnabled=False,
        ideEnabled=False,
        theme=grass,
        character=van,
        lesson="This is a really busy road. Make sure that you don't miss any of the houses.",
        hint="Did you get the last house? Think about what value the loop counter will have at that point in your code...",
        anonymous=False
    )

    level22 = Level(
        name="python_22",
        path='[{"coordinate":[2,3],"connectedNodes":[1]},{"coordinate":[2,2],"connectedNodes":[0,2,16]},{"coordinate":[3,2],"connectedNodes":[1,3]},{"coordinate":[3,1],"connectedNodes":[2,4,14]},{"coordinate":[4,1],"connectedNodes":[3,5]},{"coordinate":[5,1],"connectedNodes":[4,6,22]},{"coordinate":[5,2],"connectedNodes":[7,5]},{"coordinate":[6,2],"connectedNodes":[6,8]},{"coordinate":[6,3],"connectedNodes":[9,17,7]},{"coordinate":[6,4],"connectedNodes":[10,8]},{"coordinate":[5,4],"connectedNodes":[11,9]},{"coordinate":[5,5],"connectedNodes":[12,10]},{"coordinate":[4,5],"connectedNodes":[13,11]},{"coordinate":[3,5],"connectedNodes":[12]},{"coordinate":[3,0],"connectedNodes":[15,3]},{"coordinate":[2,0],"connectedNodes":[16,14]},{"coordinate":[2,1],"connectedNodes":[1,15]},{"coordinate":[7,3],"connectedNodes":[8,18]},{"coordinate":[8,3],"connectedNodes":[17,19]},{"coordinate":[8,2],"connectedNodes":[18,20]},{"coordinate":[8,1],"connectedNodes":[21,19]},{"coordinate":[7,1],"connectedNodes":[22,20]},{"coordinate":[6,1],"connectedNodes":[5,21]}]',
        traffic_lights="[]",
        cows="[]",
        origin='{"coordinate":[2,3],"direction":"S"}',
        destinations="[[3,5]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=True,
        pythonEnabled=False,
        pythonVieWEnabled=True,
        ideEnabled=False,
        theme=grass,
        character=van,
        lesson="There are lots of turns here, don't get distracted.",
        hint="Think about the order of the questions you ask using your if and elif statements.",
        anonymous=False
    )

    level23 = Level(
        name="python_23",
        path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[2,5],"connectedNodes":[1,28,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,3],"connectedNodes":[3,5]},{"coordinate":[2,2],"connectedNodes":[4,6]},{"coordinate":[2,1],"connectedNodes":[5,7]},{"coordinate":[3,1],"connectedNodes":[6,8]},{"coordinate":[4,1],"connectedNodes":[7,9]},{"coordinate":[5,1],"connectedNodes":[8,10]},{"coordinate":[6,1],"connectedNodes":[9,11]},{"coordinate":[7,1],"connectedNodes":[10,12]},{"coordinate":[8,1],"connectedNodes":[11,13]},{"coordinate":[9,1],"connectedNodes":[12,14]},{"coordinate":[9,2],"connectedNodes":[15,13]},{"coordinate":[9,3],"connectedNodes":[16,14]},{"coordinate":[9,4],"connectedNodes":[17,15]},{"coordinate":[9,5],"connectedNodes":[18,16]},{"coordinate":[9,6],"connectedNodes":[19,17]},{"coordinate":[8,6],"connectedNodes":[20,18]},{"coordinate":[7,6],"connectedNodes":[21,19]},{"coordinate":[6,6],"connectedNodes":[22,20]},{"coordinate":[5,6],"connectedNodes":[23,21]},{"coordinate":[4,6],"connectedNodes":[22,24]},{"coordinate":[4,5],"connectedNodes":[28,23,25]},{"coordinate":[4,4],"connectedNodes":[24,26]},{"coordinate":[4,3],"connectedNodes":[25,27]},{"coordinate":[4,2],"connectedNodes":[26]},{"coordinate":[3,5],"connectedNodes":[2,24]}]',
        traffic_lights="[]",
        cows="[]",
        origin='{"coordinate":[2,7],"direction":"S"}',
        destinations="[[4,2]]",
        default=True,
        fuel_gauge=True,
        max_fuel=50,
        direct_drive=False,
        model_solution="[]",
        disable_algorithm_score=True,
        threads=1,
        blocklyEnabled=True,
        pythonEnabled=False,
        pythonVieWEnabled=True,
        ideEnabled=False,
        theme=farm,
        character=van,
        lesson="Don't go the long way around!",
        hint="Think carefully about the order in which you ask questions in your if..else if block",
        anonymous=False
    )

    level24 = Level(
        name="python_24",
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
        pythonVieWEnabled=False,
        ideEnabled=False,
        theme=farm,
        character=van,
        lesson="Look carefully for the shortest route.",
        hint="Think carefully about the order in which you ask questions in your if..elif statements.",
        anonymous=False
    )

    level25 = Level(
        name="python_25",
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
        pythonVieWEnabled=False,
        ideEnabled=False,
        theme=grass,
        character=van,
        lesson="Look carefully for the shortest route.",
        hint="Think carefully about the order in which you ask questions in your if..elif statements. Don't forget the traffic lights.",
        anonymous=False
    )

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

def add_python_den_blocks(apps, schema_editor):
    def set_blocks(level, blocks):
        set_blocks_inner(level, blocks, LevelBlock, Block)

def add_python_den_decor(apps, schema_editor):
    def set_decor(level, decor):
        set_decor_inner(level, decor, LevelDecor)

    Level = apps.get_model("game", "Level")
    level14 = Level.objects.get(name="python_14")
    level15 = Level.objects.get(name="python_15")
    level16 = Level.objects.get(name="python_16")
    level17 = Level.objects.get(name="python_17")
    level18 = Level.objects.get(name="python_18")
    level20 = Level.objects.get(name="python_20")
    level21 = Level.objects.get(name="python_21")
    level22 = Level.objects.get(name="python_22")
    level23 = Level.objects.get(name="python_23")

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
            + ']'
        )
    )