#!/usr/bin/env python3

import sys
import math

from common import print_tour, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def cal_path_length(cities, tour):
    N = len(cities)
    return sum(distance(cities[tour[i]], cities[tour[(i + 1) % N]]) for i in range(N))


def greedy(cities, current_city):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    unvisited_cities = set(range(0, N))
    unvisited_cities.remove(current_city)
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    return tour, dist


def two_opt(tour, dist):
    N = len(tour)
    while True:
        cnt = 0
        for i in range(N - 2):
            for j in range(i + 2, N):
                if i != 0 or (j + 1) % N != 0:
                    l1 = dist[tour[i]][tour[i + 1]]
                    l2 = dist[tour[j]][tour[(j + 1) % N]]
                    l3 = dist[tour[i]][tour[j]]
                    l4 = dist[tour[i + 1]][tour[(j + 1) % N]]
                    if l1 + l2 > l3 + l4:
                        tour[i + 1:j + 1] = tour[i + 1:j + 1][::-1]
                        cnt += 1
        if cnt == 0:
            break

    return tour


def change_start(cities):
    N = len(cities)
    min_tour = []
    min_path_length = 10**100
    for i in range(N):
        temp_tour, dist = greedy(cities, i)
        temp_tour = two_opt(temp_tour, dist)
        temp_path_length = cal_path_length(cities, temp_tour)
        if temp_path_length < min_path_length:
            min_tour = temp_tour
            min_path_length = temp_path_length
    return min_tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    cities = read_input(sys.argv[1])
    tour = change_start(cities)
    print_tour(tour)
