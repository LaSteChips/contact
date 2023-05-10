import sys
import sqlite3
conn = sqlite3.connect('contact')
cur = conn.cursor()

def Insert_into(Nom,Prenom,Surnom,Telephone,Email,Adresse):
    try:
        Insert_clients ='''INSERT INTO Contact VALUES(?,?,?,?,?,?)'''
        inserer = (Nom, Prenom, Surnom, Telephone, Email, Adresse)
        cur.execute(Insert_clients, inserer)
        conn.commit()
    except sqlite3.Error as error:
        print("Petit soucis !", error)

def list(): 
    try:
        sql = '''Select * from Contact'''
        result = cur.execute(sql)
        result = cur.fetchall()
        print(result)
        conn.commit()
    except sqlite3.Error as error:
        print("Petit soucis !", error)

def man():
    print("\n")
    print("\n")
    print("\n")
    print("bonsoir jeune padawan ;)")
    print('vue la commande que tu à effectuer je sens que tu es perdu')
    print("mais ne t'en fais pas, pas de panique, je vais te passer un petit tuto ci-dessous")
    print('\n')
    print("En tapant 1, tu peux ajouter un utilisateurs dans ta base de données, il faudra juste que tu connaisse :")
    print("son Nom, son Prenom, son Surnom, son numéro de Téléphone, son adresse mail et son adresse")
    print("En tapant 2, tu peux afficher toute la liste des contact que tu à ajouter récemment avec toutes les données bien sur ;)")
    print("En tapant 3, tu peux rechercher de manière plus précise un ou plusieurs contact en particulier")
    print("en tapant 4, tu pourra obtenir cette aide-ci ;)")
    print("En tapant 5, tu pourras rayer un des contacts que tu a enregistrer de la surface du globe, tout simplement ._.")
    print("En tapant 6, tu pourras modifier la donnée que tu a renseigner sur un contact au cas tu a fais une petite boulette")
    print('\n')
    print("et voila bg, tu a toutes les infos requis pour pouvoir utiliser ma base de données tanquillement ;)")
    

def search(zone, rechercher):
    try:
        if zone == "Nom":
            select = '''Select * from Contact WHERE Nom = ?'''
        if zone == "Prenom":
            select = '''Select * from Contact WHERE Prenom = ?'''
        if zone == "Téléphone":
            select = '''Select * from Contact WHERE Téléphone = ?'''
        if zone == "Surnom":
            select = '''Select * from Contact WHERE Surnom = ?'''
        if zone == "Email":
            select = '''Select * from Contact WHERE Email = ?'''
        if zone == "Adresse":
            select = '''Select * from Contact WHERE Adresse = ?'''
        utile = (rechercher, )
        result = cur.execute(select, utile)
        result = cur.fetchall()
        print(result)
        conn.commit()
    except sqlite3.Error as error:
        print("Petit soucis !", error)


def intéract():
    choix = None
    print("bonsoir et bienvenue dans le help jeune padawan :D")
    print("voici toutes les commandes que tu peux utiliser sur cette base de donnée ;)")
    while choix != "bye":
        print("Tapez 1 pour ajouter un contact ")
        print("Tapez 2 pour afficher la liste des contacts ")
        print("Tapez 3 pour rechercher un ou plusieurs contacts ")
        print("Tapez 4 pour avoir l'aide ")
        print("Tapez 5 pour supprimer un contact ")
        print("Tapez 6 pour modifier les informations d'un contact ")
        choix = input("Que voulez vous faire ? : ")
        if choix == "1":
            Nom= input('Quel est son nom ? : ')
            Prenom= input('Quel est son prénom ? : ')
            Surnom= input('Quel est son surnom ? : ')
            Telephone= input('Quel est son numéro de téléphone ? : ')
            Email = input('Quel est son Email ? : ')
            Adresse= input("Quel est son adresse ? : ")
            Insert_into(Nom,Prenom,Surnom,Telephone,Email,Adresse)
            print("Ajouter avec succès bro")
            print("\n")
            print("\n")      
        if choix == "2":    
            list()   
            print("\n")
            print("\n")
        if choix == "3":
            zone = input("Sur quel zone spécifique (Nom/Prenom/Surnom/Téléphone/Email/Adresse) recherche-tu ? : ")
            rechercher = input("Quel donnée recherche tu ? ? ")
            search(zone, rechercher) 
            print("\n")
            print("\n")
        if choix =="4":
            man()
            print("\n")
            print("\n")
        if choix =="5":
            Nom= input('Quel est le nom de votre contact que tu veux supprimer ?: ')
            Prenom= input('Quel est le prénom du contact que tu veux supprimer ? : ')
            Surnom= input('Quel est le surnom du contact que tu veux supprimer ? : ')
            Telephone= input('Quel est le numéro de téléphone du contact que tu veux supprimer ? : ')
            Email= input('Quel est l Email du contact que tu veux supprimer ? : ')
            Adresse= input("Quel est l'adresse du contact que tu veux supprimer ? : ")
            supprimer(Nom,Prenom,Surnom,Telephone,Email,Adresse)
            print("Suppression réussie mon gars !")
            print("\n")
            print("\n")
        if choix =="6":
            Loca_update = input("Quel est la colonne a modifier (Nom/Prenom/Surnom/Téléphone/Email/Adresse): ")
            New_data = input("Quel est la nouvelle donnée : ")
            Nom= input('Quel est le nom de votre contact à mettre a jour : ')
            Prenom= input('Quel est le prénom de votre contact a mettre a jour : ')
            Surnom= input('Quel est le surnom de votre contact a mettre a jour : ')
            Telephone= input('Quel est le numéro de téléphone de votre contact a mettre a jour : ')
            Email= input('Quel est l Email de votre contact a mettre a jour : ')
            Adresse= input("Quel est l'adresse de votre contact a mettre a jour : ")
            maj(Loca_update, New_data, Nom, Prenom, Surnom, Telephone, Email, Adresse)
            print("\n")
            print("\n")

def supprimer(Nom, Prenom, Surnom, Telephone, Email, Adresse):
    try:
        Delete ='''Delete from Contact where Nom = ? AND Prenom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
        Suppr = (Nom, Prenom, Surnom, Telephone, Email, Adresse)
        cur.execute(Delete, Suppr)
        conn.commit()  
    except sqlite3.Error as error:
        print("y a un shmilblique mon petit gars ! ", error)

def maj(Loca_update,New_data,Nom, Prenom, Surnom, Téléphone, Email, Adresse):
    if Loca_update == "Nom":
        Cmd ='''UPDATE Contact SET Nom = ? WHERE Nom = ? AND Prenom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
    if Loca_update == "Prenom":
        Cmd ='''UPDATE Contact SET Prenom = ? WHERE Nom = ? AND Prenom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
    if Loca_update == "Surnom":
        Cmd ='''UPDATE Contact SET Surnom = ? WHERE Nom = ? AND Prenom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
    if Loca_update == "Téléphone":
        Cmd ='''UPDATE Contact SET Téléphone = ? WHERE Nom = ? AND Prenom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
    if Loca_update == "Email":
        Cmd ='''UPDATE Contact SET Email = ? WHERE Nom = ? AND Prenom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
    if Loca_update == "Adresse":
        Cmd ='''UPDATE Contact SET Adresse = ? WHERE Nom = ? AND Prenom = ? AND Surnom = ? AND Téléphone=? AND Email=? AND Adresse=? '''
    try:
        Update = (New_data,Nom, Prenom, Surnom, Téléphone, Email, Adresse)
        cur.execute(Cmd, Update)
        conn.commit()  
    except sqlite3.Error as error:
        print("y a un shmilblique mon petit gars ! ", error)

for arg in sys.argv:
    try:
        if sys.argv[1] == "new" :
            Nom= input('Quel est le nom du contact : ')
            Prenom= input('Quel est le prénom du contact : ')
            Surnom= input('Quel est le surnom du contact :')
            Telephone= input('Quel est le numéro de téléphone du contact : ')
            Email= input('Quel est l Email du contact ')
            Adresse= input("Quel est l'adresse du contact ")
            Insert_into(Nom,Prenom,Surnom,Telephone,Email,Adresse)
            print("3... 2... 1... et... TA DA.")
            print("Félicitation, ta base de données compte 1 membre de plus ! :D")
            break
              

        if sys.argv[1] == "list" :
            list()
            break

        if sys.argv[1] == "?":
            man()
            break
        if sys.argv[1] == "delete":
            Nom= input('Quel est le nom du contact ? :')
            Prenom= input('Quel est le prénom du contact ? :')
            Surnom= input('Quel est le surnom du contact ? :')
            Telephone= input('Quel est le numéro de téléphone du contact ? :')
            Email= input('Quel est l Email du contact ? :')
            Adresse= input("Quel est l'adresse du contact ? :")
            supprimer(Nom,Prenom,Surnom,Telephone,Email,Adresse)
            print("Félicitation !")
            print("tu viens de rayer ce contact de la réalité B)")
            break
            
        if sys.argv[1] == "update":
            Loca_update = input("Quel colonne est à modifier (Nom/Prenom/Surnom/Téléphone/Email/Adresse) ? : ")
            New_data = input("Mais quel est donc ta nouvelle donnée ? : ")
            Nom= input('Par quel nom doit-il être mis a jour ? : ')
            Prenom= input('Par quel Prenom doit-il être mis a jour ? :')
            Surnom= input('Par quel Surnom doit-il être mis a jour ? :')
            Telephone= input('Par quel numéro de téléphone doit-il être mis a jour ? : ')
            Email= input('Par quel adresse Email doit-il être mis a jour ?: ')
            Adresse= input("Par quel adresse doit-il être mis a jour ? : ")
            maj(Loca_update, New_data, Nom, Prenom, Surnom, Telephone, Email, Adresse)
            break
        
        if sys.argv[1] == "search":
            rechercher = sys.argv[3]
            try:
                if sys.argv[2] == "--by-name" :
                    zone = "Nom"
                if sys.argv[2] == "--by-tel" :
                    zone = "Téléphone"
                if sys.argv[2] == "--by-email" :
                    zone = "Email"
                if sys.argv[2] == "--by-nickname" :
                    zone = "Surnom"
                if sys.argv[2] == "--by-firstname" :
                    zone = "Prenom"
                if sys.argv[2] == "--by-address" :
                    zone = "Adresse"
                search(zone, rechercher)
            except:
                    print ("Press F to pay respect to the commands :( ")
                    print ("ou alors n'hésite pas de consulter la commande help :)")
            break
    except:
            intéract()