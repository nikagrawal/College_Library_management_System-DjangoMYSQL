"""DjangoURL Configuration

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
    path('login',views.loginpage),
    path('logout',views.logout,name='logout'),
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
    path('Students_edit/<int:student_id>', views.Students_edit),
    path('Students_update/<int:student_id>', views.Students_update),
    path('Students_destroy/<int:student_id>', views.Students_destroy),

    path('book_a', views.book_a),
    path('Book_show', views.Book_show),
    path('Book_edit/<int:book_id>', views.Book_edit),
    path('Book_update/<int:book_id>', views.Book_update),
    path('Book_destroy/<int:book_id>', views.Book_destroy),

    path('issue_a', views.issue_a),
    path('Issue_show', views.Issue_show),
    path('Issue_edit/<int:issue_id>', views.Issue_edit),
    path('Issue_update/<int:issue_id>', views.Issue_update),
    path('Issue_destroy/<int:issue_id>', views.Issue_destroy),

    path('return_a', views.return_a),
    path('Return_show', views.Return_show),
    path('Return_edit/<int:return_id>', views.Return_edit),
    path('Return_update/<int:return_id>', views.Return_update),
    path('Return_destroy/<int:return_id>', views.Return_destroy),

    path('penalty_a', views.penalty_a),
    path('Penalty_show', views.Penalty_show),
    path('Penalty_edit/<int:penalty_id>', views.Penalty_edit),
    path('Penalty_update/<int:penalty_id>', views.Penalty_update),
    path('Penalty_destroy/<int:penalty_id>', views.Penalty_destroy),

    path('book_lost_a', views.book_lost_a),
    path('Book_lost_show', views.Book_lost_show),
    path('Book_lost_edit/<int:book_lost_id>', views.Book_lost_edit),
    path('Book_lost_update/<int:book_lost_id>', views.Book_lost_update),
    path('Book_lost_destroy/<int:book_lost_id>', views.Book_lost_destroy),

    path('demand_a', views.demand_a),
    path('Demand_show', views.Demand_show),
    path('Demand_edit/<int:demand_id>', views.Demand_edit),
    path('Demand_update/<int:demand_id>', views.Demand_update),
    path('Demand_destroy/<int:demand_id>', views.Demand_destroy),

]