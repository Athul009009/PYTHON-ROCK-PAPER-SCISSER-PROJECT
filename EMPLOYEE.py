# from datetime import datetime


class componey:
    componey="Google"
    
# @staticmethod 
# def time():
#     now=datetime.now()
#     current_time=now.strftime("%H;%M;%S")
#     print(f"AS OF TIME {current_time} THE DATA IS AS FOLLOWS!!")
    
    def profile(self):
        print(f"{self.a} IS A MEMBER OF {self.c} AND HIS/HER SALERY IS {self.b}")
        
        if self.c=="GOOGLE":
            f1=open("googleregister.txt","a")
            f1.write(f"NAME  :{self.a} \n SALERY    :{self.b}\n COMPONY :GOOGLE") 
        elif self.c=="TCS":
            f2=open("TCSregister.txt","a")
            f2.write(f"NAME  :{self.a} \n SALERY    :{self.b}\n COMPONY :TCS") 
        elif self.c=="AMAZON":
            f3=open("AMAZONregister.txt","a")
            f3.write(f"NAME  :{self.a} \n SALERY    :{self.b}\n COMPONY :AMAZON") 
        elif self.c=="WIPRO":
            f4=open("WIPROregister.txt","a")
            f4.write(f"NAME  :{self.a} \n SALERY    :{self.b}\n COMPONY :WIPRO") 
        elif self.c=="FACEBOOK":
            f5=open("FACEBOOKregister.txt","a")
            f5.write(f"NAME  :{self.a} \n SALERY    :{self.b}\n COMPONY :FACEBOOK") 
        elif self.c=="INFOSYS":
            f6=open("INFOSYSregister.txt","a")
            f6.write(f"NAME  :{self.a} \n SALERY    :{self.b}\n COMPONY :INFOSYS") 
        else:
            print("THE ENTERD COMPONEY IS NOT IN THE LIST IT WILL NOT BE SAVED IN THE REGISTERY")
        
        f=open("Register.txt","a")
        f.write(f"\n\nNAME  :{self.a}\nSALERY :{self.b}\nCOMPONEY   :{self.c} \n",end="\n")
        # f.time()
        f.close

athul=componey()
athul.a=input("enter your name    :")
athul.b=int(input("enter your salary  :"))
print("THE AVAIL COMPONYS ARE \n GOOGLE , TCS, WIPRO , AMAZON , INFOSIS , FACEBOOK ")
athul.c=input("enter the name of compony  :").upper()
athul.profile()
