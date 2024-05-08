from puntajebolos.model.frames import solicitar_frames
from puntajebolos.model.puntaje import JuegoBolos

print("-BIENVENIDO-\n")
print("Esta aplicacion le permitira calcular el puntaje de su juego de bolos")
print("Para calcular el puntaje necesitamos saber los pines que tumbo en cada frame\n")

frames = solicitar_frames()
juego = JuegoBolos()

for frame in frames:
    if frame == "X":
        juego.roll(10)
    elif frame[1] == "/":
        juego.roll(10 - int(frame[0]))
    else:
        juego.roll(int(frame[0]) + int(frame[1]))

print("\nPUNTAJE FINAL: ", juego.puntaje())
print("-------------------")