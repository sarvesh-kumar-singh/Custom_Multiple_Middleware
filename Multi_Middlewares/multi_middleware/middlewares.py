from django.shortcuts import HttpResponse
class BrotherMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("One Time Brother Initialization !")

    def __call__(self,request):
        print("This Is Brother before Views!!")
        response=self.get_response(request)
        print("This Is Brother After Views!")
        return response
    


    
class FatherMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("One Time  Father Initialization !")

    def __call__(self,request):
        print("This Is Father before Views!!")
        response=self.get_response(request)
        # response=HttpResponse("Chal Nikal Lo!") if response from Father Then this Code will Use!!!
        print("This Is Father After Views!")
        return response
    


class MotherMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("One Time Mother Initialization !")

    def __call__(self,request):
        print("This Is Mother before Views!!")
        response=self.get_response(request)
        print("This Is Mother After Views!")
        return response