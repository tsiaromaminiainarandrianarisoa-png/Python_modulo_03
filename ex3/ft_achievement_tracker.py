import random

def gen_player_achievements()->set:
	achievements = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer']
	k = random.randint(1,13)
	p_achievements = set(random.sample(achievements, k))
	return p_achievements

def achievement_tracker()->None:
	print("=== Achievement Tracker System ===\n")
	
	alice_achievements = gen_player_achievements()
	print(f"Player Alice: {alice_achievements}")
	bob_achievements = gen_player_achievements()
	print(f"Player Bob: {bob_achievements}")
	charlie_achievements = gen_player_achievements()
	print(f"Player Charlie: {charlie_achievements}")
	dylan_achievements = gen_player_achievements()
	print(f"Player Dylan: {dylan_achievements}")

	union = set.union(alice_achievements, bob_achievements, charlie_achievements, dylan_achievements)
	print(f"\nAll distinct achievements: {union}")
	comm = set.intersection(alice_achievements, bob_achievements, charlie_achievements, dylan_achievements)
	print(f"\nCommon achievements: {comm}\n")

	other1 = set.union(bob_achievements, charlie_achievements, dylan_achievements)
	print(f"Only Alice has: {(alice_achievements.difference(other1))}")
	other2 = set.union(alice_achievements, charlie_achievements, dylan_achievements)
	print(f"Only Bob has: {(bob_achievements.difference(other2))}")
	other3 = set.union(bob_achievements, alice_achievements, dylan_achievements)
	print(f"Only Charlie has: {(charlie_achievements.difference(other3))}")
	other4 = set.union(bob_achievements, charlie_achievements, alice_achievements)
	print(f"Only Dylan has: {(dylan_achievements.difference(other4))}")

	print("")
	print(f"Alice is missing: {(other1.difference(alice_achievements))}")
	print(f"Bob is missing: {(other2.difference(bob_achievements))}")
	print(f"Charlie is missing: {(other3.difference(charlie_achievements))}")
	print(f"Dylan is missing: {(other4.difference(dylan_achievements))}")

if __name__ == "__main__":
	achievement_tracker()
