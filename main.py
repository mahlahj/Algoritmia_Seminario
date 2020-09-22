import os
from datetime import date
def programa():
        Año = input("Año de Nacimiento: " )
        Mes = input("Mes de Nacimiento: " )
        Dia = input("Dia de Nacimiento: " )
        Año_de_Nacimiento = (Dia + "/" + Mes + "/" + Año)
        print('Tu fecha de Nacimiento es ' + Año_de_Nacimiento)
        d = date.today()
        y = d.year
        os.system("cls")

        if ((int(Mes)==12 and int(Dia) >= 22)or(int(Mes)==1 and int(Dia)<= 19)):
                signo_zodiacal = ("\n Capricornio")
        elif ((int(Mes)==1 and int(Dia) >= 20)or(int(Mes)==2 and int(Dia)<= 17)):
                signo_zodiacal = ("\n Acuario")
        elif ((int(Mes)==2 and int(Dia) >= 18)or(int(Mes)==3 and int(Dia)<= 19)):
                signo_zodiacal = ("\n Piscis")
        elif ((int(Mes)==3 and int(Dia) >= 20)or(int(Mes)==4 and int(Dia)<= 19)):
                signo_zodiacal = ("\n Aries")
        elif ((int(Mes)==4 and int(Dia) >= 20)or(int(Mes)==5 and int(Dia)<= 20)):
                signo_zodiacal = ("\n Tauro")
        elif ((int(Mes)==5 and int(Dia) >= 21)or(int(Mes)==6 and int(Dia)<= 20)):
                signo_zodiacal = ("\n Geminis")
        elif ((int(Mes)==6 and int(Dia) >= 21)or(int(Mes)==7 and int(Dia)<= 22)):
                signo_zodiacal = ("\n Cancer")
        elif ((int(Mes)==7 and int(Dia) >= 23)or(int(Mes)==8 and int(Dia)<= 22)): 
                signo_zodiacal = ("\n Leo")
        elif ((int(Mes)==8 and int(Dia) >= 23)or(int(Mes)==9 and int(Dia)<= 22)): 
                signo_zodiacal = ("\n Virgo")
        elif ((int(Mes)==9 and int(Dia) >= 23)or(int(Mes)==10 and int(Dia)<= 22)):
                signo_zodiacal = ("\n Libra")
        elif ((int(Mes)==10 and int(Dia) >= 23)or(int(Mes)==11 and int(Dia)<= 21)): 
                signo_zodiacal = ("\n Escorpio")
        elif ((int(Mes)==11 and int(Dia) >= 22)or(int(Mes)==12 and int(Dia)<= 21)):
                signo_zodiacal = ("\n Sagitario")

        print(signo_zodiacal)
        
programa()