"""
A decorator is a function that takes another functin as an argument
add functionality and returns another function without altering the 
source code of the original function(DNA)
"""


# def give_fly_powers(person):
#     def new_person():
#         print("fly powers given")
#         return person()
#     return new_person

# @give_fly_powers
# def person():
#     print("Laser powers")
#     print("People skills")

# person()



# def provide_logger(func):
#     def given_logger():
#         logger = True
#         func()
    
#     return given_logger


# @provide_logger
# def skills():
#     if logger == True:
#         print("Logger given")
#     print("People Skills")

# skills()


# Global skills for a person
skills = ["seeing", 'listening']
skills_one = []
skills_two = []

skills_one.extend(skills)
skills_two.extend(skills)



def add_skill(person):
    def new_person():
        pass


def person_one():
    skills_one.append("moving")
    print(f'Person One Skills: {skills_one}')
  


def person_two():
    skills_two.append("boxing")
    print(f'Person two Skills: {skills_two}')


person_one()
person_two()











