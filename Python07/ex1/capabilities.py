from abc import ABC, abstractmethod
from ex0.factory import Creature, CreatureFactory


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature: pass
    def create_evolved(self) -> Creature: pass


class HealCapability(ABC):

    @abstractmethod
    def heal(self, target: "Creature | None " = None): pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.is_transformed: bool = False

    @abstractmethod
    def transform(self) -> str: pass

    @abstractmethod
    def revert(self) -> str: pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> Creature:
        super().__init__(name="Sproutling", creature_type="Grass")

    def heal(self, target: "Creature | None " = None) -> str:
        targ = target if target is not None else self
        return (f"Healing {targ}")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> Creature:
        super().__init__(name="Bloomelle", creature_type="Grass/Fairy")

    def heal(self, target: "Creature | None " = None) -> str:
        targ = target if target is not None else self
        return (f"Healing {targ}")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> Creature:
        super().__init__(name="Shiftling", creature_type="Normal")

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally"

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} shifts into a shaper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return "return to normal"


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> Creature:
        super().__init__(name="Morphagon", creature_type="Normal/Dragon")

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} unleashes a devastating morph strike"
        return f"{self.name} attacks normally"

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} morphs into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return "stabilizes its form"
