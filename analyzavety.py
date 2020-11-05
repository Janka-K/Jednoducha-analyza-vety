##ZADÁNÍ
#
#Vytvořte následující program, schopný jednoduché statistické analýzy zadaného #textu.
#
#Do programu uložte vybranou větu, rčení nebo přísloví. Například: "Programátor #se zasekne ve sprše, protože instrukce na šampónu byly: namydlit, omýt, opakovat.#" Po spuštění program větu zobrazí. Následně se provede a také vypíše analýza #těchto počtů:
#
#počet samohlásek, počet souhlásek, počet ostatních znaků počet slov (řešte podle #mezer - slov bude +1) celkový počet znaků ve větě Tip 1: Pokud budete používat #podprogramy, potom proměnné, obsahující seznam možných samohlásek (string) a #seznam možných souhlásek (string) založte v programu jako globální proměnné #(narozdíl od ostatních proměnných).
#
#Tip 2: Počet ostatních znaků a celkový počet znaků určitě není potřeba počítat #jednotlivě.
#
#Tip 3: Použitím stringové metody .Contains(znak) ušetříte jeden cyklus
#
#Tip 4: Použitím stringové metody .ToLower() si ušetříte práci s případnými #velkými písmeny
#
#Bonusové řešení: Ke globálním proměnným přidejte celý seznam vět (stringové pole #obsahující 5-10 vět). Vždy po stisknutí nějaké klávesy se vylosuje jedno z #uložených přísloví a k němu jeho statistika...

programator = "Programátor se zasekne ve sprše, protože instrukce na šampónu byly: namydlit, omýt, opakovat."

samohlasky = ["a","á","e","é","i","í","o","ó","u","ú"]

souhlasky = ["b", "c", "č", "d", "ď", "f", "g", "h", "j", "k", "l", "m", "n", "ň", "p", "r", "ř", "s", "š", "t", "ť", "v", "z", "ž", "ch"]

print(f"<<<{programator}>>>\n")

pocet_samohlasek = 0
pocet_souhlasek = 0 
pocet_ostatnich = 0
pocet_slov = 1

for pismeno in programator.lower():
  if pismeno in samohlasky:
    pocet_samohlasek +=1
  elif pismeno in souhlasky:
    pocet_souhlasek +=1
  elif pismeno.endswith(" "):
    pocet_slov +=1
  else: 
    pocet_ostatnich +=1
print(f"Pocet samohlasek ve vete je: {pocet_samohlasek}\nPocet souhlasek ve vete je: {pocet_souhlasek}\nPocet ostatnich znaku ve vete je: {pocet_ostatnich}\nPocet vsech vsech znaku ve vete je: {pocet_samohlasek + pocet_souhlasek + pocet_ostatnich}\nPocet slov ve vete je: {pocet_slov}")





