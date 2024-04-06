import random
import heapq

graph = {
    'A': {},
    'B': {},
    'C': {},
    'D': {},
    'E': {}
}


sp = ['A', 'E']
net_3 = ['D', 'B', 'C']

for i in sp:
    n_1 = random.choice(net_3)
    net_3.remove(n_1)
    n_2 = random.choice(net_3)
    net_3.append(n_1)

    count_1 = random.randint(3, 6)
    graph[i][n_1] = count_1
    graph[n_1][i] = count_1

    count_2 = random.randint(3, 6)
    graph[i][n_2] = count_2
    graph[n_2][i] = count_2

    n_1 = random.choice(net_3)
    net_3.remove(n_1)
    n_2 = random.choice(net_3)
    net_3.append(n_1)

    count_1 = random.randint(1, 4)
    graph[n_1][n_2] = count_1
    graph[n_2][n_1] = count_1


def dijkstra(graph, start, end):
    queue = []
    heapq.heappush(queue, (0, start))
    visited = set()

    while queue:
        cost, node = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            if node == end:
                return cost
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor))
    return float('inf')  # если путь не найден


def ex_4():
    test_list = {
        'data': [],
        'answer': []
    }

    shortest_path = dijkstra(graph, 'A', 'E')

    test_list['data'] = ['Между населенными пунктами А, В, С, D, Е, F построены дороги, протяженность которых '
                         'приведена в таблице:', graph, 'Определите длину кратчайшего пути между пунктами А и F. '
                                                        'Передвигаться можно только по дорогам, протяженность которых'
                                                        ' указана в таблице.']
    test_list['answer'] = [shortest_path]

    return test_list


print(ex_4())
