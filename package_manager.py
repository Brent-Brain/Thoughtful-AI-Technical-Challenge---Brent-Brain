MAX_VOLUME = 1000000
HEAVY_MASS = 20
INDIVIDUAL_DIMENSION_THRESHOLD = 150


def sort(width, height, length, mass):
    # Separating checks out to provide more verbose error logging

    # NOTE: I set the logic to reject values equal to 0 as invalid. It was not specified in the requirements but it seemed logical to assume that a package cannot have zero dimensions or mass.
    checks = {
        "width_valid": isinstance(width, (int,float)) and width > 0,
        "height_valid": isinstance(height, (int,float)) and height > 0,
        "length_valid": isinstance(length, (int,float)) and length > 0,
        "mass_valid": isinstance(mass, (int,float)) and mass > 0,
    }

    if not all(checks.values()):
        raise ValueError(f"Invalid dimensions or mass provided: {checks}")

    volume = width * height * length
    is_heavy = mass >= HEAVY_MASS
    is_bulky = volume >= MAX_VOLUME or any(dim >= INDIVIDUAL_DIMENSION_THRESHOLD for dim in (width, height, length))

    if is_heavy and is_bulky:
        return "REJECTED"
    elif is_heavy or is_bulky:
        return "SPECIAL"
    else:
        return "STANDARD"
