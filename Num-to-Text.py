def zahlen_zu_text(zahlen):
    text = ""
    for zahl in zahlen:
        if zahl == 0:
            text += " "
        else:
            buchstabe = chr(zahl + 64).lower()
            text += buchstabe
    return text

zahlen = input("Enter the numbers here (comma separated): ")
zahlen_liste = [int(x) for x in zahlen.split(",")]
ergebnis = zahlen_zu_text(zahlen_liste)
print("The text is:", ergebnis)
