from django.contrib import admin
from .models import Project, Skill, Experience


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "github_url")
    list_filter = ("date",)
    search_fields = ("title", "technologies")
    readonly_fields = ()


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "category")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("position", "company", "start_date", "end_date")
    list_filter = ("company",)
    search_fields = ("position", "company")

