from django.contrib import admin

from game.models import Level, Block, Episode, Workspace, LevelDecor


class LevelAdmin(admin.ModelAdmin):
    search_fields = ["name", "id", "owner__user__username", "owner__user__first_name"]
    raw_id_fields = ["next_level", "locked_for_class"]
    readonly_fields = ["owner"]
    list_display = ["name", "id", "episode", "owner"]


class WorkspaceAdmin(admin.ModelAdmin):
    raw_id_fields = ["owner"]


class LevelDecorAdmin(admin.ModelAdmin):
    search_fields = ["level__name"]
    list_display = ["id", "level", "x", "y", "decorName"]


admin.site.register(Level, LevelAdmin)
admin.site.register(Workspace, WorkspaceAdmin)
admin.site.register(Episode)
admin.site.register(Block)
admin.site.register(LevelDecor, LevelDecorAdmin)
