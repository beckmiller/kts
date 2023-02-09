__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    time_components = []
    time_components.append(str(seconds % 60).zfill(2) + "s")
    seconds = seconds // 60
    if seconds == 0:
        return time_components[-1]

    time_components.append(str(seconds % 60).zfill(2) + "m")
    seconds = seconds // 60
    if seconds == 0:
        return "".join(reversed(time_components))

    time_components.append(str(seconds % 24).zfill(2) + "h")
    seconds = seconds // 24
    if seconds == 0:
        return "".join(reversed(time_components))

    time_components.append(str(seconds).zfill(2) + "d")
    return "".join(reversed(time_components))




