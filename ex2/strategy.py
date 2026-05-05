from abc import ABC, abstractmethod
import ex0.creature_factory as factory
from ex1.capabilities import HealCapability, TransformCapability

class BattleStrategy(ABC):
	@abstractmethod
	def act(self, creature: factory.Creature) -> None:
		pass
	@abstractmethod
	def is_valid(self, creature: factory.Creature) -> bool:
		pass

class NormalStrategy(BattleStrategy):
	def is_valid(self, creature: factory.Creature)-> bool:
		return True

	def act(self, creature: factory.Creature) -> None:
		print(creature.attack())

class AggressiveStrategy(BattleStrategy):
	def is_valid(self, creature: factory.Creature) -> bool:
		state = False
		if isinstance(creature, TransformCapability):
			state = True
		return state

	def act(self, creature: factory.Creature) -> None:
		if not self.is_valid(creature):
			raise Exception(f"Invalid Creature '{creature._name}' for this aggressive strategy")
		print(creature.transform())
		print(creature.attack())
		print(creature.revert())

class DefensiveStrategy(BattleStrategy):
	def is_valid(self, creature: factory.Creature) -> bool:
		state = False
		if isinstance(creature, HealCapability):
			state = True
		return state

	def act(self, creature: factory.Creature) -> None:
		if not self.is_valid(creature):
			raise Exception(f"Invalid Creature '{creature._name}' for this defensive strategy")
		print(creature.attack())
		print(creature.heal("itself"))
