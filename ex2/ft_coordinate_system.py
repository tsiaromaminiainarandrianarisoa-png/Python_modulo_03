import math

def raise_error(coordinates)-> None:
	if (len(coordinates) != 3):
		raise ValueError("Invalid syntax")

def get_pos() -> list:
	try :
		coordinates = input("Enter new coordinates as floats in format 'x,y,z': ").split(",")
		raise_error(coordinates)
	except ValueError as error:
			print(f"{error}")
			coordinates = get_pos()
	try :
		loc = 0
		for info in coordinates:
			coordinates[loc] = float(info)
			loc += 1
	except ValueError as error:
		print(f"Error on parameter '{info}': {error}")
		coordinates = get_pos()
	return coordinates

def get_player_pos() -> tuple:
	coordinates = get_pos()
	return tuple(coordinates)

def coordinate_system()-> None:
	print("=== Game Coordinate System ===")
	print("\nGet a first set of coordinates")
	set1 = get_player_pos()
	print(f"Got a first tuple: {set1}")
	x1 = set1[0]
	y1 = set1[1]
	z1 = set1[2]
	print(f"It includes: X={round(x1, 1)}, Y={round(y1,1)}, Z={round(z1, 1)}")
	distance = math.sqrt((set1[0])**2 + (set1[1])**2 + (set1[2])**2)
	print(f"Distance to center: {round(distance, 4)}")

	print("\nGet a second set of coordinates")
	set2 = get_player_pos()
	x2 = set2[0]
	y2 = set2[1]
	z2 = set2[2]
	distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
	print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")

if __name__ == "__main__":
	coordinate_system()
