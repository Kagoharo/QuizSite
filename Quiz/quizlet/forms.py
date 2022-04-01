from django import forms


class CategoryForm(forms.Form):
    """
    Форма для категории
    """

    category_name = forms.CharField(min_length=10)

    def clean_category_name(self):
        cleaned_data = self.cleaned_data
        category_name = cleaned_data.get('category_name')
        return category_name
