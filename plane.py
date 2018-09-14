"""
Programmet skriver, och tar höjd, hastighet och temperatur i m, km/h och Celcius som input från användaren.
Värdena användaren skriver in används för att skapa mått som är konverterade till feet, mph och Farenheit.
"""

höjd = input("Höjd över havet (meter): ") # Användaren matar in höjd
hastighet = input("Hastighet (km/h): ") # Användaren matar in hastighet
temperatur = input("Temperatur utanför flygplanet (Celcius): ") # Användaren matar in temperatur

konverterad_höjd = str(float(höjd) * 3.28084)
konverterad_hastighet = str(float(hastighet) * 0.62137)
konverterad_temperatur = str(float(temperatur) * (9 / 5 + 32))
# Konverterar värden som matats in till feet, MPH och Farenheit.
# Eftersom höjd, hastighet och temperatur är av typen int måste de först konverteras till sträng.

output1 = ("Höjd över havet (feet):" + " " + str(konverterad_höjd))
output2 = ("Hastighet (mph):" + " " + str(konverterad_hastighet))
output3 = ("Temperatur utanför flygplanet (Farenheit):" + " " + str(konverterad_temperatur))
# Sätter ihop "Höjd", "Hastighet" och "Temperatur" med konverterade värden som visas för användaren genom print nedan

print(output1)
print(output2)
print(output3)
# Ger output till användaren i konverterad form. Utan print ges ingen output.
