import csv

from django.http import HttpResponse
from app.models import User


def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response,delimiter=';')
    writer.writerow(['First name', 'Last name', 'Email address'])

    users = User.objects.all().values_list( 'firstname', 'lastname', 'email' )
    
    for user in users:
        writer.writerow(user)

    return response

    #class User(models.Model): el models.py de la app tiene esto,modifico la views pero del excel,colocando first_name,etc
    #firstname = models.CharField(max_length=100)
    #lastname = models.CharField(max_length=100)
    #email = models.CharField(max_length=200, unique=True)
    #password = models.CharField(max_length=70)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)

