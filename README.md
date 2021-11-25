# SocketIO-Remote-Shell

## Descarga

Primero descargamos git si no lo tenemos
``` 
sudo apt install git
```

Despues clonamos este repositorio
```
git clone https://github.com/AnderGamer33/SocketIO-Remote-Shell.git
cd SocketIO-Remote-Shell
```

## Instalacion de python

Instalamos python y todos los modulos necesarios
```
bash install.sh
```

## Configuracion

Editamos el archivo ```execute.sh``` y cambiamos CONTRASEÑA por tu contraseña de usuario y RUTA por la ruta donde se encuentra el usuario

Ejemplo:
```
#!/bin/bash
echo CONTRASEÑA | sudo -S python3 RUTA/script.py
```
por 
```
#!/bin/bash
echo 1234 | sudo -S python3 /home/ander/SocketIO-Remote-Shell/script.py
```


Tambien editamos el archivo ```script.py``` y cambiamos la ruta ```http://localhost:9000/``` (Linea 17) por la ruta de nuestro servidor

Ejemplo:
```
url = "https://miservidor.com/ngrok?link=" + tunnel
```

## Configuracion para el inicio automatico

Primero le damos permisos de ejecucion a ```script.py```y ```execute.sh```
```
chmod o+x script.py
chmod +x execute.sh
```

Abrimos el archivo crontab con el siguiente comando
```
sudo crontab -e
```

Añadimos la siguiente linea al final del archivo:
```
@reboot RUTA/execute.sh
```

Cambiamos RUTA por la ruta del archivo
Ejemplo:
```
@reboot /home/ander/SocketIO-Remote-Shell/execute.sh
```
