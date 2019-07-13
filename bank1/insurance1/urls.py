from insurance1.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'librarian', LibrarianVset, basename='emp')
router.register(r'library', LibraryVset, basename='library')
router.register(r'student', StudentVset, basename='students')
router.register(r'books', BookVset, basename='books')

urlpatterns = router.urls