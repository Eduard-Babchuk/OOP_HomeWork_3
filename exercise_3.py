import datetime

class Car:
    def __init__(self, brand="Unknown", model="Unknown", year=0, mileage=0.0):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        
        current_year = datetime.datetime.now().year
        if self.year > current_year:
            print(f"Рік випуску не може бути більшим за поточний. Встановлено поточний рік ({current_year}).")
            self.year = current_year 
        elif self.year == 0:
            print(f"Рік випуску не може бути нульовим. Встановлено поточний рік ({current_year}).")
            self.year = current_year  
        else:
            print(f"Автомобіль {self.brand} {self.model} створений.")

    def __copy__(self):
        return Car(self.brand, self.model, self.year, self.mileage)

    def __del__(self):
        print(f"Автомобіль {self.brand} {self.model} видалено з пам'яті.")

    def get_info(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Рік: {self.year}, Пробіг: {self.mileage} км."

    def update_mileage(self, new_mileage):
        if new_mileage > self.mileage:
            self.mileage = new_mileage
            print(f"Пробіг оновлено: {self.mileage} км.")
        else:
            print("Новий пробіг повинен бути більшим за попередній.")

    def compare(self, other_car):
        if self.year != other_car.year:
            return self.year > other_car.year
        return self.mileage < other_car.mileage 

try:
    car1 = Car() 
    car2 = Car("Toyota", "Corolla", 2015, 150000) 
    car3 = car2.__copy__()  

    print(car1.get_info())
    print(car2.get_info())
    print(car3.get_info())

    car2.update_mileage(160000)
    car2.update_mileage(140000)

    if car2.compare(car3):
        print("Автомобіль 2 новіший або з меншим пробігом.")
    else:
        print("Автомобіль 3 новіший або з меншим пробігом.")

except Exception as e:
    print(f"Помилка: {e}")