
def yhteenlasku(luku1, luku2):
    return print(f"Laskun tulos on: {luku1 + luku2}")

def vähennyslasku(luku1, luku2):
    return print(f"Laskun tulos on: {luku1 - luku2}")

def kertolasku(luku1, luku2):
    return print(f"Laskun tulos on: {luku1 * luku2}")

def jakolasku(luku1, luku2):
    if luku2 == 0:
        return print("Nollalla ei voi jakaa!")
    else:
        return print(f"Laskun tulos on: {luku1 / luku2}")    

def funktio(luku1, luku2, laskutoimitus):
    if laskutoimitus == "Yhteenlasku":
        return yhteenlasku(luku1, luku2)

    if laskutoimitus == "Vähennyslasku":
        return vähennyslasku(luku1, luku2)

    if laskutoimitus == "Kertolasku":
        return kertolasku(luku1,luku2)

    if laskutoimitus == "Jakolasku":
        return jakolasku(luku1, luku2)

    else:
        return print("Et antanut laskutoimitusta vaihtoehdoista.")

print("Tämä ohjelma laskee kahden kokonaisluvun yhteen-, vähennys-, kerto- ja jakolaskun.")

while True:
    luku1 = float(input("Anna ensimmäinen kokonaisluku: "))
    luku2 = float(input("Anna toinen kokonaisluku: "))
    laskutoimitus = input("Mikä laskutoimitus suoritetaan? Yhteenlasku, Vähennyslasku, Kertolasku vai Jakolasku?: ")

    if laskutoimitus == "Lopeta":
        break

    funktio(luku1, luku2, laskutoimitus)

     



