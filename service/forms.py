from django import forms
from service.models import ServiceClient


class ServiceForm(forms.ModelForm):
    name = forms.CharField(
        label="Nome",
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Nome completo"}),
    )
    phone = forms.CharField(
        label="Telefone",
        required=False,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Telefone"}),
    )
    date = forms.DateField(
        label="Data do contrato",
        required=False,
        widget=forms.widgets.DateInput(
            attrs={
                "placeholder": "Data do contrato",
                "type": "text",
                "onfocus": "(this.type='date')",
                "onblur": "(this.type='text')",
            }
        ),
    )
    birth_date = forms.DateField(
        label="Data de nascimento",
        required=False,
        widget=forms.widgets.DateInput(
            attrs={
                "placeholder": "Data de nascimento",
                "type": "text",
                "onfocus": "(this.type='date')",
                "onblur": "(this.type='text')",
            }
        ),
    )
    rg = forms.CharField(
        label="RG",
        required=False,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Digite o número de RG"}),
    )
    cpf = forms.CharField(
        label="CPF",
        required=False,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Digite o número de CPF"}),
    )
    address = forms.CharField(
        label="Endereço",
        required=False,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Endereço"}),
    )
    house_number = forms.IntegerField(
        label="Número",
        required=False,
        widget=forms.widgets.NumberInput(attrs={"placeholder": "Nº"}),
    )
    district = forms.CharField(
        label="Bairro",
        required=False,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Bairro"}),
    )
    city = forms.CharField(
        label="Cidade",
        required=False,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Cidade"}),
    )
    complement = forms.CharField(
        label="Complemento",
        required=False,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Complemento"}),
    )
    photo = forms.ImageField(
        label="Imagem de perfil",
        required=False,
        widget=forms.widgets.FileInput(attrs={"class": "form-control"}),
    )
    service_type = forms.CharField(
        label="Tipo do serviço",
        required=False,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Tipo do serviço"}),
    )
    machine = forms.CharField(
        label="Máquina",
        required=False,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Máquina"}),
    )
    model = forms.CharField(
        label="Modelo",
        required=False,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Modelo"}),
    )
    total = forms.FloatField(
        label="Valor total",
        required=True,
        widget=forms.widgets.NumberInput(attrs={"placeholder": "Valor total"}),
    )
    payment = forms.CharField(
        label="Forma de pagamento",
        required=False,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Forma de pagamento"}),
    )
    obs = forms.CharField(
        label="Observações",
        required=False,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Observações"}),
    )

    class Meta:
        model = ServiceClient
        fields = [
            "name",
            "phone",
            "date",
            "birth_date",
            "rg",
            "cpf",
            "address",
            "house_number",
            "district",
            "city",
            "complement",
            "photo",
            "service_type",
            "machine",
            "model",
            "total",
            "payment",
            "obs",
        ]
