from django.contrib import admin

# Register your models here.

'''
User.objects.create(atributo='valor',atrib2='valor')
con save() se salva el objeto tambien LOS DOS SALVAN
delete() borra al objeto
User.objects.get(nombre_atributo='valor atributo') te devuelve uno, si hay mas de uno tira error
User.objects.filter(email__endswith='@platzi.com') filter retorna los que cumplan la condicion, email attributo __endswith los que terminan con tal parametro
User.objects.all() los trae a todos
User.objects.filter(first_name='arturo').update(password='4567') update actualiza una lista que puede ser de uno
'''