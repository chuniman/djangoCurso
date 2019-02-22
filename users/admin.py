from django.contrib import admin

from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # aca lo que se muestra cuando se listan
    list_display = ('user','phone','website','picture')
    
    # lo que se puede editar en la lista sin entrar al nombre
    list_editable = ('phone','website','picture')
    
    # user__email(como user.email) manera es la manera de acceder al email que tiene user la clase dentro de profile
    # los campos que usa para buscar
    search_fields = ('user__email','phone')

    # esto es para que aparezcan esos filtros de tiempo
    list_filter = ('created','modified')