from django import forms
from .models import Blog, Product, Category

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'created_at', 'publication_sign', 'count_of_views']


class ProductForm(forms.ModelForm):  # Изменено на ModelForm
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'price', 'category']  # Убедитесь, что поля соответствуют модели


class CategoryForm(forms.ModelForm):  # Исправлено название класса
    class Meta:
        model = Category
        fields = ['name', 'description']
