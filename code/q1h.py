import q1e as p
import matplotlib.pyplot as plt
import time

def  trace_courbe(nb_sommets, temps_complet, temps_cycle, temps_biparti):
	# Plot some numbers:
	fig, ax = plt.subplots()
	complet, = ax.plot(nb_sommets, temps_complet, label='complet') 
	cycle, = ax.plot(nb_sommets, temps_cycle, label='cycle')
	biparti, = ax.plot(nb_sommets, temps_biparti, label='biparti')

	plt.title("Temps de calcul en fonction du nombre de sommets") 
	ax.legend([complet, cycle, biparti], ['complet', 'cycle', 'biparti'])
	# Display the plot:
	plt.show()

def test():
	nb_sommets = [i for i in range(10, 100, 10)]
	temps_complet = []
	temps_cycle = []
	temps_biparti = []

	for n in nb_sommets:
		g_complet = p.g_complet(n)
		g_cycle = p.g_cycle(n)
		g_biparti = p.g_biparti(n)

		t1 = time.time()
		p.algo_karger(g_complet)
		t2 = time.time()
		temps_complet.append(t2 - t1)

		t1 = time.time()
		p.algo_karger(g_cycle)
		t2 = time.time()
		temps_cycle.append(t2 - t1)

		t1 = time.time()
		p.algo_karger(g_biparti)
		t2 = time.time()
		temps_biparti.append(t2 - t1)

	trace_courbe(nb_sommets, temps_complet, temps_cycle, temps_biparti)

test()
