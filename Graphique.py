from Labyrinthe import *
import turtle

"""donne les coordonnées du point de départ du labyrinthe
   en fonction du nombre de cases en largeur, longueur et taille en pixels d'une case du labyrinthe"""
def coordsDepart(longueurLabyrinthe,largeurLabyrinthe,pixelsBloc):
    xDepart=(longueurLabyrinthe/2*pixelsBloc-pixelsBloc/2)*-1           
    yDepart=largeurLabyrinthe/2*pixelsBloc-pixelsBloc/2
    return xDepart,yDepart

"""fonction qui fait tourner le curseur sur place pour regarder vers le nord et le fait avancer de x pixels dans cette direction"""
def haut(pixelsBloc):
    turtle.setheading(90)
    turtle.forward(pixelsBloc)
    
"""fonction qui fait tourner le curseur sur place pour regarder vers l'ouest et le fait avancer de x pixels dans cette direction"""
def gauche(pixelsBloc):
    turtle.setheading(180)
    turtle.forward(pixelsBloc)
    
"""fonction qui fait tourner le curseur sur place pour regarder vers l'est et le fait avancer de x pixels dans cette direction"""
def droite(pixelsBloc):
    turtle.setheading(0)
    turtle.forward(pixelsBloc)
    
"""fonction qui fait tourner le curseur sur place pour regarder vers le sud et le fait avancer de x pixels dans cette direction"""
def bas(pixelsBloc):
    turtle.setheading(270)
    turtle.forward(pixelsBloc)
    
"""fonction qui execute une série de commandes afin d'afficher une fenetre turtle
   que l'on utilisera par la suite dans la fonction chemin"""
def setTurtle(labyrinthe):
    longueurLaby=labyrinthe.longueur
    largeurLaby=labyrinthe.hauteur
    pixelsBloc=labyrinthe.pixelsBloc
    turtle.setup()
    turtle.title("Résolution de labyrinthe")   
    turtle.shape("circle")      
    turtle.showturtle()                                               #le curseur en forme de cercle devient visible
    turtle.bgpic(labyrinthe.imageLaby)                                #on met l'image du labyrinthe en fond d'écran
    turtle.up()
    turtle.goto(coordsDepart(longueurLaby,largeurLaby,pixelsBloc))    #on positionne le curseur sur les coords du point de depart
    turtle.down()
    turtle.width(4)          
    turtle.pencolor("red")
    turtle.speed(2)

    
"""affiche graphiquement la resolution du labyrinthe à l'aide de la fonction solutionOptimale de la classe Labyrinthe"""
def chemin(nomLaby):
    setTurtle(nomLaby)
    solution=nomLaby.solutionOptimale()   
    for i in range(0,len(solution)-1):
        if int(solution[i])-int(solution[i+1])==-1:                           #deplacement vers la droite
            droite(nomLaby.pixelsBloc)
        elif int(solution[i])-int(solution[i+1])==1:                          #deplacement vers la gauche
            gauche(nomLaby.pixelsBloc)
        elif int(solution[i])-int(solution[i+1])==nomLaby.longueur*(-1):      #deplacement vers le bas
            bas(nomLaby.pixelsBloc)
        else:                                                                 #deplacement vers le haut
            haut(nomLaby.pixelsBloc)
    turtle.hideturtle()    
    turtle.up()
    bas(nomLaby.pixelsBloc)   #le curseur fait un dernier deplacement vers le bas avec le stylo levé pour s'écarter de l'image
    turtle.write("Vous avez résolu le labyrinthe!",align="right",font=("times new roman",17,"bold"))    #texte affiché à la fin du tracé
    turtle.exitonclick()      #ferme la fenetre turtle lorsque l'utlisatuer fait un clic droit
    
