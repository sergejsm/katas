import itertools

def fight(robot_1, robot_2, tactics):
    current, second = (robot_1, robot_2) if robot_1["speed"] >= robot_2["speed"] else (robot_2, robot_1)

    while current['tactics'] or second['tactics']:
        try:
            second['health'] -= tactics[current['tactics'].pop(0)]
        except IndexError:
            pass

        if second['health'] <= 0:
            return f'{current["name"]} has won the fight.'

        current, second = second, current

    if current["health"] == second["health"]:
        return "The fight was a draw."

    winner = current if current["health"] > second["health"] else second
    return f"{winner['name']} has won the fight."




robot_1 = {
    "name": "Rocky",
    "health": 100,
    "speed": 20,
    "tactics": ["punch", "punch", "laser", "missile"]
}
robot_2 = {
    "name": "Missile Bob",
    "health": 100,
    "speed": 21,
    "tactics": ["missile", "missile", "missile", "missile"]
}
tactics = {
    "punch": 20,
    "laser": 30,
    "missile": 35
}

print(fight(robot_1, robot_2, tactics))