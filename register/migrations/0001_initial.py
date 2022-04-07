# Generated by Django 4.0.3 on 2022-04-06 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondStepMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_middlename', models.CharField(max_length=100, verbose_name="O'quvchi otasining ismi")),
                ('student_age', models.IntegerField(choices=[(11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54)], verbose_name='Yoshi')),
                ('student_school', models.CharField(max_length=200, verbose_name="O'qish yoki Ish joyi")),
                ('phone_number', models.CharField(max_length=20, unique=True, verbose_name='Telefon raqami')),
                ('bio', models.CharField(max_length=500, verbose_name='Avtobiografiyasi')),
                ('spec', models.CharField(max_length=500, verbose_name='IT sohasidagi bilimi')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='second_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FirstStepMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_middlename', models.CharField(max_length=100, verbose_name="O'quvchi otasining ismi")),
                ('student_class', models.CharField(choices=[('3-sinf', '3-sinf'), ('4-sinf', '4-sinf'), ('5-sinf', '5-sinf'), ('6-sinf', '6-sinf'), ('7-sinf', '7-sinf')], max_length=20, verbose_name='Sinfi')),
                ('student_school', models.CharField(choices=[('1-maktab', '1-maktab'), ('2-maktab', '2-maktab'), ('3-maktab', '3-maktab'), ('4-maktab', '4-maktab'), ('5-maktab', '5-maktab'), ('6-maktab', '6-maktab'), ('7-maktab', '7-maktab'), ('8-maktab', '8-maktab'), ('9-maktab', '9-maktab'), ('10-maktab', '10-maktab'), ('11-maktab', '11-maktab'), ('12-maktab', '12-maktab'), ('13-maktab', '13-maktab'), ('14-maktab', '14-maktab'), ('15-maktab', '15-maktab'), ('16-maktab', '16-maktab'), ('17-maktab', '17-maktab'), ('18-maktab', '18-maktab'), ('19-maktab', '19-maktab'), ('20-maktab', '22-maktab'), ('23-maktab', '23-maktab'), ('24-maktab', '24-maktab'), ('25-maktab', '25-maktab'), ('26-maktab', '26-maktab'), ('27-maktab', '27-maktab'), ('28-maktab', '28-maktab'), ('29-maktab', '29-maktab'), ('30-maktab', '30-maktab'), ('31-maktab', '31-maktab'), ('32-maktab', '32-maktab'), ('33-maktab', '33-maktab'), ('34-maktab', '34-maktab'), ('35-maktab', '35-maktab'), ('36-maktab', '36-maktab'), ('37-maktab', '37-maktab'), ('38-maktab', '38-maktab'), ('39-maktab', '39-maktab'), ('40-maktab', '40-maktab'), ('41-maktab', '41-maktab'), ('42-maktab', '42-maktab'), ('43-maktab', '43-maktab'), ('44-maktab', '44-maktab'), ('45-maktab', '45-maktab'), ('46-maktab', '46-maktab'), ('47-maktab', '47-maktab'), ('48-maktab', '48-maktab'), ('49-maktab', '49-maktab'), ('50-maktab', '50-maktab'), ('51-maktab', '51-maktab'), ('52-maktab', '52-maktab'), ('53-maktab', '53-maktab'), ('54-maktab', '54-maktab'), ('55-maktab', '55-maktab'), ('56-maktab', '56-maktab'), ('57-maktab', '57-maktab'), ('58-maktab', '58-maktab'), ('59-maktab', '59-maktab'), ('60-maktab', '60-maktab'), ('61-maktab', '61-maktab'), ('62-maktab', '62-maktab'), ('63-maktab', '63-maktab'), ('64-maktab', '64-maktab'), ('65-maktab', '65-maktab'), ('66-maktab', '66-maktab'), ('67-maktab', '67-maktab'), ('1-IDUM', '1-IDUM'), ('2-IDUM', '2-IDUM')], max_length=20, verbose_name='Maktabi')),
                ('phone_number', models.CharField(max_length=20, unique=True, verbose_name='Telefon raqami')),
                ('bio', models.CharField(max_length=500, verbose_name='Avtobiografiyasi')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='first_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
