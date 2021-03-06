from django.contrib import admin
from .models import *


# Common drop logs
@admin.register(RuneDrop)
class RuneDropAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slot', 'stars', 'main_stat']


@admin.register(MonsterDrop)
class MonsterDropAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'grade']


# Run logs
@admin.register(RunLog)
class RunLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'wizard_id', 'summoner', 'dungeon', 'stage', 'drop_type', 'drop_quantity', 'drop_monster', 'drop_rune')
    list_filter = ('dungeon', 'stage', 'drop_type')
    readonly_fields = ['summoner', 'drop_monster', 'drop_rune']


@admin.register(SummonLog)
class SummonLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'wizard_id', 'summoner', 'summon_method', 'monster')
    search_fields = ['wizard_id', 'summon_method', 'monster']
    readonly_fields = ['summoner', 'monster']


# Rift dungeon logs
class RiftDungeonItemDropInline(admin.TabularInline):
    model = RiftDungeonItemDrop
    extra = 0


class RiftDungeonMonsterDropInline(admin.TabularInline):
    model = RiftDungeonMonsterDrop
    extra = 0


class RiftDungeonRuneDropInline(admin.StackedInline):
    model = RiftDungeonRuneDrop
    extra = 0


class RiftDungeonRuneCraftDropInline(admin.TabularInline):
    model = RiftDungeonRuneCraftDrop
    extra = 0


@admin.register(RiftDungeonLog)
class RiftDungeonAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'wizard_id', 'summoner', 'dungeon', 'grade', 'total_damage']
    readonly_fields = ['summoner']
    inlines = [
        RiftDungeonItemDropInline,
        RiftDungeonMonsterDropInline,
        RiftDungeonRuneDropInline,
        RiftDungeonRuneCraftDropInline,
    ]


# Rune crafting
class RuneCraftInline(admin.StackedInline):
    model = RuneCraft
    extra = 0


@admin.register(RuneCraftLog)
class RuneCraftLogAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'wizard_id', 'summoner', 'craft_level']
    readonly_fields = ['summoner']
    inlines = [
        RuneCraftInline
    ]


class MagicBoxRuneDropInline(admin.StackedInline):
    model = MagicBoxRuneDrop
    extra = 0


class MagicBoxItemDropInline(admin.TabularInline):
    model = MagicBoxItemDrop
    extra = 0


class MagicBoxRuneCraftDropInline(admin.TabularInline):
    model = MagicBoxRuneCraftDrop
    extra = 0


@admin.register(MagicBoxCraft)
class MagicBoxCraftAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'wizard_id', 'summoner', 'box_type']
    readonly_fields = ['summoner']
    inlines = [
        MagicBoxRuneDropInline,
        MagicBoxItemDropInline,
        MagicBoxRuneCraftDropInline,
    ]


# Magic shop
class ShopRefreshRuneInline(admin.TabularInline):
    model = ShopRefreshRune
    fields = ['cost', 'type', 'stars', 'slot', 'value', 'quality']
    extra = 0


class ShopRefreshItemInline(admin.TabularInline):
    model = ShopRefreshItem
    extra = 0


class ShopRefreshMonsterInline(admin.TabularInline):
    model = ShopRefreshMonster
    extra = 0


@admin.register(ShopRefreshLog)
class ShopRefreshLogAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'wizard_id', 'summoner',]
    readonly_fields = ['summoner']
    inlines = [
        ShopRefreshRuneInline,
        ShopRefreshItemInline,
        ShopRefreshMonsterInline
    ]


# World boss
class WorldBossItemDropInline(admin.TabularInline):
    model = WorldBossItemDrop
    extra = 0


class WorldBossRuneDropInline(admin.StackedInline):
    model = WorldBossRuneDrop
    extra = 0


class WorldBossMonsterDropInline(admin.TabularInline):
    model = WorldBossMonsterDrop
    extra = 0


@admin.register(WorldBossLog)
class WorldBossLogAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'wizard_id', 'summoner', 'grade']
    readonly_fields = ['summoner']
    inlines = [
        WorldBossItemDropInline,
        WorldBossRuneDropInline,
        WorldBossMonsterDropInline,
    ]


# Rift Raid
class RiftRaidItemDropInline(admin.TabularInline):
    model = RiftRaidItemDrop
    extra = 0


class RiftRaidMonsterDropInline(admin.TabularInline):
    model = RiftRaidMonsterDrop
    extra = 0


class RiftRaidRuneCraftDropInline(admin.StackedInline):
    model = RiftRaidRuneCraftDrop
    extra = 0


@admin.register(RiftRaidLog)
class RiftRaidLogAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'wizard_id', 'summoner', 'difficulty']
    readonly_fields = ['summoner']
    inlines = [
        RiftRaidItemDropInline,
        RiftRaidMonsterDropInline,
        RiftRaidRuneCraftDropInline,
    ]


# Wishes
class WishItemDropInline(admin.TabularInline):
    model = WishItemDrop
    extra = 0


class WishMonsterDropInline(admin.TabularInline):
    model = WishMonsterDrop
    extra = 0


class WishRuneDropInline(admin.StackedInline):
    model = WishRuneDrop
    extra = 0


@admin.register(WishLog)
class WishLogAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'wizard_id', 'summoner']
    readonly_fields = ['summoner']
    inlines = [
        WishItemDropInline,
        WishMonsterDropInline,
        WishRuneDropInline,
    ]


# Export manager
@admin.register(ExportManager)
class ExportManagerAdmin(admin.ModelAdmin):
    list_display = ['export_category', 'last_row']
