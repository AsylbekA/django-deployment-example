from django.contrib import admin
from .models import Bb, Rubric, Machine, Spare, AdvUser


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'kind', 'content', 'price', 'rubric', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


class AdvUser(admin.ModelAdmin):
    list_display = ('is_activated', 'user')


admin.site.register(Bb)
admin.site.register(BbAdmin)
admin.site.register(Machine)
admin.site.register(AdvUser)
admin.site.register(Rubric)
admin.site.register(Spare)

