class multiplefunctions():
    def OddEven():
        num=int(input("Enter a number : "))
        print("Enter a number : ",num)
        if(num%2==0):
            print(num,"is Even number") 
        else:
            print(num,"is Odd number")
    def AgeCategory():
        age=int(input("Enter your age: "))
        if(age<18):
            print("Children")
            Categ="Children"
        elif(age<35):
            print("Adult")
            Categ="Adult"
        elif(age<59):
            print("Citizen")
            Categ="Citizen"
        else:
            print("Senior Citizen")
            Categ="Senior Citizen"
        return Categ
    def BMI():
        BMI=float(input("Enter the BMI Index:"))
        print("Enter the BMI Index:", BMI)
              
        if(BMI<18.5):
            print("Underweight")
        elif(BMI<=24.9):
            print("Healthy Weight")
        elif(BMI<=29.9):
            print("Overweight")
        else:
            print("Very Overweight")
            
class SubfieldsInAI():
    def Subfields():
        print("Sub-fields in AI are:")
        AI_course = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        for course in AI_course:
            print(course)

class OddEven():
    def OddEven():
        num=int(input("Enter a number : "))
        print("Enter a number : ",num)
        if(num%2==0):
            print(num,"is Even number")
            
        else:
            print(num,"is Odd number")

class ElegiblityForMarriage():
    def Elegible():
        gender=input("Enter your Gender:")
        age=int(input("Enter your Age:"))
        if(gender=="Male"):
            if(age>=21):
                print("Your Gender:", gender)
                print("Your Age:", age)
                print("ELIGIBLE")
              
            else:
                print("Your Gender:", gender)
                print("Your Age:", age)
                print("NOT ELIGIBLE")
                
                
        elif(gender=="Female"):
            if(age>=18):
                print("Your Gender:", gender)
                print("Your Age:", age)
                print("ELIGIBLE")
            
            else:
                print("Your Gender:", gender)
                print("Your Age:", age)
                print("NOT ELIGIBLE")
               
                 
        else:
            print("Invalid Gender")

class FindPercent():
    def percentage():
        sub1=98
        sub2=87
        sub3=95
        sub4=95
        sub5=93
        total=sub1+sub2+sub3+sub4+sub5
        Perc=total/500*100
        print("Subject1=", sub1)
        print("Subject2=", sub2)
        print("Subject3=", sub3)
        print("Subject4=", sub4)
        print("Subject5=", sub5)
        print("Total :", total)
        print("Percentage :", Perc)

class triangle():
    def triangle():
        H=32
        B=34
        print("Height:", H)
        print("Breadth:", B)
        AT=(H*B)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:", AT)
        H1=2
        H2=4
        B1=4
        print("Height1:", H1)
        print("Height2:", H2)
        print("Breadth:", B1)
        PF=H1+H2+B1
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ", PF)