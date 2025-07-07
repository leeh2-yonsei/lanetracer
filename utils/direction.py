def get_direction(vector) -> int:
    if vector[0] >= 0.5:
        return 0
    elif vector[0] >= -0.5:
        return 1
    else:
        return 2