from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from render.models import Operation
from render.serializers import OperationSerializer
from rest_framework.views import APIView
# import openai
# import os


# openai.api_key =  os.getenv("OPENAI_API_KEY")


# def ai_answer(prompt=""):
#     response = openai.Completion.create(
#         model="text-davinci-002",
#         prompt=prompt,
#         temperature=1.2,
#         max_tokens=30,
#         echo=False
#     )
#     return (response.choices[0]['text'])

class Arithmetic(APIView):
    # def get(self, request, format=None):
    #     ans = Operation.objects.all()
    #     serializer = OperationSerializer(ans, many=True)
    #     return Response(serializer.data)
    def get(self, request, format=None):
        return Response({"slackUsername": "anthonyvictor385",
                     "backend": True,
                     "age": 23,
                     "bio": "An AI enthusiast with interest in backend"})
    
    
    def post(self, request, format=None):
        serializer = OperationSerializer(data=request.data)
        data = {}
        result = 0
        if serializer.is_valid():
                calculate = serializer.save()
                data["slackUsername"] = "anthonyvictor385"
                alist = calculate.operation_type.split()
                if "addition" in alist or "sum" in alist or "add" in alist:
                    result = calculate.x + calculate.y
                elif "subtraction" in alist or "minus" in alist or "subtract" in alist or "difference" in alist:
                    result = calculate.x - calculate.y
                elif "multiplication" in alist or "multiply" in alist or "product" in alist or "times" in alist:
                    result = calculate.x * calculate.y
                # else:
                #     result=ai_answer(calculate.operation_type)
                data['result'] = result
                data['operattion_type'] = calculate.operation_type          
        
        else:
            data = serializer.errors
            
        return Response(data, status=status.HTTP_201_CREATED)   




    
    
            