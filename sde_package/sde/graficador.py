import os
import matplotlib.pyplot as plt

from sde.parametros import ParametrosSDE


class Graficador:
    def __init__(self, params):
       
        self.params = params

    def graficar(self, tiempos, todas_trayectorias,
                 lista_valor_medio_exacto, lista_varianza):
       
        p = self.params
        print("  Generando gráficas...")

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

        fig.suptitle(
            f"SDE Autónoma: dXt = (a·Xt + b)dt + (c·Xt + d)dBt\n"
            f"a={p.a}, b={p.b}, c={p.c}, d={p.d},  "
            f"X0={p.X0},  n={p.n},  M={p.M},  t∈(0,{p.t_final})",
            fontsize=12
        )

        ax1.set_title("Trayectorias (azul) y Valor Medio Exacto (rojo)")
        ax1.set_xlabel("t")
        ax1.set_ylabel("Xt")


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
        ax1.legend(fontsize=9)
        ax1.grid(True, alpha=0.3)


        ax2.set_title("Varianza empírica de Xt")
        ax2.set_xlabel("t")
        ax2.set_ylabel("Var(Xt)")

        ax2.plot(
            tiempos,
            lista_varianza,
            color="green",
            linewidth=2.5,
            label="Var(Xt) empírica"
        )
        ax2.legend(fontsize=9)
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()


        carpeta_raiz = os.path.dirname(os.path.abspath(__file__))
        carpeta_raiz = os.path.join(carpeta_raiz, "..")
        ruta_guardado = os.path.join(carpeta_raiz, "sde_simulacion.png")
        ruta_guardado = os.path.normpath(ruta_guardado)

        plt.savefig(ruta_guardado, dpi=150, bbox_inches="tight")
        plt.show()

        print(f"  Gráfica guardada en: {ruta_guardado}")
