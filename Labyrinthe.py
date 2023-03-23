from Pile import *
from random import *


class Labyrinthe:
    
    
    def __init__(self,imageLaby,caseArrivee,longueur,hauteur,pixelsBloc):    
        self.dico=dict()
        self.imageLaby=imageLaby
        self.caseArrivee=caseArrivee
        self.longueur=longueur
        self.hauteur=hauteur
        self.pixelsBloc=pixelsBloc
    
    
    def __repr__(self):
        return str(self.dico)
    
    def getLabyrinthe(self):    
        casesRangees=list()
        for i in self.dico:
            casesRangees.append(int(i))
        casesRangees=sorted(casesRangees)
        for i in casesRangees:
            print("la case numero:",int(i),"a pour voisin(s) la/les case(s):",self.dico[str(i)]) 
            
                        
    def setCaseVoisin(self,case,voisin1,voisin2="0",voisin3="0"):   
        if case not in self.dico:
            self.dico[case]=[]
        if voisin1 not in self.dico:
            self.dico[voisin1]=[]    
        self.dico[case].append(voisin1)  
        self.dico[voisin1].append(case)
        if voisin2!="0":
            if voisin2 not in self.dico:
                self.dico[voisin2]=[]    
            self.dico[case].append(voisin2)  
            self.dico[voisin2].append(case)
        if voisin3!="0":
            if voisin3 not in self.dico:
                self.dico[voisin3]=[]    
            self.dico[case].append(voisin3)  
            self.dico[voisin3].append(case)
        

       
    def voisinsContinus(self,case1,case2,case3,case4="0",case5="0",case6="0",case7="0"): 
        self.setCaseVoisin(case1,case2)
        self.setCaseVoisin(case2,case3)
        if case4!="0":
            self.setCaseVoisin(case3,case4)
        if case5!="0":
            self.setCaseVoisin(case4,case5)
        if case6!="0":
            self.setCaseVoisin(case5,case6)
        if case7!="0":
            self.setCaseVoisin(case6,case7)
            
    def parcoursProfondeur(self): 
        caseDep="1"
        caseArr=self.caseArrivee
        casesRetenues=[]
        p=Pile()
        casesVisites=[caseDep]
        p.empiler(caseDep)
        while not p.pilevide():
            case=p.sommet()
            voisins = [v for v in self.dico[case] if v not in casesVisites]
            if len(voisins)!=0:
                if caseArr in voisins:
                    v=caseArr
                    casesVisites.append(v)
                    return casesVisites
                else:
                    v=choice(voisins)
                    p.empiler(v)
                    casesVisites.append(v)
            else :
                casesRetenues.append(case)
                p.depiler()
        return casesVisites 
        

    def solutionOptimale(self): 
        l=[]
        for i in range(1000):
            l.append(self.parcoursProfondeur())
        return min(l, key=len)
    



laby1=Labyrinthe("laby1.png","60",10,6,60)                                  #taper dans la console:  chemin(laby1)
laby1.setCaseVoisin("2","3")
laby1.setCaseVoisin("3","13")
laby1.setCaseVoisin("4","14")
laby1.setCaseVoisin("23","33")
laby1.setCaseVoisin("43","53")
laby1.setCaseVoisin("17","27")
laby1.setCaseVoisin("37","47")
laby1.setCaseVoisin("50","60")
laby1.setCaseVoisin("35","36")
laby1.setCaseVoisin("44","45")
laby1.setCaseVoisin("22","23")
laby1.voisinsContinus("2","12","22")
laby1.voisinsContinus("8","18","28")
laby1.voisinsContinus("32","33","34")
laby1.voisinsContinus("24","34","44")
laby1.voisinsContinus("36","46","56")
laby1.voisinsContinus("19","29","39")
laby1.voisinsContinus("26","27","28")
laby1.voisinsContinus("41","42","43")
laby1.voisinsContinus("6","7","8","9")
laby1.voisinsContinus("15","25","35","45")
laby1.voisinsContinus("47","48","49","50")
laby1.voisinsContinus("57","58","59","60")
laby1.voisinsContinus("37","38","39","40")
laby1.voisinsContinus("10","20","30","40")
laby1.voisinsContinus("1","11","21","31","41")
laby1.voisinsContinus("13","14","15","16","17")
laby1.voisinsContinus("4","5","6","7","8","9","10")
laby1.voisinsContinus("51","52","53","54","55","56")


laby2=Labyrinthe("laby2.png","42",7,6,38)                                  #taper dans la console:  chemin(laby2)
laby2.setCaseVoisin("4","11")
laby2.setCaseVoisin("6","13")
laby2.setCaseVoisin("27","28")
laby2.setCaseVoisin("36","37")
laby2.setCaseVoisin("38","39")
laby2.setCaseVoisin("8","1","9")
laby2.setCaseVoisin("14","13","21")
laby2.setCaseVoisin("20","21","27")
laby2.setCaseVoisin("25","24","32")
laby2.setCaseVoisin("31","30","38")
laby2.setCaseVoisin("41","40","34")
laby2.voisinsContinus("5","6","7")
laby2.voisinsContinus("1","2","3","4")
laby2.voisinsContinus("16","23","30")
laby2.voisinsContinus("28","35","42")
laby2.voisinsContinus("3","10","17","24")
laby2.voisinsContinus("15","22","29","36")
laby2.voisinsContinus("15","16","17","18","19")  
laby2.voisinsContinus("5","12","19","26","33","40")  
                 