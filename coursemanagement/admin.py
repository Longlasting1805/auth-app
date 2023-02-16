from django.contrib import admin
from coursemanagement.models import Course, Collection

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at', 'is_deleted')

admin.site.register(Course, CourseAdmin)
admin.site.register(Collection)

