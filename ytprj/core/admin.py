from django.contrib import admin
from .models import Video, Comment
from import_export.admin import ImportExportModelAdmin

class VideoAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Video, VideoAdmin)


class CommentAdmin(ImportExportModelAdmin):
    list_display = ['user','comment','video','active']


admin.site.register(Comment, CommentAdmin)
