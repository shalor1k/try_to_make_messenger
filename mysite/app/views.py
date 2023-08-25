from django.shortcuts import render
from django.http import JsonResponse
from random import randint as random
from app.models import *
from django.views.decorators.csrf import csrf_exempt
import smtplib


client = []
event = None
client_send = []


def home(request):
    return render(request, "index.html")


@csrf_exempt
def api(request):
    global client, event, client_send

    if request.method == "POST":
        method = request.POST.get('method')

        if method is not None:
            if method == 'register':
                email = str(request.GET['email'])
                smtp = smtplib.SMTP("smtp.mail.ru", 587)
                smtp.starttls()
                smtp.login("rodion_art@mail.ru", "roart2003roart2405")
                code = random(10000, 90000)
                smtp.sendmail('rodion_art@mail.ru', f"{email}", f"Код подтверждения {code}")
                smtp.quit()
                response = {"response": "code", "code": code}

            elif method == 'confirm':
                email = str(request.POST.get('email'))
                password = str(request.POST.get('pass'))
                first_name = str(request.POST.get('first_name'))
                last_name = str(request.POST.get('last_name'))
                Account.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
                user = Account.objects.get(email=email)
                response = {"response": user.id}

            elif method == 'login':
                email = str(request.POST.get('email'))
                password = str(request.POST.get('pass'))
                user = Account.objects.get(email=email)
                if user.password == password:
                    response = {"response": user.id}
                else:
                    response = {"response": 'error', "error_code": 201}

        else:
            response = {'Response': 404}

    elif request.method == "GET":
        method = request.GET.get('method')

        if method is not None:
            if method == 'get_client_name':
                client_name = random(1000, 9000)
                if client_name in client:
                    client_name = random(1000, 9000)
                if str(client_name) not in str(client):
                    client.append(client_name)
                response = {"client_name": client_name}

            elif method == 'update':
                client_name = request.GET.get('client_name')
                array = {"client_name": client_name, "update": []}
                if event is not None:
                    if client_name not in client_send:
                        array['update'].append(event)
                        client_send.append(client_name)
                    if len(client) == len(client_send):
                        event = None
                        client_send = []
                response = array

            elif method == 'message':
                message = request.GET.get('message')
                user_id = request.GET.get('user_id')
                account = Account.objects.get(id=user_id)
                event = {"type": "message_now", "message": message, "peer_id": user_id,
                         "first_name": account.first_name, "last_name": account.last_name}
                # 'to' 'from' need to add event
                response = {"Response": 200}

            elif method == 'quit':
                client_name = int(request.GET.get('client_name'))
                for i in range(len(client)):
                    if client_name == client[i]:
                        del client[i]
                response = {"Response": 200}

        else:
            response = {'Response': 404}

    return JsonResponse(response)
# def api(request):
#     try:
#         method = str(request.GET['method'])
#         if method == "registr":
#             try:
#                 email = str(request.GET['email'])
#                 # smtp = smtplib.SMTP("smtp.mail.ru", 587)
#                 # smtp.starttls()
#                 print(1)
#                 # smtp.login("rodion_art@mail.ru", "ekLWdTmDNpY37uANE6EZ")
#                 print(2)
#                 code = random(10000, 99999)
#                 print(3)
#                 print(code)
#                 # smtp.sendmail('rodion_art@mail.ru', f"{email}", f"Код подтверждения для сайта Параллель {code}")
#                 print(4)
#                 # smtp.quit()
#                 print(5)
#                 response = {"response": "code", "code": code}
#                 print(6)
#
#             except Exception as e:
#                 response = {"response": "error", "error_code": 101}
#
#         elif method == "confirm":
#             try:
#                 response = str(request.GET['response'])
#                 if response == 'done':
#                     email = str(request.GET['email'])
#                     password = str(request.GET['pass'])
#                     first_name = str(request.GET['first_name'])
#                     last_name = str(request.GET['last_name'])
#                     Account.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
#
#                 response = {"response": "200"}
#
#             except Exception as e:
#                 response = {"response": 'error', "error_code": 102}
#
#         elif method == "login":
#             try:
#                 email = str(request.GET['email'])
#                 password = str(request.GET['pass'])
#                 user = Account.objects.get(email=email)
#                 if user.password == password:
#                     response = {"response": "200"}
#                 else:
#                     response = {"response": 'error', "error_code": 201}
#
#             except:
#                 response = {"response": 'error', "error_code": 103}
#
#     except:
#         response = {"response": 'error', "error_code": 100}
#
#     return JsonResponse(response)