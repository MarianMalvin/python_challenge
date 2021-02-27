nothing = 90052

# while True:
#     with open(f"./channel/{nothing}.txt", "r") as file:
#         text = file.read()
#         print(text)
#         nothing = text.split()[-1]

import zipfile

comments = []
while True:
    try:
        with zipfile.ZipFile("./channels.zip", "r") as zip_file:
            text = zip_file.read(f"{nothing}.txt")
            comment = zip_file.getinfo(f"{nothing}.txt").comment
            comments.append(comment.decode())
            nothing = text.decode().split()[-1]
    except:
        break

print(*comments)
