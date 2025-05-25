#Definisi Fungsi
def dfs_recursive(graph, node, goal, visited=None, path=None):
    #node=yang dikunjungi, visited=node yang sudah dilewati, path=jalan yang dilewati
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(node)
    path.append(node)  

    if node == goal:
        print(" -> ".join(path))  
        return True  

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs_recursive(graph, neighbor, goal, visited, path):
                return True  

    path.pop()  #DFS iteratif
    return False  

# Adjacency List
graph = {
    'Oradea': ['Zerind', 'Sibiu'],
    'Zerind': ['Arad', 'Oradea'],
    'Arad': ['Timisoara', 'Sibiu', 'Zerind'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Dobreta': ['Mehadia', 'Craiova'],
    'Sibiu' : ['Oradea', 'Arad', 'Fagaras', 'Rimnicu Vilcea'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Craiova': ['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Neamt' : ['Iasi'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Iasi': ['Neamt', 'Vaslui'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova']
}

#User Input Data
start = input("Masukkan Kota Asal: ")
goal = input("Masukkan Kota Tujuan: ")

#Output
if start not in graph:
    print("Kota Asal Tidak Ditemukan di Rumania")
elif goal not in graph:
    print("Kota Tujuan Tidak Ditemukan di Rumania")
else:
    print(f"Jalur dari {start} ke {goal} adalah:")
    if not dfs_recursive(graph, start, goal):
        print("Jalan Menuju Kota Tujuan Tidak Ditemukan")