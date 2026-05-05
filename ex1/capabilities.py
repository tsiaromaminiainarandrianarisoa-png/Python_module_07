from abc import ABC, abstractmethod
import ex0.creature_factory as factory

class HealCapability(ABC):
	@abstractmethod
	def heal(self, target: str) -> str:
		pass

class TransformCapability(ABC):
	@abstractmethod
	def transform(self) -> str:
		pass
	@abstractmethod
	def	revert(self) -> str:
		pass

class Sproutling(factory.Creature, HealCapability):
	def __init__(self, name: str, creature_type: str) -> None:
		super().__init__(name, creature_type)

	def attack(self) -> str:
		return f"{self._name} uses Vine Whip!"
	def heal(self, target: str) -> str:
		return f"{self._name} heals {target} for a small amount"

class Bloomelle(factory.Creature, HealCapability):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)

    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"
    def heal(self, target: str) -> str:
        return f"{self._name} heals {target} for a large amount"

class HealingCreatureFactory(factory.CreatureFactory):
	def create_base(self) -> factory.Creature:
		return Sproutling("Sproutling", "Grass")
	def create_evolved(self) -> factory.Creature:
		return Bloomelle("Bloomelle", "Grass/Fairy")

class Shiftling(factory.Creature, TransformCapability):
	def __init__(self, name: str, creature_type: str)-> None:
		super().__init__(name, creature_type)
		self.state = "attacks normally."

	def attack(self) -> str:
		return f"{self._name} {self.state}"
	def transform(self) -> str:
		self.state = "performs a boosted strike!"
		return f"{self._name} shifts into a sharper form!"
	def revert(self) -> str:
		self.state = "attacks normally."
		return f"{self._name} returns to normal."

class Morphagon(factory.Creature, TransformCapability):
	def __init__(self, name: str, creature_type: str)-> None:
		super().__init__(name, creature_type)
		self.state = "attacks normally."

	def attack(self) -> str:
		return f"{self._name} {self.state}"
	def transform(self) -> str:
		self.state = "unleashes a devastating morph strike!"
		return f"{self._name} morphs into a dragonic battle form!"
	def revert(self) -> str:
		self.state = "attacks normally."
		return f"{self._name} stabilizes its form."

class TransformCreatureFactory(factory.CreatureFactory):
	def create_base(self) -> factory.Creature:
		return Shiftling("Shiftling", "Normal")
	def create_evolved(self) -> factory.Creature:
		return Morphagon("Morphagon", "Normal/Dragon")
