from collections import deque


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


def bfs(pages_id_to_title: dict, pages_title_to_id: dict, links: dict, start: str, target: str):
    queue = deque()
    distance = {}
    before_node = {}
    start_node = pages_title_to_id[start]
    target_node = pages_title_to_id[target]

    # if node is checked, it is not -1
    for key in pages_id_to_title:
        distance[key] = -1

    distance[start_node] = 0
    queue.append(start_node)

    while queue:
        current_node = queue.popleft()

        if current_node == target_node:
            path, distance = show_path(pages_id_to_title, before_node, distance, target_node, start_node)
            return path, distance

        if current_node in links:
            for linked_node in links[current_node]:
                if distance[linked_node] != -1:
                    continue
                distance[linked_node] = distance[current_node] + 1
                before_node[linked_node] = current_node
                queue.append(linked_node)

    return None, None


def show_path(pages_id_to_title, before_node, distance, target_node, start_node):
    temp_node = target_node
    path = [pages_id_to_title[temp_node]]
    while (temp_node != start_node):
        path.append(pages_id_to_title[before_node[temp_node]])
        temp_node = before_node[temp_node]
    return path[::-1], distance[target_node]


def main():
    # You can change start and target here
    start = "Google"
    target = "渋谷"

    pages_key_id, pages_key_title = read_pages('data/pages.txt')
    links = read_links('data/links.txt')
    path, distance = bfs(pages_key_id, pages_key_title, links, start, target)

    if path is None and distance is None:
        print("Cannot find path from " + start + " to " + target)
    else:
        print(" -> ".join(path))
        print("Shortest distance from " + start + " to " + target + " is: " + str(distance))


if __name__ == '__main__':
    main()
