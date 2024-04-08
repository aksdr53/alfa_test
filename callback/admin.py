from django.contrib import admin
from .models import Player, Game


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'updated_at')
    search_fields = ('name', 'email')


class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_players_names', 'created_at', 'updated_at')
    inlines = [PlayerInline]

    def get_players_names(self, obj):
        return ", ".join([player.name for player in obj.players.all()])
    get_players_names.short_description = 'Players'


class PlayerInline(admin.TabularInline):
    model = Game.players.through


admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)