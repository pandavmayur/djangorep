from django.db import models

# Create your models here.


print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

#orm -- object relational mapping

class Librarian(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField()

    class Meta:
        db_table = "emp_data"


class Library(models.Model):
    libname = models.CharField(max_length=50)
    landline = models.IntegerField()
    librian = models.OneToOneField(Librarian, on_delete=models.CASCADE, primary_key=True)

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


# Librarian -- Library --- 1 - 1
# Library -- Books  -- 1-M
# Books -- Students --- M-M