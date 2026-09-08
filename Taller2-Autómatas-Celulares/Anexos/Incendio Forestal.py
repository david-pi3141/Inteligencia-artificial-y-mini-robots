import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.ndimage import gaussian_filter  # Necesario para concentrar las rocas

# --- 1. CONFIGURACIÓN DEL MODELO ---
L = 100               # Dimensión del retículo (100x100 = 10,000 celdas)
P_BASE = 0.25         # Probabilidad base de propagación del fuego
DURACION_FUEGO = 3    # Cuántos ciclos permanece encendida una celda

# 💨 CONFIGURACIÓN DEL VIENTO
# Opciones válidas: 'ESTE', 'OESTE', 'NORTE', 'SUR'
DIRECCION_VIENTO = 'NORTE' 

# Estados del Autómata Celular
VEGETACION = 0  
FUEGO = 1       
CENIZAS = 2     
ROCA = 3        

# --- 2. INICIALIZACIÓN DEL RETÍCULO CON ROCAS CONCENTRADAS ---
grid = np.zeros((L, L), dtype=int)
tiempo_fuego = np.zeros((L, L), dtype=int)

# Generar mapa de ruido suavizado para concentrar los obstáculos
ruido_aleatorio = np.random.rand(L, L)
ruido_suavizado = gaussian_filter(ruido_aleatorio, sigma=3.5)
umbral_roca = np.percentile(ruido_suavizado, 15) # Asegura el 15% de cobertura

for i in range(L):
    for j in range(L):
        if ruido_suavizado[i, j] < umbral_roca:
            grid[i, j] = ROCA

# Inicializar un foco de incendio en el centro de la matriz
centro = L // 2
grid[centro, centro] = FUEGO
tiempo_fuego[centro, centro] = DURACION_FUEGO

# --- 3. LOGÍSICA Y REGLAS PROBABILÍSTICAS (Por ciclo) ---
def actualizar_ciclo(frame, img, grid_ref):
    global grid, tiempo_fuego
    
    if not np.any(grid == FUEGO):
        return [img]

    nuevo_grid = grid.copy()
    nuevo_tiempo = tiempo_fuego.copy()

    for i in range(L):
        for j in range(L):
            if grid[i, j] == VEGETACION:
                p_contagio_total = 0.0
                
                # Evaluar la Vecindad de Moore
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        
                        ni, nj = i + di, j + dj
                        if 0 <= ni < L and 0 <= nj < L:
                            if grid[ni, nj] == FUEGO:
                                
                                # CONTROL DINÁMICO DEL VIENTO
                                factor_viento = 1.0  # Factor por defecto (sin viento)
                                
                                if DIRECCION_VIENTO == 'ESTE':
                                    if dj == -1: factor_viento = 2.0   # Fuego viene desde la izquierda
                                    elif dj == 1: factor_viento = 0.3  # Fuego va en contra
                                    
                                elif DIRECCION_VIENTO == 'OESTE':
                                    if dj == 1: factor_viento = 2.0    # Fuego viene desde la derecha
                                    elif dj == -1: factor_viento = 0.3 # Fuego va en contra
                                    
                                elif DIRECCION_VIENTO == 'NORTE':
                                    if di == 1: factor_viento = 2.0    # Fuego viene desde abajo
                                    elif di == -1: factor_viento = 0.3 # Fuego va en contra
                                    
                                elif DIRECCION_VIENTO == 'SUR':
                                    if di == -1: factor_viento = 2.0   # Fuego viene desde arriba
                                    elif di == 1: factor_viento = 0.3  # Fuego va en contra

                                p_contagio_total += P_BASE * factor_viento
                
                if p_contagio_total > 0:
                    p_contagio_total = min(p_contagio_total, 1.0)
                    if np.random.rand() < p_contagio_total:
                        nuevo_grid[i, j] = FUEGO
                        nuevo_tiempo[i, j] = DURACION_FUEGO

            elif grid[i, j] == FUEGO:
                nuevo_tiempo[i, j] -= 1
                if nuevo_tiempo[i, j] <= 0:
                    nuevo_grid[i, j] = CENIZAS

    grid = nuevo_grid
    tiempo_fuego = nuevo_tiempo
    img.set_data(grid)
    return [img]

# --- 4. RENDERIZACIÓN Y ANIMACIÓN ---
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_title(f"Incendio Forestal AC - Viento hacia el {DIRECCION_VIENTO}")

from matplotlib.colors import ListedColormap
cmap_personalizado = ListedColormap(['#2ecc71', '#e74c3c', '#7f8c8d', '#d35400']) 

img = ax.imshow(grid, cmap=cmap_personalizado, vmin=0, vmax=3)

ani = animation.FuncAnimation(
    fig, actualizar_ciclo, fargs=(img, grid), 
    frames=150, interval=100, blit=True, repeat=False
)

plt.colorbar(img, ticks=[0, 1, 2, 3], format=plt.FuncFormatter(lambda val, loc: ['Vegetación', 'Fuego', 'Cenizas', 'Roca'][int(val)]))
plt.show()