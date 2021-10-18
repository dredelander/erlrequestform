
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    #Authorizations to log in (Sign up)
    path('signup/', views.signupuser, name ='signupuser' ),

    # Current To do's:
    path('current/', views.currenttodos, name ='currenttodos' ),

    # logout
    path('logout/', views.logoutuser, name ='logoutuser' ),

    #home
    path('', views.home, name ='home' ),

     #login
    path('login/', views.loginuser, name ='loginuser' ),

    # create todo
    path('create/', views.createtodo, name ='createtodo' ),

    # view single todo
    path('todo/<int:todo_pk>', views.viewtodo, name ='viewtodo' ),

      # complete todo
    path('todo/<int:todo_pk>/complete', views.completetodo, name ='completetodo' ),
     
     # delete todo
    path('todo/<int:todo_pk>/delete', views.deletetodo, name ='deletetodo' ),

    # Completed To do's:
    path('completed/', views.completedtodos, name ='completedtodos' ),

     # revisetodo
    path('revise/<int:todo_pk>/', views.reviserequest, name ='reviserequest' ),

    # billing list
    path('billing/', views.billingList, name ='billingList' ),

    # Mark as billed
    path('billing/<int:todo_pk>/billed', views.markbilled, name ='markbilled' ),

    # to Order list
    path('currentorderlist/', views.toOrderList, name ='toOrderList' ),

    # Mark as Ordered
    path('current/<int:todo_pk>/ordered', views.markordered, name ='markordered' ),

    # Ordered list
    path('ordered/', views.orderedList, name ='orderedList' ),
    
    # Billed Complete list
    path('billedcomplete/', views.billedcomplete, name ='billedcomplete' ),

    # Results list
    path('searchResults/', views.seach_results, name ='search_results' ),
    
    # Repeat Request
    path('repeatRequest/<int:todo_pk>/', views.repeat_request, name ='repeat_request' ),
    
    # Results View (NO Results)
    path('noResults/',views.noResults, name ='no_results' ),

]