base_str = "pc/def/map"

result = ""
for char in base_str:
    result += chr(ord(char) + 2)

print(result.replace('"', ' ').replace('{', 'a').replace('|', 'b').replace('0', '.').replace('*', '(').replace(')', "'").replace('+', ')'))