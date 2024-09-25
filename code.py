from datetime import datetime
import random

class Medicine:
    def __init__(self, name, price, expiry_date):
        self._name = name
        self._price = random.randint(10, 100)
        self.expiry_date = expiry_date
    
    @property
    def name(self):
        name = ["Paracetamol", "Amoxicillin", "Cetirizine", "Vitamin C ", "Omeprazole"]
        return random.choice(name)
    
    @property
    def price(self):
        return self._price
    
    @property
    def is_expired(self):
        return datetime.now() > self.expiry_date

    def display_info(self):
        return f"Medicine: {self.name}, Price: {self.price} UAH, Expiry Date: {self.expiry_date}"

    def update_price(self, new_price):
        self._price = new_price

    @staticmethod
    def category():
        categories = ["Pain Relievers", "Antibiotics", "Vitamins", "Antihistamines", "Digestive Aids"]
        return random.choice(categories)

    def sell(self, quantity):
        return f"Sold {quantity} units of {self.name}"

class Supplier:
    def __init__(self, supplier_name, contact_info):
        self._supplier_name = supplier_name
        self._contact_info = contact_info

    @property
    def supplier_name(self):
        return self._supplier_name

    @property
    def contact_info(self):
        return self._contact_info

    def display_supplier_info(self):
        return f"Supplier: {self.supplier_name}, Contact: {self.contact_info}"

class SupplierMedicine(Medicine, Supplier):
    def __init__(self, name, price, expiry_date, supplier_name, contact_info):
        Medicine.__init__(self, name, price, expiry_date)
        Supplier.__init__(self, supplier_name, contact_info)

    def display_info(self):
        return f"{super().display_info()} | Supplier: {self.supplier_name}"

medicine = Medicine("Aspirin", 50, datetime(2025, 5, 1))

print(medicine.display_info())
print(medicine.category())
print(medicine.sell(3))
print("Expired:", medicine.is_expired)
