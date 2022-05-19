from decimal import Decimal
from backend.products import Company, Category, Coupon, Product
from random import randint
from time import sleep

class SupportForData:

    def create_models(self):
        self.companies = [Company(name=company_name) for company_name in ['Samsung', 'Apple', 'Positivo', 'Motorola']]
        Company.objects.bulk_create(self.companies)
        
        self.categories = [Category(name=category_name) for category_name in ['Tecnologia', 'Celular', 'Computador', 'Notebook']]
        Category.objects.bulk_create(self.categories)
        
        self.coupons = [Coupon(name=coupon_name, value=Decimal(f'{randint(10, 40)}.00')) for coupon_name in ['black', 'red', 'blue']]
        Coupon.objects.bulk_create(self.coupons)

        self.products = []
        for c in range(1, 21):
            name = f"{['Celular', 'Notebook', 'Computador'][randint(0, 2)]} {self.companies[randint(0, 3)]}"
            cashback = [True, False][randint(0, 1)]
            product = Product(
                name=f'{name} {c}',
                description=f'description {c}',
                current_price=Decimal(f'{randint(1500, 5000)}.00'),
                promotion_price=[Decimal(f'{randint(1000, 1500)}.00'), None][randint(0, 1)],
                cashback_value=Decimal(f'{randint(1, 25)}.00') if cashback else None,
                cashback_is_percent=True if cashback else None,
                quantity=randint(1, 1500),
                company=self.companies[randint(0, 3)]
            )
            product.save()
            product.categories.add(self.categories[randint(0, 3)])
            product.coupons.add(self.coupons[randint(0, 2)])
            self.products.append(product)
            product.save()
            sleep(0.1)
        