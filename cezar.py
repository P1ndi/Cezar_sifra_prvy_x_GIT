#cezar mistra sifra
rot = int(input("zadaj kluc: "))
action = input("chces [s]ifrovat alebo [d]esifrovat: ")
data = input("Zadaj text: ")

if action == "s" or action == "sifrovat":
    text = ""
    for char in data:
        char_ord = ord(char)
        if 32 <= char_ord <= 126:
            char_ord -= 32
            char_ord += rot
            char_ord = char_ord % 94
            char_ord += 32
            text += chr(char_ord)
        else:
            text += char
    print("sifra: '{}'".format(text))
elif action == "d" or action == "desifrovat":
    text = ""
    for char in data:
        char_ord = ord(char)
        if 32 <= char_ord <= 126:
            char_ord -= 32
            char_ord -= rot
            char_ord = char_ord % 94
            char_ord += 32
            text += chr(char_ord)
        else:
            text += char
    print("text: '{}".format(text))
else:
    print("Niecoas neprebehlo v poriadku")
