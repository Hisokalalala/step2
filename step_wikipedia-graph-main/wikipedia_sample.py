from collections import deque


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


def bfs(pages_key_is_id: dict, pages_key_is_title: dict, links: dict, start: str, target: str):
    container = deque()
    shortest_path = {}
    before_node = {}
    start_node = pages_key_is_title[start]
    target_node = pages_key_is_title[target]

    # if node is checked, it is not -1
    for key in pages_key_is_id:
        shortest_path[key] = -1

    shortest_path[start_node] = 0
    container.append(start_node)

    while container:
        now_node = container.popleft()

        if now_node == target_node:
            temp_node = target_node
            path = [pages_key_is_id[temp_node]]
            while (temp_node != start_node):
                path.append(pages_key_is_id[before_node[temp_node]])
                temp_node = before_node[temp_node]
            return path[::-1], shortest_path[target_node]

        if now_node in links:
            for linked_node in links[now_node]:
                if shortest_path[linked_node] != -1:
                    continue
                shortest_path[linked_node] = shortest_path[now_node] + 1
                before_node[linked_node] = now_node
                container.append(linked_node)

    return None, None


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
