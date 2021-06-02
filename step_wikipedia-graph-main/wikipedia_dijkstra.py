from collections import deque
import heapq
import time


def read_pages(file_path):
    pages_key_is_id = {}
    pages_key_is_title = {}
    with open(file_path) as f:
        for data in f.read().splitlines():
            page = data.split('\t')
            # page[0]: id, page[1]: title
            pages_key_is_id[page[0]] = page[1]
            pages_key_is_title[page[1]] = page[0]
    return pages_key_is_id, pages_key_is_title


def read_links(file_path):
    links = {}
    with open(file_path) as f:
        for data in f.read().splitlines():
            link = data.split('\t')
            # link[0]: id (from), links[1]: id (to)
            if link[0] in links:
                links[link[0]].add(link[1])
            else:
                links[link[0]] = {link[1]}
    return links


def dijkstra(pages_key_is_id, pages_key_is_title, links, start, target):
    INF = 10 ** 9
    start_node = pages_key_is_title[start]
    target_node = pages_key_is_title[target]
    distance = {id: INF for id in pages_key_is_id.keys()}
    distance[start_node] = 0
    before_node = {id: None for id in pages_key_is_id.keys()}
    queue = [(0, start_node)]
    heapq.heapify(queue)

    while queue:
        now_length, now_node = heapq.heappop(queue)

        # avoid nodes have seen
        if now_length > distance[now_node]:
            continue

        if now_node in links:
            for link in links[now_node]:
                edge_length = 1
                if distance[link] > edge_length + distance[now_node]:
                    distance[link] = edge_length + distance[now_node]
                    before_node[link] = now_node
                    heapq.heappush(queue, (distance[link], link))

    temp_node = target_node
    path = [pages_key_is_id[temp_node]]
    while (temp_node != start_node):
        if before_node[temp_node] is None:
            return None, None
        path.append(pages_key_is_id[before_node[temp_node]])
        temp_node = before_node[temp_node]

    return path[::-1], distance[target_node]


def main():
    # You can change start and target here
    start = "Google"
    target = "渋谷"
    s = time.time()
    pages_key_id, pages_key_title = read_pages('data/pages.txt')
    links = read_links('data/links.txt')
    m = time.time()
    print(m-s)
    path, distance = dijkstra(pages_key_id, pages_key_title, links, start, target)
    e = time.time()
    print(e-m)

    if path is None and distance is None:
        print("Cannot find path from " + start + " to " + target)
    else:
        print(" -> ".join(path))
        print("Shortest distance from " + start + " to " + target + " is: " + str(distance))


if __name__ == '__main__':
    main()
