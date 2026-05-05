import ex0
import ex1
import ex2

factory_flame = ex0.FlameFactory()
factory_aqua = ex0.AquaFactory()
factory_heal = ex1.HealingCreatureFactory()
factory_trans = ex1.TransformCreatureFactory()

normal_strategy = ex2.strategy.NormalStrategy()
defensive_strategy = ex2.strategy.DefensiveStrategy()
aggressive_strategy = ex2.strategy.AggressiveStrategy()

def battle(opponents: list) -> None:
	print("*** Tournament ***")
	print(f"{len(opponents)} opponents involved")
	for n in range(len(opponents)):
		for opponent in opponents[:n]:
			print("\n* Battle *")
			creature_one = opponents[n][0].create_base()
			creature_two = opponent[0].create_base()
			print(f"{creature_two.describe()}")
			print(" vs.")
			print(f"{creature_one.describe()}")
			print("now fight!")
			try:
				opponent[1].act(creature_two)
				opponents[n][1].act(creature_one)
			except Exception as error:
				print(f"Battle error, aborting tournament: {error}")

print("Tournament 0 (basic)")
print("	[ (Flameling+Normal), (Healing+Defensive) ]")
first_opponents = [(factory_flame, normal_strategy), (factory_heal, defensive_strategy)]
battle(first_opponents)

print("\nTournament 1 (error)")
print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
second_opponents = [(factory_flame, aggressive_strategy), (factory_heal, defensive_strategy)]
battle(second_opponents)

print("\nTournament 2 (multiple)")
print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
third_opponents = [(factory_aqua, normal_strategy), (factory_heal, defensive_strategy), (factory_trans, aggressive_strategy)]
battle(third_opponents)
