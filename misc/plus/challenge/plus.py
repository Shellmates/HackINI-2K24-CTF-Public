#!/usr/bin/python3

secret="shellmates{F4ke_fL4g}"

class Plus:
    def print_plus(self):
        print("WELCOME to the most secure + printer")
        self.plus=input("give me how many + you want to be printed on the screen : ")
        text="printing {self.plus} +'s : \n{:+^"+self.plus+"}"
        print(text.format("",self=self))

a=Plus()
try:
   a.print_plus()
except:
   print('an error has occured ... \n')
