# Base Class: MusicInstrument
class MusicInstrument:
    def __init__(self, name, category, material):
        self.name = name
        self.category = category
        self.material = material

    def play(self):
        return f"The {self.name} is being played."

    def describe(self):
        return f"The {self.name} is a {self.category} instrument made of {self.material}."

# Subclass: StringInstrument
class StringInstrument(MusicInstrument):
    def __init__(self, name, material, string_count):
        super().__init__(name, "String", material)
        self.string_count = string_count

    def play(self):
        return f"The {self.name} is strummed or bowed, producing beautiful melodies."

    def tune(self):
        return f"Tuning the {self.string_count} strings of the {self.name}."

# Example Usage
flute = MusicInstrument("Flute", "Wind", "Metal")
guitar = StringInstrument("Guitar", "Wood", 6)

print(flute.describe())
print(flute.play())
print(guitar.describe())
print(guitar.play())
print(guitar.tune())
