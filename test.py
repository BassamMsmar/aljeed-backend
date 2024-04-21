from datetime import datetime

# تواريخ الشحنات
date_1 = datetime(2024, 1, 1)
date_2 = datetime(2024, 1, 5)

# حساب الفرق بين التواريخ بالأيام
difference = date_2 - date_1

# طباعة الفرق بالأيام
print(difference.days)
