import curses

# Definir las teclas y la selección del botón
BUTTONS = [
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', 'x'],
    ['0', '.', '⌫', '÷'],
    ['=']  # Solo un botón "=" en la última fila
]

def draw_calculator(win, selected_row, selected_col, result):
    win.clear()
    win.border(0)

    # Configuración de colores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)  # Texto negro, fondo verde

    # Dibuja los bordes laterales "||" en la parte superior y la parte inferior
    for i in range(35):  # Asegúrate de que se dibuje en la longitud adecuada
        win.addstr(i, 2, "||")
        win.addstr(i, 39, "||")

    # Pantalla superior
    win.addstr(1, 4, "===================================")
    win.addstr(2, 4, "                                  ")
    win.addstr(3, 4, "   _____________________________  ")
    win.addstr(4, 4, "  |                             | ")
    # Muestra el resultado con un máximo de 20 caracteres
    win.addstr(5, 4, f"  |       {result:<20}|  ")
    win.addstr(6, 4, "  |_____________________________| ")
    win.addstr(7, 4, "                                 ")

    # Dibuja los botones con bordes
    for i, row in enumerate(BUTTONS):
        for j, button in enumerate(row):
            y = 8 + i * 4  # Calcula la posición vertical
            x = 6 + j * 8  # Calcula la posición horizontal

            # Resalta el botón seleccionado
            if i == selected_row and j == selected_col:
                win.attron(curses.color_pair(1))  # Activa el color verde
                # Si es el botón "=", ocupa toda la fila
                if i == 4:
                    win.addstr(y, x, " _______________________________ ")
                    win.addstr(y + 1, x, "|                               |")
                    win.addstr(y + 2, x, f"|               {button}               |")
                    win.addstr(y + 3, x, "|_______________________________|")
                else:
                    win.addstr(y, x, " _____ ")
                    win.addstr(y + 1, x, f"|     |")
                    win.addstr(y + 2, x, f"|  {button}  |")
                    win.addstr(y + 3, x, "|_____|")
                win.attroff(curses.color_pair(1))  # Desactiva el color verde
            else:
                # Si es el botón "=", ocupa toda la fila
                if i == 4:
                    win.addstr(y, x, " _______________________________ ")
                    win.addstr(y + 1, x, "|                               |")
                    win.addstr(y + 2, x, f"|               {button}               |")
                    win.addstr(y + 3, x, "|_______________________________|")
                else:
                    win.addstr(y, x, " _____ ")
                    win.addstr(y + 1, x, f"|     |")
                    win.addstr(y + 2, x, f"|  {button}  |")
                    win.addstr(y + 3, x, "|_____|")

    # Instrucciones
    win.addstr(32, 4, "Usa las teclas de flecha para moverte.")
    win.addstr(33, 4, "Enter para seleccionar. ESC para salir.")

    win.refresh()

def main(stdscr):
    curses.curs_set(0)  # Desactiva el cursor
    stdscr.nodelay(1)  # No bloquea la entrada del usuario

    selected_row = 0
    selected_col = 0
    result = "0.0"  # Inicializamos el resultado como "0.0"

    while True:
        draw_calculator(stdscr, selected_row, selected_col, result)

        key = stdscr.getch()
        if key == 27:  # Tecla ESC
            break
        elif key == curses.KEY_UP:
            selected_row = (selected_row - 1) % len(BUTTONS)  # Mover hacia arriba
        elif key == curses.KEY_DOWN:
            selected_row = (selected_row + 1) % len(BUTTONS)  # Mover hacia abajo
        elif key == curses.KEY_LEFT:
            selected_col = (selected_col - 1) % len(BUTTONS[selected_row])  # Mover hacia la izquierda
        elif key == curses.KEY_RIGHT:
            selected_col = (selected_col + 1) % len(BUTTONS[selected_row])  # Mover hacia la derecha
        elif key == ord('\n'):  # Enter
            if selected_row < 4:  # Si es un botón numérico u operador
                if result == "0.0":  # Si el resultado es "0.0", lo reemplazamos por el primer número
                    result = BUTTONS[selected_row][selected_col]
                else:
                    result += BUTTONS[selected_row][selected_col]  # Agrega el número u operador al resultado
            elif selected_row == 4:  # Si es el botón "="
                try:
                    result = str(eval(result))  # Evalúa la expresión
                except:
                    result = " ERROR "
            elif selected_row == 3 and selected_col == 2:  # Si es el botón de borrar
                result = result[:-1] if len(result) > 0 else "0.0"  # Borra el último carácter

# Inicia la aplicación
curses.wrapper(main)
