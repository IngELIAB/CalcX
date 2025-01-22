import curses

def draw_calculator(win):
    # Dibuja el marco de la calculadora
    win.clear()
    win.border(0)

    # Pantalla superior
    win.addstr(1, 2, " _______________________")
    win.addstr(2, 2, "|  _________________    |")
    win.addstr(3, 2, "| |              0.0 |   |")  # Aquí se actualizaría el número
    win.addstr(4, 2, "| |_________________|    |")
    
    # Botones de la calculadora
    win.addstr(5, 2, "|  ___   ___   ___   ___ |")
    win.addstr(6, 2, "| | 7 | | 8 | | 9 | | + | |")
    win.addstr(7, 2, "| |___| |___| |___| |___| |")
    
    win.addstr(8, 2, "|  ___   ___   ___   ___ |")
    win.addstr(9, 2, "| | 4 | | 5 | | 6 | | - | |")
    win.addstr(10, 2, "| |___| |___| |___| |___| |")
    
    win.addstr(11, 2, "|  ___   ___   ___   ___ |")
    win.addstr(12, 2, "| | 1 | | 2 | | 3 | | x | |")
    win.addstr(13, 2, "| |___| |___| |___| |___| |")
    
    win.addstr(14, 2, "|  ___   ___   ___   ___ |")
    win.addstr(15, 2, "| | 0 | | . | | = | | ÷ | |")
    win.addstr(16, 2, "| |___| |___| |___| |___| |")
    
    win.addstr(17, 2, "|_______________________|")
    
    # Mensaje para indicar la espera de una entrada
    win.addstr(18, 2, "Usa las teclas para elegir una opción. ESC para salir.")
    win.refresh()

def main(stdscr):
    curses.curs_set(0)  # Desactiva el cursor
    stdscr.nodelay(1)  # No bloquea la entrada del usuario
    
    while True:
        draw_calculator(stdscr)
        
        key = stdscr.getch()
        
        # Si se presiona ESC, salir del programa
        if key == 27:
            break
        
        # Otras teclas para simular una acción
        if key == ord('1'):
            stdscr.addstr(19, 2, "Elegiste el número 1")
        elif key == ord('2'):
            stdscr.addstr(19, 2, "Elegiste el número 2")
        elif key == ord('3'):
            stdscr.addstr(19, 2, "Elegiste el número 3")
        elif key == ord('4'):
            stdscr.addstr(19, 2, "Elegiste el número 4")
        elif key == ord('5'):
            stdscr.addstr(19, 2, "Elegiste el número 5")
        elif key == ord('6'):
            stdscr.addstr(19, 2, "Elegiste el número 6")
        elif key == ord('7'):
            stdscr.addstr(19, 2, "Elegiste el número 7")
        elif key == ord('8'):
            stdscr.addstr(19, 2, "Elegiste el número 8")
        elif key == ord('9'):
            stdscr.addstr(19, 2, "Elegiste el número 9")
        elif key == ord('0'):
            stdscr.addstr(19, 2, "Elegiste el número 0")
        
        # Refresca la ventana
        stdscr.refresh()

        # Espera un segundo para limpiar la salida y actualizar el menú
        curses.napms(1000)

# Inicia la aplicación
curses.wrapper(main)
