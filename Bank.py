import json
import random
import string
from pathlib import Path


class Bank:
    database='data.json'
    data=[]

    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.loads(fs.read())
        else:
            print("No such file exists. ")
    except Exception as err:
        print(f"An error occured as {err}.")


    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))


    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters, k=3)
        num=random.choices(string.digits, k=3)
        spchar=random.choices('!@#$%^&*',k=1)
        id=alpha+num+spchar
        random.shuffle(id)
        return "".join(id)


    def createaccount(self):
        info={
            "name":input("Enter your name: "),
            "age":int(input("Enter your age: ")),
            "email":input("Enter your email: "),
            "pin":int(input("Enter 4 number pin: ")),
            "accountno": Bank.__accountgenerate(),
            "balance":0
        }
        if info['age']<18 or len(str(info['pin']))!=4:
            print("Sorry you cannot create your account.")
        else:
            print("Account has been Created Successfully.")
            for i in info:
                print(f"{i}:{info[i]}")
            print("Please notedown your Account Number")

            Bank.data.append(info)

            Bank.__update()


    def depositmoney(self):
        accnumber = input("Enter your account Number: ")
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i['accountno'] == accnumber and i['pin'] == pin]

        if userdata==False:
            print("Sorry no user found.")
        else:
            amount = int(input("Enter the amount for deposit: "))
            if amount>10000 or amount<0:
                print("Sorry the amount is too much you can deposit below 10000 and above 0.")
            else:
                userdata[0]["balance"]+=amount
                Bank.__update()
                print("Amount deposited Successfully.")


    def withdrawmoney(self):
        accnumber = input("Enter your account Number: ")
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i['accountno'] == accnumber and i['pin'] == pin]

        if userdata==False:
            print("Sorry no user found.")
        else:
            amount = int(input("Enter the amount for withdraw: "))
            if userdata[0]['balance']<amount:
                print("Sorry you don't have that much money.")
            
            else:

                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdraw successfully.")

    def showdetails(self):
        accnumber = input("Enter your account Number: ")
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i['accountno'] == accnumber and i['pin'] == pin]
        print ("Your information are \n\n\n")
        for i in userdata[0]:
            print(f"{i}:{userdata[0][i]}")

    
    def updatedetails(self):
        accnumber = input("Enter your account Number: ")
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i['accountno'] == accnumber and i['pin'] == pin]

        if userdata==False:
            print("Sorry no user found.")
        
        else:
            print("You cannot change the age, account number and balance")

            print("Fill the detaild for change or leave if no change")

            newdata= {
                "name":input("Enter your new name or press enter to skip: "),
                "email":input("Enter your new email or press enter to skip: "),
                "pin":input("Enter new pin or press enter to skip: ")
            }

            if newdata["name"]=="":
                newdata["name"]==userdata[0]['name']
            if newdata["email"]=="":
                newdata["email"]==userdata[0]['email']
            if newdata["pin"]=="":
                newdata["pin"]==userdata[0]['pin']
            else:
                newdata["pin"] = int(newdata["pin"])

            newdata['age']=userdata[0]['age']  
            newdata['accountno']=userdata[0]['accountno']
            newdata['balance']=userdata[0]['balance']

            for i in newdata:
                if newdata[i]==userdata[0][i]:
                    continue
                else:
                    userdata[0][i]=newdata[i]

            Bank.__update()
            print("Details updated successfully.")


    def delete(self):
        accnumber = input("Enter your account Number: ")
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i['accountno'] == accnumber and i['pin'] == pin]

        if userdata==False:
            print("Sorry no user found.")

        else:
            check=input("press y if you actually want to delete the account or press n")
            if check=='n' or check=='N':
                print("Bypassed")
            else:
                index=Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted successfully ")
                Bank.__update()

              

user= Bank()
print("Press 1 for Creating an Account.")
print("Press 2 for Depositing the money in the Bank.")
print("Press 3 for Withdrawing the money.")
print("Press 4 for Details.")
print("Press 5 for Updating the details.")
print("Press 6 for Deleting your Account.")

check = int(input("Tell your response :- "))

if check == 1:
    user.createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.delete()