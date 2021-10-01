from django.contrib import admin
from game.models import Level, Block, Episode, Workspace


class LevelAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    raw_id_fields = ["next_level"]
    readonly_fields = ["owner"]


class WorkspaceAdmin(admin.ModelAdmin):
    raw_id_fields = ["owner"]


admin.site.register(Level, LevelAdmin)
admin.site.register(Workspace, WorkspaceAdmin)
admin.site.register(Episode)
admin.site.register(Block)
