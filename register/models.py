from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import random

class_list = [(f'{i} - sinf', f'{i} - sinf') for i in range(3, 8)]

student_age = [(i , i) for i in range(11, 55)]



schools_choice = [
    ('1-maktab','1-maktab'),('2-maktab','2-maktab'), ('3-maktab','3-maktab'),('4-maktab','4-maktab'),('5-maktab','5-maktab'),('6-maktab','6-maktab'),
    ('7-maktab','7-maktab'), ('8-maktab','8-maktab'), ('9-maktab','9-maktab'), ('10-maktab','10-maktab'), ('11-maktab','11-maktab'),('12-maktab','12-maktab'),
    ('13-maktab','13-maktab'), ('14-maktab','14-maktab'),('15-maktab','15-maktab'), ('16-maktab','16-maktab'), ('17-maktab','17-maktab'),('18-maktab','18-maktab'),
    ('19-maktab','19-maktab'), ('20-maktab','22-maktab'),('23-maktab','23-maktab'),('24-maktab','24-maktab'), ('25-maktab','25-maktab'),('26-maktab','26-maktab'),
    ('27-maktab','27-maktab'),('28-maktab','28-maktab'), ('29-maktab','29-maktab'), ('30-maktab','30-maktab'), ('31-maktab','31-maktab'),('32-maktab','32-maktab'),
    ('33-maktab','33-maktab'), ('34-maktab','34-maktab'),('35-maktab','35-maktab'), ('36-maktab','36-maktab'), ('37-maktab','37-maktab'),('38-maktab','38-maktab'),
    ('39-maktab','39-maktab'), ('40-maktab','40-maktab'), ('41-maktab','41-maktab'), ('42-maktab','42-maktab'), ('43-maktab','43-maktab'), 
    ('44-maktab','44-maktab'),('45-maktab','45-maktab'), ('46-maktab','46-maktab'), ('47-maktab','47-maktab'),('48-maktab','48-maktab'),
    ('49-maktab','49-maktab'), ('50-maktab','50-maktab'), ('51-maktab','51-maktab'), ('52-maktab','52-maktab'), ('53-maktab','53-maktab'),
    ('54-maktab','54-maktab'),('55-maktab','55-maktab'), ('56-maktab','56-maktab'), ('57-maktab','57-maktab'),('58-maktab','58-maktab'),
    ('59-maktab','59-maktab'), ('60-maktab','60-maktab'), ('61-maktab','61-maktab'), ('62-maktab','62-maktab'),('63-maktab','63-maktab'),
    ('64-maktab','64-maktab'),('65-maktab','65-maktab'), ('66-maktab','66-maktab'), ('67-maktab','67-maktab'), ('1-IDUM', '1-IDUM'),('2-IDUM', '2-IDUM'),
]


class FirstStepMembers(models.Model):

    #creating a relationship with user class (not inheriting)
    first_name = models.CharField(max_length=20, verbose_name="Ismi")
    last_name = models.CharField(max_length=20, verbose_name="Familiyasi")
    student_class = models.CharField(max_length=20, choices=class_list, verbose_name="Sinfi")
    student_school = models.CharField(max_length=20, choices=schools_choice, verbose_name="Maktabi")
    phone_number = models.CharField(max_length=20, verbose_name="Telefon raqami", unique=True)
    bio = models.CharField(max_length=500, verbose_name="Avtobiografiyasi")

    student_id = models.CharField(max_length=20,blank=True, default=0)

    def save(self, *args, **kwargs):
        self.student_id = f"CS{random.randint(1000000,10000000)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name + " " + self.last_name

class SecondStepMembers(models.Model):

    #creating a relationship with user class (not inheriting)
    first_name = models.CharField(max_length=20, verbose_name="Ismi")
    last_name = models.CharField(max_length=20, verbose_name="Familiyasi")
    student_age = models.IntegerField(choices=student_age, verbose_name="Yoshi")
    student_school = models.CharField(max_length=200, verbose_name="O'qish yoki Ish joyi")
    phone_number = models.CharField(max_length=20, verbose_name="Telefon raqami", unique=True)
    bio = models.CharField(max_length=500, verbose_name="Avtobiografiyasi")
    spec = models.CharField(max_length=500,  verbose_name="IT sohasidagi bilimi")

    
    def __str__(self):
        return self.first_name + " " + self.last_name