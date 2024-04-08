import pygame
import sys
import asyncio


# Definimos la ecuación diferencial
def ecuacion_diferencial(y, t):
    return t**3 - (y / t)

# Método de Euler mejorado
def euler_mejorado(y0, t0, h):
    k1 = ecuacion_diferencial(y0, t0)
    y_temp = y0 + h * k1
    t_temp = t0 + h
    k2 = ecuacion_diferencial(y_temp, t_temp)
    y_next = y0 + (h / 2) * (k1 + k2)
    return y_next

# Configuración de Pygame
pygame.init()
WIDTH, HEIGHT = 600, 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

suelo_y = HEIGHT - 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animación Método de Euler Mejorado")

font = pygame.font.SysFont(None, 36)
mensaje = font.render('¡La pelota ha llegado al suelo!', True, BLACK)
mensaje_rect = mensaje.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Parámetros de la simulación
t0 = 1.0  # Tiempo inicial (s)
tf = 8.00  # Tiempo final (s)
h = 0.05  # Paso de tiempo (s)
y = 0.01

# Bucle principal
clock = pygame.time.Clock()


async def main():
    global y
    global t0
    while True:  # Bucle infinito
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        # Imprimimos en la consola el tiempo y la posición en el eje y
        print("Tiempo: {:.2f} s - Posición y: {:.4f} m".format(t0, y))

        # Calculamos la siguiente posición vertical del círculo utilizando el método de Euler mejorado
        y = euler_mejorado(y, t0, h)

        # Dibujamos en la pantalla
        screen.fill(WHITE)
        pygame.draw.circle(screen, BLACK, (WIDTH // 2, int(y)), 20)
        pygame.draw.line(screen, BLACK, (0, suelo_y), (WIDTH, suelo_y), 2)
        pygame.display.flip()
        clock.tick(60)

        # Incrementamos el tiempo para la siguiente iteración
        t0 += h

        # Verificamos si hemos alcanzado el tiempo final
        if t0 >= tf:
            screen.blit(mensaje, mensaje_rect)
            pygame.display.flip()
            pygame.time.delay(2000)  # Espera un poco antes de salir
            break  # Salir del bucle infinito

        y = euler_mejorado(y, t0, h)
        y = min(max(y, 20), HEIGHT - 60)
        
        await asyncio.sleep(0)

asyncio.run(main())