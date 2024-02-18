
class Vehicle:

    #Базовый класс для транспортных средств.

    def __init__(self, brand: str, year: int):

        # Конструктор класса Vehicle.
        #
        # Args:
        #     brand: Марка транспортного средства.
        #     year: Год выпуска транспортного средства.
        #
        self.brand = brand
        self.year = year

    def __str__(self) -> str:

        # Магический метод, возвращающий строковое представление экземпляра класса.
        #
        # Returns:
        #     Строковое представление экземпляра класса.
        #
        return f"{self.brand} {self.year}"

    def __repr__(self) -> str:

        # Магический метод, возвращающий представление экземпляра класса для отладки.
        #
        # Returns:
        #     Представление экземпляра класса для отладки.
        #
        return f"{self.__class__.__name__}(brand={self.brand}, year={self.year})"


class Car(Vehicle):

    #Класс для легковых автомобилей.


    def __init__(self, brand: str, year: int, color: str):

        # Конструктор класса Car.
        #
        # Args:
        #     brand: Марка автомобиля.
        #     year: Год выпуска автомобиля.
        #     color: Цвет автомобиля.
        #
        super().__init__(brand, year)
        self.color = color

    def __str__(self) -> str:
        #
        # Магический метод, возвращающий строковое представление экземпляра класса.
        #
        # Returns:
        #     Строковое представление экземпляра класса.
        #
        return f"{self.brand} {self.color} {self.year}"

    def __repr__(self) -> str:

        # Магический метод, возвращающий представление экземпляра класса для отладки.
        #
        # Returns:
        #     Представление экземпляра класса для отладки.
        #
        return f"{self.__class__.__name__}(brand={self.brand}, year={self.year}, color={self.color})"

    def start_engine(self) -> str:

        # Метод, запускающий двигатель автомобиля.
        #
        # Returns:
        #     Строка с сообщением о запуске двигателя.

        return "Двигатель запущен."

    def open_window(self) -> str:

        # Метод, открывающий окно автомобиля.
        #
        # Returns:
        #     Строка с сообщением об открытии окна.

        return "Окно открыто."


class Truck(Vehicle):

    # Класс для грузовых автомобилей.


    def __init__(self, brand: str, year: int, payload_capacity: float):

        # Конструктор класса Truck.
        #
        # Args:
        #     brand: Марка грузового автомобиля.
        #     year: Год выпуска грузового автомобиля.
        #     payload_capacity: Грузоподъемность грузового автомобиля в тоннах.

        super().__init__(brand, year)
        self.payload_capacity = payload_capacity

    def __str__(self) -> str:

        # Магический метод, возвращающий строковое представление экземпляра класса.
        #
        # Returns:
        #     Строковое представление экземпляра класса.

        return f"{self.brand} (грузоподъемность: {self.payload_capacity} тонн)"

    def __repr__(self) -> str:

        # Магический метод, возвращающий представление экземпляра класса для отладки.
        #
        # Returns:
        #     Представление экземпляра класса для отладки.

        return f"{self.__class__.__name__}(brand={self.brand}, year={self.year}, payload_capacity={self.payload_capacity})"

    def load_cargo(self, weight: float) -> str:

        # Метод, загружающий груз в грузовик.
        #
        # Args:
        #     weight: Вес груза в тоннах.
        #
        # Returns:
        #     Строка с сообщением о загрузке груза.

        return f"Грузовик загружен грузом весом {weight} тонн."

    def unload_cargo(self) -> str:

        # Метод, разгружающий грузовик.
        #
        # Returns:
        #     Строка с сообщением о разгрузке грузовика.

        return "Грузовик разгружен."

if __name__ == "__main__":
    car = Car("Toyota", 2020, "черный")
    print(car)  # Вывод: Toyota черный 2020
    print(repr(car))  # Вывод: Car(brand=Toyota, year=2020, color=черный)
    print(car.start_engine())  # Вывод: Двигатель запущен.
    print(car.open_window())  # Вывод: Окно открыто.

    truck = Truck("Volvo", 2015, 20)
    print(truck)  # Вывод: Volvo (грузоподъемность: 20 тонн)
    print(repr(truck))  # Вывод: Truck(brand=Volvo, year=2015, payload_capacity=20)
    print(truck.load_cargo(15))  # Вывод: Грузовик загружен грузом весом 15 тонн.
    print(truck.unload_cargo())

