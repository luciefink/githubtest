# 1 Řetězce jako sekvence
# Uložte si v Python konzoli do proměnné jmeno svoje celé jméno a nechte vypsat jeho třetí, pátý a sedmý znak. Vyzkoušejte, co se stane, když budete chtít znak na pozici, která překračuje délku řetězce.
# jmeno = 'Lucie Finková'
# jmeno[2]
# jmeno[4]
# jmeno[6]

# Upravte program registrace.py tak, že bude kromě uživatelského jména chtít také e-mailovou adresu. Ověřte, že adresa je v platném formátu, tedy že obsahuje zavináč, tečku a má alespoň pět znaků.

# heslo = input('Zadej heslo: ')
# heslo_kontrola = input('Zadej znovu heslo pro ověření: ')
# if heslo != heslo_kontrola:
#     print('Kontrolní heslo není stejné. Zadejte znovu pro kontrolu.')
# if len(heslo) > 8:
#     print('Heslo je bezpečné.')
# elif len(heslo) <= 8:
#     print('Heslo není bezpečné, zadejte více než 8 znaků.')


# email = input('Zadej emailovou adresu: ')
# if '@' not in email or '.' not in email or len(email) < 5:
#     print('Spatně zadaný tvar emailu.')
# else:
#     print('Spravně zadaný email.')

    
    # 1 Seznam hodnocení
# Mějme seznam hodnocení divadelní hry Plyšáci na útěku, který vypadá takto:

hodnoceni = [7, 9, 6, 7, 9, 8]
# Vytvořte program, který projde tento seznam a vypíše každé hodnocení na nový řádek.
# for h in hodnoceni:
#     print(h)
# Upravte program tak, aby vypisoval výstup v tomto formátu
# 7/10
# 9/10
# 6/10
# 7/10
# 9/10
# 8/10

# for h in hodnoceni:
#     print(h,'/10', sep='')

# 3 Složitější seznam
# Založte si program cykly02.py a použijte v něm následující seznam měsíců v roce, Všimněte si, že je to seznam seznamů.
mesice = [
    ["leden", 31],
    ["únor", 28],
    ["březen", 31],
    ["duben", 30],
    ["květen", 31],
    ["červen", 30],
    ["červenec", 31],
    ["srpen", 31],
    ["září", 30],
    ["říjen", 31],
    ["listopad", 30],
    ["prosinec", 31],
]
# Pomocí cyklu projděte tento seznam a vypište na výstup názvy jednotlivých měsíců.
# Pomocí dalšího cyklu vypište na výstup počty dní v jednotlivých měsících.

# for nazev in mesice:
#   print(nazev[0])

# for den in mesice:
#   print(den[1])

# 2 Procházení seznamu
# Založte si program hesla.py a na jeho začátek vložte následující kód obsahující seznam hesel pro přihlášení do nějakého systému
hesla = [
    "xyz101",
    "punťa",
    "razor-blade",
    "1234",
    "12011986",
    "martin111",
    "trhnisi",
    "hokuspokus",
    "jeník15",
    "kristus-te-spasi",
    "beruška",
    "strčprstskrzkrk",
]
# Pomocí cyklu vypište všechny hesla na obrazovku, každé na jeden řádek.
# for heslo in hesla:
#     print(heslo)
# Upravte váš program tak, aby vypisoval jen bezpečná hesla, tedy taková, jež jsou delší než 8 znaků.
# for heslo in hesla:
#     if len(heslo) > 8:
#       print(heslo)
# Upravte váš program tak, aby vypisoval jen ta hesla, jež obsahují znak pomlčky ‘-’.
for heslo in hesla:
    if '-' in heslo:
      print(heslo)