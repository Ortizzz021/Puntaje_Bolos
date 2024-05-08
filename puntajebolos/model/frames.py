def solicitar_frames():
    print("Ingrese los resultados de los frames:")
    resultados = []
    for i in range(10):
        while True:
            frame = input(f"Frame {i + 1}: ").upper()
            if validar_frame(frame):
                resultados.append(frame)
                break
            else:
                print("Entrada inválida. Por favor, ingrese nuevamente.")

    return resultados

def validar_frame(frame):
    if len(frame) == 1 and frame == 'X':
        return True
    elif len(frame) == 2 and frame[0].isdigit() and frame[1] in ['/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    elif len(frame) == 3 and frame[0].isdigit() and frame[1] == '/' and frame[2].isdigit():
        return True
    else:
        return False