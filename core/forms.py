from django import forms

from .models import Product, Supplier


class ProductForm(forms.ModelForm):
    # Текстовые поля для "умного" ввода
    category_name = forms.CharField(label="Категория", required=True)
    manufacturer_name = forms.CharField(label="Производитель", required=True)
    supplier_name = forms.CharField(label="Поставщик", required=True)

    class Meta:
        model = Product
        fields = [
            "article",
            "name",
            "unit",
            "price",
            "discount",
            "quantity",
            "description",
            "photo",
            "category",
            "manufacturer",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Предзаполняем поля при редактировании
        if self.instance.pk:
            if self.instance.category:
                self.fields["category_name"].initial = self.instance.category.name
            if self.instance.manufacturer:
                self.fields[
                    "manufacturer_name"
                ].initial = self.instance.manufacturer.name
            if self.instance.supplier:
                self.fields["supplier_name"].initial = self.instance.supplier.name

    def save(self, commit=True):
        # Логика "найти существующий или создать новый"
        supplier, _ = Supplier.objects.get_or_create(
            name=self.cleaned_data["supplier_name"].strip()
        )

        instance = super().save(commit=False)
        instance.supplier = supplier

        if commit:
            instance.save()
        return instance

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")
        return price

    def clean_quantity(self):
        qty = self.cleaned_data.get("quantity")
        if qty < 0:
            raise forms.ValidationError("Количество не может быть отрицательным")
        return qty
