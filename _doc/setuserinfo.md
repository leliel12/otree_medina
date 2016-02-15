# Como usar la herramienta para asignar avatares y género a los participantes

## Nota

Hay que entender en primer lugar que oTree es una programa que favorece por diseño
que los participantes sean anónimos, esto hace que la asignacion de cosas como
avatares y nombres a usuarios sea algo complejo.

## Pasos

1. Copiar el proyecto y desplegarlo como lo indica la
   [documentación](http://otree.readthedocs.org/en/latest/server.html)
2. Copiar todas las imagenes de los usuarios a una carpeta dentro de
   `participants_conf`
   (ahi pueden ver la carpeta con los 38 avatares de los simpsons)
3. Crear dentro de la carpeta `participants_conf` un archivo de configuracion
   csv (pueden ayudarse con excel pero garanticen que el archivo se guarda
   separados por "," y no ";" cosa que hace excel normalmente)

   No usen caracteres no ascii como ñ o acentos ni en los nombres de usuario ni
   en los nombres de archivos, como todo esto es de informacióninterna no
   es relevante ser tan estrictos con el español.

   Pueden usar como ejemplo de archivo el que brino en la carpeta [`conf.csv`]
   (https://github.com/leliel12/otree_medina/blob/master/participants_conf/conf.csv)
   ([source](https://raw.githubusercontent.com/leliel12/otree_medina/master/participants_conf/conf.csv))
   
   La primer fila del archivo es la cabecera y cada celda debe tener **obligatoriamente** las columnas:
   **Name**, **Avatar**, **Gender**, **Email** (es importante respetar la capitalización)
   
   La segunda fila en adelante son los datos.
   
   - **Nombre** es información para el científico y no se guarda internamente
   - **Avatar** tiene el path relativo al archivo de la imagen a partir del la carpeta `participant_conf`
   - **Gender** puede tener los valores `Hombre` o `Mujer` respetando la capitalización.
   - **Email** email es informacion para el científico y no se usa internamente
   
   
   
