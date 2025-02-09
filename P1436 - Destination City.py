from typing import List


def destCity(paths: List[List[str]]) -> str:
    cities = {}

    for city in paths:
        if city[0] not in cities:
            cities[city[0]] = 1
        else:
            cities[city[0]] = cities[city[0]] + 1

        if city[1] not in cities:
            cities[city[1]] = 1
        else:
            cities[city[1]] = cities[city[1]] + 1

    end = None

    for city in paths:
        if cities[city[1]] == 1:
            end = city[1]

    return end
