from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. 254 characters maximum")
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        #no usar widget sino machacamos todas las validaciones y configuraciones que ya tiene el form
    
    #metodo de validacion de email
    def clean_email(self):
        #recupero el email enviado en el form
        email = self.cleaned_data.get('email')
        #compruebo si existe uno o varios emails con la misma direccion
        if User.objects.filter(email=email).exists():
            #invoco error de validacion si ese email ya existe
            raise forms.ValidationError("El email ya esta registrado, prueba con otro.")
        #devuelvo el email si ese email no existia
        return email
    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografía'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'}),
        }
        

class EmailForm(forms.ModelForm):
    email=forms.EmailField(required=True, help_text="Requerido. 254 caracteres como maximo")
    
    class Meta:
        model = User
        fields = ['email']
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        
        if "email" in self.changed_data:
            
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya esta registrado, prueba con otro.")
        return email