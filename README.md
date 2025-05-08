# 🎞️ Compositing (VHS Edition)

Este proyecto en Python permite unir una fotografía real con un personaje estilo anime (en PNG con transparencia), aplicando una serie de filtros estéticos como bordes suavizados, grano de película, partículas tipo "pepper" y un filtro VHS glitch que ayuda a camuflar las diferencias de estilos.

¿El objetivo? Generar una imagen en la que ambos elementos (realidad y anime) compartan un lenguaje visual común, ideal para composiciones artísticas, memes, o estéticas retro.

## � ¿Qué hace este script?

- Carga una imagen de fondo real (formato JPG o PNG).
- Carga una imagen PNG de personaje anime con fondo transparente.
- Permite posicionar y escalar el personaje.
- Aplica filtros para mezclar estilos y suavizar bordes:
  - Suavizado del borde recortado (feathering).
  - Desenfoque del fondo (blur).
  - Ruido tipo partículas "pepper".
  - Grano tipo película (film grain).
  - Glitch y líneas horizontales estilo VHS.
  - Ajuste de contraste y color para que ambos estilos se integren mejor.

## 🛠️ Librerías utilizadas

| Librería       | Propósito                                                                 |
|----------------|---------------------------------------------------------------------------|
| PIL (Pillow)   | Procesamiento de imágenes: recorte, filtros, pegado con transparencia.    |
| NumPy          | Aplicación eficiente de ruido aleatorio (film grain, pepper noise).       |
| random         | Generación de coordenadas aleatorias para partículas.                     |

## 💻 Cómo instalar y ejecutar

### 🔁 Clonar el proyecto

```
git clone https://github.com/AlfonsoSalda/Compositing/tree/main
cd compositing
```

## 🔧 Instalar dependencias

Asegúrate de tener Python 3.8 o superior. Luego, ejecuta:

```
pip install pillow numpy
```

▶️ **Ejecutar el script**  
Coloca tus archivos de entrada (imagen de fondo, personaje PNG) en la misma carpeta.  

Edita las rutas en la parte superior del archivo `compositing.py` dentro del bloque **CONFIG**.  

Después simplemente corre:  

```
python compositing.py
```
🖼️ **Ejemplos de salida**  
Aquí tienes 5 ejemplos del resultado que se puede lograr:  
[Ejemplo 1](examples/resultado.jpg)  
[Ejemplo 2](examples/resultado2.jpg)
[Ejemplo 3](examples/resultado3.jpg)
[Ejemplo 4](examples/resultado4.jpg)
[Ejemplo 5](examples/resultado5.jpg)

⚙️ **Personalización**  
Modifica valores en el bloque `CONFIG` del archivo principal:  

- `"position": (x, y)`         # Posición del personaje  
- `"scale_percent": 130`       # Tamaño en porcentaje  
- `"feather_radius": 4`        # Suavizado del borde (más = más suave)  
- `"vhs_effect": True`         # Efecto glitch y líneas de TV  
- `"pepper_noise": True`       # Partículas tipo polvo  
- `"film_grain": True`         # Grano cinematográfico  
