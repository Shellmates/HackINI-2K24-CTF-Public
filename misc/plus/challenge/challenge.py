#!/usr/bin/python3

secret="shellmates{AV01d_F0RM4T_$TrIng_MISTaKE$_1N_PYth0N!!!}"

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
