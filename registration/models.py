from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save


#instance hace referencia al objeto que se esta guardando pero despues de que hayamos confirmado el nuevo valor
# si nosotros vamos a la instancia y comprobamos el valor de avatar, nos saldra el valor de avatar que habremos puesto
# y en el file name tendremos el nombre del fichero con la imagen que queremos sobreescribir
def custom_upload_to(instance, filename):
#     #recuperamos la instancia antes de guardarla
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename






# Create your models here.
class Profile(models.Model):
    #indica un perfil por cada usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    
    class Meta:
        ordering = ['user__username']

    
    
    
# oldAvatar = ""
 
# """ Antes de guardar un perfil almacenamos su avatar actual """
# @receiver(pre_save, sender=Profile)
# def signal(sender, instance, update_fields=None, **kwargs):
#     global oldAvatar
#     profile = Profile.objects.get(id=instance.id)
#     oldAvatar = profile.avatar
 
# """ Después de guardar un perfil, si el avatar antiguo es distinto lo borramos """
# @receiver(post_save, sender=Profile)
# def delete_avatar(sender, instance, **kwargs):
#     profile = Profile.objects.get(pk=instance.pk)
#     newAvatar = profile.avatar
#     if oldAvatar != "" and newAvatar == "":
#         oldAvatar.delete()






# Una señal que no es mas que una funcion que ejecuta un codigo en un momento determinado de la vida de una instancia(en este caso, luego de guardarla)    

@receiver(post_save, sender=User)
def ensure_profile_exists( sender, instance, **kwargs):
    #si existe created, se acaba de crear la instancia y si no exisite no entramos, asi nos aseguramos de entrar solo la primera vez
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print("se acaba de crear un usuario y su perfil enlazado")
    
    
    
    
    
    
