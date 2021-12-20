def greedy_alg_for_stations_covering(stations_d, target_states_s):
    """
    The input type of 'stations_d' should be dict. The input type of 'target_states_s' should be set.
    Strategy: going through every station and pick the 'best_station' that covers the most uncovered states.
    """
    if not isinstance(stations_d, dict) or not isinstance(target_states_s, set):
        raise TypeError("The input type has to be instances of (dict, set).")
    final_stations_s = set()
    target_states_s = target_states_s.copy()
    while target_states_s:
        best_station = None
        states_covered_s = set()  # a set of all the states this station covers that have not been covered yet
        for station, states_for_station in stations_d.items():
            covered_s = target_states_s & states_for_station  # the set of uncovered states that this station covers
            if len(covered_s) > len(states_covered_s):
                best_station = station
                states_covered_s = covered_s
        target_states_s -= states_covered_s
        final_stations_s.add(best_station)
    return final_stations_s


if __name__ == '__main__':
    states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
    stations = {"kone": {"id", "nv", "ut"}, "ktwo": {"wa", "id", "mt"}, "kthree": {"or", "nv", "ca"},
                "kfour": {"nv", "ut"}, "kfive": {"ca", "az"}}

    final_stations = greedy_alg_for_stations_covering(stations, states_needed)
    print(final_stations)
