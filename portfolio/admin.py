from django.contrib import admin

from .models import (
    About,
    Skill,
    Project,
    # Blog,
    Contact
)


admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Project)
# admin.site.register(Blog)
admin.site.register(Contact)
