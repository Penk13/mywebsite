from django.contrib import admin

from .models import (
    Portfolio,
    Skill,
    Project,
    Blog,
    Contact
)


admin.site.register(Portfolio)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(Contact)
