from django.db import models
from accounts.models import *

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)

    description = models.CharField(max_length=200, 
                                  null=True)
    author = models.ForeignKey(UserData, 
                               on_delete=models.SET_NULL, 
                               null=True)
    created_at = models.DateTimeField(auto_now_add=True, 
                                      null=True, 
                                      blank=True)
    updated_at = models.DateField(auto_now=True, 
                                  null=True, 
                                  blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Collection(models.Model):
    author = models.ForeignKey(UserData, 
                               on_delete=models.SET_NULL, 
                               null=True)
    collection_name = models.CharField(max_length=200, 
                                       null=True )
    courses = models.ManyToManyField(Course, 
                                    help_text='select a course for this collection')    

    def __str__(self):
        return self.collection_name

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #        Collection.objects.filter(pk=self.courses).update(courses_count=F('courses_count')+1)
    #     super().save(*args, **kwargs)    

    

class Quiz(models.Model):
    name = models.CharField(max_length=200, 
                            null=True)
    topic = models.CharField(max_length=200, 
                            null=True)
    number_of_questions = models.IntegerField(null=True)
    required_score_to_pass = models.IntegerField(help_text='required scores to pass', 
                                                default=1)
    courses = models.ForeignKey(Course, 
                                on_delete=models.CASCADE,  
                                null=True)
    time_limit = models.PositiveIntegerField(null=True, 
                                            blank=True, 
                                            help_text='duration of the quiz in minute')
    created_at = models.DateTimeField(auto_now_add=True, 
                                     null=True, 
                                     blank=True)
       
    def __str__(self):
        return self.name

    def get_questions(self):
        return self.questions_set.all()    

QUESTION_TYPE = (
    ('single', 'single'),
    ('multiple', 'multiple'),
)        

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=200, 
                                    choices=QUESTION_TYPE, 
                                    default='single')

    def __str__(self):
        return self.question_text

    def get_answers(self):
        return self.answer_set.all()   

class QuizTaker(models.Model):
    quiz = models.ForeignKey(Quiz, 
                             on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(UserData, 
                                on_delete=models.CASCADE, null=True)
    score = models.FloatField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.quiz)

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, 
                                on_delete=models.CASCADE)   
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'question: {self.question.question_text}, answer: {self.text}, correct: {self.correct}' 

class Assignment(models.Model):
    essay = models.TextField()
    description = models.CharField(max_length=200)
    student = models.ForeignKey(UserData, 
                                on_delete=models.CASCADE, null=True)
    schedule = models.DateTimeField()
    deadline = models.DateTimeField()
    grade = models.PositiveIntegerField()
    is_graded = models.BooleanField(default=False)

    def __str__(self):
        return self.essay

    def is_publish(self):
        if self.schedule and date.today() > self.deadline:
            return True
        return False    

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, 
                                   on_delete=models.CASCADE, null=True) 
    student = models.ForeignKey(UserData, 
                                on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return f'Student Grade: {self.assignment.grade}' 
