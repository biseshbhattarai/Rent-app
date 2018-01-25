from django.conf.urls import url


from . import views

app_name_ = 'rentapp'


urlpatterns = [
    url(r'^$',views.rentlist ,name='rent-list'),
    url(r'^rentform/', views.rentform, name="rent-form")
    

]
