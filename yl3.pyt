
n = input("Sisesta täisarv vahemikus 1-9: ")


if n.isdigit() and 1 <= int(n) <= 9:
    
    nn = n + n  
    nnn = n + n + n  

    
    tulemus = int(n) + int(nn) + int(nnn)

   
    print(f"{n} + {nn} + {nnn} = {tulemus}")
else:
    print("Sisesta palun täisarv vahemikus 1-9.")
