nimi = input("Mis on sinu nimi: ")
print(f"Tere, {nimi}!")
elukoht = input("Mis on sinu elukoht?: ")
if elukoht == "Saaremaa":
    print("Saaremaa, kena koht!")

vanus = int(input("Kui vana sa oled? "))
if vanus < 18:
    print("Oled liiga noor, et autot juhtida.")
elif vanus == 18:
    print("Õnnitlused, sa oled täisealine!")
else:
    print("Sa võid autot juhtida.")