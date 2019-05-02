from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import validate_email


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
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Введите ваш никнейм"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Введите ваш email"}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Введите ваше имя"}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Введите фамилию"}))
    password1 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Введите пароль", 'type':"password" }))
    password2 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Введите пароль заново", 'type':"password" }))

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
        user.username = self.cleaned_data['email']

        if commit:
            user.save()


    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                if len(password2)<8:
                    raise forms.ValidationError('Пароль должен содержать минимум 8 символов')
                elif password2.isdigit():
                    raise forms.ValidationError('Пароль не должен состоять только из цифр')
                else :
                    return password2
        raise forms.ValidationError('Пароли не совпадают')

    def clean_email(self):
        email = self.cleaned_data['email']

        try:
            mt = validate_email(email)
            try:
                user = User.objects.filter(email=email)
                if (len(user)!=0):
                    raise forms.ValidationError('Пользователь с таким emailом существует')
            except User.DoesNotExist:
                return email
        except:
            raise forms.ValidationError('E-mail введен не корректно')

        return email

    def clean_username(self):
        username = self.cleaned_data['username']

        try:
            user = User.objects.filter(username=username)
            if (len(user) != 0):
                raise forms.ValidationError('Пользователь с таким никнеймом существует')
        except User.DoesNotExist:
            return username
        return username


