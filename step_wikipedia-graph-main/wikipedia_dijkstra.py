import heapq


def read_pages(file_path):
    pages_id_to_title = {}
    pages_title_to_id = {}
    with open(file_path) as f:
        for data in f.read().splitlines():
            page = data.split('\t')
            # page[0]: id, page[1]: title
            pages_id_to_title[page[0]] = page[1]
            pages_title_to_id[page[1]] = page[0]
    return pages_id_to_title, pages_title_to_id


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


def show_path(pages_id_to_title, before_node, distance, target_node, start_node):
    temp_node = target_node
    path = [pages_id_to_title[temp_node]]
    while (temp_node != start_node):
        if before_node[temp_node] is None:
            return None, None
        path.append(pages_id_to_title[before_node[temp_node]])
        temp_node = before_node[temp_node]

    return path[::-1], distance[target_node]


def dijkstra(pages_id_to_title, pages_title_to_id, links, start, target):
    INF = 10 ** 9
    start_node = pages_title_to_id[start]
    target_node = pages_title_to_id[target]
    distance = {id: INF for id in pages_id_to_title.keys()}
    distance[start_node] = 0
    before_node = {id: None for id in pages_id_to_title.keys()}
    queue = [(0, start_node)]
    heapq.heapify(queue)

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # avoid nodes have seen
        if current_distance > distance[current_node]:
            continue

        if current_node in links:
            for link in links[current_node]:
                edge_distance = 1
                if distance[link] > edge_distance + distance[current_node]:
                    distance[link] = edge_distance + distance[current_node]
                    before_node[link] = current_node
                    heapq.heappush(queue, (distance[link], link))

    path, distance = show_path(pages_id_to_title, before_node, distance, target_node, start_node)
    return path, distance


def main():
    # You can change start and target here
    start = "Google"
    target = "渋谷"
    pages_key_id, pages_key_title = read_pages('data/pages.txt')
    links = read_links('data/links.txt')
    path, distance = dijkstra(pages_key_id, pages_key_title, links, start, target)

    if path is None and distance is None:
        print("Cannot find path from " + start + " to " + target)
    else:
        print(" -> ".join(path))
        print("Shortest distance from " + start + " to " + target + " is: " + str(distance))


if __name__ == '__main__':
    main()
