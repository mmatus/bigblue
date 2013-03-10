from django.db import models


# Entities
class Instructor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=200)
    email_address = models.EmailField()

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Course(models.Model):
    SEMESTERS = ( 
        ('F', 'Fall'),
        ('J', 'IAP'),
        ('S', 'Spring'),
        ('E', 'Summer'),
    )
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    year = models.IntegerField(default=2013)
    semester = models.CharField(max_length=2, choices=SEMESTERS)
    instructors = models.ManyToManyField(Instructor)

    def __unicode__(self):
        return self.name

class Session(models.Model): 
    course = models.ForeignKey(Course)
    instructor = models.ForeignKey(Instructor)
    date = models.DateTimeField('class date-time')

    def __unicode__(self):
        return '%s: session %s' % (course.name, self.id)

class Student(models.Model):
    LEVELS = (
        ('U', 'Undergraduate'),
        ('G', 'Graduate'),
        ('S', 'Special'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    major = models.CharField(max_length=200)
    level = models.CharField(max_length=2, choices = LEVELS)
    year = models.IntegerField(default=0)
    email_address = models.EmailField()
    enrolled_courses = models.ManyToManyField(Course)
    current_session = models.ForeignKey(Session)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Quiz(models.Model):
    TYPES = (
        ('P', 'Poll'),
        ('C', 'Confusometer'),
    )
    session = models.ForeignKey(Session)
    qtype = models.CharField(max_length=2, choices = TYPES)
    content = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    post_time = models.TimeField()

    def __unicode__(self):
        return self.content

class Response(models.Model):
    student = models.ForeignKey(Student)
    quiz = models.ForeignKey(Quiz)
    content = models.CharField(max_length=200)
    resp_time = models.TimeField()

    def __unicode__(self):
        return self.content