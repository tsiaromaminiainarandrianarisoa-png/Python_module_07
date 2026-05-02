import ex0

flame_factory = ex0.FlameFactory()
aqua_factory = ex0.AquaFactory()

def test_factory(factory: ex0.CreatureFactory) -> None:
	print("Testing factory")
	base = factory.create_base()
	print(base.describe())
	print(base.attack())
	evolved = factory.create_evolved()
	print(evolved.describe())
	print(f"{evolved.attack()}\n")

test_factory(flame_factory)
test_factory(aqua_factory)

def make_em_fight(flame: ex0.CreatureFactory, aqua: ex0.CreatureFactory) -> None:
	print("Testing battle")
	base_flame = flame.create_base()
	base_aqua = aqua.create_base()
	print(f"{base_flame.describe()}\n vs.\n{base_aqua.describe()}")
	print(" fight!")
	print(base_flame.attack())
	print(base_aqua.attack())

make_em_fight(flame_factory, aqua_factory)
