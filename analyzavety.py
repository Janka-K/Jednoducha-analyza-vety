
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





