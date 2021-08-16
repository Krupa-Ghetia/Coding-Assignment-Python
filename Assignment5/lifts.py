import random


number_of_floors = 20
number_of_lifts = 5
lift_movement_status = ["U", "D", ""]
lift_positions = []
lift_distances = []


def initialize_lift_positions():
    for lift_count in range(5):
        lift_positions.append(str(random.randint(0, 20)) + random.choice(lift_movement_status))


def validate_input(user_request):

    if not len(user_request):
        raise Exception("Invalid request!")

    if str.isdigit(user_request):
        raise Exception("You need to specify the direction!")

    if user_request[-1] not in lift_movement_status:
        raise Exception("Invalid direction!")

    if int(user_request[0:-1]) > 20:
        raise Exception("Invalid floor!")


def allot_lift(user_request):

    validate_input(user_request)

    user_floor, user_direction = int(user_request[0:-1]), user_request[-1]

    if user_floor > 20:
        raise Exception("Invalid floor!")

    compute_lift_distances(user_floor, user_direction)

    least_distance_index = lift_distances.index(min(lift_distances))

    return least_distance_index + 1


def compute_lift_distances(user_floor, user_direction):
    for position in lift_positions:
        if str.isdigit(position):
            lift_floor, lift_direction = int(position), ""
        else:
            lift_floor, lift_direction = int(position[0:-1]), position[-1]

        # Lift and user are on the same floor
        if lift_floor == user_floor:
            lift_distances.append(0)
            continue

        # Lift is idle
        if lift_direction == "":
            lift_distances.append(abs(user_floor - lift_floor))
            continue

        # User travels down and lift travels up
        if user_direction == "D" and lift_direction == "U":
            lift_distances.append((number_of_floors - lift_floor) + (number_of_floors - user_floor))
            continue

        # User travels up and lift travels down
        if user_direction == "U" and lift_direction == "D":
            lift_distances.append(lift_floor + user_floor)
            continue

        # User and lift travel downward
        if user_direction =="D" and lift_direction == "D":
            if user_floor < lift_floor:
                lift_distances.append(lift_floor - user_floor)

            if user_floor > lift_floor:
                lift_distances.append(lift_floor + user_floor)
                continue

        # User and lift travel upward
        if user_direction == "U" and lift_direction == "U":
            if user_floor < lift_floor:
                lift_distances.append((number_of_floors - lift_floor) + (number_of_floors - user_floor))
            if user_floor > lift_floor:
                lift_distances.append(user_floor - lift_floor)
                continue


if __name__ == "__main__":
    initialize_lift_positions()
    print(f"""Following are the lift positions: {lift_positions}""")
    user_request = input("Enter a request? ").upper()

    try:
        alloted_lift = allot_lift(user_request)

    except Exception as e:
        print(e)

    print(f"""Lift #{alloted_lift} will be coming to receive you.""")


