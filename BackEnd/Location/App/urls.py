from django.urls import path
from App.views import LocationShow
from App.views import home
from App.views import LocationUpdate
from App.views import LocationDelete
from App.views import LocationAdd

urlpatterns = [
    path('',home),
    path('add',LocationAdd.as_view()),
    path('show',LocationShow.as_view()),
    path('update/<int:pk>',LocationUpdate.as_view()),
    path('delete/<int:pk>',LocationDelete.as_view())
]
