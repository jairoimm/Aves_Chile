# 🐦 Explorador de Aves de Chile

![Banner de Aves](https://via.placeholder.com/1200x300?text=Explorador+de+Aves+de+Chile) Un proyecto web sencillo desarrollado en Python para explorar la rica avifauna de Chile. Consume datos de la API de Aves de Chile y los presenta en una galería interactiva de tarjetas (cards) con diseño moderno y responsivo gracias a Bootstrap 5.

## 🌟 Características Principales

* **Galería Dinámica de Aves:** Muestra una colección de aves chilenas, obteniendo sus datos en tiempo real de una API.
* **Diseño Atractivo y Responsivo:** Implementa Bootstrap 5 y estilos CSS personalizados para una experiencia de usuario agradable en cualquier dispositivo (escritorio, tablet, móvil).
* **Información Detallada por Ave:** Cada tarjeta presenta el nombre del ave en español, inglés y su nombre científico en latín, junto con una imagen ilustrativa.
* **Generación Estática de HTML:** La página `index.html` se genera de forma programática, facilitando su despliegue y compatibilidad.

## 🚀 Cómo Ponerlo en Marcha

Sigue estos pasos para ejecutar la aplicación en tu entorno local.

### 📋 Prerrequisitos

Asegúrate de tener instalado **Python 3.x** en tu sistema.

* Puedes descargarlo desde el sitio oficial de Python: [python.org/downloads/](https://www.python.org/downloads/)

Además, este proyecto requiere la librería `requests` para interactuar con la API. Si no la tienes, instálala usando `pip`:

```bash
pip install requests

⚙️ Configuración e Instalación
** Clona el Repositorio (si aún no lo has hecho):

Bash

git clone [https://github.com/tu-usuario/tu-repositorio-aves.git](https://github.com/tu-usuario/tu-repositorio-aves.git)  # <-- REEMPLAZA con la URL real de tu repositorio
cd tu-repositorio-aves # <-- REEMPLAZA con el nombre de la carpeta de tu proyecto
Genera la Página Web index.html:
Ejecuta el script principal de Python desde la raíz del proyecto. Este script se encargará de:

Conectar con la API de aves.
Procesar los datos.
Generar el archivo index.html con todas las tarjetas de aves.
<!-- end list -->

Bash

python main.py
Una vez ejecutado, verás que se ha creado o actualizado el archivo index.html en la misma carpeta.

Abre la Aplicación en tu Navegador:
Simplemente abre el archivo index.html generado con tu navegador web preferido. Puedes hacerlo de varias maneras:

Doble clic: Navega a la carpeta de tu proyecto y haz doble clic en index.html.
Desde la terminal (macOS/Linux):
Bash

open index.html
Desde la terminal (Windows - en PowerShell):
PowerShell

Invoke-Item index.html
O simplemente start index.html en CMD.

.
📂 Estructura del Proyecto
El proyecto está modularizado en varios scripts de Python para una mejor organización:

main.py: El script principal que coordina todas las operaciones: obtiene datos, construye las tarjetas y genera el HTML final.
consulta.py: Encargado de realizar las peticiones HTTP a la API externa para obtener los datos de las aves.
crear_card.py: Contiene la lógica para formatear los datos de cada ave en una estructura de tarjeta HTML (Bootstrap Card).
vista_usuario.py: Genera la plantilla HTML base de la página, incluyendo el doctype, head, body, enlaces a Bootstrap y los estilos CSS personalizados.
crear_archivo.py: Una función auxiliar para escribir el contenido HTML final en el archivo index.html, asegurando la codificación UTF-8.
index.html: El resultado final de la ejecución de main.py, que es el archivo que se visualiza en el navegador.

🌐 API de Datos
Este proyecto consume la siguiente API pública para obtener la información de las aves de Chile:

Aves.Ninja API: https://aves.ninjas.cl/api/birds
