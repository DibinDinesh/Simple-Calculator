from django.shortcuts import render

# Create your views here.

from django.views.generic import View

from operations.forms import BmrForm,TemperatureForm


class AdditionView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"add.html")
    
    def post(self,request,*args,**kwargs):

        num1=request.POST.get("box1")
        num2=request.POST.get("box2")
        result=int(num1)+int(num2)
        print(result)
        return render(request,"add.html",{"data":result})
    
class SubtractionView(View):

        def get(self,request,*args,**kwargs):
        
            return render(request,"sub.html")

        def post(self,request,*args,**kwargs):

            num1=request.POST.get("box1")
            num2=request.POST.get("box2")
            result=int(num1)-int(num2)
            print(result)
            return render(request,"sub.html",{"data":result})


class MultiplicationView(View):
    
    def get(self,request,*args,**kwargs):
        return render(request,"mul.html")

    def post(self,request,*args,**kwargs):

        num1=request.POST.get("box1")
        num2=request.POST.get("box2")
        result=int(num1)*int(num2)
        print(result)
        return render(request,"mul.html",{"data":result})

class Factorialview(View):

    def get(self,request,*args,**kwargs):

        return render(request,"factorial.html")
    
    def post(self,request,*args,**kwargs):

        num=int(request.POST.get("box"))

        result=1
        for i in range(1,(num+1)):
            result=result*i

        return render(request,"factorial.html",{"data":result})
    
class PrimeNumberView(View):

    def get(self,request,*args,**kwargs):
        return render(request,"prime_num.html")
    
    def post(self,request,*args,**kwargs):

        num=int(request.POST.get("box"))

        is_prime=True
        for i in range(2,num):
            if num % i==0:
                is_prime=False
                break

        return render(request,"prime_num.html",{"data":is_prime})
    
class BmiView(View):

    def get(self,request,*args,**kwargs):
        return render(request,"bmi.html")
    
    def post(self,request,*args,**kwargs):

        height=int(request.POST.get("hbox"))
        weight=int(request.POST.get("wbox"))
        height_in_meter=height/100
        bmi=weight/(height_in_meter)**2
        bmi=round(bmi,2)

        return render(request,"bmi.html",{"data":bmi})
    

from operations.forms import RegistrationForm

class SighUpView(View):

    def get(self,request,*args,**kwargs):

        form=RegistrationForm()
    
        return render(request,"registration.html",{"form":form})

    

class BmrView(View):
    def get(self,request,*args,**kwargs):

        form_instance=BmrForm() #created a instance /object of BmrForm

        return render(request,"bmr.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_instance=BmrForm(request.POST)

        if form_instance.is_valid():

            print(form_instance.cleaned_data)

            validat_data=form_instance.cleaned_data

            height=validat_data.get("height")

            weight=validat_dataget("weight")

            age=validat_data.get("age")

            gender=validat_data.get("gender")

            activity_level=validat_data.get("activity_level")

            print(height,weight,age,gender,activity_level)

            return render(request,"bmr.html",{"form":form_instance})
        else:

            print("error")

            return render(request,"bmr.html",{"form":form_instance})


        bmr=0

        if (gender=="male"):

            bmr= (10*weight) + (6.25*height) - (5*age)+ 5
        
        elif gender=="female":

            bmr=(10*weight) + (6.25*height) - (5*age)+ 161

        form=BmrForm()

        calories=0

        if activity_level==1:
            calories=bmr*1.2
        
        elif activity_level==2:
            calories=bmr*1.375

        elif activity_level==3:
            calories=bmr*1.55

        elif activity_level==4:
            calories=bmr*1.725

        elif activity_level==5:
            calories=bmr*1.9

        print(bmr)

        print(f"number of calories you need in order to maintain your current weight",calories)
        weight_loss_per_month=int(request.POST.get("weight_loss_per_month"))

        target_weight=int(request.POST.get("target_weight"))

        weight_loss_calorie_per_kg=7700

        activity_factor=1.55

        bmr=bmr*activity_factor

        total_weight_loss_calories=weight_loss_per_month*weight_loss_calorie_per_kg

        daily_calori_in_take=bmr-(total_weight_loss_calories/30)

        print(daily_calori_in_take)


        return render(request,"bmr.html",{"form":form})



class TemperatureView(View):

    def get(self,request,*args,**kwargs):

        form_instance=TemperatureForm()

        return render(request,"temp.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargss):

        form_instance=TemperatureForm(request.POST)

        if form_instance.is_valid():
            print("no errors")
            print(form_instance.cleaned_data)


        else:

            print("error")

        return render(request,"temp.html",{"form":form_instance})

