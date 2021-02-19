import requests

nothing = 12345
for i in range(400):
    response = requests.get(f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}")
    nothing = response.text.split(" ")[-1]
    print(i, response.text)