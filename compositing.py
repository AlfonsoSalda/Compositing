from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageDraw
import numpy as np
import random

# === CONFIGURACIÓN (SOLO MODIFICA AQUÍ) ===
CONFIG = {
    "background_path": "fondo.jpg",
    "anime_path": "noodle.png",
    "output_path": "resultado.jpg",
    "position": (0, 0),     # ← Posición del personaje en X, Y
    "scale_percent": 0,       # ← Escala en porcentaje (100 = original, 130 = +30%)
    "feather_radius": 0,        # ← Borde suave para eliminar "corte duro"
    "apply_filters": True,      # ← Desactivar si quieres solo pegar sin efectos (false)
    "pepper_noise": True,
    "film_grain": True,
    "vhs_effect": True,
    "blur": True,
    "adjust_contrast": True
}

# === FILTROS ===

def apply_pepper_noise(image, amount=0.01):
    arr = np.array(image)
    black = [0, 0, 0]
    num_pepper = int(amount * image.size[0] * image.size[1])
    for _ in range(num_pepper):
        x = random.randint(0, image.size[0] - 1)
        y = random.randint(0, image.size[1] - 1)
        arr[y, x] = black
    return Image.fromarray(arr)

def apply_film_grain(image, intensity=3):
    arr = np.array(image)
    noise = np.random.randint(-intensity, intensity + 1, arr.shape, dtype='int16')
    noisy = np.clip(arr.astype('int16') + noise, 0, 255).astype('uint8')
    return Image.fromarray(noisy)

def apply_vhs_effect(image):
    """Simula glitch VHS con split de canales y líneas horizontales"""
    # Separar canales
    r, g, b = image.split()
    r = r.transform(r.size, Image.AFFINE, (1, 0, -1, 0, 1, 0))  # mover rojo a la izquierda
    b = b.transform(b.size, Image.AFFINE, (1, 0, 1, 0, 1, 0))   # mover azul a la derecha
    image = Image.merge("RGB", (r, g, b))

    # Agregar líneas horizontales tipo TV
    draw = ImageDraw.Draw(image)
    for y in range(0, image.height, 4):
        draw.line((0, y, image.width, y), fill=(0, 0, 0), width=1)

    return image

# === COMPOSICIÓN ===

def composite_images(config):
    # Cargar imágenes
    bg = Image.open(config["background_path"]).convert("RGB")
    anime = Image.open(config["anime_path"]).convert("RGBA")

    # Escalado
    scale = config["scale_percent"] / 100.0
    anime = anime.resize((int(anime.width * scale), int(anime.height * scale)))

    # Suavizar bordes
    def soften_edges(img, radius):
        mask = img.split()[3]
        mask_blurred = mask.filter(ImageFilter.GaussianBlur(radius=radius))
        img.putalpha(mask_blurred)
        return img

    anime = soften_edges(anime, config["feather_radius"])

    # Componer imagen
    composite = bg.copy()
    composite.paste(anime, config["position"], anime)

    # Aplicar filtros al resultado final
    if config["apply_filters"]:
        if config["blur"]:
            composite = composite.filter(ImageFilter.GaussianBlur(radius=1.5))
        if config["pepper_noise"]:
            composite = apply_pepper_noise(composite)
        if config["film_grain"]:
            composite = apply_film_grain(composite, intensity=3)
        if config["adjust_contrast"]:
            composite = ImageEnhance.Contrast(composite).enhance(0.9)
            composite = ImageEnhance.Color(composite).enhance(0.85)
        if config["vhs_effect"]:
            composite = apply_vhs_effect(composite)

    # Guardar resultado
    composite.save(config["output_path"])
    print(f"✅ Imagen guardada como: {config['output_path']}")

# === EJECUTAR ===
composite_images(CONFIG)
