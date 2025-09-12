class AC:
    def cool_wind(self):
        pass

    def heat_wind(self):
        pass

    def swing_l_r(self):
        pass


class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")

    def heat_wind(self):
        print("美的空调制热")

    def swing_l_r(self):
        print("美的空调左右摆风")


class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def heat_wind(self):
        print("格力空调制热")

    def swing_l_r(self):
        print("格力空调左右摆风")


def make_cool(ac: AC):
    ac.cool_wind()


midea_ac = Midea_AC()
gree_ac = GREE_AC()

make_cool(midea_ac)
make_cool(gree_ac)
