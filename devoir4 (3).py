# Auteur : Samy Smail
# Date : 4 novembre 2023
#
# Ce programme implimente la fonction penrose() qui permet de tracer un pavage 
# (une collection de formes géométriques dont l'union sans recouvrement
# couvre le plan) spécifique de Penrose (des pavages non périodiques).


# La procédure losange() permet de tracer des losanges.
# Elle prend 2  paramètre: (1) 'dist',la longueur de ses côtés et
# (2)'aigu', l'angle aigu du losange en degrés.

def losange(dist,aigu):
    for _ in range(2):   
        fd(dist)
        rt(aigu)   
        fd(dist)
        rt(180 - aigu)   # Afin d'obtenir l'angle obtus

        

    
# La procédure penrose() permet de tracer un pavage de Penrose particulier
# formé de losanges. Elle est structurée de manière à tracer le pavage 
# en 3 couches. La première trace les losanges épais au centre, la deuxième
# trace les losanges minces et la troisième trace les losanges épais sur le 
# périmètre du pavage. Elle prend un paramètre: (1) 'dist', la longueur de 
# chaque côté des losanges formant le pavage.

def penrose(dist):
    #ht()
    
    pu()
    
    # 1ere Couche avec des losanges épais
    for i in range(5): 
        lt(90)        
        pd();
        losange(dist,72)
        rt(18) # On prend en compte la première rotation de 90 degrés,
               # alors 90 - 72 (l'angle aigu) demande un rotation vers la 
               # droite de 18 degrés afin que la tortue soit bien alignée
               # lors de la prochain itération.
        
    
    # afin que la tortue soit bien alignée pour commencer la 2e couche
    pu(); lt(90); fd(dist); lt(72); fd(dist); rt(144)
    
    
    # 2e Couche avec des losanges minces
    for i in range (5):        
        pd()
        losange(dist, 36);
        pu(); 
        fd(dist); rt(36); fd(dist); rt(36) # alignement de la tortue
                                           # avant la prochain itération
    
    
    
    # alignement de la tortue pour commencer la 3e couche
    lt(108); fd(dist); rt(108);
    
    
    
    # 3e Couche avec des losanges épais
    for i in range (5):  
        pd()
        for i in range(3):
            losange(dist, 72)
            pu();
            fd(dist);lt(36);fd(dist); rt(108); # alignement de la tortue 
                                               # avant la prochaine itération
            pd() 
            
        pu();
        rt(72); fd(dist); rt(36); fd(dist); rt(108); # alignement de la tortue
                            
    
 
penrose(35)