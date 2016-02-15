# Como usar la herramienta para asignar avatares y género a los participantes

## Nota

Hay que entender en primer lugar que oTree es una programa que favorece por diseño
que los participantes sean anónimos, esto hace que la asignación de cosas como
avatares y nombres a usuarios sea algo complejo.

## Pasos

1. Copiar el proyecto y desplegarlo como lo indica la
   [documentación](http://otree.readthedocs.org/en/latest/server.html)
2. Copiar todas las imágenes de los usuarios a una carpeta dentro de
   `participants_conf`
   (ahi pueden ver la carpeta con los 38 avatares de los simpsons)
3. Crear dentro de la carpeta `participants_conf` un archivo de configuración
   csv (pueden ayudarse con excel pero garanticen que el archivo se guarda
   separados por "," y no ";" cosa que hace excel normalmente)

   No usen caracteres no ascii como ñ o acentos ni en los nombres de usuario ni
   en los nombres de archivos, como todo esto es de información interna no
   es relevante ser tan estrictos con el español.

   Pueden usar como ejemplo de archivo el que brino en la carpeta [`conf.csv`]
   (https://github.com/leliel12/otree_medina/blob/master/participants_conf/conf.csv)
   ([source](https://raw.githubusercontent.com/leliel12/otree_medina/master/participants_conf/conf.csv))

   La primer fila del archivo es la cabecera y cada celda debe tener **obligatoriamente** las columnas:
   **Name**, **Avatar**, **Gender**, **Email** (es importante respetar la capitalización)

   La segunda fila en adelante son los datos.

   - **Nombre** le da un nombre al participante para que al momento de extraer los resultados sea simple encontrarlos
   - **Avatar** tiene el path relativo al archivo de la imagen a partir del la carpeta `participant_conf`
   - **Gender** puede tener los valores `Hombre` o `Mujer` respetando la capitalización.
   - **Email** email es información para el científico y no se usa internamente
4. Ahora es el momento de crear una session con el comando

   ```bash
   $ otree create_session fullgame 38
   ```

   El número **38** es la cantidad de participantes del juego (38 es un ejemplo arbitrario). Lo que si, ese número tiene que
   ser igual a la cantidad de filas de su archivo de configuracion, sin contar la cabecera.
5. Ahora necesita saber como se llama su session, por lo cual tiene que ejecutar el comando `otree listsessions` el cual le
   otorgara una salida parecida a:

   ```
   Name        Code       Participants   App Sequence
   ----------- ---------- -------------- -----------------------------------
   Full Game   XXXXXXXX   38             section1, section2, questionnaire
   ```

   donde `XXXXXXXX` es el código de su nueva session creada.

   Ahora si estamos listos para asignar los avatares, nombres y genero a los participantes de dicha session.
6. El comando para ejecutar lo deseado es:

   ```bash
   $ otree setuserinfo --session XXXXXXXX --conf tuarchivo.csv --out salida.csv --host localhost:8000
   ```

   Donde `XXXXXXXX` es el código devuelvo por listsession, `tuarchivo.csv` es el archivo donde relacionaron
   los nombres, avatares, genero y emails, `salida.csv` les va a informar donde esta el link para cada
   usuario, y `localhost:8000` es la ip y el puerto donde corre otree (esta ultima información se utiliza
   para construir los links que aparecerán por pantalla y en `salida.csv`; es útil para distribuir cómodamente
   los links a los participantes)







