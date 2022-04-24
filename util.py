

def limit(num: int, lower_bound: int, upper_bound: int) -> int:
    return min(max(num, lower_bound), upper_bound)


def area_of_frame(x: int, y: int, frame_size: int, upper_bound_x: int, upper_bound_y: int):
    return (limit(x + frame_size // 2, 0, upper_bound_x) - limit(x - frame_size // 2, 0, upper_bound_x) + 1) * \
           (limit(y + frame_size // 2, 0, upper_bound_y) - limit(y - frame_size // 2, 0, upper_bound_y) + 1)
