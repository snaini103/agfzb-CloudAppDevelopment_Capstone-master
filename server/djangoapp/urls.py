from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    
    #path for index

    path(route='index.html', view=views.get_dealerships, name='index'),

    # path for static_django_template view
    
    path(route='static_django_template.html', view=views.static_django_template, name='static_django_template'),


    # path for about view
    
    path(route='about_us.html', view=views.about_us, name='about_us'),

    # path for contact us view
    
    path(route='contact_us.html', view=views.contact_us, name='contact_us'),

    # path for registration

    path(route='registration.html', view=views.registration_request, name='registration'),

    # path for login

    path(route='login/', view=views.login_request, name='login'),

    # path for logout

    path(route='logout/', view=views.logout_request, name='logout'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

