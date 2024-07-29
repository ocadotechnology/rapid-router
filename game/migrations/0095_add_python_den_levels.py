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
        name="14",
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
        theme=farm,
        threads=1,
        traffic_lights="[]",
        cows='[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":2,"y":4},{"x":5,"y":4},{"x":7,"y":4}],"type":"WHITE"}]',
        lesson="This is a nice long straight road, but there are cows about!",
        hint="Make sure you sound the horn to get the cows off the road."
        # next_level
    )
