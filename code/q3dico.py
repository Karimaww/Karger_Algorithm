import q1e as e
import copy
import numpy as np
import math

#Exercice 3 :

#Question 3-d :
def	contraction_partielle(g, t):
	gi = copy.deepcopy(g)
	n = len(g)

	while (n > t):
		aretes_dispo = e.update_aretes(gi)
		a = e.arete_alea(aretes_dispo)
		gi = e.contraction(gi, a)
		n -= 1
	return gi

def	taille_coupe(g, sommets):
	# si dans sommets on a un seul sommet
	if isinstance(sommets, int):
		return len(g[sommets])

	# sinon on parcours tous les sommets
	m = np.inf
	for som in sommets:
		if len(g[som]) < m:
			m = len(g[som])
	return m

def	karger_stein(ginit, g):
	n = len(g)
	if n <= 6:
		m = np.inf
		for key in list(g.keys()):
			if len(g[key]) < m:
				s = key
				m = len(g[key])
		return s, m
	
	t = math.ceil(1 + n / math.sqrt(2))

	g1 = contraction_partielle(g, t)
	s1, _ = karger_stein(ginit, g1)
	m1 = taille_coupe(ginit, s1)

	g2 = contraction_partielle(g, t)
	s2, _ = karger_stein(ginit, g2)
	m2 = taille_coupe(ginit, s2)

	if m1 < m2:
		return (s1, m1)
	return (s2, m2)
"""
ginit = e.g_cycle(7)
print(ginit)
s2, m2 = karger_stein(ginit, ginit)
print(s2, m2)
"""