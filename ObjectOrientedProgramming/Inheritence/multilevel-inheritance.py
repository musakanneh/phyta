class Music:
    name = "Jazz"


class Instrument(Music):
    color = "Yellow"


class Features(Instrument):
    def __init__(self):
        if self.name and self.color:
            print("There is a music called {} with {} color cover".format(
                self.name, self.color))


music_features = Features()
