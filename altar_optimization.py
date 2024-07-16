
if __name__ == "__main__":
    from math import floor
  
    class Altar:
        def __init__(self, sec_p_pro, base_pro, delta_pro, base_stor, delta_stor, base_cost, delta_cost, curr_lvl=None):
            self._SecPerProduction: float = sec_p_pro
            self._BaseProduction: float = base_pro
            self._DeltaProduction: float = delta_pro
            self._BaseStorage: float = base_stor
            self._DeltaStorage: float = delta_stor
            self._BaseCost: float = base_cost
            self._DeltaCost: float = delta_cost

            self._Level: int = 1
            self._CurrProduction: int = 0
            self._CurrStorage: int = 0
            self._CurrCost: int = 0

            if curr_lvl is not None:
                self.set_level(curr_lvl)
            else:
                self.set_level(1)

        def _get_production(self, lvl: int) -> int:
            return floor(self._BaseProduction + self._DeltaProduction * (lvl - 1))

        def _get_storage(self, lvl: int) -> int:
            return floor(self._BaseStorage + self._DeltaStorage * (lvl - 1))

        def _get_cost(self, lvl: int) -> int:
            return floor(self._BaseCost * pow(self._DeltaCost, lvl - 1))

        def set_level(self, lvl: int):
            self._Level = lvl
            self._CurrProduction = self._get_production(lvl)
            self._CurrStorage = self._get_storage(lvl)
            self._CurrCost = self._get_cost(lvl)

        def calc_lvlup_effeciency(self) -> float:
            curr_p_min_pro: float = (60.0 / self._SecPerProduction) * self._CurrProduction
            next_pro = self._CurrProduction + self._DeltaProduction
            next_p_min_pro: float = (60.0 / self._SecPerProduction) * next_pro

            cost_p_promin: float = (next_p_min_pro - curr_p_min_pro) / self._CurrCost
            return cost_p_promin

        def level_up(self):
            self.set_level(self._Level + 1)

        def get_cost(self) -> int:
            return self._CurrCost

        def get_lvl(self) -> int:
            return self._Level

    Beast = Altar(5, 6, 0.5, 5000, 1200, 100, 1.06, 47)
    """                                             ^       Modify the last # to be your current Beast Altar Lvl"""
    Library = Altar(15, 25, 2.5, 7000, 5000, 250, 1.08, 51)
    """                                                 ^   Modify the last # to be your current Library Altar Lvl"""
    Arcane = Altar(300, 230, 50, 8500, 6000, 1500, 1.08, 47)
    """                                                  ^  Modify the last # to be your current Arcane Altar Lvl"""

    essence = 843070 
    """       ^^^                                           Modify this to be your currently saved up essence"""
    affordable = True
    while floor(essence) > 0 and affordable:
        b = (Beast, Beast.calc_lvlup_effeciency())
        l = (Library, Library.calc_lvlup_effeciency())
        a = (Arcane, Arcane.calc_lvlup_effeciency())
        best: tuple = max((a, b, l), key=lambda pair: pair[1])
        if essence - best[0].get_cost() >= 0:
            essence -= best[0].get_cost()
            best[0].level_up()
        else:
            affordable = False

    print(f"Beast lvl {Beast.get_lvl()}, Library Lvl {Library.get_lvl()}, "
          f"Arcane Lvl {Arcane.get_lvl()}, remaining essence; {essence}")

