from django import forms

# class para login
class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Manuel"
            }
        )
    )
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a sua senha"
            }
        )
    )
    
# class para o form de cadastro
class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Nome de Cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Manuel Manuel"
            }
        )
    )
    email=forms.EmailField(
        label="Endereço de E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: manuel@gmail.com"
            }
        )
    )
    senha_1=forms.CharField(
        label="Digite a Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a sua senha"
            }
        )
    )
    senha_2=forms.CharField(
        label="Confirmação da Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a sua senha novamente"
            }
        )
    )
    # imagem=forms.CharField(
    #      required=True,
    #     max_length=70,
    #     widget=forms.FileInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Carregar a imagem"
    #         }
    #     )
    # )