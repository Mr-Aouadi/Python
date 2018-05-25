#Jeux Vache Toureaux (2 chiffres)

def Random_Func(Usd_Nr):
    #definir un nombre aleatoire apar les nombres deja choisis
    import random
    rand_Nr=random.choice([i for i in range(0,9) if i not in Usd_Nr])
    return rand_Nr;

def Check_Res(Gss_Res):
    #traiter le resultat de vérification
    if Gss_Res=='2T0V': 
        Exp_Nr=['11111']
    elif Gss_Res=='0T2V': 
        Exp_Nr=['22222']
    elif Gss_Res=='0T1V': 
        Exp_Nr=[Rnd_Nr1,Rnd_Nr2]
    elif Gss_Res=='1T0V': 
        Exp_Nr=[Rnd_Nr1,Rnd_Nr2]    
    elif Gss_Res=='0T0V': 
        Exp_Nr=[Rnd_Nr1,Rnd_Nr2]   
    return Exp_Nr

Rnd_Nr1= str(Random_Func([]))
Rnd_Nr2= str(Random_Func([Rnd_Nr1]))
Rnd_Nr=Rnd_Nr1+Rnd_Nr2
print (Rnd_Nr)
Res = input('Enter guessing result as ?v?t ')
Exp = list(map(int, Check_Res(Res)))

if Exp==[11111]:
    print ('YOOPI')
    
if Exp==[22222]:
    Rnd_Nr=Rnd_Nr2+Rnd_Nr1
    print ('This is your Number',Rnd_Nr)
    
if Res=='0T0V':
    while Res=='0T0V':
      Rnd_Nr1= str(Random_Func(Exp))
      Exp.extend(list(map(int,Rnd_Nr1)))
      Rnd_Nr2= str(Random_Func(Exp))
      Rnd_Nr=Rnd_Nr1+Rnd_Nr2
      print (Rnd_Nr)
      Res = input('Enter guessing result as ?v?t ')
      Exp.extend(list(map(int, Check_Res(Res))))
      
if Res=='0T1V': 
    V_Check=Rnd_Nr1
    Rnd_Nr1= str(Random_Func(Exp))
    Rnd_Nr=Rnd_Nr2+Rnd_Nr1
    print (Rnd_Nr)
    Res = input('Enter guessing result as ?v?t ')
    if Res=='0T0V':
        Rnd_Nr2= str(Random_Func(Exp))
        Rnd_Nr=Rnd_Nr2+V_Check
        print (Rnd_Nr)
        Res = input('Enter guessing result as ?v?t ')
        Exp.extend(list(map(int, Check_Res(Res))))
        while Res!='2T0V':
            Rnd_Nr2= str(Random_Func(Exp))
            Rnd_Nr=Rnd_Nr2+V_Check
            print (Rnd_Nr)
            Res = input('Enter guessing result as ?v?t ')
            Exp.extend(list(map(int, Check_Res(Res))))
    elif Res=='1T0V':
         while Res!='2T0V':
             Rnd_Nr1= str(Random_Func(Exp))
             Rnd_Nr=Rnd_Nr2+Rnd_Nr1
             print (Rnd_Nr)
             Res = input('Enter guessing result as ?v?t ')
             Exp.extend(list(map(int, Check_Res(Res))))    

if Res=='1T0V':
    V_Check2=Rnd_Nr1
    Rnd_Nr1= str(Random_Func(Exp))
    Rnd_Nr=Rnd_Nr2+Rnd_Nr1
    print (Rnd_Nr)
    Res = input('Enter guessing result as ?v?t ')
    if Res=='0T0V':
        Rnd_Nr2= str(Random_Func(Exp))
        Rnd_Nr=Rnd_Nr2+V_Check2
        print (Rnd_Nr)
        Res = input('Enter guessing result as ?v?t ')
        Exp.extend(list(map(int, Check_Res(Res))))
        while Res!='2T0V':
            Rnd_Nr2= str(Random_Func(Exp))
            Rnd_Nr=Rnd_Nr2+V_Check2
            print (Rnd_Nr)
            Res = input('Enter guessing result as ?v?t ')
            Exp.extend(list(map(int, Check_Res(Res))))
    elif Res=='1T0V':
         while Res!='2T0V':
             Rnd_Nr1= str(Random_Func(Exp))
             Rnd_Nr=Rnd_Nr2+Rnd_Nr1
             print (Rnd_Nr)
             Res = input('Enter guessing result as ?v?t ')
             Exp.extend(list(map(int, Check_Res(Res))))