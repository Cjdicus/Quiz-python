import tkinter as tk
import random

# --- Données des questions (Thèmes) ---
Technologie = {
    "Débutant": [
        {"question": "Quel moyen de paiement mobile est très populaire en Afrique ?",
         "choix": ["paypal", "Mobile money", "visa"], "reponse": "Mobile money"},
        {"question": "Dans quel pays se trouve la startup Andela ?",
         "choix": ["Ghana", "Nigeria", "Afrique du sud"], "reponse": "Afrique du sud"},
        {"question": "Quel est un grand opérateur mobile au Burkina Faso ?",
         "choix": ["Telecel", "Orange", "Moov africa"], "reponse": "Orange"}
    ],
    "Intermédiaire": [
        {"question": "Quel est le but de l'initiative Smart Africa ?",
         "choix": ["Lutter contre la pollution", "Numériser l'administration publique", "Accélérer la transformation numérique du continent"], "reponse": "Accélérer la transformation numérique du continent"},
        {"question": "Que représente « Silicon Savannah » ?",
         "choix": ["Une vallée agricole", "Un pôle technologique au Kenya", "Un projet de plantation d'arbres"], "reponse": "Un pôle technologique au Kenya"},
        {"question": "Quelle est la spécialité de Carnegie Mellon Africa ?",
         "choix": ["Agriculture", "Droit", "TICS"], "reponse": "TICS"}
    ],
    "Avancé": [
        {"question": "Quel pays africain a lancé le satellite Mohammed VI-B ?",
         "choix": ["Nigéria", "Égypte", "Maroc"], "reponse": "Maroc"},
        {"question": "Quel est le principal obstacle au numérique en zones rurales africaines ?",
         "choix": ["Trop de soleil", "Mauvaise alimentation", "Manque d'infrastructures"], "reponse": "Manque d'infrastructures"},
        {"question": "Quelle entreprise fintech africaine est très en vue ?",
         "choix": ["Flutterwave", "Stripe", "Binance"], "reponse": "Flutterwave"}
    ]
}

culture_generale = {
    "Débutant": [
        {"question": "Quel est le plus grand pays d'Afrique par la superficie ?", "choix": ["Nigeria", "Algerie", "RDC"], "reponse": "Algerie"},
        {"question": "Dans quel pays se trouve la ville de Lagos ?", "choix": ["Ghana", "Nigeria", "cote d'ivoire"], "reponse": "Nigeria"},
        {"question": "Combien y a-t-il de pays en Afrique", "choix": ["54", "48", "60"], "reponse": "54"}
    ],
    "Intermédiaire": [
        {"question": "Qui a été le premier président du Burkina Faso ?", "choix": ["Thomas SANKARA", "Maurice YAMEOGO", "Blaise COMPAORE"], "reponse": "Maurice YAMEOGO"},
        {"question": "Quelle est la capitale de l'Éthiopie ?", "choix": ["Kampala", "Nairobi", "Addis Abeba"], "reponse": "Addis Abeba"},
        {"question": "Quelle est la langue la plus parlée en Afrique ?", "choix": ["swahili", "Arabe", "Francais"], "reponse": "swahili"}
    ],
    "Avancé": [
        {"question": "En quelle année s'est tenue la conférence de Berlin?", "choix": ["1900", "1884", "1895"], "reponse": "1884"},
        {"question": "Où se trouve le siège de l'Union Africaine?", "choix": ["johannesburg", "Nairobi", "Addis-Abeba"], "reponse": "Addis-Abeba"},
        {"question": "Quelle civilisation a construit les pyramides de Méroé ?", "choix": ["les egyptiens", "les koushites", "les carthaginois"], "reponse": "les koushites"}
    ]
}

Santé = {
    "Débutant": [
        {"question": "Quel est le plus grand pays d'Afrique?", "choix": ["Burkina", "Egypte", "Nigeria", "Tanzanie"], "reponse": "Nigeria"},
        {"question": "Qui est le premier président du Burkina Faso?", "choix": ["Thomas SANKARA", "Blaise COMPAORE", "Ouezzin COULIBALY", "Maurice Yameogo"], "reponse": "Maurice Yameogo"},
        {"question": "En quelle année la première guerre mondiale a-t-elle débuté?", "choix": ["2001", "1939", "1914", "1945"], "reponse": "1914"}
    ],
    "Intermédiaire": [
        {"question": "Quelle est la capitale de l'Italie ?", "choix": ["Rome", "Milan", "Venise", "Florence"], "reponse": "Rome"},
        {"question": "Combien de côtés a un hexagone ?", "choix": ["5", "6", "7", "8"], "reponse": "6"}
    ],
    "Avancé": [
        {"question": "Qui a développé la théorie de la relativité ?", "choix": ["Newton", "Einstein", "Galilée", "Tesla"], "reponse": "Einstein"},
        {"question": "Quel est le plus long fleuve du monde ?", "choix": ["Nil", "Amazone", "Yangtsé", "Mississippi"], "reponse": "Amazone"}
    ]
}

Sport = {
    "Débutant": [
        {"question": "Quel est le sport le plus populaire en Afrique ?", "choix": ["Basket-ball", "Football", "Tennis"], "reponse": "Football"},
        {"question": "En quelle année l'Afrique du Sud a-t-elle accueilli la Coupe du Monde ?", "choix": ["2006", "2010", "2014"], "reponse": "2010"},
        {"question": "Quel joueur ivoirien est une légende du football ?", "choix": ["Yaya Touré", "Didier Drogba", "Samuel Eto'o"], "reponse": "Didier Drogba"}
    ],
    "Intermédiaire": [
        {"question": "Qui détient le record de titres à la CAN ?", "choix": ["Cameroun", "Sénégal", "Égypte"], "reponse": "Égypte"},
        {"question": "Quel pays a remporté la CAN 2021 ?", "choix": ["Burkina Faso", "Sénégal", "Maroc"], "reponse": "Sénégal"},
        {"question": "Quel coureur africain est célèbre en marathon ?", "choix": ["Eliud Kipchoge", "Haile Gebrselassie", "Kenenisa Bekele"], "reponse": "Eliud Kipchoge"}
    ],
    "Avancé": [
        {"question": "Quel Burkinabè a remporté une médaille olympique en triple saut ?", "choix": ["Fabrice Zongo", "Hugues Fabrice Zango", "Ibrahim Traoré"], "reponse": "Hugues Fabrice Zango"},
        {"question": "Quelle nage est la plus rapide ?", "choix": ["Brasse", "Dos", "Crawl"], "reponse": "Crawl"},
        {"question": "Quelle compétition est réservée aux joueurs évoluant dans les clubs africains ?", "choix": ["CAN", "CHAN", "CAF"], "reponse": "CHAN"}
    ]
}

themes = {
    "Technologie": Technologie,
    "Culture générale": culture_generale,
    "Santé": Santé,
    "Sport": Sport
}

# --- Interface graphique ---
fenetre = tk.Tk()
fenetre.title("Quiz Afrique")
fenetre.geometry("600x500")
fenetre.configure(bg="#F0F8FF")

theme_selectionne = None
niveau_selectionne = None
question_actuelle = {}
score = 0
questions_posees = []

def montrer_accueil():
    global score, questions_posees
    score = 0
    questions_posees = []
    for widget in fenetre.winfo_children():
        widget.destroy()
    tk.Label(fenetre, text="Choisissez un thème", font=("Arial", 20, "bold"), bg="#F0F8FF").pack(pady=30)
    for theme in themes:
        tk.Button(fenetre, text=theme, width=25, height=2, bg="#87CEEB", font=("Arial", 14),
                  command=lambda t=theme: choisir_theme(t)).pack(pady=10)

def choisir_theme(theme):
    global theme_selectionne
    theme_selectionne = theme
    for widget in fenetre.winfo_children():
        widget.destroy()
    tk.Label(fenetre, text=f"Thème : {theme}", font=("Arial", 20, "bold"), bg="#F0F8FF").pack(pady=30)
    tk.Label(fenetre, text="Choisissez un niveau", font=("Arial", 16), bg="#F0F8FF").pack(pady=10)
    for niveau in themes[theme]:
        tk.Button(fenetre, text=niveau, width=20, height=2, bg="#90EE90", font=("Arial", 14),
                  command=lambda n=niveau: commencer_quiz(n)).pack(pady=8)
    tk.Button(fenetre, text="🏠 Retour à l'accueil", command=montrer_accueil, bg="#FF7F7F", font=("Arial", 12)).pack(pady=5)

def commencer_quiz(niveau):
    global niveau_selectionne, questions_posees
    niveau_selectionne = niveau
    questions_posees = []
    afficher_question()

def afficher_question():
    global question_actuelle, score_label
    
    for widget in fenetre.winfo_children():
        widget.destroy()
    
    # Afficher le score
    score_label = tk.Label(fenetre, text=f"Score: {score}", font=("Arial", 14, "bold"), bg="#F0F8FF")
    score_label.pack(pady=10)
    
    questions_disponibles = [q for q in themes[theme_selectionne][niveau_selectionne] if q not in questions_posees]
    
    if not questions_disponibles:
        tk.Label(fenetre, text="Félicitations ! Vous avez répondu à toutes les questions !", font=("Arial", 16, "bold"), bg="#F0F8FF").pack(pady=50)
        tk.Label(fenetre, text=f"Score final: {score}", font=("Arial", 18), bg="#F0F8FF").pack(pady=20)
        tk.Button(fenetre, text="🏠 Retour à l'accueil", command=montrer_accueil, bg="#FF7F7F", font=("Arial", 14)).pack(pady=20)
        return
    
    question_actuelle = random.choice(questions_disponibles)
    questions_posees.append(question_actuelle)
    
    tk.Label(fenetre, text=f"{theme_selectionne} - {niveau_selectionne}", font=("Arial", 14), bg="#F0F8FF").pack(pady=10)
    tk.Label(fenetre, text=question_actuelle["question"], font=("Arial", 16, "bold"), wraplength=500, bg="#F0F8FF").pack(pady=20)
    
    for choix in question_actuelle["choix"]:
        tk.Button(fenetre, text=choix, font=("Arial", 13), width=30, height=2, bg="#FFFACD",
                  command=lambda c=choix: verifier_reponse(c)).pack(pady=5)

    global label_resultat
    label_resultat = tk.Label(fenetre, text="", font=("Arial", 14), bg="#F0F8FF")
    label_resultat.pack(pady=15)

    tk.Button(fenetre, text="🏠 Retour à l'accueil", command=montrer_accueil, bg="#FF7F7F", font=("Arial", 12)).pack(pady=5)

def verifier_reponse(choix):
    global score
    bonne = question_actuelle["reponse"]
    if choix == bonne:
        label_resultat.config(text="✅ Bonne réponse !", fg="green")
        score += 1
    else:
        label_resultat.config(text=f"❌ Mauvaise réponse. C'était : {bonne}", fg="red")
    
    # Mettre à jour le score affiché
    score_label.config(text=f"Score: {score}")
    
    # Passer à la question suivante après 1 seconde
    fenetre.after(1000, afficher_question)

montrer_accueil()
fenetre.mainloop()