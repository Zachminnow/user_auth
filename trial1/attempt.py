class NoLowercaseAttribute(type):
    def __new__(cls, name, bases, dct):
        for attr in dct:
            if attr.startwith('_'):
                continue
            if attr.lower() == attr:
                raise ValueError(f"Attribute '{attr}' must be uppercase")
        return super().__mew__(cls, name, bases, dct)


# Ok
class Constants(mataclass=NoLowercaseAttribute):
    MAX = 10
    VALUE = 20
    