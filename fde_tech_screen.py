import sys

def sort(width, height, length, mass):
    #assume width, height and length are in cm. Assume mass is already in kg	
    volume = width * height * length
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <width> <height> <length> <mass>")
        sys.exit(1)

    try:
        width = float(sys.argv[1])
        height = float(sys.argv[2])
        length = float(sys.argv[3])
        mass = float(sys.argv[4])
    except ValueError:
        print("All arguments must be numbers (width, height, length in cm; mass in kg).")
        sys.exit(1)
        
    result = sort(width, height, length, mass)
    print(f"The package is classified as: {result}")

