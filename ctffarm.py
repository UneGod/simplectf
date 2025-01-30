import requests
import random
import string

# URL-адреса
ip = ''
registration_url = f"http://{ip}/registration"
login_url = f"http://{ip}/login"
give_coins_url = f"http://{ip}/profile/give/1368"

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_random_user():
    name = generate_random_string(8)
    email = generate_random_string(5) + "@example.com"
    password = generate_random_string(10)
    return {"name": name, "email": email, "password": password}

def register_and_send_coins():
    user = generate_random_user()
    
    with requests.Session() as s:
        registration_payload = {
            "name": user["name"],
            "email": user["email"],
            "password": user["password"]
        }
        registration_response = s.post(registration_url, data=registration_payload)
        
        if registration_response.status_code == 200:
            print(f"Пользователь {user['name']} ({user['email']}) успешно зарегистрирован.")
        else:
            print(f"Ошибка регистрации пользователя {user['name']}: {registration_response.text}")
            return
        
        login_payload = {
            "name": user["name"],
            "password": user["password"]
        }
        login_response = s.post(login_url, data=login_payload)
        
        give_coins_payload = {"cash": 5}
        give_coins_response = s.get(give_coins_url, params=give_coins_payload)
            
while True:
    register_and_send_coins()
