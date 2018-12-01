from django.db import models
from django.contrib.auth.hashers import PBKDF2PasswordHasher


class Comment(models.Model):
    feedback_id = models.IntegerField()


class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    password = PBKDF2PasswordHasher()
    nickname = models.CharField(max_length=25)
    number_of_credir_card = models.IntegerField()
    email = models.EmailField()
    photo = models.ImageField(upload_to='User', blank=True)   # при значении True поле может быть пустым
    date_of_birth = models.DateField('Дата народження')
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Answer_list(models.Model):
    answer = models.CharField(max_length=250)


class Help_list(models.Model):
    help = models.CharField(max_length=250)


class Question_list(models.Model):
    ask = models.CharField(max_length=150)


class Ask_body(models.Model):
    question_id = models.ForeignKey(Question_list, on_delete=models.CASCADE)
    answer_id = models.ForeignKey(Answer_list, on_delete=models.CASCADE)
    help_id = models.ForeignKey(Help_list, on_delete=models.CASCADE)


class Ask_mode(models.Model):
    image_ask = models.ImageField()
    ask_body_id = models.ForeignKey(Ask_body,on_delete=models.CASCADE)


class Test_body(models.Model):
    question_id = models.ForeignKey(Question_list, on_delete=models.CASCADE)
    answer_id = models.ForeignKey(Answer_list, on_delete=models.CASCADE)
    help_id = models.ForeignKey(Help_list, on_delete=models.CASCADE)


class Test_mode(models.Model):
    image_of_test = models.ImageField()
    test_body_id = models.ForeignKey(Test_body, on_delete=models.CASCADE)


class Mode_Of_Study(models.Model):
    ask_id = models.ForeignKey(Ask_mode, on_delete=models.CASCADE)
    test_id = models.ForeignKey(Test_mode, on_delete=models.CASCADE)
    name_of_mos = models.CharField(max_length=50)
    description = models.TextField()
    image_for_presentation = models.ImageField(upload_to='Mode_Of_Study',blank=True)
    text_for_read = models.TextField()
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Package(models.Model):
    mode_of_study_id = models.ForeignKey(Mode_Of_Study, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, 'Користувачі')
    name_of_package = models.CharField(max_length=100)
    price = models.FloatField(verbose_name='Ціна за пакет')
    lenght_discription = models.TextField()
    short_discription = models.TextField(max_length=200)


class Ganre_Of_Package(models.Model):
    ganre_id= models.ForeignKey(Package, on_delete=models.CASCADE, blank=True, default=None)
    name_of_ganre = models.CharField(max_length=25)