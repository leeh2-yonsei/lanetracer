def get_direction(vector) -> (int, str):
    if vector[0] >= 0.5:
        return 0, 'right'
    elif vector[0] >= -0.5:
        return 1, 'straight'
    else:
        return 2, 'left'