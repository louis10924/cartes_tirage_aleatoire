#on ajoute un paramètre pour pouvoir choisir les binomes au hasard
import random 

#Listes des personnes dans le groupe 1
personnes1 = ["Guillaume", "Noemie", "Thomas B", "Titouan", "Simon", "Vincent", "Hugo", "Fernando", "Roxane", "Aureline"]


#choix au hasard des binomes dans le groupe 1
random.shuffle(personnes1)
content = ''
for element in range(10):
	content = content + str(element) + " : " + str(personnes1[element]) + "<br />"
	if element%2 != 0:
		#liste des binomes
		display("")
display(content)