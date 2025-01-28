from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Заполнение базы данных о продуктах'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Фрукты')

        products = [
            {'name': 'апельсин', "description": "оранжевый", 'category': category},
            {"name": "яблоко", "description": "зеленое", 'category': category}
        ]

        for prod in products:
            product, created = Product.objects.get_or_create(**prod)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: '
                                                     f'{product.name} {product.description}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: '
                                                     f'{product.name} {product.description}'))
