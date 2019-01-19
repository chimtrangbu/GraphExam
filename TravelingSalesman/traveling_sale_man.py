class City(object):
    def __init__(self, city):
        self.name = city[0]
        self.x = float(city[1])
        self.y = float(city[2])

    def cal_dist(self, city2):
        # calculating distance between 2 cities
        return ((self.x - city2.x) ** 2 + (self.y - city2.y) ** 2) ** 0.5


def cal_total_dist(path):
    # calculating total distance of the path
    total = 0
    if len(path) == 1:
        return 0
    for i in range(1, len(path)):
        total += path[i].cal_dist(path[i-1])
    return total


def parse_input(cities):
    # parse list cities
    if not cities:
        raise ValueError('Invalid value')
    cities_ls = []
    for city in cities:
        try:
            cities_ls.append(City(city))
        except Exception:
            raise Exception('Wrong input')
    return cities_ls


def nearest_neighbor(cities_ls):
        start = cities_ls[0]
        must_visit = cities_ls.copy()
        path = [start]
        must_visit.remove(start)
        while must_visit:
            nearest = must_visit[0]
            cur_node = path[-1]
            nearest = min(must_visit, key=lambda k: path[-1].cal_dist(k))
            path.append(nearest)
            must_visit.remove(nearest)
        return path


def two_opt(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    continue  # changes nothing, skip then
                new_route = route[:]
                # 2woptSwap
                new_route[i:j] = route[j - 1:i - 1:-1]
                if cal_total_dist(new_route) < cal_total_dist(best):
                    best = new_route
                    improved = True
        route = best
    return best


def traveling_sale_man(cities):
    cities_ls = parse_input(cities)
    path = nearest_neighbor(cities_ls)
    if len(path) < 500:
        path = two_opt(path)
    return ([c.name for c in path], cal_total_dist(path))
