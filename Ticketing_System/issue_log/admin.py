from django.contrib import admin
from .models import Client, Severity, Issue
# Register your models here.


admin.site.register(Client)
admin.site.register(Severity)


class IssueAdmin(admin.ModelAdmin):
    list_display = ["issue_description", "client_name", "severity_index",
                    "issued_by", "is_priority", "is_open",
                    "issued_on",]

admin.site.register(Issue, IssueAdmin)