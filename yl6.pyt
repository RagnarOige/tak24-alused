
arv1 = float(input("Sisesta esimene arv: "))
arv2 = float(input("Sisesta teine arv: "))
arv3 = float(input("Sisesta kolmas arv: "))


if arv1 >= arv2 and arv1 >= arv3:
    maksimaalne = arv1
elif arv2 >= arv1 and arv2 >= arv3:
    maksimaalne = arv2
else:
    maksimaalne = arv3


print(f"Suurim arv on: {maksimaalne}")
