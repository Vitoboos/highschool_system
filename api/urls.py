from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'student', views.StudentModelViewset)
router.register(r'professor', views.ProfessorModelViewset)
router.register(r'subject', views.SubjectModelViewset)
router.register(r'grades', views.SubjectGradesModelViewset)

urlpatterns = [
    path('api/<str:name>/', views.StudentModelViewset.as_view({'get': 'list'})),
    path('api/<str:name>/', views.ProfessorModelViewset.as_view({'get': 'list'})),
    path('api/<str:name>/', views.SubjectModelViewset.as_view({'get': 'list'})),
    path('api/<str:name>/', views.SubjectGradesModelViewset.as_view({'get': 'list'})),
    path('', include(router.urls)),
]
