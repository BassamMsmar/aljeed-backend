import os
import django

# إعداد متغير البيئة لمشروع Django الخاص بك
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  # استبدل 'project' باسم مشروعك الفعلي
django.setup()

from faker import Faker
import random
from shipments.models import Shipment, City, Driver, Branch, ShipmentStatus
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

faker = Faker()

# توليد بيانات السائق الوهمي
TRUCK_TYPE_CHOICES = ['تريلة سطحة', 'تريلة ستارة', 'تريلة جوانب', 'تريلة براد', 'لوري عايدي', 'لوري براد', 'دينه عايدي', 'دينة براد']
LANGUAGE_CHOICES = ['ar', 'en', 'ur']

def create_fake_driver():
    driver = Driver.objects.create(
        name=faker.name(),
        phone=faker.phone_number(),
        id_number=faker.random_number(digits=10),
        language=random.choice(LANGUAGE_CHOICES),
        truck_type=random.choice(TRUCK_TYPE_CHOICES),
        rate=random.randint(1, 5),
    )
    return driver

def create_multiple_drivers(n):
    for _ in range(n):
        driver = create_fake_driver()
        print(f'Driver created: {driver}')


STATUS = (
    ('Shipped', _('Shipped')),
    ('Delivered', _('Delivered')),
    ('Late', _('Late')),
    ('Feedback', _('Feedback')),
)
# توليد شحنة وهمية
def create_fake_shipment():
    city = City.objects.order_by('?').first()
    driver = Driver.objects.order_by('?').first()
    branch = Branch.objects.order_by('?').first()
    
    fare = random.randint(100, 1000)
    premium = random.randint(50, 500)
    fare_return = random.randint(20, 300)
    days_stayed = random.randint(1, 30)
    stay_cost = random.randint(100, 1000)
    deducted = random.randint(10, 100)
    
    status = random.choice([status[0] for status in STATUS])
    created_at = faker.date_time_this_year(before_now=True, after_now=False, tzinfo=timezone.get_current_timezone())
    expected_arrival_date = created_at + timedelta(days=random.randint(1, 10))
    actual_delivery_date = expected_arrival_date + timedelta(days=random.randint(0, 5))
    
    shipment = Shipment.objects.create(
        user=faker.random_element(User.objects.all()),
        driver=driver,
        customer_branch=branch,
        fare=fare,
        premium=premium,
        fare_return=fare_return,
        days_stayed=days_stayed,
        stay_cost=stay_cost,
        deducted=deducted,
        status=status,
        destination=city,
        created_at=created_at,
        expected_arrival_date=expected_arrival_date,
        actual_delivery_date=actual_delivery_date,
        notes=faker.text(max_nb_chars=200)
    )
    
    shipment.save()
    return shipment

def create_multiple_shipments(n):
    for _ in range(n):
        shipment = create_fake_shipment()
        print(f'Shipment created: {shipment}')

if __name__ == "__main__":
    number_of_drivers = 30
    number_of_shipments = 100

    # print(f"Creating {number_of_drivers} fake drivers...")
    # create_multiple_drivers(number_of_drivers)

    print(f"Creating {number_of_shipments} fake shipments...")
    create_multiple_shipments(number_of_shipments)

    print(f"{number_of_drivers} drivers and {number_of_shipments} shipments created successfully.")


# في ملف initial_data.json أو في management command
ShipmentStatus.objects.create(name_en="Shipped", name_ar="تم الشحن")
ShipmentStatus.objects.create(name_en="Delivered", name_ar="تم التوصيل")
ShipmentStatus.objects.create(name_en="Late", name_ar="متأخر")
ShipmentStatus.objects.create(name_en="Feedback", name_ar="تم التقييم")