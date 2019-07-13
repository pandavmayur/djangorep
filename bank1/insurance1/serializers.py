from rest_framework.serializers import ModelSerializer
from insurance1.models import *

# converting--lang to n/w file supported and viceversa
class LibrarianSer(ModelSerializer):
    class Meta:
        model = Librarian
        fields = '__all__'

class LibrarySer(ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'

class BookSer(ModelSerializer):
    class Meta:
        model = Book
        #fields = '__all__'
        fields = ('bookname',)
class StudentSer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'