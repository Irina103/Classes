#!/usr/bin/env python
# coding: utf-8

# In[2]:


import doctest


class Glass:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Стакан"

        :param capacity_volume: Объем стакана
        :param occupied_volume: Объем занимаемой жидкости

        Примеры:
        >>> glass = Glass(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем стакана должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем стакана должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_glass(self) -> bool:
        """
        Функция которая проверяет является ли стакан пустым

        :return: Является ли стакан пустым

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.is_empty_glass()
        """
        ...

    def add_water_to_glass(self, water: float) -> None:
        """
        Добавление воды в стакан.
        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в стакане, то вызываем ошибку

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.add_water_to_glass(200)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        ...

    def remove_water_from_glass(self, estimate_water: float) -> None:
        """
        Извлечение воды из стакана.

        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в стакане,
        то возвращается ошибка.

        :return: Объем реально извлеченной жидкости

        Примеры:
        >>> glass = Glass(500, 500)
        >>> glass.remove_water_from_glass(200)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


# In[3]:


import doctest


class Glass:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Стакан"

        :param capacity_volume: Объем стакана
        :param occupied_volume: Объем занимаемой жидкости

        Примеры:
        >>> glass = Glass(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем стакана должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем стакана должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        if occupied_volume > capacity_volume:
            raise ValueError("Количество жидкости не может превышать объем стакана")
        self.occupied_volume = occupied_volume

    def is_empty_glass(self) -> bool:
        """
        Функция которая проверяет является ли стакан пустым

        :return: Является ли стакан пустым

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.is_empty_glass()
        True
        >>> glass2 = Glass(500, 100)
        >>> glass2.is_empty_glass()
        False
        """
        return self.occupied_volume == 0

    def add_water_to_glass(self, water: float) -> None:
        """
        Добавление воды в стакан.
        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в стакане, то вызываем ошибку

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.add_water_to_glass(200)
        >>> glass.occupied_volume
        200
        >>> glass.add_water_to_glass(300)
        >>> glass.occupied_volume
        500
        >>> glass.add_water_to_glass(1)
        Traceback (most recent call last):
            ...
        ValueError: В стакане недостаточно места для добавления жидкости
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        if self.occupied_volume + water > self.capacity_volume:
            raise ValueError("В стакане недостаточно места для добавления жидкости")
        self.occupied_volume += water

    def remove_water_from_glass(self, estimate_water: float) -> float:
        """
        Извлечение воды из стакана.

        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в стакане,
        то возвращается ошибка.

        :return: Объем реально извлеченной жидкости

        Примеры:
        >>> glass = Glass(500, 500)
        >>> glass.remove_water_from_glass(200)
        200
        >>> glass.occupied_volume
        300
        >>> glass.remove_water_from_glass(400)
        Traceback (most recent call last):
            ...
        ValueError: Невозможно извлечь больше жидкости, чем есть в стакане
        """
        if not isinstance(estimate_water, (int, float)):
            raise TypeError("Извлекаемая жидкость должна быть типа int или float")
        if estimate_water < 0:
            raise ValueError("Извлекаемая жидкость должна быть положительным числом")
        if estimate_water > self.occupied_volume:
            raise ValueError("Невозможно извлечь больше жидкости, чем есть в стакане")
        self.occupied_volume -= estimate_water
        return estimate_water


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


# In[ ]:


import doctest


class Table:
    def __init__(self, hight: (float, int), weight: (float, int)):
        """
        Создание и подготовка к работе объекта "Table"

        :param  hight: how tall is the Table
        :param weight: how heavy is the Table

        Примеры:
        >>> table = Table(1.5, 10)  # инициализация экземпляра класса
        """
        if not isinstance(hight, (float, int)):
            raise TypeError("Table hight cannot be str nor bool type")
        if hight <= 0:
            raise ValueError("Table cannot have negative hight")
        self.hight = hight

        if not isinstance(weight, (int, float)):
            raise TypeError("Table weight must be a number")
        if weight < 0:
            raise ValueError("Table cannot have negative mass")
        self.weight = weight

    def is_empty_table(self) -> bool:
        """
        Функция которая проверяет является ли стакан пустым

        :return: Является ли стакан пустым

        Примеры:
        >>> table = Table(1.5, 10)
        >>> table.is_empty_table()
        """
        pass
    
    def add_object_on_the_table(self, water: float) -> None:
        """
        Добавление воды в стакан.
        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в стакане, то вызываем ошибку

        Примеры:
        >>> glass = Glass(500, 0)
        >>> glass.add_water_to_glass(200)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        pass

    def remove_water_from_glass(self, estimate_water: float) -> None:
        """
        Извлечение воды из стакана.

        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в стакане,
        то возвращается ошибка.

        :return: Объем реально извлеченной жидкости

        Примеры:
        >>> glass = Glass(500, 500)
        >>> glass.remove_water_from_glass(200)
        """
        pass


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


# In[39]:


import doctest


class Table:
    def __init__(self, surface_area: (int, float), occupied_area: (int, float)):
        """
        Создание и подготовка к работе объекта "Стол"

        :param surface_area: Общая площадь стола
        :param occupied_area: Занятая площадь (предметами)

        Примеры:
        >>> table = Table(1000, 0)
        """
        if not isinstance(surface_area, (int, float)):
            raise TypeError("Площадь стола должна быть типа int или float")
        if surface_area <= 0:
            raise ValueError("Площадь стола должна быть положительным числом")
        self.surface_area = surface_area

        if not isinstance(occupied_area, (int, float)):
            raise TypeError("Занятая площадь должна быть типа int или float")
        if occupied_area < 0:
            raise ValueError("Занятая площадь не может быть отрицательной")
        if occupied_area > surface_area:
            raise ValueError("Занятая площадь не может превышать общую площадь стола")
            
        self.occupied_area = occupied_area

    def is_table_clear(self) -> bool:
        """
        Проверяет, пуст ли стол (ничего не лежит)

        Примеры:
        >>> table = Table(1000, 0)
        >>> table.is_table_clear()
        True
        >>> table2 = Table(1000, 200)
        >>> table2.is_table_clear()
        False
        """
        return self.occupied_area == 0

    def put_object_on_table(self, object_area: (int, float)) -> None:
        """
        Кладет предмет на стол (занимает часть площади)

        :param object_area: Площадь, которую займет предмет
        :raises ValueError: Если недостаточно места

        Примеры:
        >>> table = Table(1000, 200)
        >>> table.put_object_on_table(300)
        >>> table.occupied_area
        500
        >>> table.put_object_on_table(600)
        Traceback (most recent call last):
            ...
        ValueError: Недостаточно свободного места на столе
        """
        if not isinstance(object_area, (int, float)):
            raise TypeError("Площадь предмета должна быть типа int или float")
        if object_area < 0:
            raise ValueError("Площадь предмета должна быть положительным числом")
        if self.occupied_area + object_area > self.surface_area:
            raise ValueError("Недостаточно свободного места на столе")
        self.occupied_area += object_area

    def remove_object_from_table(self, object_area: (int, float)) -> (int, float):
        """
        Убирает предмет со стола (освобождает часть площади)

        :param object_area: Площадь убираемого предмета
        :raises ValueError: Если на столе занято меньше, чем нужно убрать

        :return: Реально освобожденная площадь

        Примеры:
        >>> table = Table(1000, 400)
        >>> table.remove_object_from_table(100)
        100
        >>> table.occupied_area
        300
        >>> table.remove_object_from_table(400)
        Traceback (most recent call last):
            ...
        ValueError: Нельзя убрать больше, чем занято
        """
        if not isinstance(object_area, (int, float)):
            raise TypeError("Площадь предмета должна быть типа int или float")
        if object_area < 0:
            raise ValueError("Площадь предмета должна быть положительной")
        if object_area > self.occupied_area:
            raise ValueError("Нельзя убрать больше, чем занято")
        self.occupied_area -= object_area
        return object_area


doctest.testmod()


# In[44]:


t1 = Table(1000, 100)
print(t1.occupied_area)
print(t1.is_table_clear())
t1.put_object_on_table(50)
print(t1.occupied_area)
t1.remove_object_from_table(150)
print(t1.occupied_area)
print(t1.is_table_clear())

t2 = Table(1000, 100)
print(t2.occupied_area)


# In[41]:


import doctest


class Backpack:
    def __init__(self, capacity_weight: (int, float), current_weight: (int, float)):
        """
        Инициализация объекта "Рюкзак"

        :param capacity_weight: Максимальный вес, который можно нести
        :param current_weight: Текущий вес уже загруженных предметов

        Примеры:
        >>> bp1 = Backpack(20.0, 0.0)
        >>> bp2 = Backpack(30.0, 0.0)
        """
        if not isinstance(capacity_weight, (int, float)):
            raise TypeError("Вместимость рюкзака должна быть числом")
        if capacity_weight <= 0:
            raise ValueError("Вместимость должна быть положительной")

        if not isinstance(current_weight, (int, float)):
            raise TypeError("Текущий вес должен быть числом")
        if current_weight < 0:
            raise ValueError("Текущий вес не может быть отрицательным")
        if current_weight > capacity_weight:
            raise ValueError("Перегрузка рюкзака!")

        self.capacity_weight = capacity_weight
        self.current_weight = current_weight

    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли рюкзак

        >>> bp = Backpack(20.0, 0.0)
        >>> bp.is_empty()
        True
        >>> bp2 = Backpack(20.0, 3.0)
        >>> bp2.is_empty()
        False
        """
        return self.current_weight == 0

    def add_item(self, weight: float) -> None:
        """
        Добавляет предмет в рюкзак

        :param weight: Вес предмета
        :raises ValueError: если превышается вместимость

        >>> bp = Backpack(20.0, 5.0)
        >>> bp.add_item(10.0)
        >>> bp.current_weight
        15.0
        >>> bp.add_item(10.0)
        Traceback (most recent call last):
            ...
        ValueError: Предмет не помещается в рюкзак
        """
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть числом")
        if weight < 0:
            raise ValueError("Вес должен быть положительным")
        if self.current_weight + weight > self.capacity_weight:
            raise ValueError("Предмет не помещается в рюкзак")
            
        self.current_weight += weight

    def remove_item(self, weight: float) -> float:
        """
        Удаляет предмет из рюкзака

        :param weight: Вес удаляемого предмета
        :return: Реально удалённый вес

        >>> bp = Backpack(20.0, 10.0)
        >>> bp.current_weight
        10.0
        >>> bp.remove_item(3.0)
        >>> bp.current_weight
        7.0
        >>> bp.remove_item(10.0)
        Traceback (most recent call last):
            ...
        ValueError: В рюкзаке нет столько веса для удаления
        """
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть числом")
        if weight < 0:
            raise ValueError("Вес должен быть положительным")
        if weight > self.current_weight:
            raise ValueError("В рюкзаке нет столько веса для удаления")
            
        self.current_weight -= weight


doctest.testmod()


# In[ ]:





# In[37]:


def func():
    print('Hello')
    return 10

print(func())


# In[38]:


b1 = Backpack(20, 10)

print(b1.is_empty())

print(b1.current_weight)

b1.add_item(10)

print(b1.current_weight)

b1.remove_item(5)

print(b1.current_weight)


# In[ ]:





# In[19]:


import doctest


class Battery:
    def __init__(self, capacity_mah: float, current_charge_mah: float):
        """
        Создание объекта "Батарея"

        :param capacity_mah: Емкость батареи в мАч
        :param current_charge_mah: Текущий заряд в мАч

        Примеры:
        >>> bat = Battery(4000, 1000)
        """
        if not isinstance(capacity_mah, (int, float)):
            raise TypeError("Емкость батареи должна быть числом")
        if capacity_mah <= 0:
            raise ValueError("Емкость батареи должна быть положительной")

        if not isinstance(current_charge_mah, (int, float)):
            raise TypeError("Текущий заряд должен быть числом")
        if current_charge_mah < 0:
            raise ValueError("Заряд не может быть отрицательным")
        if current_charge_mah > capacity_mah:
            raise ValueError("Заряд не может превышать емкость")

        self.capacity_mah = capacity_mah
        self.current_charge_mah = current_charge_mah

    def is_empty(self) -> bool:
        """
        Проверяет, разряжена ли батарея

        >>> bat = Battery(4000, 0)
        >>> bat.is_empty()
        True
        >>> bat2 = Battery(4000, 500)
        >>> bat2.is_empty()
        False
        """
        return self.current_charge_mah == 0

    def is_full(self) -> bool:
        """
        Проверяет, полностью ли заряжена батарея

        >>> bat = Battery(4000, 4000)
        >>> bat.is_full()
        True
        >>> bat2 = Battery(4000, 3500)
        >>> bat2.is_full()
        False
        """
        return self.current_charge_mah == self.capacity_mah

    def charge(self, amount: float) -> None:
        """
        Заряжает батарею на указанное количество мАч

        :param amount: Количество мАч для зарядки
        :raises ValueError: если зарядка превышает емкость

        >>> bat = Battery(4000, 1000)
        >>> bat.current_charge_mah
        1000
        >>> bat.charge(2000)
        >>> bat.current_charge_mah
        3000
        >>> bat.charge(1500)
        Traceback (most recent call last):
            ...
        ValueError: Перезарядка невозможна
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Значение зарядки должно быть числом")
        if amount < 0:
            raise ValueError("Нельзя заряжать отрицательным значением")
        if self.current_charge_mah + amount > self.capacity_mah:
            raise ValueError("Перезарядка невозможна")
            
        self.current_charge_mah += amount

    def discharge(self, amount: float) -> float:
        """
        Разряжает батарею на указанное количество мАч

        :param amount: Количество мАч, которое нужно израсходовать
        :raises ValueError: если батарея разряжается ниже нуля

        :return: Реально израсходованное количество мАч

        >>> bat = Battery(4000, 2000)
        >>> bat.current_charge_mah
        2000
        >>> bat.discharge(500)
        >>> bat.current_charge_mah
        1500
        >>> bat.discharge(2000)
        Traceback (most recent call last):
            ...
        ValueError: Недостаточно заряда для разрядки
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Значение разрядки должно быть числом")
        if amount < 0:
            raise ValueError("Нельзя разряжать отрицательным значением")
        if amount > self.current_charge_mah:
            raise ValueError("Недостаточно заряда для разрядки")
            
        self.current_charge_mah -= amount
    
    

doctest.testmod()


# In[31]:


b1 = Battery(1000, 100)
b2 = Battery(500, 100)
b3 = Battery(3500, 3000)


b2.discharge(50)
print(b2.current_charge_mah)


b1.charge(10)
print(b1.current_charge_mah)


b3.charge(500)
print(b3.current_charge_mah)


print(b3.is_full())
print(b2.current_charge_mah)


print(b3.is_empty())
print(b3.current_charge_mah)

# print(b.__class__)
print(b.__class__.__name__)


# In[ ]:


# make an example of class Song which will have attributes authour_of_song, name_of_song, year, (lst or dic)
# add a method which will check if the song is in russian,
# and another one which will return year of the song by taking the name of the song 
# last method should return all the songs and take in the authour as an input
# one more that will take in year and return all the songs and thier authours
# method that adds songs into the example


# 🎤 "Hello" by Adele (English)
# 🎸 "Du Hast" by Rammstein (German)
# 🎶 "All the Things She Said" by t.A.T.u. (English)
# 🎧 "Искала" by Zemfira (Russian)

# In[39]:


import doctest

class SongLibrary:
    def __init__(self):
        """
        Adds a new song to the library
        """
        self.songs = []

    def add_song(self, author: str='Unknown', name: str='Unknown', year: int=2000, language: str='Unknown') -> None:
        """
        Добавляет песню в библиотеку

        >>> lib = SongLibrary()
        >>> lib.add_song("Zemfira", "Искала", 2000, "Russian")
        >>> lib.add_song("Rammstein", "Du Hast", 1997, "German")
        >>> lib.add_song("Adele", "Hello", 2015, "English")
        >>> lib.add_song("Adele", "Hello", 2015, "English")
        'We already have this song'
        >>> len(lib.songs)
        3
        """
        dct = {
            "author": author,
            "name": name,
            "year": year,
            "language": language 
        }
        if dct not in self.songs:       
            self.songs.append(dct)
        else: 
            return 'We already have this song'

    def is_russian(self, name: str) -> bool:
        """
        Checks if a song (by title) is in Russian

        >>> lib = SongLibrary()
        >>> lib.add_song("Zemfira", "Искала", 2000, "Russian")
        >>> lib.add_song("Adele", "Hello", 2015, "English")
        >>> lib.is_russian("Искала")
        True
        >>> lib.is_russian("Hello")
        'Song is not Russian'
        >>> lib.is_russian("Unknown")
        Traceback (most recent call last):
            ...
        ValueError: Песня с таким названием не найдена
        """
        for song in self.songs:
            if song["name"] == name:
                if song["language"].lower() == "russian":
                    return True    
                else:
                    return 'Song is not Russian'
                
        raise ValueError("Песня с таким названием не найдена")
      
    def get_year_by_name(self, name: str) -> int:
        """
        Returns the year a song was released

        >>> lib = SongLibrary()
        >>> lib.add_song("Rammstein", "Du Hast", 1997, "German")
        >>> lib.get_year_by_name("Du Hast")
        1997
        >>> lib.get_year_by_name("Unknown")
        Traceback (most recent call last):
            ...
        ValueError: Песня с таким названием не найдена
        """
        for song in self.songs:
            if song["name"] == name:
                return song["year"]
            
        raise ValueError("Песня с таким названием не найдена")

    def get_songs_by_author(self, author: str) -> list:
        """
        Returns all songs by a given author

        >>> lib = SongLibrary()
        >>> lib.add_song("Zemfira", "Искала", 2000, "Russian")
        >>> lib.add_song("Adele", "Hello", 2015, "English")
        >>> lib.get_songs_by_author("Zemfira")
        ['Искала']
        >>> lib.get_songs_by_author("Adele")
        ['Hello']
        >>> lib.get_songs_by_author("Unknown")
        'This author does not have songs'
        """
        lst = [song["name"] for song in self.songs if song["author"] == author]
        if not lst: # same as if len(lst) == 0
            return 'This author does not have songs'
        else: 
            return lst
            
    def get_songs_by_year(self, year: int) -> list:
        """
        Returns all songs released in a specific year, along with their authors

        >>> lib = SongLibrary()
        >>> lib.add_song("Zemfira", "Искала", 2000, "Russian")
        >>> lib.add_song("t.A.T.u.", "All the Things She Said", 2000, "English")
        >>> lib.add_song("Adele", "Hello", 2015, "English")
        >>> lib.add_song("Rammstein", "Du Hast", 1997, "German")
        >>> lib.get_songs_by_year(2000)
        [('Искала', 'Zemfira'), ('All the Things She Said', 't.A.T.u.')]
        >>> lib.get_songs_by_year(1997)
        [('Du Hast', 'Rammstein')]
        >>> lib.get_songs_by_year(1990)
        'On this year we do not have any songs'
        """
        lst = [(song["name"], song["author"]) for song in self.songs if song["year"] == year]
        if not lst:
            return 'On this year we do not have any songs'
        else: 
            return lst
        
    def del_by_author_and_name(self, author: str='Unknown', name: str='Unknown') -> None:
        """
        Deleted the songs from the list using name and author
        >>> lib = SongLibrary()
        >>> lib.add_song("Zemfira", "Искала", 2000, "Russian")
        >>> lib.add_song("t.A.T.u.", "All the Things She Said", 2000, "English")
        >>> lib.add_song("Adele", "Hello", 2015, "English")
        >>> lib.add_song("Rammstein", "Du Hast", 1997, "German")
        >>> lib.del_by_author_and_name("Zemfira", "Искала")
        "We deleted : {'author': 'Zemfira', 'name': 'Искала', 'year': 2000, 'language': 'Russian'}"
        >>> lib.del_by_author_and_name("Something", "Искала")
        'This song have not been found'
        """
        for idx, el in enumerate(self.songs):
            if el['author'] == author and el['name'] == name:
                deleted_item = self.songs.pop(idx)
                return f'We deleted : {deleted_item}'

        return 'This song have not been found'
        
doctest.testmod()


# add another method that will delete all songs using the author and method 
# which will delete all songs using the year 


# Создайте класс с именем Rectangle
# В конструкторе пропишите длину и ширину.
# Cоздайте метод, который вычисляет площадь прямоугольника.

# Создайте класс с именем Circle
# В конструкторе пропишите радиус.
# Cоздайте метод, который вычисляет площадь круга.
# Cоздайте метод, который вычисляет периметр круга.


# Создайте класс с именем Tickets
# how much money we have and how much is the ticket and compare the 2 to find out 
# how many tickets we can buy with the given money 


# In[25]:


lst = [{'author': 'Zemfira', 'name': 'Искала', 'year': 2000, 'language': 'Russian'}, {'author': 'Rammstein', 'name': 'Du Hast', 'year': 1997, 'language': 'German'}, {'author': 't.A.T.u.', 'name': 'All the Things She Said', 'year': 2000, 'language': 'English'}, {'author': 'Adele', 'name': 'Hello', 'year': 2015, 'language': 'Unknown'}]


# lst.remove({'author': 'Zemfira', 'name': 'Искала', 'year': 2000, 'language': 'Russian'})
input_author = input()
input_name = input()
for idx, el in enumerate(lst):
    if el['author'] == input_author and el['name'] == input_name:
        deleted_item = lst.pop(idx)
        print('We deleted :', deleted_item)

print('This song have not been found')
    


# In[5]:


lib = SongLibrary()

# add songs
lib.add_song("Zemfira", "Искала", 2000, "Russian")
lib.add_song("Rammstein", "Du Hast", 1997, "German")
# lib.add_song("Adele", "Hello", 2015, "English")
lib.add_song("t.A.T.u.", "All the Things She Said", 2000, "English")
lib.add_song("Adele", "Hello", 2015)
print(lib.songs)


# # Check if songs are in Russian
# print(lib.is_russian("Искала"))    # True
# print(lib.is_russian("Du Hast"))   # False

# # Get year by song name
# print(lib.get_year_by_name("Hello"))          # 2015
# print(lib.get_year_by_name("All the Things She Said"))  # 2000

# # Get all songs by author
# print(lib.get_songs_by_author("Zemfira"))     # ['Искала']
# print(lib.get_songs_by_author("Adele"))       # ['Hello']

# # Get all songs from a given year
# print(lib.get_songs_by_year(2000))  
# # [('Искала', 'Zemfira'), ('All the Things She Said', 't.A.T.u.')]

# print(lib.get_songs_by_year(1997))  
# # [('Du Hast', 'Rammstein')]

# # Show the class name
# print(lib.__class__.__name__)  # SongLibrary


# In[13]:


# st = {{'a':1}, {'b':2}, {'c':3}}
{'a':1} == {'a':1}


# In[16]:


lst = [{'author': 'Zemfira', 'name': 'Искала', 'year': 2000, 'language': 'Russian'}, {'author': 'Rammstein', 'name': 'Du Hast', 'year': 1997, 'language': 'German'}, {'author': 't.A.T.u.', 'name': 'All the Things She Said', 'year': 2000, 'language': 'English'}, {'author': 'Adele', 'name': 'Hello', 'year': 2015, 'language': 'Unknown'}]

dct = lst[0]
dct not in lst


# In[40]:


# add another method that will delete all songs using the author and method 
# which will delete all songs using the year 


# Создайте класс с именем Rectangle
# В конструкторе пропишите длину и ширину.
# Cоздайте метод, который вычисляет площадь прямоугольника.

# Создайте класс с именем Circle
# В конструкторе пропишите радиус.
# Cоздайте метод, который вычисляет площадь круга.
# Cоздайте метод, который вычисляет периметр круга.


# Создайте класс с именем Tickets
# how much money we have and how much is the ticket and compare the 2 to find out 
# how many tickets we can buy with the given money 


# In[61]:


import doctest

class SongLibrary:
    def __init__(self):
        """
        Adds a new song to the library
        """
        self.songs = []

    def add_song(self, author: str='Unknown', name: str='Unknown', year: int=2000, language: str='Unknown') -> None:
        """
        Добавляет песню в библиотеку

        >>> lib = SongLibrary()
        >>> lib.add_song("Zemfira", "Искала", 2000, "Russian")
        >>> lib.add_song("Rammstein", "Du Hast", 1997, "German")
        >>> lib.add_song("Adele", "Hello", 2015, "English")
        >>> lib.add_song("Adele", "Hello", 2015, "English")
        'We already have this song'
        >>> len(lib.songs)
        3
        """
        dct = {
            "author": author,
            "name": name,
            "year": year,
            "language": language 
        }
        if dct not in self.songs:       
            self.songs.append(dct)
        else: 
            return 'We already have this song'

    def is_russian(self, name: str) -> bool:
        """
        Checks if a song (by title) is in Russian

        >>> lib = SongLibrary()
        >>> lib.add_song("Zemfira", "Искала", 2000, "Russian")
        >>> lib.add_song("Adele", "Hello", 2015, "English")
        >>> lib.is_russian("Искала")
        True
        >>> lib.is_russian("Hello")
        'Song is not Russian'
        >>> lib.is_russian("Unknown")
        Traceback (most recent call last):
            ...
        ValueError: Песня с таким названием не найдена
        """
        for song in self.songs:
            if song["name"] == name:
                if song["language"].lower() == "russian":
                    return True    
                else:
                    return 'Song is not Russian'
                
        raise ValueError("Песня с таким названием не найдена")
      
    def get_year_by_name(self, name: str) -> int:
        """
        Returns the year a song was released

        >>> lib = SongLibrary()
        >>> lib.add_song("Rammstein", "Du Hast", 1997, "German")
        >>> lib.get_year_by_name("Du Hast")
        1997
        >>> lib.get_year_by_name("Unknown")
        Traceback (most recent call last):
            ...
        ValueError: Песня с таким названием не найдена
        """
        for song in self.songs:
            if song["name"] == name:
                return song["year"]
            
        raise ValueError("Песня с таким названием не найдена")

    def get_songs_by_author(self, author: str) -> list:
        """
        Returns all songs by a given author

        >>> lib = SongLibrary()
        >>> lib.add_song("Zemfira", "Искала", 2000, "Russian")
        >>> lib.add_song("Adele", "Hello", 2015, "English")
        >>> lib.get_songs_by_author("Zemfira")
        ['Искала']
        >>> lib.get_songs_by_author("Adele")
        ['Hello']
        >>> lib.get_songs_by_author("Unknown")
        'This author does not have songs'
        """
        lst = [song["name"] for song in self.songs if song["author"] == author]
        if not lst: # same as if len(lst) == 0
            return 'This author does not have songs'
        else: 
            return lst
            
    def get_songs_by_year(self, year: int) -> list:
        """
        Returns all songs released in a specific year, along with their authors

        >>> lib = SongLibrary()
        >>> lib.add_song("Zemfira", "Искала", 2000, "Russian")
        >>> lib.add_song("t.A.T.u.", "All the Things She Said", 2000, "English")
        >>> lib.add_song("Adele", "Hello", 2015, "English")
        >>> lib.add_song("Rammstein", "Du Hast", 1997, "German")
        >>> lib.get_songs_by_year(2000)
        [('Искала', 'Zemfira'), ('All the Things She Said', 't.A.T.u.')]
        >>> lib.get_songs_by_year(1997)
        [('Du Hast', 'Rammstein')]
        >>> lib.get_songs_by_year(1990)
        'On this year we do not have any songs'
        """
        lst = [(song["name"], song["author"]) for song in self.songs if song["year"] == year]
        if not lst:
            return 'On this year we do not have any songs'
        else: 
            return lst
        
    def del_by_author_and_name(self, author: str='Unknown', name: str='Unknown') -> None:
        """
        Deleted the songs from the list using name and author
        >>> lib = SongLibrary()
        >>> lib.add_song("Zemfira", "Искала", 2000, "Russian")
        >>> lib.add_song("t.A.T.u.", "All the Things She Said", 2000, "English")
        >>> lib.add_song("Adele", "Hello", 2015, "English")
        >>> lib.add_song("Rammstein", "Du Hast", 1997, "German")
        >>> lib.del_by_author_and_name("Zemfira", "Искала")
        "We deleted : {'author': 'Zemfira', 'name': 'Искала', 'year': 2000, 'language': 'Russian'}"
        >>> lib.del_by_author_and_name("Something", "Искала")
        'This song have not been found'
        """
        for idx, el in enumerate(self.songs):
            if el['author'] == author and el['name'] == name:
                deleted_item = self.songs.pop(idx)
                return f'We deleted : {deleted_item}'

        return 'This song have not been found'
        




    def del_all_by_author(self, author: str) -> str:

        """
        Deletes all songs by a specific author.

        >>> lib = SongLibrary()
        >>> lib.add_song("Zemfira", "Искала", 2000, "Russian")
        >>> lib.add_song("Zemfira", "Ариведерчи", 2002, "Russian")
        >>> lib.add_song("Adele", "Hello", 2015, "English")
        >>> lib.del_all_by_author("Zemfira")
        We deleted : {'author': 'Zemfira', 'name': 'Искала', 'year': 2000, 'language': 'Russian'}
        We deleted : {'author': 'Zemfira', 'name': 'Ариведерчи', 'year': 2002, 'language': 'Russian'}
        'Deleted 2 songs by Zemfira'
        >>> lib.del_all_by_author("Zemfira")
        'This author does not have songs'
        """
#         original_len = len(self.songs)
#         self.songs = [song for song in self.songs if song["author"] != author]
#         deleted_count = original_len - len(self.songs)

#         if deleted_count > 0:
#             return f"Deleted {deleted_count} songs by {author}"
#         else:
#             return 'This author does not have songs'

        original_len = len(self.songs)
        
        count = 0
        for idx, el in enumerate(self.songs):
            if el['author'] == author:
                deleted_item = self.songs[idx]
                self.songs[idx] = 0
                count += 1
                print(f'We deleted : {deleted_item}')
                            
        for _ in range(count):  
            self.songs.remove(0)
                
        deleted_count = original_len - len(self.songs)        
        if deleted_count > 0:
            return f"Deleted {deleted_count} songs by {author}"
        else:
            return 'This author does not have songs'

    def del_all_by_year(self, year: int) -> str:
        """
        Deletes all songs from a specific year.

        >>> lib = SongLibrary()
        >>> lib.add_song("Zemfira", "Искала", 2000, "Russian")
        >>> lib.add_song("t.A.T.u.", "All the Things She Said", 2000, "English")
        >>> lib.add_song("Adele", "Hello", 2015, "English")
        >>> lib.del_all_by_year(2000)
        We deleted : {'author': 'Zemfira', 'name': 'Искала', 'year': 2000, 'language': 'Russian'}
        We deleted : {'author': 't.A.T.u.', 'name': 'All the Things She Said', 'year': 2000, 'language': 'English'}
        'Deleted 2 songs from year 2000'
        >>> lib.del_all_by_year(1990)
        'On this year we do not have any songs'
        """
#         original_len = len(self.songs)
#         self.songs = [song for song in self.songs if song["year"] != year]
#         deleted_count = original_len - len(self.songs)

#         if deleted_count > 0:
#             return f'Deleted {deleted_count} songs from year {year}'
#         else:
#             return 'On this year we do not have any songs'

        original_len = len(self.songs)
        
        count = 0
        for idx, el in enumerate(self.songs):
            if el['year'] == year:
                deleted_item = self.songs[idx]
                self.songs[idx] = 0
                count += 1
                print(f'We deleted : {deleted_item}')
                            
        for _ in range(count):  
            self.songs.remove(0)
                
        deleted_count = original_len - len(self.songs)        
        if deleted_count > 0:
            return f'Deleted {deleted_count} songs from year {year}'
        else:
            return 'On this year we do not have any songs'

doctest.testmod()


# In[44]:


lib = SongLibrary()

# Add songs
lib.add_song("Zemfira", "Искала", 2000, "Russian")
lib.add_song("Rammstein", "Du Hast", 1997, "German")
lib.add_song("t.A.T.u.", "All the Things She Said", 2000, "English")
lib.add_song("Adele", "Hello", 2015)

# Check library before deletion
print("Initial library:")
print(lib.songs)

# Delete all by author
print("\nDeleting all songs by 'Zemfira':")
print(lib.del_all_by_author("Zemfira"))  # Should say 1 song deleted
print("Library after deletion by author:")
print(lib.songs)

# Delete all by year
print("\nDeleting all songs from year 2000:")
print(lib.del_all_by_year(2000))  # Should say 1 song deleted (t.A.T.u.)
print("Library after deletion by year:")
print(lib.songs)

# Attempt to delete again
print("\nTrying to delete again:")
print(lib.del_all_by_author("Zemfira"))  # Should say no songs found
print(lib.del_all_by_year(2000))         # Should say no songs found

# Final state of the library
print("\nFinal library state:")
print(lib.songs)


# In[69]:


class Rectangle:
    def __init__(self, length: float, width: float):
        """
        Initializes a rectangle with the given length and width.
        """
        if not isinstance(length, (int, float)):
            raise TypeError("length should be a number")
        if not isinstance(width, (int, float)):
            raise TypeError("width should be a number")
        self.length = length
        self.width = width

    def area(self) -> float:
        """
        Calculates the area of the rectangle.

        >>> r = Rectangle(5, 3)
        >>> r.area()
        15
        """
        return self.length * self.width
    
doctest.testmod()


# In[70]:


# Create a Rectangle object
rect1 = Rectangle(5, 3)

# Show attributes
print("Length:", rect1.length)    # 5
print("Width:", rect1.width)      # 3

# Calculate area
print("Area:", rect1.area())      # 15

# Create another Rectangle object
rect2 = Rectangle(10, 10)
print("\nNew Rectangle:")
print("Length:", rect2.length)    # 10
print("Width:", rect2.width)      # 10
print("Area:", rect2.area())      # 100

# Show class name
print("\nClass name:")
print(rect1.__class__.__name__)   # Rectangle


rect3 = Rectangle('name', 10)


# In[63]:


import math

class Circle:
    def __init__(self, radius: float):
        """
        Initializes a circle with the given radius.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius should be a number")
            
        self.radius = radius

    def area(self) -> float:
        """
        Calculates the area of the circle.

        >>> c = Circle(3)
        >>> round(c.area(), 2)
        28.27
        """
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        """
        Calculates the perimeter (circumference) of the circle.

        >>> c = Circle(3)
        >>> round(c.perimeter(), 2)
        18.85
        """
        return 2 * math.pi * self.radius

doctest.testmod()


# In[67]:


c1 = Circle(3)

print("Radius:", c1.radius)
print("Area:", round(c1.area(), 2))         # 28.27
print("Perimeter:", round(c1.perimeter(), 2))  # 18.85

c2 = Circle('name')


# In[65]:


class Tickets:
    def __init__(self, money: float, ticket_price: float):
        """
        Initializes the Tickets class with available money and ticket price.
        """
        if not isinstance(money, (int, float)):
            raise TypeError("Money should be a number")
        if not isinstance(ticket_price, (int, float)):
            raise TypeError("Ticket price should be a number")
            
        self.money = money
        self.ticket_price = ticket_price

    def tickets_can_buy(self) -> int:
        """
        Calculates how many tickets can be bought with the given money.

        >>> t = Tickets(50, 12)
        >>> t.tickets_can_buy()
        4
        """
        return int(self.money // self.ticket_price)  # Integer division
    
doctest.testmod()


# In[66]:


t = Tickets(50, 12)

print("Money available:", t.money)
print("Ticket price:", t.ticket_price)
print("Tickets you can buy:", t.tickets_can_buy())  # Output: 4

t2 = Tickets('name', 12)


# In[ ]:


# create 2 classes: Book and Library 
# in Book, in innit it has atributes: id = identificator of the book(type int), name = name of the book,
# number_of_pages, colour_of_the_book, author
# methods: 
# read pages = fixes the number of pages we read so far so it would take int value, (can't be more then pages)
# number of read pages = returns the number of read pages
# remove_page_by_number 
# adds_pages_number

b1 = Book1 
b2 = Book2
b3 = Book3
books = [b1, b2, b3]

# in Library, add the Books using the class Book, so it has a list of explaes from Book
# innit has a list 
# methods:
# find the book using id, if not found then retun 'We haved found the book' if found then return all info about the book
# new_id, it creates a new id which we haven't used yet so it can add the new book in the library
# add_books, in this method use the results from method new_id
# method that gets all the books by the author
# gets the books which has specific number of pages
# gets the books which has specific colour
# deletes all books by the number of pages
# deletes book by the id 


# another class: PaperBook - simillar to Book class but different 
# another class: AudioBook - simillar to Book class but different 





# In[86]:


a = [1, 2, 3, 4, 5]
b = [2, 3]
for i in b:
    a.remove(i)
print(a)


# In[5]:


import doctest

class Book:
    
    def __init__(self, id_: int, name: str, number_of_pages: int, colour: str, author: str):
        """
        Initializes a Book instance.

        >>> b = Book(1, "Test Book", 100, "Red", "Author A")
        >>> b.name
        'Test Book'
        """
        self.id = id_
        self.name = name
        self.number_of_pages = [i for i in range(1, number_of_pages+1)]
        self.colour = colour
        self.author = author
        
        self.read_pages = 0

    def read_pages_now(self, pages: int) -> str:
        """
        Marks pages as read.

        >>> b = Book(1, "Book", 50, "Red", "Author")
        >>> b.read_pages_now(20)
        'You read 20 more pages.'
        >>> b.read_pages_now(40)
        "You can't read more pages than the book has"
        """
        if pages < 0:
            return "Invalid input"
        if self.read_pages + pages > len(self.number_of_pages):
            return "You can't read more pages than the book has"
        self.read_pages += pages
        return f"You read {pages} more pages."

    def number_of_read_pages(self) -> int:
        """
        Returns how many pages have been read.

        >>> b = Book(1, "Book", 50, "Red", "Author")
        >>> b.read_pages_now(10)
        'You read 10 more pages.'
        >>> b.number_of_read_pages()
        10
        """
        return self.read_pages

    def remove_page_by_number(self, pages: list) -> str:
        """
        Removes pages from the book.

        >>> b = Book(1, "Book", 100, "Red", "Author")
        >>> b.remove_page_by_number([1, 2, 3])
        '3 pages removed.'
        >>> len(b.number_of_pages)
        97
        """
        if len(pages) >= len(self.number_of_pages):
            return "Can't remove that many pages"
        
        for page_number in pages:
            self.number_of_pages.remove(page_number)
        
        if self.read_pages > len(self.number_of_pages):
            self.read_pages = len(self.number_of_pages)
        return f"{len(pages)} pages removed."
#     number of pages shouldn't be just a number but each page should have it's own index and we will be 
#     removing the page using that index 
# a = [1, 2, 3, 4, 5]
# b = [2, 3]
# for i in b:
#     a.remove(i)
# print(a)

    def add_pages_number(self, pages: list) -> str:
        """
        Adds pages to the book.

        >>> b = Book(1, "Book", 50, "Red", "Author")
        >>> b.add_pages_number([1, 2, 3, 4, 5])
        '5 pages added.'
        >>> len(b.number_of_pages)
        55
        """
        self.number_of_pages += pages
        return f"{len(pages)} pages added."
#     add pages in the middle of the book such that the rest of the pages thin change their numbers(i.e index)

    def __str__(self):
        return f"{self.name} by {self.author} ({len(self.number_of_pages)} pages, {self.colour}, ID: {self.id})"


class PaperBook(Book):
    def __init__(self, id_: int, name: str, number_of_pages: int, colour: str, author: str, cover_type: str = "soft"):
        """
        >>> pb = PaperBook(2, "Paper Test", 150, "Blue", "Author B", cover_type="hard")
        >>> pb.cover_type
        'hard'
        """
        super().__init__(id_, name, number_of_pages, colour, author)
        self.cover_type = cover_type

    def __str__(self):
        return super().__str__() + f" [PaperBook: {self.cover_type} cover]"


class AudioBook(Book):
    def __init__(self, id_: int, name: str, number_of_pages: int, colour: str, author: str, duration_min: int = 60):
        """
        >>> ab = AudioBook(3, "Audio Test", 0, "Black", "Author C", duration_min=90)
        >>> ab.duration_min
        90
        """
        super().__init__(id_, name, number_of_pages, colour, author)
        self.duration_min = duration_min

    def __str__(self):
        return super().__str__() + f" [AudioBook: {self.duration_min} mins]"



doctest.testmod()


# In[6]:


# Create regular book
b1 = Book(1, "The Little Prince", 96, "Yellow", "Antoine de Saint-Exupéry")
print(b1.read_pages_now(20))               # You read 20 more pages.
print(b1.number_of_read_pages())           # 20
print(b1.remove_page_by_number([1, 2, 4, 6]))        # 10 pages removed.
print(b1.add_pages_number([1, 2, 4]))              # 4 pages added.
print(b1)                                  # The Little Prince by Antoine de Saint-Exupéry (90 pages, Yellow, ID: 1)

# Create paper book
b2 = PaperBook(2, "Pride and Prejudice", 432, "White", "Jane Austen", cover_type="hard")
print(b2)                                  # Pride and Prejudice by Jane Austen (432 pages, White, ID: 2) [PaperBook: hard cover]

# Create audio book
b3 = AudioBook(3, "Becoming", 400, "Blue", "Michelle Obama", duration_min=1140)
print(b3)                                  # Becoming by Michelle Obama (400 pages, Blue, ID: 3) [AudioBook: 1140 mins]


# In[ ]:


# in Library, add the Books using the class Book, so it has a list of explaes from Book
# innit has a list 
# methods:
# find the book using id, if not found then retun 'We haved found the book' if found then return all info about the book
# new_id, it creates a new id which we haven't used yet so it can add the new book in the library
# add_books, in this method use the results from method new_id
# method that gets all the books by the author
# gets the books which has specific number of pages
# gets the books which has specific colour
# deletes all books by the number of pages
# deletes book by the id 


# In[7]:


class Library:
    def __init__(self):
        self.books = []

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return str(book)
        return "We haven't found the book"

    def new_id(self):
        existing_ids = {book.book_id for book in self.books}
        new_id = 1
        while new_id in existing_ids:
            new_id += 1
        return new_id

    def add_book(self, title, author, pages, colour):
        book_id = self.new_id()
        new_book = Book(title, author, pages, colour, book_id)
        self.books.append(new_book)
        return f"Book added with ID: {book_id}"

    def get_books_by_author(self, author):
        return [str(book) for book in self.books if book.author == author]

    def get_books_by_pages(self, page_count):
        return [str(book) for book in self.books if book.pages == page_count]

    def get_books_by_colour(self, colour):
        return [str(book) for book in self.books if book.colour == colour]

    def delete_books_by_pages(self, page_count):
        original_count = len(self.books)
        self.books = [book for book in self.books if book.pages != page_count]
        return f"Deleted {original_count - len(self.books)} books with {page_count} pages."

    def delete_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                return f"Deleted book with ID: {book_id}"
        return "Book with given ID not found"


# In[80]:


class Library:
    def __init__(self):
        """
        Initializes an empty library.

        >>> lib = Library()
        >>> len(lib.books)
        0
        """
        self.books = []

    def _used_ids(self):
        return {book.id for book in self.books}

    def new_id(self) -> int:
        """
        Returns the smallest unused ID.

        >>> lib = Library()
        >>> lib.new_id()
        1
        >>> lib.books.append(Book(1, "B1", 100, "Red", "A1"))
        >>> lib.new_id()
        2
        """
        current = 1
        used = self._used_ids()
        while current in used:
            current += 1
        return current
#     it creates a new id which we haven't used yet so it can add the new book in the library

    def add_book(self, name: str, number_of_pages: int, colour: str, author: str, book_type: str = "paper", **kwargs):
        """
        Adds a book to the library using a unique ID.

        >>> lib = Library()
        >>> lib.add_book("Book1", 100, "Red", "Author1")
        'Book added: Book1 by Author1 (100 pages, Red, ID: 1) [PaperBook: soft cover]'
        """
        book_id = self.new_id()
        if book_type == "paper":
            book = PaperBook(book_id, name, number_of_pages, colour, author, **kwargs)
        elif book_type == "audio":
            book = AudioBook(book_id, name, number_of_pages, colour, author, **kwargs)
        else:
            book = Book(book_id, name, number_of_pages, colour, author)
        self.books.append(book)
        return f"Book added: {book}"

    def find_by_id(self, book_id: int):
        """
        Finds a book by its ID.

        >>> lib = Library()
        >>> lib.add_book("Book1", 100, "Red", "Author1")
        'Book added: Book1 by Author1 (100 pages, Red, ID: 1) [PaperBook: soft cover]'
        >>> str(lib.find_by_id(1))
        'Book1 by Author1 (100 pages, Red, ID: 1) [PaperBook: soft cover]'
        >>> lib.find_by_id(10)
        "We haven't found the book"
        """
        for book in self.books:
            if book.id == book_id:
                return book
        return "We haven't found the book"

    def get_books_by_author(self, author: str):
        """
        Returns a list of books by a specific author.

        >>> lib = Library()
        >>> lib.add_book("Book1", 100, "Red", "Author1")
        'Book added: Book1 by Author1 (100 pages, Red, ID: 1) [PaperBook: soft cover]'
        >>> lib.add_book("Book2", 200, "Blue", "Author2")
        'Book added: Book2 by Author2 (200 pages, Blue, ID: 2) [PaperBook: soft cover]'
        >>> [b.name for b in lib.get_books_by_author("Author1")]
        ['Book1']
        """
        return [book for book in self.books if book.author == author]

    def get_books_by_pages(self, pages: int):
        """
        Returns books with a specific number of pages.

        >>> lib = Library()
        >>> lib.add_book("Book1", 100, "Red", "Author1")
        'Book added: Book1 by Author1 (100 pages, Red, ID: 1) [PaperBook: soft cover]'
        >>> lib.add_book("Book2", 200, "Blue", "Author2")
        'Book added: Book2 by Author2 (200 pages, Blue, ID: 2) [PaperBook: soft cover]'
        >>> [b.name for b in lib.get_books_by_pages(200)]
        ['Book2']
        """
        return [book for book in self.books if book.number_of_pages == pages]

    def get_books_by_colour(self, colour: str):
        """
        Returns books with a specific colour (case-insensitive).

        >>> lib = Library()
        >>> lib.add_book("Book1", 100, "Red", "Author1")
        'Book added: Book1 by Author1 (100 pages, Red, ID: 1) [PaperBook: soft cover]'
        >>> lib.add_book("Book2", 200, "Blue", "Author2")
        'Book added: Book2 by Author2 (200 pages, Blue, ID: 2) [PaperBook: soft cover]'
        >>> [b.name for b in lib.get_books_by_colour("red")]
        ['Book1']
        """
        return [book for book in self.books if book.colour.lower() == colour.lower()]

    def delete_books_by_pages(self, pages: int):
        """
        Deletes all books with a specific number of pages.

        >>> lib = Library()
        >>> lib.add_book("Book1", 100, "Red", "Author1")
        'Book added: Book1 by Author1 (100 pages, Red, ID: 1) [PaperBook: soft cover]'
        >>> lib.add_book("Book2", 100, "Blue", "Author2")
        'Book added: Book2 by Author2 (100 pages, Blue, ID: 2) [PaperBook: soft cover]'
        >>> lib.delete_books_by_pages(100)
        'Deleted 2 books'
        >>> len(lib.books)
        0
        """
        original_len = len(self.books)
        self.books = [book for book in self.books if book.number_of_pages != pages]
        return f"Deleted {original_len - len(self.books)} books"

    def delete_book_by_id(self, book_id: int):
        """
        Deletes a book by its ID.

        >>> lib = Library()
        >>> lib.add_book("Book1", 100, "Red", "Author1")
        'Book added: Book1 by Author1 (100 pages, Red, ID: 1) [PaperBook: soft cover]'
        >>> lib.delete_book_by_id(1)
        'Book with ID 1 deleted'
        >>> lib.delete_book_by_id(99)
        'Book not found'
        """
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                return f"Book with ID {book_id} deleted"
        return "Book not found"

    def list_books(self):
        """
        Returns all books as string list.

        >>> lib = Library()
        >>> lib.add_book("Book1", 100, "Red", "Author1")
        'Book added: Book1 by Author1 (100 pages, Red, ID: 1) [PaperBook: soft cover]'
        >>> len(lib.list_books())
        1
        """
        return [str(book) for book in self.books]


# In[81]:


lib = Library()

# Add books of different types
print(lib.add_book("The Little Prince", 96, "Yellow", "Antoine de Saint-Exupéry"))
print(lib.add_book("Pride and Prejudice", 432, "White", "Jane Austen", book_type="paper", cover_type="hard"))
print(lib.add_book("Becoming", 400, "Blue", "Michelle Obama", book_type="audio", duration_min=1140))

# Find by ID
print(lib.find_by_id(2))      # Should print PaperBook details
print(lib.find_by_id(10))     # We haven't found the book

# Filter
print([b.name for b in lib.get_books_by_author("Jane Austen")])       # ['Pride and Prejudice']
print([b.name for b in lib.get_books_by_colour("blue")])              # ['Becoming']
print([b.name for b in lib.get_books_by_pages(96)])                   # ['The Little Prince']

# Delete by ID
print(lib.delete_book_by_id(1))  # Deletes "The Little Prince"
print(lib.delete_book_by_id(99)) # Book not found

# Delete by page number
print(lib.delete_books_by_pages(400))  # Deletes "Becoming"

# List remaining books
print(lib.list_books())  # Should show just "Pride and Prejudice"


# In[ ]:




