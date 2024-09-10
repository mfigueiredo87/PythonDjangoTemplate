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
    
    # metodo para validar os campos
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        # verificar se o nome ta certo
        # usar strip para retirar os espacos vazios antes e depois do texto
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não são permitidos espaços nesse campo")
            else:
                return nome
    # validacao da senha
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")
        
        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("As senhas não são iguais.")
            else:
                return senha_2
            
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