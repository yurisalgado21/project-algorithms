def best_time_to_study(permanence_period, target_time: int) -> int:
    count_students = 0
    for period in permanence_period:
        if period[0] <= target_time <= period[1]:
            count_students += 1
    return count_students


def study_schedule(permanence_period, target_time: int) -> int:
    count_students = 0
    for period in permanence_period:
        for value in period:
            if not isinstance(value, int) or target_time is None:
                # print("caiu aqui")
                return None
    count_students = best_time_to_study(permanence_period, target_time)
    return count_students


print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 5))
