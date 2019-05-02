from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm (forms.Form):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={ 'class':"form-control", 'id':"inputEmail" ,'placeholder':"E-mail"}))
    password = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'type':"password", 'name':"password", 'class':"form-control", 'id':"inputPassword", 'placeholder':"Password"}))

    def clean_username(self):
        username = self.cleaned_data['username']

        if '@' in username:
            try:
                user = User.objects.filter(email=username)
                if len(user) == 1:
                    user = user.first()
                    return user.username
                elif len(user) > 1:
                    raise forms.ValidationError("Попробуйте, пожалуйста, войти через username")
                else:
                    raise forms.ValidationError("Пользователь не найден! Пожалуйста, проверьте корректность введенных данных!")
            except User.DoesNotExist:
                raise forms.ValidationError("Пользователя с таким емаилом не существует")

        return username

class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Enter username"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Enter email"}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Enter name"}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Enter lastname"}))
    password1 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Enter password", 'type':"password" }))
    password2 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Enter password again", 'type':"password" }))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()