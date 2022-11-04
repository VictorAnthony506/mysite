from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from render.models import Operation
from render.serializers import OperationSerializer
from rest_framework.views import APIView
import openai


openai.api_key = OPEN_AI_KEY


def ai_answer(prompt=""):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=1.2,
        max_tokens=30,
        echo=False
    )
    return int(response.choices[0]['text'].split()[-1])

class Arithmetic(APIView):
    # def get(self, request, format=None):
    #     ans = Operation.objects.all()
    #     serializer = OperationSerializer(ans, many=True)
    #     return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = OperationSerializer(data=request.data)
        data = {}
        result = 0
        if serializer.is_valid():
                calculate = serializer.save()
                data["slackUsername"] = "anthonyvictor385"
                if calculate.operation_type == "addition":
                    result = calculate.x + calculate.y
                elif calculate.operation_type == "subtraction":
                    result = calculate.x - calculate.y
                elif calculate.operation_type == "multiplication":
                    result = calculate.x * calculate.y
                else:
                    result=ai_answer(calculate.operation_type)
                data['result'] = result
                data['operattion_type'] = calculate.operation_type          
        
        else:
            data = serializer.errors
            
        return Response(data, status=status.HTTP_201_CREATED)   




    
    
            