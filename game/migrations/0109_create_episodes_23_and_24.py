from django.apps.registry import Apps
from django.db import migrations


def create_episodes_23_and_24(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")

    episode_23 = Episode.objects.create(
        pk=23,
        name="2D Lists",
        student_worksheet_link="https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-12-2d-lists",
        indy_worksheet_link="https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-12-2d-lists",
        video_link="https://www.youtube.com/watch?v=MBU49ivZk6w",
        lesson_plan_link="https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/EMEzsyyl4uRclyA9LDGN/python-12-2d-lists",
        slides_link="https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2F3Q4X7ZDk1TNej5c2e7LW%2FPython%2012%202D%20Lists.pptx?alt=media&token=847d9d69-4610-4c67-a649-0c6e0f88d372",
    )

    episode_24 = Episode.objects.create(
        pk=24,
        name="Procedures and Functions",
        student_worksheet_link="https://code-for-life.gitbook.io/student-resources/python-den-student-resources/worksheet-13-procedures-and-functions",
        indy_worksheet_link="https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-13-procedures-and-functions",
        video_link="https://www.youtube.com/watch?v=LJMfI7P3Dzk",
        lesson_plan_link="https://code-for-life.gitbook.io/python-lessons-with-raspberry-pi-ide/EMEzsyyl4uRclyA9LDGN/python-13-procedures-and-functions",
        slides_link="https://4077022412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2Fmr6FvFzY3LVuaGT1zd6d%2FPython%2013%20Procedures%20and%20Functions.pptx?alt=media&token=c5835e00-8d42-4567-8cf4-868b0f23dc0a",
    )
    
    episode_23.next_episode = episode_24
    episode_23.save()
    
    episode_16 = Episode.objects.get(pk=16)
    episode_16.indy_worksheet_link = "https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-1-output-operators-and-data"
    episode_16.save()

    episode_17 = Episode.objects.get(pk=17)
    episode_17.indy_worksheet_link = "https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-2-variables-input-and-casting"
    episode_17.save()

    episode_18 = Episode.objects.get(pk=18)
    episode_18.indy_worksheet_link = "https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-3-selection"
    episode_18.save()

    episode_19 = Episode.objects.get(pk=19)
    episode_19.indy_worksheet_link = "https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-4-complex-selection"
    episode_19.save()

    episode_12 = Episode.objects.get(pk=12)
    episode_12.indy_worksheet_link = "https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-5-iteration-part-1"
    episode_12.save()

    episode_13 = Episode.objects.get(pk=13)
    episode_13.indy_worksheet_link = "https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-7-selection-in-a-loop"
    episode_13.save()

    episode_14 = Episode.objects.get(pk=14)
    episode_14.indy_worksheet_link = "https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-8-indeterminate-loops"
    episode_14.save()

    episode_20 = Episode.objects.get(pk=20)
    episode_20.indy_worksheet_link = "https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-9-string-manipulation"
    episode_20.save()

    episode_21 = Episode.objects.get(pk=21)
    episode_21.indy_worksheet_link = "https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-10-1d-lists"
    episode_21.save()
    
    episode_15 = Episode.objects.get(pk=15)
    episode_15.next_episode = episode_23
    episode_15.indy_worksheet_link = "https://code-for-life.gitbook.io/independent-student-resources/python-den-resources-beta/session-11-using-for-loops"
    episode_15.save()


def delete_episodes_23_and_24(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")

    episode_15 = Episode.objects.get(pk=15)
    episode_15.next_episode = None
    episode_15.indy_worksheet_link = None
    episode_15.save()
    
    Episode.objects.filter(pk__in=[
        16, 17, 18, 19, 12, 13, 14, 20, 21
    ]).update(indy_worksheet_link=None)

    Episode.objects.filter(pk__in=[23, 24]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0108_episode_indy_worksheet_link"),
    ]

    operations = [
        migrations.RunPython(
            code=create_episodes_23_and_24,
            reverse_code=delete_episodes_23_and_24,
        )
    ]
