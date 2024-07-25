from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        fields = ['username', 'email', 'password1', 'password2']