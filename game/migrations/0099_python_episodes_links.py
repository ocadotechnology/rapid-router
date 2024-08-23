from django.apps.registry import Apps
from django.db import migrations


def add_resource_links_to_episodes(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")

    episode16 = Episode.objects.get(pk=16)
    episode16.worksheet_link = "https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-1-output-operators-and-data"
    episode16.video_link = "https://youtu.be/ve0RTsLGli0"
    episode16.lesson_plan_link = "https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-1-output-operators-and-data"
    episode16.slides_link = "https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FEPwYyCp6pw2WqdeV84OY%2FPython%201%20-%20Output%2C%20Operators%20and%20Data.pptx?alt=media&token=771964a8-acab-4503-aa3d-034f24a93d3d"

    episode17 = Episode.objects.get(pk=17)
    episode17.worksheet_link = "https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-2-variables-input-and-casting"
    episode17.video_link = "https://www.youtube.com/watch?v=H8askW-zd3I"
    episode17.lesson_plan_link = "https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-2-variables-input-and-casting"
    episode17.slides_link = "https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FLFOUoXuOPUmeOdZ09cHW%2FPython%202%20-%20Variables%2C%20Input%20and%20Casting.pptx?alt=media&token=ef6d1581-36bd-4885-9a99-4dac53eee4c3"

    episode18 = Episode.objects.get(pk=18)
    episode18.worksheet_link = "https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-3-selection"
    episode18.video_link = "https://www.youtube.com/watch?v=3XiQ97kP7H8"
    episode18.lesson_plan_link = "https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-3-selection"
    episode18.slides_link = "https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2F2mfkW4jWmJutkItlEnje%2FPython%203%20-%20Selection.pptx?alt=media&token=f6056de3-ef31-4031-aab8-be95da17d4cd"

    episode19 = Episode.objects.get(pk=19)
    episode19.worksheet_link = "https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-4-complex-selection"
    episode19.video_link = "https://youtu.be/QOe5G-ZvWoc"
    episode19.lesson_plan_link = "https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-4-complex-selection"
    episode19.slides_link = "https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2Fgx68HomHKoxDxcoC72n6%2FPython%204%20-%20Complex%20Selection.pptx?alt=media&token=7d7c2c77-57a8-42a9-980b-015ff9b5b818"

    episode12 = Episode.objects.get(pk=12)
    episode12.worksheet_link = "https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-5-iteration-part-1"
    episode12.video_link = "https://youtu.be/nJm3cWSkoi0"
    episode12.lesson_plan_link = "https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-5-iteration-part-1"
    episode12.slides_link = "https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FG1pLAqvXg6s6hGtnb5ss%2FPython%205%20-%20Iteration%201.pptx?alt=media&token=d9bf3e3f-bf12-4227-89b7-70515e16dcc9"

    episode14 = Episode.objects.get(pk=14)
    episode14.worksheet_link = "https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-7-selection-in-a-loop"
    episode14.video_link = "https://www.youtube.com/watch?v=WV_PLCcohMg"
    episode14.lesson_plan_link = "https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-7-selection-in-a-loop"
    episode14.slides_link = "https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FPtj4c6IjIafaUPN8k4u1%2FPython%207%20-%20Selection%20in%20a%20loop.pptx?alt=media&token=9f5fce8e-bb72-4e38-8715-89ec7bcc6d6c"

    episode13 = Episode.objects.get(pk=13)
    episode13.worksheet_link = "https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-8-indeterminate-loops"
    episode13.video_link = "https://www.youtube.com/watch?v=XgMGI8UzMDM"
    episode13.lesson_plan_link = "https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-8-indeterminate-loops"
    episode13.slides_link = "https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FkxewOibLrvKLpJpuDBRH%2FPython%208%20-%20Indeterminate%20Loops.pptx?alt=media&token=ddf212d5-f0a7-47b2-8a6b-420ca2cccc12"

    episode20 = Episode.objects.get(pk=20)
    episode20.worksheet_link = "https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-9-string-manipulation"
    episode20.video_link = "https://www.youtube.com/watch?v=E4AMg57_eoI"
    episode20.lesson_plan_link = "https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-9-string-manipulation"
    episode20.slides_link = "https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FOAj7ngrHzqNAJgcYLz55%2FPython%209%20-%20String%20manipulation.pptx?alt=media&token=a7bdb069-6321-4828-8218-d4eabf4605ad"

    episode21 = Episode.objects.get(pk=21)
    episode21.worksheet_link = "https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-10-1d-lists"
    episode21.video_link = "https://www.youtube.com/watch?v=Kb_-7IqWV0E"
    episode21.lesson_plan_link = "https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-10-1d-lists"
    episode21.slides_link = "https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FZdt2shodTgZjNH4ai7ky%2FPython%2010%20-1D%20Lists.pptx?alt=media&token=66bdc866-2144-4203-b55e-93fa04b977a3"

    episode15 = Episode.objects.get(pk=15)
    episode15.worksheet_link = "https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-11-for-loops"
    episode15.video_link = "https://www.youtube.com/watch?v=jNT_gQx9-k8"
    episode15.lesson_plan_link = "https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-11-using-for-loops"
    episode15.slides_link = "https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2F8AjR4b5mO4yOzEIVNI4V%2FPython%2011%20-%20For%20loops.pptx?alt=media&token=5eaa671c-a5eb-43a3-9f13-3478349027e5"

    episode16.save()
    episode17.save()
    episode18.save()
    episode19.save()
    episode12.save()
    episode14.save()
    episode13.save()
    episode20.save()
    episode21.save()
    episode15.save()


def remove_resource_links_from_episodes(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")

    for i in range(12, 21):
        episode = Episode.objects.get(pk=i)
        episode.worksheet_link = None
        episode.video_link = None
        episode.lesson_plan_link = None
        episode.slides_link = None
        episode.save()


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0098_add_episode_link_fields"),
    ]

    operations = [
        migrations.RunPython(
            code=add_resource_links_to_episodes,
            reverse_code=remove_resource_links_from_episodes,
        )
    ]
