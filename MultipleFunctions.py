class mltifunction():
    def Agecategory():
        age=int(input("Enter the age:"))
        if(age<18):
            print("children")
            cate="children"
        elif(age<35):
            print("Adult")
            cate="Adult"
        elif(age<59):
            print("Citizen")
            cate="Citizen"
        else:
            print("Senior Citizen")
            cate="Senior Citizen"
        return cate
    
    def oddeven():
        num=int(input("Enter the number:"))
        if((num%2)==0):
            print("Even number")
            message=("Even number")
        else:
            print("Odd number")
            message=("Odd number")
        return message
          
        
    def BMI():
        BMI=int(input("Enter the BMI Index:"))
        if(BMI<18.5):
            print("Underweight")
            message=("Underweight")
        elif(BMI<25):
            print("Normal")
            message=("Normal")
        elif(BMI<30):
            print("Overweight")
            message=("Overweight")
        else:
            print("Very Overweight")
            message=("Very Overweight")
        return message
    
    def Eligible():
        Gender=str(input("Your Gender: "))
        Age=int(input("Your Age: "))
        if(Gender=="Male"):
            if(Age>=21):
                print("ELIGIBLE")
                message="ELIGIBLE"
            else:
                print("Not ELIGIBLE")
                message="Not ELIGIBLE"
        return message

        if(Gender=="Female"):
            if(Age>=18):
                print("ELIGIBLE")
                message="ELIGIBLE"
            else:
                print("Not ELIGIBLE")
                message="Not ELIGIBLE"
        return message