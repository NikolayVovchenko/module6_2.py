
class Vehicle:

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'while']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner # атрибут Владелец траспорта
        self.__model = model # атрибут Модель (марка)
        self.__endine_power = engine_power # Мощность двигателя
        self.__color = color # Цвет авто

    def get_model(self):# Первый метод
        return f'Модель {self.__model}'#возвращает название модели траспорта

    def get_horsepower(self):# мощность двигателя
        return f'Мощность двигателя {self.__endine_power}'# возвращает строку мощность двигателя

    def get_color(self):# цвет транспорта
        return f'Цвет {self.__color}'#возвращает строку цвет транспорта

    def print_info(self):# Выводит на экран заданные название,цвет,мощность и владельца
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print('Владелец', self.owner)

    def set_color(self, new_color):#метод позволяющий изменить цвет на имеющийся в списке цветов
        if new_color.lower() in self.__COLOR_VARIANTS:# переводим все символы в нижний регистр обращаясь к списку цветов
            self.__color = new_color# сравниваем возможность изменить цвет
        else:
            print(f'Нельзя изменить цвет на {new_color}')

class Sedan(Vehicle):# дочерний класс траспорта
    __PASSENGERS_LIMIT = 5

print('-----------------------------')
vehicle1 = Sedan('Fedos','Toyota MarkII', 'blue', 500)
vehicle1.print_info()
print('-----------------------------')
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
print('-----------------------------')
vehicle1.print_info()
print('-----------------------------')





    

