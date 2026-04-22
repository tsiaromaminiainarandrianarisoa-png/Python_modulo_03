import sys

def check_param(param, stock)->list:
	item = param.split(":")
	if len(item) != 2:
		raise ValueError(f"Error - invalid parameter '{param}'")

	try:
		check_redundant = stock[item[0]]
	except KeyError:
		pass
	else:
		raise ValueError(f"Redundant item '{item[0]}' - discarding")

	try:
		nbr_check = int(item[1])
	except ValueError as error:
		raise ValueError(f"Quantity error for '{item[0]}': {error}")
	return item

def stock_items()-> dict:
	stock = {}
	items = sys.argv[1:]
	for item in items:
		try:
			valid_item = check_param(item, stock)
		except ValueError as error:
			print(f"{error}")
		else:
			key = valid_item[0]
			value = int(valid_item[1])
			stock.update({key: value})
	return stock

def inventory_operation()-> None:
	print("=== Inventory System Analysis ===\n")
	stock = stock_items()
	print(f"Got inventory: {stock}")
	print(f"Item list: {stock.keys()}")
	total = sum(stock.values())
	print(f"Total quantity of the {len(stock)} items: {total}")
	for item in stock:
		print(f"Item {item} represents: {round(((stock[item] / total )* 100), 1)}%")
	print(f"Item most abundant:  with quantity ")
	print(f"Item least abundant:  with quantity ")
	stock.update({"magic_item":1})
	print(f"Updated inventory: {stock}")

if __name__ == "__main__":
	inventory_operation()
