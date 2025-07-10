def get_direction(vector) -> (int, str):
    if vector[0] >= 0.5:
        return 2, 'right'
    elif vector[0] >= -0.5:
        return 1, 'straight'
    else:
        return 0, 'left'