from django.urls import path  
from .views import EmployeeCreate, EmployeeDetail, EmployeeRetrieve, EmployeeUpdate, EmployeeDelete

app_name = 'book'  
urlpatterns = [  
    path('emp-gcreate/', EmployeeCreate.as_view(), name = 'EmployeeCreate'),  
    path('emp-retrive/', EmployeeRetrieve.as_view(), name = 'EmployeeRetrieve'),  
    path('emp-retrive/<int:pk>/', EmployeeDetail.as_view(), name = 'EmployeeDetail'),  
    path('emp-update/<int:pk>/update/', EmployeeUpdate.as_view(), name = 'EmployeeUpdate'),  
    path('emp-delete/<int:pk>/delete/', EmployeeDelete.as_view(), name = 'EmployeeDelete'),  
    
]  