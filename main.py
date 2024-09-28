# Класс Animal (Животное)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} ({self.species})"

# Класс Employee (Сотрудник)
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __repr__(self):
        return f"{self.name} ({self.position})"

# Класс Zoo (Зоопарк) - использует композицию
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []  # Список для животных
        self.employees = []  # Список для сотрудников

    # Метод для добавления животного
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} был добавлен в зоопарк {self.zoo_name}.")

    # Метод для добавления сотрудника
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} был нанят на работу в зоопарк {self.zoo_name}.")

    # Метод для отображения всех животных
    def display_animals(self):
        if not self.animals:
            print(f"В зоопарке {self.zoo_name} пока нет животных.")
        else:
            print(f"Животные в зоопарке {self.zoo_name}:")
            for animal in self.animals:
                print(animal)

    # Метод для отображения всех сотрудников
    def display_employees(self):
        if not self.employees:
            print(f"В зоопарке {self.zoo_name} пока нет сотрудников.")
        else:
            print(f"Сотрудники зоопарка {self.zoo_name}:")
            for employee in self.employees:
                print(employee)

# Пример использования композиции

# Создаем зоопарк
my_zoo = Zoo("Central Zoo")

# Создаем животных
elephant = Animal("Dumbo", "Elephant")
lion = Animal("Simba", "Lion")

# Создаем сотрудников
keeper = Employee("Alice", "Animal Keeper")
veterinarian = Employee("Dr. Bob", "Veterinarian")

# Добавляем животных в зоопарк
my_zoo.add_animal(elephant)
my_zoo.add_animal(lion)

# Добавляем сотрудников в зоопарк
my_zoo.add_employee(keeper)
my_zoo.add_employee(veterinarian)

# Отображаем всех животных и сотрудников
my_zoo.display_animals()
my_zoo.display_employees()
