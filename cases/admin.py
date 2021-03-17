from django.contrib import admin

from .models import Vanished, Story, Point


class PointInline(admin.StackedInline):
    model = Point
    extra = 2


class SubjectInline(admin.TabularInline):
    model = Story.vanished.through


class StoryInline(admin.StackedInline):
    model = Story
    extra = 2


class StoryAdmin(admin.ModelAdmin):
    inlines = [SubjectInline]


class VanishedAdmin(admin.ModelAdmin):
    inlines = [PointInline, SubjectInline]
    exclude = ('vanished',)


admin.site.register(Vanished, VanishedAdmin)
admin.site.register(Story)
admin.site.register(Point)
