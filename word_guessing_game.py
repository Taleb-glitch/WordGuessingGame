import random


words = ["python", "ordinateur", "programmation", "clavier", "souris", "algorithme", "jeu"]

def choisir_mot():
    return random.choice(words)

def afficher_mot(mot_secret, lettres_devinees):
    return " ".join([lettre if lettre in lettres_devinees else "_" for lettre in mot_secret])

def jouer():
    print("🎯 Bienvenue dans le jeu de devinettes de mots !")
    mot_secret = choisir_mot()
    lettres_devinees = set()
    tentatives = 6  

    while tentatives > 0:
        print("\nMot à deviner :", afficher_mot(mot_secret, lettres_devinees))
        print("Tentatives restantes :", tentatives)
        lettre = input("Devinez une lettre : ").lower()

        if not lettre.isalpha() or len(lettre) != 1:
            print("⚠️ Veuillez entrer une seule lettre valide.")
            continue

        if lettre in lettres_devinees:
            print("🔁 Vous avez déjà deviné cette lettre.")
            continue

        lettres_devinees.add(lettre)

        if lettre not in mot_secret:
            tentatives -= 1
            print("❌ Mauvais choix !")

        if all(l in lettres_devinees for l in mot_secret):
            print("\n🎉 Félicitations ! Vous avez deviné le mot :", mot_secret)
            break
    else:
        print("\n💀 Vous avez perdu ! Le mot était :", mot_secret)

if __name__ == "__main__":
    jouer()
