import random as id_rng
class ID_Generator:
    ID_list = list(range(1000000))

    @classmethod
    def generateID(cls):
        ID = id_rng.choice(cls.ID_list)
        cls.ID_list.remove(ID)
        return ID