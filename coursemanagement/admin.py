from django.contrib import admin
from coursemanagement.models import Course, Collection, Quiz, Question, QuizTaker, Answer

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at', 'is_deleted')

admin.site.register(Course, CourseAdmin)
admin.site.register(Collection)
admin.site.register(Quiz)
admin.site.register(Answer)

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]    
admin.site.register(Question, QuestionAdmin)    

class QuizTakerAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'student', 'score', 'completed')

admin.site.register(QuizTaker)

