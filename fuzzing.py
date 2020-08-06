import requests
"""Fuzzing, sisteme beklenmedik, yarı geçerli, 
sıralı verilerin gönderimi gibi yöntemlerle sistemin 
iç yapısındaki hataları bulmayı hedefleyen Kapalı-Kutu 
yazılım test etme yöntemi. """
file = open("fuzzing.txt", "r")
content = file.read()
file.close()
header = {"Cookie": ""}
for i in content.split("\n"):
    print(i)
    url = "http://10.10.10.10"+str(i)
    result = requests.get(url=url, headers=header)
    if "200" in str(result.status_code):
        print("result and index exists.",i)
    else:
        print("result and index doesn't exists.",i)
