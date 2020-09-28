from django.contrib import admin
from  .models import Tutorials
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.
class TutorialsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/Date",{"fields":["title","published"]}),
        ("Content",{"fields":["content"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget':TinyMCE()}
    }



admin.site.register(Tutorials,TutorialsAdmin)