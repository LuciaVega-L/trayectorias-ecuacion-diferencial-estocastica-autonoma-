import math
import random

from sde.parametros import ParametrosSDE


class BrownianoEuler:
    
    def __init__(self, params):
 
        self.params = params

    # ----------------------------------------------------------
    # Método 1: vector de tiempos
    # ----------------------------------------------------------

    def construir_vector_tiempos(self):
   
        tiempos = []

        i = 0
        while i <= self.params.n:

            ti = i * self.params.delta_t
            tiempos.append(ti)
            i = i + 1

        return tiempos

    # ----------------------------------------------------------
    # Método 2: una trayectoria del Browniano
    # ----------------------------------------------------------

    def simular_browniano(self):
    
        n = self.params.n
        delta_t = self.params.delta_t
        B = []
        lista_delta_B = []
        BX_timns1 = 0.0
        B.append(BX_timns1)
        i = 1
        while i <= n:

            Rand = random.gauss(0, 1)
            raiz_delta_t = math.sqrt(delta_t)
            delta_B = raiz_delta_t * Rand
            B_ti = BX_timns1 + delta_B

            lista_delta_B.append(delta_B)
            B.append(B_ti)

            BX_timns1 = B_ti

            i = i + 1

        return lista_delta_B, B

    # ----------------------------------------------------------
    # Método 3: una trayectoria de Xt con Euler
    # ----------------------------------------------------------

    def euler_una_trayectoria(self, lista_delta_B):
        a       = self.params.a
        b       = self.params.b
        c       = self.params.c
        d       = self.params.d
        X0      = self.params.X0
        n       = self.params.n
        delta_t = self.params.delta_t


        Xt = []
        Xt.append(X0)

        X_timns1 = X0

        i = 1
        while i <= n:

            delta_B = lista_delta_B[i - 1]

            a_por_X_timns1 = a * X_timns1
            a_por_X_timns1_mas_b = a_por_X_timns1 + b
            parte_determinista = a_por_X_timns1_mas_b * delta_t

            c_por_X_timns1 = c * X_timns1
            c_por_X_timns1_mas_d = c_por_X_timns1 + d
            parte_estocastica = c_por_X_timns1_mas_d * delta_B

            Xti = X_timns1 + parte_determinista + parte_estocastica

            Xt.append(Xti)

            X_timns1 = Xti

            i = i + 1

        return Xt

    # ----------------------------------------------------------
    # Método 4: bucle completo de M trayectorias
    # ----------------------------------------------------------

    def simular_M_trayectorias(self):
        M = self.params.M

        todas_trayectorias = []

        print(f"  Simulando {M} trayectorias con el método de Euler...")

        j = 1
        while j <= M:


            lista_delta_B, B = self.simular_browniano()

            trayectoria_Xt = self.euler_una_trayectoria(lista_delta_B)

            todas_trayectorias.append(trayectoria_Xt)

            j = j + 1

        print(f"  Trayectorias generadas: {len(todas_trayectorias)}")
        print()

        return todas_trayectorias
    
