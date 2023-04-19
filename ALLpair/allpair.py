INF = 1000000000
def floyd_warshall(vertex, adjacency_matrix):
	# calculating all pair shortest path
	for k in range(0, vertex):
		for i in range(0, vertex):
			for j in range(0, vertex):
				
				adjacency_matrix[i][j] = min(adjacency_matrix[i][j], adjacency_matrix[i][k] + adjacency_matrix[k][j])
	# pretty print the graph
	# o/d means the leftmost row is the origin vertex
	# and the topmost column as destination vertex
	print("n", end='')
	for i in range(0, vertex):
		print("\t{:d}".format(i+1), end='')
	print();
	for i in range(0, vertex):
		print("{:d}".format(i+1), end='')
		for j in range(0,vertex):
			print("\t{:d}".format(adjacency_matrix[i][j]), end='')
		print();
"""
input is given as adjacency matrix,
input represents this undirected graph
 A--3--B----8---A
 |     |
 7      2
 |     |
 |      |
 D--INF--C---5--A
should set infinite value for each pair of vertex that has no edge
 """
adjacency_matrix = [
					[  0,   3, INF, 7],
					[  8,   0, 2, INF],
					[  5,   INF, 0,   1],
					[2, INF, INF,   0]
					]
floyd_warshall(4, adjacency_matrix);
# All_pair shortest path via 4 vertex