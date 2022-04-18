from django.urls import path
from . import views

urlpatterns = [    
    path('' , views.index , name="index" ),
    path('<int:just_id>/meal' , views.just, name="dish"),
    path('book/<str:name_meal>' , views.book , name="book"),
    path('unbook/<str:chair_id>', views.unbook , name="unbook"),
    path('register' , views.register , name="register" ),
    path('povar', views.povar , name="povar"),
    path('kirish', views.login_view , name="log-in"),
    path('chiqish', views.logout_view , name="log-out"),
    path('add' , views.addMeal , name="add")
]