 
KROONIDE_EURO_KURSS = 15.6466


kroonid = float(input("Sisesta summa kroonides: "))


eurodesse = kroonid / KROONIDE_EURO_KURSS


eurodesse_umardatud = round(eurodesse, 2)


print(f"Summa eurodes: {eurodesse_umardatud} EUR")
