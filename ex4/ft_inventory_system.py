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
	stock: dict[str, int] = {}
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
	print(f"Item list: {list(stock.keys())}")
	total = sum(stock.values())
	print(f"Total quantity of the {len(stock)} items: {total}")
	max_q = 0
	min_q = total
	for item in stock:
		print(f"Item {item} represents {round(((stock[item] / total )* 100), 1)}%")
		if stock[item] > max_q:
			max_q = stock[item]
			max_item = item
		if stock[item] < min_q:
			min_q = stock[item]
			min_item = item
	if len(stock) != 0:		
		print(f"Item most abundant: {max_item} with quantity {max_q}")
		print(f"Item least abundant: {min_item} with quantity {min_q}")
	stock.update({"magic_item":1})
	print(f"Updated inventory: {stock}")

if __name__ == "__main__":
	inventory_operation()
