from abc import ABC, abstractmethod
from ex0.factory import Creature
from ex1.capabilities import HealCapability, TransformCapability


class StrategyFail(Exception):
    def __init__(self, msg: str = "Strategy is not compatible") -> None:
        super().__init__(msg)


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, beast: Creature) -> list[str]: ...

    @abstractmethod
    def is_valid(self, beast: Creature) -> bool: ...


class NormalStrategy(BattleStrategy):
    def act(self, beast: Creature) -> list[str]:
        if not self.is_valid(beast):
            raise StrategyFail
        return [beast.attack()]

    def is_valid(self, beast: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, beast: Creature) -> list[str]:
        if not self.is_valid(beast):
            raise StrategyFail(
                f"Invalid Creature '{beast.name}' for this aggressive strategy"
                )
        return [
            beast.transform(),  # type: ignore
            beast.attack(),
            beast.revert()  # type: ignore
            ]

    def is_valid(self, beast: Creature) -> bool:
        if isinstance(beast, TransformCapability):
            return True
        else:
            return False


class DefensiveStrategy(BattleStrategy):
    def act(self, beast: Creature) -> list[str]:
        if not self.is_valid(beast):
            raise StrategyFail(
                f"Invalid Creature '{beast.name}' for this defensive strategy"
                )
        return [beast.attack(), beast.heal()]  # type: ignore

    def is_valid(self, beast: Creature) -> bool:
        if isinstance(beast, HealCapability):
            return True
        else:
            return False
