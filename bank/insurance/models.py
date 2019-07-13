from django.db import models



print('Hello MayurGood Night')   # ithe zale changes yes..need more practice..Fakta puu push pull psuh pull push

# Create your models here.

class Librarians(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField()

    class Meta:
        db_table = "libr_data"
# BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

class Library(models.Model):
    libname = models.CharField(max_length=50)
    landline = models.IntegerField()
    librian = models.OneToOneField(Librarians, on_delete=models.CASCADE, primary_key=True)
    #librian = models.ForeignKey(Librarian, unique=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "library_data"



class Book(models.Model):
    bookname = models.CharField(max_length=50)
    price = models.IntegerField()
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    class Meta:
        db_table = "book_data"


class Student(models.Model):
   name = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   address = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()
   age = models.IntegerField()
   books = models.ManyToManyField(Book)

   class Meta:
      db_table = "student_data"
