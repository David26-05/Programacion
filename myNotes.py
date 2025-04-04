# Escritura de Archivo de Texto
# Crear un nuevo archivo llamado my_notes.txt y escribir tres líneas de notas personales
with open('my_notes.txt', 'w') as file:
    file.write("Tendencias tecnológicas que van a revolucionar 2025.\n")
    file.write("Este año ha marcado un punto de inflexión en el camino a la digitalización y los avances tecnológicos. Los desarrollos en inteligencia artificial, los nuevos planteamientos en seguridad o las cuestiones éticas a la hora de aplicar nuevas tecnologías, están marcando el presente y futuro de la economía mundial.\n")
    file.write("Los CIOs y altos directivos de IT se enfrentan a grandes retos que cambian y se transforman de forma vertiginosa, donde la única forma de conservar el liderazgo es contar con la capacidad de anticiparse y estar listos para lo que el futuro nos tiene preparados.\n")
    file.write("Según Gartner, las tecnologías e innovaciones tecnológicas que van a marcar 2025 se dividen en tres grandes bloques: imperativos y riesgos de la IA, nuevas fronteras de la informática y sinergias entre hombre y máquina.\n")
# Lectura de Archivo de Texto
# Abrir el archivo my_notes.txt y leer su contenido línea por línea
with open('my_notes.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line.strip())  # Mostrar cada línea leída en la consola
        line = file.readline()
# Nota: No es necesario cerrar el archivo cuando se usa 'with', ya que se cierra automáticamente.
