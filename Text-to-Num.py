def text_zu_zahlen(text):
    text = text.upper()
    zahlen = []
    for char in text:
        if char.isalpha():
            zahl = ord(char) - 64
            zahlen.append(zahl)
        elif char.isspace():
            zahlen.append(0)
    return zahlen

text = input("Enter text here: ")
ergebnis = text_zu_zahlen(text)
print("The numbers are:", ergebnis)
