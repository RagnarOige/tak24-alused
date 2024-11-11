aasta = int(input("Sisesta positiivne täisarv (aasta): "))

if (aasta % 400 == 0) or (aasta % 4 == 0 and aasta % 100 != 0):
    print(f"{aasta} on liigaasta.")
else:
    print(f"{aasta} on lihtaasta.")
