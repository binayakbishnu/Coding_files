# String formatting
# print("There are " + str(30) + " days in April")
# print(f"There are {30} days in April")
# print("There are {} days in April".format(30))
# print(f"There are {20*24*60*60} seconds in 20 days")

# i=0
# while i<5:
#     input()
#     i+=1

# Exception handling
# s = int(input())
# print(s+20) #ValueError shown for hello
# try:
#     s = int(input())
#     print(s+20)
# except ValueError:
#     print("Give a number")
# l = [12,13,93]
# try:
#     print(l[4])
# except:
#     print("Index problem")

# import logging

# countdown app
# import datetime

# deadline = input("Enter goal-deadline: ").split("-")

# deadline_goal = deadline[0]
# input_deadline_date = deadline[1]


# deadline_date = datetime.datetime.strptime(input_deadline_date, "%d.%m.%y")
# print(deadline_goal.capitalize() + " by",deadline_date)
# current_date = datetime.datetime.today()
# print("Today is:",current_date)

# difference = deadline_date - current_date
# print("Days left:",difference.days)
# print("Hours left: {}".format(round(difference.seconds/3600,2)))

# working with excel
# import openpyxl

# inv_file = openpyxl.load_workbook("Z:\Coding\Python\Python Bootcamp\inventory.xlsx")
# sheet = inv_file["Sheet1"]

# prod_per_sup = {} # dict
# tvalue_per_sup = {}
# inv_less10 = {}

# for row in range(2, sheet.max_row + 1):
#     sup_name = sheet.cell(row, 4)
#     # ^^will take in info of cell and not extract value
#     sup_name = sheet.cell(row, 4).value
#     # print(sup_name)
    
#     # products per supplier
#     if sup_name not in prod_per_sup:
#         print("Adding...")
#         prod_per_sup[sup_name] = 1
    
#     elif sup_name in prod_per_sup:
#         prod_per_sup[sup_name] += 1

#     # total value of inventory per supplier
#     # sup_name taken above
#     inv_amount = sheet.cell(row, 2).value
#     price = sheet.cell(row, 3).value
    
#     if sup_name not in tvalue_per_sup:
#         print("Adding...")
#         tvalue_per_sup[sup_name] = inv_amount * price
    
#     elif sup_name in tvalue_per_sup:
#         tvalue_per_sup[sup_name] += inv_amount * price

#     # inventory less than 10
#     # inv_amount taken above
#     prod_no = int(sheet.cell(row,1).value)
#     if inv_amount < 10:
#         inv_less10[prod_no] = int(inv_amount)

#     # creating new column python to excel
#     total_price = sheet.cell(row, 5) # no value
#     total_price.value = inv_amount * price
    
# print(prod_per_sup)
# print(tvalue_per_sup)
# print(inv_less10)
# # to push into new file
# inv_file.save("inventory.xlsx")

# class object
# class User:
#     def __init__(self,user_email,user_name,user_password,user_jobtitle):
#         self.email = user_email
#         self.name = user_name
#         self.password = user_password
#         self.curr_jobtitle = user_jobtitle

#     def print_info(self):
#         print(f"{self.name}; {self.email}; {self.password}; {self.curr_jobtitle}")

#     def change_password(self,new_password):
#         self.password = new_password

#     def change_jobtitle(self, new_jobtitle):
#         self.curr_jobtitle = new_jobtitle

# user1 = User("bishnu.binayak12@gmail.com","Binayak","Aen%40","Intern")
# user1.print_info()
# user1.change_jobtitle("Junior Developer")
# user1.print_info()

# API req to GitLab
