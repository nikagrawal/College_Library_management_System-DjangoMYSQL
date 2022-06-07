"""DjangoJavaTpointCRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views




urlpatterns = [
    path('dash', views.base),
    path('', views.dash),
    path('base', views.base),
    path('emp', views.emp),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),

    path('department_a', views.department_a),
    path('Department_show', views.Department_show),
    path('Department_edit/<int:department_id>', views.Department_edit),
    path('Department_update/<int:department_id>', views.Department_update),
    path('Department_destroy/<int:department_id>', views.Department_destroy),

    path('author_a', views.author_a),
    path('Author_show', views.Author_show),
    path('Author_edit/<int:author_id>', views.Author_edit),
    path('Author_update/<int:author_id>', views.Author_update),
    path('Author_destroy/<int:author_id>', views.Author_destroy),

    path('publication_a', views.publication_a),
    path('Publication_show', views.Publication_show),
    path('Publication_edit/<int:publication_id>', views.Publication_edit),
    path('Publication_update/<int:publication_id>', views.Publication_update),
    path('Publication_destroy/<int:publication_id>', views.Publication_destroy),

    path('students_a', views.students_a),
    path('Students_show', views.Students_show),
    path('Students_destroy/<int:student_id>', views.Students_destroy),
]