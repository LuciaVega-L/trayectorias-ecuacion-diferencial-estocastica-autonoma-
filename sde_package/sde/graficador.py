import os
import matplotlib.pyplot as plt

from sde.parametros import ParametrosSDE


class Graficador:

    def __init__(self, params):

        self.params = params

    def graficar(self, tiempos, todas_trayectorias, lista_valor_medio_exacto, lista_2do_momento, lista_varianza):

        p = self.params
        print("  Generando gráfica...")

        # --- AQUÍ ESTÁ EL TRUCO ---
        # Fuerza a Matplotlib a ignorar el tema oscuro de la app y usar el diseño limpio/clásico
        plt.style.use('default') 

        # Creamos la figura asegurando los fondos blancos
        fig, ax1 = plt.subplots(1, 1, figsize=(12, 6), facecolor="white")
        ax1.set_facecolor("white")

        E_Xt_final   = lista_valor_medio_exacto[-1]
        E_Xt2_final  = lista_2do_momento[-1]
        Var_Xt_final = lista_varianza[-1]

        fig.suptitle(
            f"SDE Autónoma: dXt = (a·Xt + b)dt + (c·Xt + d)dBt\n"
            f"a={p.a}, b={p.b}, c={p.c}, d={p.d},  "
            f"X0={p.X0},  n={p.n},  M={p.M},  t∈(0,{p.t_final})\n"
            f"Var(Xt) = E[Xt2] − (E[Xt])²  =  {E_Xt2_final:.6f} − ({E_Xt_final:.6f})²  =  {Var_Xt_final:.6f}",
            fontsize=12,
            color="black"  # Nos aseguramos de que el texto del título sea negro
        )

        ax1.set_title("Trayectorias (azul) y Valor Medio Exacto (rojo)", color="black")
        ax1.set_xlabel("t", color="black")
        ax1.set_ylabel("Xt", color="black")
        
        # Cambia el color de los números de los ejes a negro
        ax1.tick_params(colors='black')

        j = 0
        while j < p.M:
            ax1.plot(
                tiempos,
                todas_trayectorias[j],
                color="steelblue",
                alpha=0.4,
                linewidth=0.8
            )
            j = j + 1

        ax1.plot(
            tiempos,
            lista_valor_medio_exacto,
            color="red",
            linewidth=2.5,
            label=r"$E(X_t) = \left(\frac{b}{a}(e^{at}-1) + X_0 e^{at}\right)\mu(t)$"
        )
        
        # Configuramos la leyenda con texto negro
        ax1.legend(fontsize=9, facecolor="white", edgecolor="black", labelcolor="black")
        ax1.grid(True, alpha=0.3, color="gray") # Cuadrícula gris para que sea visible en fondo blanco

        plt.tight_layout()

        carpeta_raiz  = os.path.dirname(os.path.abspath(__file__))
        carpeta_raiz  = os.path.join(carpeta_raiz, "..")
        ruta_guardado = os.path.join(carpeta_raiz, "sde_simulacion.png")
        ruta_guardado = os.path.normpath(ruta_guardado)

        # Guardamos forzando el fondo blanco
        plt.savefig(ruta_guardado, dpi=150, bbox_inches="tight", facecolor="white", edgecolor='none')
        plt.show()

        print(f"  Gráfica guardada en: {ruta_guardado}")