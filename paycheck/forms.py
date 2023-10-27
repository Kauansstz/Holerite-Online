from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, "")
    field.widget.attrs[attr_name] = f"{existing} {attr_new_val}".strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, "placeholder", placeholder_val)


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields["password"], "Password...")
        add_placeholder(self.fields["email"], "E-mail...")

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        error_messages={"required": "Inserir senha válido"},
        label="Password",
    )

    class Meta:
        model = User
        fields = [
            "email",
            "password",
        ]
        labels = {"email": "E-mail"}
