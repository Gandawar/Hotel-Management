class Movie:
       
     def __init__(self,p=0,f=0,name='',address='',age=''):
         
         self.p=p
         self.f=f
         self.name=name
         self.address=address
         self.age=age
         
     def info(self):
       self.name=str(input("Enter your name  :"))
       self.address=str(input("Enter your address :"))
       self.age=int(input("Enter your age :"))
      
     def movie(self):
        
         print("1:shao--->100")
         print("2:kgf---->200")
         print("3:chichore---->100")
         print("4:Bahubali---->500")
         print("5:Exit")
         
         while(1):
            
            c=int(input("Enter your choice :"))
            
            if(c==1):
             b=int(input("Enter the person :"))
             self.p=b*100
             print("movie bill is :",self.p)
             
            elif(c==2):
             b=int(input("Enter the person :"))
             self.p=b*200
             print("movie bill is :",self.p)
             
            elif(c==3):
             b=int(input("Enter the person :"))
             select.p=b*100
             print("movie bill is :",self.p)
             
            elif(c==4):
             b=int(input("Enter the person :"))
             select.p=b*500
             print("movie bill is :",self.p)
             
            elif(c==5):
                 break;
            else : 
              print("plzz select movie..")
              
              print("movie bill is :",self.p,"\n")
      
     def food(self):
          
         print("1:pizza---->100")
         print("2:cofee---->50")
         print("3:sandwitch---->150")
         print("4:Tea---->20")
         print("5:Exit")          
        
         while(1):
             
             d=int(input("Enter your choice :"))
          
             if(d==1):
                 e=int(input("Enter the quantity :"))
                 self.f=100*e
                 print("Toatl rupess of foood is ",self.f)
                  
             elif(d==2):
                 e=int(input("Enter the quantity :"))
                 self.f=50*e
                 print("Toatl rupess of foood is ",self.f)
                  
             elif(d==3):
                 e=int(input("Enter the quantity :"))
                 self.f=150*e
                 print("Toatl rupess of foood is ",self.f)
                  
             elif(d==4):
                 e=int(input("Enter the quantity :"))
                 self.f=20*e
                 print("Toatl rupess of foood is ",self.f)
                  
             elif(d==5):
                   
                   break;
             
             else :
                 
                 print("Do not enter any food..")
                 
                 print("Toatl rupess of foood is ",self.f)
     
     def display(self):
    
        print("My name is :",self.name)
        print("My address is :",self.address)
        print("My age is :",self.age)
        print("Toatl rupess of foood is ",self.f)
        print("movie bill is :",self.p)
 
       
def main():
    
    a=Movie()
    
    while(1):
       print("1.Enter Customer data :")
       print("2.Display Customer data :")
       print("3.Select movie :")
       print("4:select food :")
       print("5:Exit :")
       
       b=int(input("Enter your choice :"))
       
       if (b==1):
         a.info()
         
       if (b==2):
         a.display()
         
       if (b==3):
         a.movie()
       
       if (b==4):
         a.food()
       
       if (b==5):
           break;
           
main()
       
       