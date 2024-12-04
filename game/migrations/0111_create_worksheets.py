from django.apps.registry import Apps
from django.db import migrations


def create_worksheets(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")
    Worksheet = apps.get_model("game", "Worksheet")
    Level = apps.get_model("game", "Level")
    
    Worksheet.objects.bulk_create(
        [
            Worksheet(
                episode=Episode.objects.get(pk=16),
                before_level=None,
                lesson_plan_link="https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-1-output-operators-and-data",
                slides_link="https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FEPwYyCp6pw2WqdeV84OY%2FPython%201%20-%20Output%2C%20Operators%20and%20Data.pptx?alt=media&token=771964a8-acab-4503-aa3d-034f24a93d3d",
                student_worksheet_link="https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-1-output-operators-and-data",
                indy_worksheet_link="https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-1-output-operators-and-data",
                video_link="https://youtu.be/ve0RTsLGli0",
            ),
            Worksheet(
                episode=Episode.objects.get(pk=17),
                before_level=None,
                lesson_plan_link="https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-2-variables-input-and-casting",
                slides_link="https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FLFOUoXuOPUmeOdZ09cHW%2FPython%202%20-%20Variables%2C%20Input%20and%20Casting.pptx?alt=media&token=ef6d1581-36bd-4885-9a99-4dac53eee4c3",
                student_worksheet_link="https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-2-variables-input-and-casting",
                indy_worksheet_link="https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-2-variables-input-and-casting",
                video_link="https://www.youtube.com/watch?v=H8askW-zd3I",
            ),
            Worksheet(
                episode=Episode.objects.get(pk=18),
                before_level=None,
                lesson_plan_link="https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-3-selection",
                slides_link="https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2F2mfkW4jWmJutkItlEnje%2FPython%203%20-%20Selection.pptx?alt=media&token=f6056de3-ef31-4031-aab8-be95da17d4cd",
                student_worksheet_link="https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-3-selection",
                indy_worksheet_link="https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-3-selection",
                video_link="https://www.youtube.com/watch?v=3XiQ97kP7H8",
            ),
            Worksheet(
                episode=Episode.objects.get(pk=19),
                before_level=None,
                lesson_plan_link="https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-4-complex-selection",
                slides_link="https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2Fgx68HomHKoxDxcoC72n6%2FPython%204%20-%20Complex%20Selection.pptx?alt=media&token=7d7c2c77-57a8-42a9-980b-015ff9b5b818",
                student_worksheet_link="https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-4-complex-selection",
                indy_worksheet_link="https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-4-complex-selection",
                video_link="https://youtu.be/QOe5G-ZvWoc",
            ),
            Worksheet(
                episode=Episode.objects.get(pk=12),
                before_level=Level.objects.get(default=True, name="1001"),
                lesson_plan_link="https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-5-iteration-part-1",
                slides_link="https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FG1pLAqvXg6s6hGtnb5ss%2FPython%205%20-%20Iteration%201.pptx?alt=media&token=d9bf3e3f-bf12-4227-89b7-70515e16dcc9",
                student_worksheet_link="https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-5-iteration-part-1",
                indy_worksheet_link="https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-5-iteration-part-1",
                video_link="https://youtu.be/nJm3cWSkoi0",
            ),
            Worksheet(
                episode=Episode.objects.get(pk=12),
                before_level=None,
                lesson_plan_link="https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-6-iteration-part-2",
                slides_link="https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FcEO90C76g4N17ss2K5PN%2FPython%206%20-%20Iteration%202.pptx?alt=media&token=df237a62-21ad-44a8-a4fe-bc9eed24092b",
                student_worksheet_link="https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-6-iteration-part-2",
                indy_worksheet_link="https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-6-iteration-part-2",
                video_link="https://youtu.be/kf-EavpnBNg",
            ),
            Worksheet(
                episode=Episode.objects.get(pk=13),
                before_level=Level.objects.get(default=True, name="1014"),
                lesson_plan_link="https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-7-selection-in-a-loop",
                slides_link="https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FPtj4c6IjIafaUPN8k4u1%2FPython%207%20-%20Selection%20in%20a%20loop.pptx?alt=media&token=9f5fce8e-bb72-4e38-8715-89ec7bcc6d6c",
                student_worksheet_link="https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-7-selection-in-a-loop",
                indy_worksheet_link="https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-7-selection-in-a-loop",
                video_link="https://www.youtube.com/watch?v=WV_PLCcohMg",
            ),
            Worksheet(
                episode=Episode.objects.get(pk=14),
                before_level=Level.objects.get(default=True, name="1026"),
                lesson_plan_link="https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-8-indeterminate-loops",
                slides_link="https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FkxewOibLrvKLpJpuDBRH%2FPython%208%20-%20Indeterminate%20Loops.pptx?alt=media&token=ddf212d5-f0a7-47b2-8a6b-420ca2cccc12",
                student_worksheet_link="https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-8-indeterminate-loops",
                indy_worksheet_link="https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-8-indeterminate-loops",
                video_link="https://www.youtube.com/watch?v=XgMGI8UzMDM",
            ),
            Worksheet(
                episode=Episode.objects.get(pk=20),
                before_level=None,
                lesson_plan_link="https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-9-string-manipulation",
                slides_link="https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FOAj7ngrHzqNAJgcYLz55%2FPython%209%20-%20String%20manipulation.pptx?alt=media&token=a7bdb069-6321-4828-8218-d4eabf4605ad",
                student_worksheet_link="https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-9-string-manipulation",
                indy_worksheet_link="https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-9-string-manipulation",
                video_link="https://www.youtube.com/watch?v=E4AMg57_eoI",
            ),
            Worksheet(
                episode=Episode.objects.get(pk=21),
                before_level=None,
                lesson_plan_link="https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-10-1d-lists",
                slides_link="https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FZdt2shodTgZjNH4ai7ky%2FPython%2010%20-1D%20Lists.pptx?alt=media&token=66bdc866-2144-4203-b55e-93fa04b977a3",
                student_worksheet_link="https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-10-1d-lists",
                indy_worksheet_link="https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-10-1d-lists",
                video_link="https://www.youtube.com/watch?v=Kb_-7IqWV0E",
            ),
            Worksheet(
                episode=Episode.objects.get(pk=15),
                before_level=Level.objects.get(default=True, name="1041"),
                lesson_plan_link="https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/DGiFT28ihVJK7ghZQHqu/python-11-using-for-loops",
                slides_link="https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2F8AjR4b5mO4yOzEIVNI4V%2FPython%2011%20-%20For%20loops.pptx?alt=media&token=5eaa671c-a5eb-43a3-9f13-3478349027e5",
                student_worksheet_link="https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-11-for-loops",
                indy_worksheet_link="https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-11-using-for-loops",
                video_link="https://www.youtube.com/watch?v=jNT_gQx9-k8",
            ),
            Worksheet(
                episode=Episode.objects.get(pk=23),
                before_level=None,
                lesson_plan_link="https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/EMEzsyyl4uRclyA9LDGN/python-12-2d-lists",
                slides_link="https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2F3Q4X7ZDk1TNej5c2e7LW%2FPython%2012%202D%20Lists.pptx?alt=media&token=847d9d69-4610-4c67-a649-0c6e0f88d372",
                student_worksheet_link="https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-12-2d-lists",
                indy_worksheet_link="https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-12-2d-lists",
                video_link="https://www.youtube.com/watch?v=MBU49ivZk6w",
            ),
            Worksheet(
                episode=Episode.objects.get(pk=24),
                before_level=None,
                lesson_plan_link="https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/EMEzsyyl4uRclyA9LDGN/python-13-procedures-and-functions",
                slides_link="https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2Fmr6FvFzY3LVuaGT1zd6d%2FPython%2013%20Procedures%20and%20Functions.pptx?alt=media&token=c5835e00-8d42-4567-8cf4-868b0f23dc0a",
                student_worksheet_link="https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-13-procedures-and-functions",
                indy_worksheet_link="https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-13-procedures-and-functions",
                video_link="https://www.youtube.com/watch?v=LJMfI7P3Dzk",
            ),
        ]
    )


def delete_worksheets(apps: Apps, *args):
    Worksheet = apps.get_model("game", "Worksheet")
    Worksheet.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0110_remove_episode_indy_worksheet_link_and_more"),
    ]

    operations = [
        migrations.RunPython(
            code=create_worksheets,
            reverse_code=delete_worksheets,
        )
    ]
