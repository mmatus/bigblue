"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from targetED.models import *

class TestDB(TestCase):
    def setUp(self):
        # Instructors
        self.inst = Instructor(first_name='David',
                               last_name='Gifford',
                               department='EECS',
                               email_address='fake@mit.edu')
        self.inst.save()

        
        # Courses
        self.course = Course(code='7.91', 
                             name='Intro to Comp & Sys Bio',
                             year=2013,
                             semester='S')        
        self.course.save()
        self.course.instructors.add(self.inst)

        self.course2 = Course(code='6.437',
                             name='Inference and Info',
                             year=2013,
                             semester='S')
        self.course2.save()
        self.course2.instructors.add(self.inst)

        
        # Sessions
        self.session = Session(course=self.course, 
                               instructor=self.inst,
                               date=timezone.now())
        self.session.save()
        

        # Students
        self.stud = Student(first_name='Vincent',
                            last_name='Xue',
                            major='CSB',
                            level='G',
                            year='1',
                            email_address='vxue@gmail.com', 
                            current_session=self.session)
        self.stud.save()
        self.stud.enrolled_courses.add(self.course)

        self.stud2 = Student(first_name='Mariana',
                            last_name='Matus',
                            major='CSB',
                            level='G',
                            year='1',
                            email_address='mgmatus@mit.edu', 
                            current_session=self.session)
        self.stud2.save()
        self.stud2.enrolled_courses.add(self.course)
        self.stud2.enrolled_courses.add(self.course2)


        # Quizzes
        self.quiz = Quiz(session=self.session,
                         qtype='P',
                         content='What time is it?', 
                         answer='1',
                         post_time=timezone.now())
        self.quiz.save()
        

        # Responses
        self.resp = Response(student=self.stud,
                             quiz=self.quiz,
                             content='2',
                             resp_time=self.quiz.post_time+timedelta(seconds=20))
        self.resp2 = Response(student=self.stud2,
                              quiz=self.quiz,
                              content='1',
                              resp_time=self.quiz.post_time+timedelta(seconds=30))
        self.resp.save()
        self.resp2.save()
        

    def test_Students(self):
        s = Student.objects.filter(major='CSB')
        self.assertEqual(s[0].first_name, 'Vincent')
        self.assertEqual(s[1].first_name, 'Mariana')

    def test_QuizResponses(self):
        q = Quiz.objects.filter(qtype='P')
        self.assertEqual(q[0].content,'What time is it?')

        r = Response.objects.filter(student__first_name='Vincent')
        self.assertEqual(r[0].content,'2')

        q = Quiz.objects.get(id=1)
        r = Response.objects.filter(quiz=q, content=q.answer)
        self.assertEqual(r[0].student.first_name, 'Mariana')

