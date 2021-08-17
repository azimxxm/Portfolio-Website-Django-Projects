from django.contrib import admin
from .models import Skills
from django.utils.safestring import mark_safe

@admin.register(Skills)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["id", 'name', 'html', 'css', 'javascript', 'python', 'postgresql', 'photoshoop', 'photographer', 'mysql', 'mongoDB', 'reactjs', 'nextjs', 'vuejs', 'i18next_community', 'images']
    search_fields = ['name', 'html', 'css', 'javascript', 'python', 'postgresql', 'photoshoop', 'photographer', 'mysql', 'mongoDB', 'reactjs', 'nextjs', 'vuejs', 'i18next_community']
    list_filter = ['name']
    list_editable = ['name', 'html', 'css', 'javascript', 'python', 'postgresql', 'photoshoop', 'photographer', 'mysql', 'mongoDB', 'reactjs', 'nextjs', 'vuejs', 'i18next_community', 'images']
    