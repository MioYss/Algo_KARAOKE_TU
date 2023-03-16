


##SCORES KARAOKE A/

#####################################################################################################
###################################### CLASSE JOUEUR ################################################
#####################################################################################################

class Player:

    # Constructeur
    def __init__(self, nom, score1, score2, score3, score4, score5):
        self.__nom = nom
        self.__score1 = score1
        self.__score2 = score2
        self.__score3 = score3
        self.__score4 = score4
        self.__score5 = score5


    # Methode garde score + meileur score + score total + score moyenne + meilleur chanson
    # On lance chaque chanson pour qu'elles obtient un score
    def garde_score(self, chanson5):
        import random
        score = [0,0,0,0,0]
        meilleur_score =0
        score_total = 0
        score_moyenne = 0
        meilleur_chanson0 = False
        meilleur_chanson1 = False
        meilleur_chanson2 = False
        meilleur_chanson3 = False
        meilleur_chanson4 = False
        meilleur_chanson = "aucune"
        
        #Ajout aléatoire du score de la chanson
        for i in range (0, len(chanson5)):
            if (chanson5 == 0) :
                score [0]= random (50,100)

            if (chanson5 == 2) :
                score [1] = random (50,100)

            if (chanson5 == 3) :
                score [2] = random (50,100)

            if (chanson5 == 4) :
                score [3] = random (50,100)

            if (chanson5 == 5) :
                score [4] = random (50,100)
    
    #On garde le meilleur score dans une variable
        if score [0] >= score[1] and score[2] and score[3] and score[4] :
            score[0] = meilleur_score
            meilleur_chanson0 = True

        if score [1] >= score[0] and score[2] and score[3] and score[4] :
            score[1] = meilleur_score
            meilleur_chanson1 = True

        if score [2] >= score[1] and score[0] and score[3] and score[4] :
            score[2] = meilleur_score
            meilleur_chanson2 = True

        if score [3] >= score[1] and score[2] and score[0] and score[4] :
            score[3] = meilleur_score
            meilleur_chanson3 = True

        if score [4] >= score[1] and score[2] and score[3] and score[0] :
            score[4] = meilleur_score
            meilleur_chanson4 = True

    #Score total
        str score[0] + str score[1] + str score[2] + str score[3] + str score[4] = score_total

    #Moyenne score 
        score_moyenne = (score_total / 2)

    # Methode affiche n° chanson
        if meilleur_chanson0 == True:
            meilleur_chanson = "1"

        if meilleur_chanson1 == True:
            meilleur_chanson = "2"
        
        if meilleur_chanson2 == True:
            meilleur_chanson = "3"

        if meilleur_chanson3 == True:
            meilleur_chanson = "4"

        if meilleur_chanson4 == True:
            meilleur_chanson = "5"

    #Affichage score et meilleur chanson
        print ("les scores sont:")
        print (int score [0])
        print (int score [1])
        print (int score [2])
        print (int score [3])
        print (int score [4])
        print ( "La meilleur chanson est :") + (meilleur_chanson)
        print ("le score total est :")
        print (score_total)


    # Getters
    def getNom(self):
        return self.__nom

    def getScore1(self):
        return self.__score1

    def getScore2(self):
        return self.__score2

    def getScore3(self):
        return self.__score3

    def getScore4(self):
        return self.__score4

    def getScore5(self):
        return self.__score5


##### DEBUT DU JEU #####

joueur1 = Player ( self, 0, 0, 0, 0, 0)
joueur1.garde_score



##SCORES KARAOKE B/

class Karaoke:

    # Constructeur
    def __init__(self, chanson1, chanson2):
        self.__chanson1 = chanson1
        self.__chanson2 = chanson2


class Player2:

    # Constructeur
    def __init__(self, nom, score1, score2, scoretotal, scoremoyenne):
        self.__nom = nom
        self.__score1 = score1
        self.__score2 = score2
        self.__scoretotal = scoretotal
        self.__scoremoyenne = scoremoyenne

## Ajout player

## Sppression player

## Afichage meilleur score pour joueur spécifique

## Afichage moyenne score pour joueur spécifique