class JuegoBolos:
    def __init__(self):
        self.rolls: list[int] = []

    def roll(self, pines: int):
        self.rolls.append(pines)

    def puntaje(self):
        puntaje_total = 0
        numero_frame = 0
        for frame in range(10):
            if self.es_strike(numero_frame):
                puntaje_total += 10 + self.bono_strike(numero_frame)
                numero_frame += 1
            elif self.es_spare(numero_frame):
                puntaje_total += 10 + self.bono_spare(numero_frame)
                numero_frame += 2
            else:
                puntaje_total += self.puntaje_frame(numero_frame)
                numero_frame += 2

        if numero_frame < len(self.rolls):
            puntaje_total += self.rolls[numero_frame] + self.rolls[numero_frame + 1]
            
        return puntaje_total

    def es_strike(self, numero_frame: int):
        if numero_frame < len(self.rolls):
            return self.rolls[numero_frame] == 10
        else:
            return False

    def es_spare(self, numero_frame: int):
        if numero_frame + 1 < len(self.rolls):
            return self.rolls[numero_frame] + self.rolls[numero_frame + 1] == 10
        else:
            return False

    def bono_strike(self, numero_frame: int):
        if numero_frame + 2 < len(self.rolls):
            return self.rolls[numero_frame + 1] + self.rolls[numero_frame + 2]
        else:
            return 0

    def bono_spare(self, numero_frame: int):
        if numero_frame + 2 < len(self.rolls):
            return self.rolls[numero_frame + 2]
        else:
            return 0

    def puntaje_frame(self, numero_frame: int):
        if numero_frame + 1 < len(self.rolls):
            return self.rolls[numero_frame] + self.rolls[numero_frame + 1]
        else:
            return 0