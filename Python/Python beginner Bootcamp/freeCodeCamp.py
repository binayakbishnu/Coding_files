# from math import *

# # mad libs game
# # use random words from  user to enter into pre-written stories
# colour = input("Enter a colour: ")
# noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")
# print(f"Roses are {colour}")
# print(f"{noun.capitalize()} are blue")
# print(f"I love {celebrity}")

# # List copying
# w = [1,6,2,9,4]
# x = w
# y = w.copy()
# z = list(x)
# a = w[:]
# x[1] = "x"
# print(x)
# y[2] = "y"
# print(x)
# z[3] = "z"
# print(x)
# a[4] = "a"
# print(x)

# w = [1,6,2,9,4]
# l = list(w)
# l.sort()
# l.sort(reverse=True)
# print(l)
# print(sorted(l))
# print(sorted(l,reverse=True))

# d = {
#     "Jan":"January",
#     "Feb":"February",
# }
# print(d["Mar"]) # returns error
# print(d.get("Mar")) # return none
# print(d.get("Apr","Not present")) # customise default output

# # Guessing game
# secret_word = "girrafe"
# guesses=""
# while guesses != secret_word:
#     guesses = input("Enter your guess: ")
# print("Good one!")

# # Error handling with original error msg
# try:
#     10/0
# except ZeroDivisionError as err:
#     print(err)

# import math
# print(dir(math))

# import docx

# emp_file = open("Z:\Coding\Python\Python Bootcamp\employees.txt", "r")

# # print(emp_file.readable())

# # print(emp_file.read())

# # print()
# # print(emp_file.readline())
# # print(emp_file.readline())

# # print(emp_file.readlines())
# # print(emp_file.readlines()[1])

# for employee in emp_file.readlines():
#     print(employee)

# emp_file.close()

# emp_file = open("Z:\Coding\Python\Python Bootcamp\employees.txt", "a")  #append mode
# emp_file.write("Toby - Human Resources")
# emp_file.write("\nKelly - Customer Service")
# emp_file.close()

# emp_file = open("Z:\Coding\Python\Python Bootcamp\employees.txt", "w")
# # overwrites
# emp_file.close()

# emp_file = open("Z:\Coding\Python\Python Bootcamp\employees2.txt", "w")
# # new file created
# emp_file.close()

# emp_file = open("Z:\Coding\Python\Python Bootcamp\employees2.html", "w")
# # new html file created
# emp_file.close()

# MCQ
# class Question:
#     def __init__(self, prompt, answer):
#         self.prompt = prompt
#         self.answer = answer

# questions_prompts = [
#     "What colour are apples?\n(a) Red   (b)Purple   (c)Orange\n\n",
#     "What colour are bananas?\n(a) Teal   (b)Magenta   (c)Yellow\n\n",
#     "What colour are strawberries?\n(a) Yellow   (b)Red   (c)Blue\n\n"
# ]

# questions = [
#     Question(questions_prompts[0],"a"),
#     Question(questions_prompts[1],"c"),
#     Question(questions_prompts[2],"b")
# ]

# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1

#     print(f"Score: {score}/{len(questions)}")

# run_test(questions)

# class inheritance
class Chef:
    def make_chicken(self):
        print("Chef makes chicken")
        
    def make_salad(self):
        print("Chef makes salad")
    
    def make_special_dish(self):
        print("Chef makes bbq")

class ChineseChef(Chef):
    def make_fried_rice(self):
        print("Chef makes fried rice")

    def make_special_dish(self):
        print("Chef makes orange chicken")

myChef = ChineseChef()
myChef.make_chicken()
myChef.make_special_dish()

