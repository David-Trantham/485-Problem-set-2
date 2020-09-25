import sys
import numpy as np
import queue

# Calculate the number of shortest paths from node a (src) to b (goal) using a
# list of edges
def shortest_paths(E, a):
	E = G.edges
	q = queue.SimpleQueue
	q.put(s)
	while(not q.Empty):	#Until Queue is empty
		if a in E:
			##TODO stopping here cus I can't think clearly anymore


# Calculate (non-normalized) edge betweenness for every edge in graph G
# Since the graph is undirected, assume that each shortest path from a to b is 
# the same as from b to a, and so we only count one direction
def edge_betweenness(G):
	# Betweenness score for each edge, to be added up and returned
	bw = { (a,b) : 0 for (a,b) in tuple(G.edges()) }

	# Do something for each source...
	for s in G.nodes():
		#--------------------------------------------------------------------------
		#BFS approach
		shortest_paths(E, s)



		#---------------------------------------------------------------------------
	# 	i = 0
	# 	for edge in G.edges:
	# 		if s in edge:
	# 			i = i + 1
	#
	# 		bw.update({edge: bw.get(edge) + i})
		#######################
		# ... XXX: TODO q1 Implement me
		#######################




		pass
		
	# Normalize back since we looked at every directed pair of nodes
	return bw



# Girvan Newman hierarchical clustering method
def girvan_newman(Gorig):
	# Ensure we don't mess up the original graph, take a copy
	G = Gorig.copy()
	res = []

	# Repeatedly remove the highest valued note w.r.t. edge betweenness.
	while G.number_of_edges() > 0:
		#######################
		# ... XXX:TODO q2 Implement me
		#######################

		pass

	# Edge list of the decomposition
	# res = [ (v1,v2,bw1), (v3,v4,bw2), ... ] means the edge (v1,v2) was removed 
	# first with edge betweenness value of bw1, followed by the edge (v3,v4), and so forth.
	return res


if __name__ == "__main__":
	print ("Run: python3 eval.py instead.")


