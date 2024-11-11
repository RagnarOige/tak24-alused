a = float(input("Sisesta esimene külg: "))
b = float(input("Sisesta teine külg: "))
c = float(input("Sisesta kolmas külg: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Kolmnurk on võrdkülgne.")
    elif a == b or a == c or b == c:
        print("Kolmnurk on võrdhaarne.")
    else:
        print("Kolmnurk on erikülgne.")
else:
    print("Selline kolmnurk ei saa eksisteerida.")