from django.contrib import admin

from game.models import Level, Block, Episode, Workspace, LevelDecor, Attempt, Worksheet


class LevelAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
        "id",
        "owner__user__username",
        "owner__user__first_name",
    ]
    raw_id_fields = ["next_level", "locked_for_class"]
    readonly_fields = ["owner"]
    list_display = ["name", "id", "episode", "owner"]


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class WorkspaceAdmin(admin.ModelAdmin):
    raw_id_fields = ["owner"]


class AttemptAdmin(admin.ModelAdmin):
    search_fields = [
        "level",
        "student",
        "start_time",
        "finish_time",
        "is_best_attempt",
    ]
    raw_id_fields = ["student"]
    list_display = [
        "level",
        "student",
        "start_time",
        "finish_time",
        "is_best_attempt",
    ]


class LevelDecorAdmin(admin.ModelAdmin):
    search_fields = ["level__name"]
    list_display = ["id", "level", "x", "y", "decor_name"]


class WorksheetAdmin(admin.ModelAdmin):
    list_display = ["id", "episode"]


admin.site.register(Level, LevelAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Workspace, WorkspaceAdmin)
admin.site.register(Block)
admin.site.register(Attempt, AttemptAdmin)
admin.site.register(LevelDecor, LevelDecorAdmin)
admin.site.register(Worksheet, WorksheetAdmin)
