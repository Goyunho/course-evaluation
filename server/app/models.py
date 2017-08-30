from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class University(models.Model):
    name = models.CharField(
        verbose_name='학교명', default='', max_length=50)
    name_short = models.CharField(
        verbose_name='축약명', default='', max_length=50, blank=True)
    name_en = models.CharField(
        verbose_name='영문명', default='', max_length=50, blank=True)
    name_en_short = models.CharField(
        verbose_name='축약영문명', default='', max_length=50, blank=True)

    def __str__(self):
        return self.name


class Undergraduate(models.Model):
    name = models.CharField(
        verbose_name='학부명', default='', max_length=50)
    university = models.ForeignKey(University, related_name='undergraduate', verbose_name='학교',
                                   on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return ' '.join([self.university.__str__(), self.name])


class Department(models.Model):
    name = models.CharField(
        verbose_name='학과명', default='', max_length=50)
    undergraduate = models.ForeignKey(Undergraduate, related_name='department', verbose_name='학부',
                                      on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return ' '.join([self.undergraduate.__str__(), self.name])


class Faculty(models.Model):
    photo = models.ImageField(
        verbose_name='사진', null=True, blank=True)
    name = models.CharField(
        verbose_name='교수명', default='', max_length=50)
    age = models.PositiveSmallIntegerField(verbose_name='나이', null=True)
    email = models.EmailField(verbose_name='메일', default='', blank=True)
    phone = models.CharField(
        verbose_name='전화번호', default='', max_length=20)
    belong = models.ForeignKey(
        Department, related_name='faculty', verbose_name='소속', on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(
        verbose_name='강의명', max_length=20)
    belong = models.ForeignKey(
        Department, related_name='course', verbose_name='소속', on_delete=models.DO_NOTHING, blank=True, null=True)
    faculty = models.ForeignKey(
        Faculty, verbose_name='강사', on_delete=models.DO_NOTHING)
    info = models.TextField(
        verbose_name='설명', blank=True, null=True, default='')

    def __str__(self):
        return self.name


class CourseEvaluation(models.Model):
    course = models.ForeignKey(
        Course, verbose_name='강의', on_delete=models.DO_NOTHING)
    pnc = models.BooleanField(default=True)
    description = models.CharField(verbose_name='평가내용', max_length=20)

    def __str__(self):
        return self.description


class EvaluationRecord(models.Model):
    evaluation = models.ForeignKey(CourseEvaluation, verbose_name='평가내용')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    score = models.PositiveSmallIntegerField(verbose_name='점수', default=1,
                                             validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return self.evaluation.__str__()
