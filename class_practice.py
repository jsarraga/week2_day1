class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
class Student(Person):
    def __init__(self, first_name, last_name, gpa, classes = []):
        super().__init__(first_name, last_name)
        self.gpa = gpa
        self.classes = classes
    
    def update_gpa(self, gpa):
        self.gpa = gpa


class Teacher(Person):
    def __init__(self, first_name, last_name, tenure, subject):
        super().__init__(first_name, last_name)
        self.tenure = tenure
        self.subject = subject
    
    def add_students(self, students):
        self.students = students 

class Food:
    def __init__(self, name, healthy, price):
        self.name = name
        self.healthy = healthy
        self.price = price

class ShoppingList:
    def __init__(self, shopping_list=[]):
        self.shopping_list = shopping_list

    def add_to_list(self, name, healthy, price):
        food = Food(name, healthy, price)
        self.shopping_list.append(food)

    def view_list(self):
        total = 0
        for item in self.shopping_list:
            print(item.name, item.price)
            total += item.price
        print("Total Cost: ${}".format(total)) 
    
    def healthy_list(self):
        total = 0
        for item in self.shopping_list:
            if item.healthy == True:
                total += 1
            elif item.healthy == False:
                total -= 1
        if total > 0:
            print("You skinny bitch!")
        elif total == 0:
            print("You have a pretty normal diet bro")
        else:
            print("You are a fatty!")

            



# justin = Student('Justin', 'Sarraga', 4.0, ['web development'])
# print(justin.first_name)
# print(justin.gpa)
# justin.update_gpa(2.3)
# print(justin.gpa)

apple = Food('apple',True, 1.0)
# print(apple.name, apple.healthy, apple.price)
foodlist = ShoppingList()
foodlist.add_to_list('apple', True, 1.0)
foodlist.add_to_list('bacon', False, 7.0)
# foodlist.add_to_list('steak', False, 10.0)
foodlist.add_to_list('carrot', True, 2.0)
# foodlist.add_to_list('twinkies', False, 5.0)
foodlist.view_list()
foodlist.healthy_list()
