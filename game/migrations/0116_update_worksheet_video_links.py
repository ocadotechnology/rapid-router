from django.apps.registry import Apps
from django.db import migrations


def update_video_links_to_gitbook(apps: Apps, *args):
    Worksheet = apps.get_model("game", "Worksheet")

    gitbook_links = {
        1: "https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FDK3lKfWsWXseNCfGjvbW%2FPython%20-%201.mp4?alt=media",
        2: "https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FSm6U98LfPiX29BHxiV6K%2FPython%20Den%202_%20Variables%2C%20Input%20and%20Casting.mp4?alt=media",
        3: "https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FBOgSQVurnqF8wAvujZfU%2FPython%20Den%20Session%203_%20Selection.mp4?alt=media",
        4: "https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FbCvmsaMKoSB1YnWpY6Q0%2FPython%20-%204.mp4?alt=media",
        5: "https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FJ316sUFw7gDae6DqN6ic%2FPython%20Den%20Session%205%20-%20Iteration%2C%20Part%201.mp4?alt=media",
        6: "https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FAejhabL6uQNcH267vHVP%2FPython%20Den%20Session%206_%20Iteration%2C%20part%202.mp4?alt=media",
        7: "https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FtOt5a50oebdFciVmzACB%2FPython%20Den%20Session%207_%20Selection%20in%20a%20Loop.mp4?alt=media",
        8: "https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2F8p5qyWb2trqu4ar5LKP8%2FPython%20Den%20Session%208_%20Indeterminate%20Loops.mp4?alt=media",
        9: "https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FRhMHYNbPaR4cdmFxQHSJ%2FPython%20Den%20Session%209_%20String%20Manipulation.mp4?alt=media",
        10: "https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2F31nxEQMiyUex576uO1QV%2FPython%20Den%20Session%2010_%201D%20Lists.mp4?alt=media",
        11: "https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2FcwLKAhjeFxoZwxrc4KiY%2FPython%20Den%20Session%2011_%20Using%20for%20loops.mp4?alt=media",
        12: "https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2F6FoQVGJyqMmiZxxg3pQQ%2FPython%20Den%20Session%2012_%202D%20Lists.mp4?alt=media",
        13: "https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwAuC4Q5WQz4ea2O2b2JP%2Fuploads%2Fs0V186tQxn3G3fmRAP9D%2FPython%20Den%20Session%2013_%20Procedures%20and%20Functions.mp4?alt=media",
    }
    
    worksheets = Worksheet.objects.all()

    for worksheet in worksheets:
        worksheet.video_link = gitbook_links[worksheet.id]
        worksheet.save()


def update_video_links_to_youtube(apps: Apps, *args):
    Worksheet = apps.get_model("game", "Worksheet")

    youtube_links = {
        1: "https://www.youtube.com/watch?v=PiSxeThHztY",
        2: "https://www.youtube.com/watch?v=NkShv_bSB3I",
        3: "https://www.youtube.com/watch?v=jQ7RceRVapo",
        4: "https://www.youtube.com/watch?v=yMu_0-ryf_s",
        5: "https://www.youtube.com/watch?v=ihFg81V9aNE",
        6: "https://www.youtube.com/watch?v=Xhibd1JxPrU",
        7: "https://www.youtube.com/watch?v=WV_PLCcohMg",
        8: "https://www.youtube.com/watch?v=RkWu2wV8Bt0",
        9: "https://www.youtube.com/watch?v=E4AMg57_eoI",
        10: "https://www.youtube.com/watch?v=Kb_-7IqWV0E",
        11: "https://www.youtube.com/watch?v=jNT_gQx9-k8",
        12: "https://www.youtube.com/watch?v=MBU49ivZk6w",
        13: "https://www.youtube.com/watch?v=LJMfI7P3Dzk",
    }

    worksheets = Worksheet.objects.all()

    for worksheet in worksheets:
        worksheet.video_link = youtube_links[worksheet.id]
        worksheet.save()


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0115_level_level__default_does_not_need_approval"),
    ]

    operations = [
        migrations.RunPython(
            code=update_video_links_to_gitbook,
            reverse_code=update_video_links_to_youtube,
        )
    ]
