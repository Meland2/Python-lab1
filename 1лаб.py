# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Phon:
    def __init__(self, brand: str, screen_size: float, is_smart: bool):
        """
        Создание объекта Телефон
        :param brand: Фирма телефона
        :param screen_size: Размер экрана в дюймах
        :param is_smart:  телефон является смартфоном
        >>> phon = Phon('huawei', 24, True)
        """
        if not isinstance(brand, str):
            raise TypeError('Фирма телефона должна быть строкой')
        self.brand = brand

        if not isinstance(screen_size, (int, float)):
            raise TypeError('Размер в дюймах должен быть числом')
        if screen_size <= 0:
            raise ValueError('Размер экрана должен быть положительным числом')
        self.screen_size = screen_size

        if not isinstance(is_smart, bool):
            raise TypeError('Черта-смартфон "is_smart" должен быть типа bool')
        self.is_smart = is_smart

    def turn(self, turn_to: str) -> str:
        """
        Включение или выключение телевизора.
        :param turn_to: выбор включения или выключения телевизора.
        :return: Сообщение о включении
        Примеры:
        >>> phon = Phon("iphone", 42, True)
        >>> phon.turn('on')
        """
        if turn_to not in ('on', 'off'):
            raise TypeError('Положение поворота может быть on или off')
        ...

    def change_number(self, channel: int) -> None:
        """
        звонок с телефона
        :param number: номер телефона
        Примеры:
        >>> phon = Phon("LG", 49, False)
        >>> phon.change_number(79234924166)
        """
        ...


class Animal:
    def __init__(self, name: str, height: float, weight: float):
        """
        Создание объекта Животное
        :param name: вид животного
        :param height: Рост животного
        :param weight: Вес животного
        Примеры:
        >>> pet = Animal('Медведь', 200, 176.5)
        """
        if type(name) != str:
            raise TypeError('Вид должен быть str')
        self.name = name

        if type(height) not in (int, float):
            raise TypeError('Рост должен быть number')
        if height <= 0:
            raise ValueError('Рост должна быть положительным числом')
        self.height = height

        if type(weight) not in (int, float):
            raise TypeError('Вес должен быть number')
        if weight <= 0:
            raise ValueError('Вес должна быть положительным числом')
        self.weight = weight

    def eat(self, food: str) -> str:
        """
        Функция для представления приема пищи
        :param food: Пища, которую ест животное
        :return: Сообщение о приеме пищи
        Примеры:
        >>> pet = Animal('Крокодил', 240, 150 )
        >>> pet.eat('Рыба')
        """
        ...

    def sleep(self, hours: int) -> str:
        """
        Функция для представления сна
        :param hours: Количество часов сна
        :return: Сообщение о сне
        Примеры:
        >>> pet = Animal('Кот', 6.5, 5.8)
        >>> pet.sleep(16)
        """
        ...

class Car:
        def __init__(self, model: str, year: int, num: str):
            """
            Создание объекта Автомобиль
            :param model: Модель автомобиля
            :param year: Год выпуска автомобиля
            :param num: Номер автомобиля
            Примеры:
            >>> car1 = Car('BMV', 1964, '123qwe')
            """
            if type(model) != str:
                raise TypeError('Модель автомобиля должна быть str')
            self.model = model

            if type(year) != int:
                raise TypeError('Год машины должен быть int')
            self.year = year

            if type(num) != str:
                raise TypeError('Номер машины должен быть  str')
            self.num = num


        def beep(self) -> str:
            """
            Включение фак
            :return: Сообщение включенных фарах
            Примеры:
            >>> car1 = Car('BMV', 1964, 'а123qwe')
            >>> car1.beep()
            """
            ...

        def protection(self) -> str:
            """
            пристегивание ремнём безопасности.
            :return: Сообщение о ремне безопасности
            Примеры:
            >>> car1 = Car('BMV', 1964, '123qwe')
            >>> car1.protection()
            """
            ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
