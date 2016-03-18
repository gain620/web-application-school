from django.http import HttpResponse
from django.shortcuts import render_to_response

# create your views here


def hello(request):
    return HttpResponse('Hello world!')


def calculate(request, num1, sign, num2):
    n1 = int(num1)
    n2 = int(num2)
    result = 0

    if sign == '+':
        result = n1 + n2
    elif sign == '-':
        result = n1 - n2
    elif sign == '*':
        result = n1 * n2
    elif sign == '/':
        if n2 == 0:
            result = "can't divide by 0"
        else:
            result = n1 / n2

    return HttpResponse('' + num1 + ' ' + sign + ' ' + num2 + ' = ' + str(result))


def soccer(request, team):

    members = []

    if team == 'Barcelona':
        members.append('Messi')
        members.append('Neymar')
    elif team == 'ManUtd':
        members.append('Rooney')
        members.append('JS Park')
    else:
        members.append('Who')
        members.append('Are')
        members.append('You')


    return render_to_response('soccer.html', {'team':team, 'members':members})



