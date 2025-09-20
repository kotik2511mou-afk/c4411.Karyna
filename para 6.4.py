class BildingError(Exception):
    def __str__(self):
        return f"With so much material the house connot be built!"
def checker_material(amount_of_material, limit_value):
    if amount_of_material > limit_value:
        return "Enough material"
    else:
        raise BildingError (amount_of_material)
    material = 123
    checker_material(material,300)