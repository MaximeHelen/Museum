# -*- coding: utf-8 -*-
from xml.dom import minidom
import primitives as prims
import salle as salle

signaletique = salle.Signaletique()

def getAttributs(node):
	attributs = node.attributes
	res = {}
	for cle in attributs.keys():
		attr = attributs[cle]
		res[cle] = attr.value
	return res 

def parse(node):
	nomBalise = node.tagName
	attributs = getAttributs(node)
	lesFils = [parse(e) for e in node.childNodes if e.nodeType==e.ELEMENT_NODE]
	# print "La balise : ", nomBalise
	# print "Les fils : ", lesFils
	# print "Les attributs : ", attributs
	# print "==============================================================="

	if(signaletique.count==16):
		signaletique.draw()

	if nomBalise == "Rectangle" : 
		rect = prims.Rectangle(attributs)
		return rect
	elif nomBalise == "Tableau":
		return prims.Tableau(attributs)
	elif nomBalise == "Cloison" : 
		return prims.MurPlein(attributs)
	elif nomBalise == "Transform" : 
		return prims.Transform(lesFils,attributs)
	elif nomBalise == "Scene" :
		scene = prims.Scene(lesFils)
		return scene
	elif nomBalise == "Sol" :
		return prims.Sol(attributs)
	elif nomBalise == "Salle" :
		tmp = salle.Salle(attributs)
		signaletique.add_salle(tmp)
		signaletique.count_salle()
		return tmp
	elif nomBalise == "Signaletique" :
		return signaletique
	


def parser(nomFichier):
	fichier = open('scene.xml')
	xmldoc = minidom.parse(fichier)
	#print xmldoc.toxml()
	fichier.close()

	print '\n\n'

	racine = xmldoc.childNodes[0]

	return parse(racine)	

if __name__ == "__main__":
	fichier = open('scene.xml')
	xmldoc = minidom.parse(fichier)
	#print xmldoc.toxml()
	fichier.close()

	print '\n\n'

	racine = xmldoc.childNodes[0]

	parse(racine)

