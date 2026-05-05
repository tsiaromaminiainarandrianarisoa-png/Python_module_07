import ex1
from ex0.creature_factory import Creature

heal_creature_factory = ex1.HealingCreatureFactory()
print("Testing Creature with healing capability")
print(" base:")
base = heal_creature_factory.create_base()
print(base.describe())
print(base.attack())
print(base.heal("itself"))

print(" evolved:")
evolved = heal_creature_factory.create_evolved()
print(evolved.describe())
print(evolved.attack())
print(evolved.heal("itself and others"))
print()
trans_creature_factory = ex1.TransformCreatureFactory()
print("Testing Creature with transform capability")
creatures = (trans_creature_factory.create_base(), trans_creature_factory.create_evolved())
def actions(creature: Creature)-> None:
	print(creature.describe())
	print(creature.attack())
	print(creature.transform())
	print(creature.attack())
	print(creature.revert())

print(f" base:")
actions(creatures[0])
print(f" evolved:")
actions(creatures[1])
