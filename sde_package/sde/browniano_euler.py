import math
import random

from sde.parametros import ParametrosSDE


class BrownianoEuler:
    
    def __init__(self, params):
 
        self.params = params
    # Método 1: vector de tiempos

    def construir_vector_tiempos(self):
   
        tiempos = []

        i = 0
        while i <= self.params.n:

            # ti = i * delta_t
            ti = i * self.params.delta_t
            tiempos.append(ti)

            i = i + 1

        return tiempos

    # Método 2: una trayectoria del Browniano

    def simular_browniano(self):
    
        n       = self.params.n
        delta_t = self.params.delta_t

        # Lista de valores del Browniano
        B = []

        # Lista de incrementos (se pasan al método de Euler)
        lista_delta_B = []

        # Condición inicial B0 = 0  
        B_anterior = 0.0
        B.append(B_anterior)

        # Construir la trayectoria paso a paso
        i = 1
        while i <= n:

            # Rand = N(0,1)
            Rand = random.gauss(0, 1)

            # sqrt(delta_t)
            raiz_delta_t = math.sqrt(delta_t)

            # delta_B = sqrt(delta_t) * Rand
            delta_B = raiz_delta_t * Rand

            # Bti = Bti_1 + delta_B
            B_actual = B_anterior + delta_B

            lista_delta_B.append(delta_B)
            B.append(B_actual)

            B_anterior = B_actual

            i = i + 1

        return lista_delta_B, B

    # Método 3: una trayectoria de Xt con Euler

    def euler_una_trayectoria(self, lista_delta_B):
        a       = self.params.a
        b       = self.params.b
        c       = self.params.c
        d       = self.params.d
        X0      = self.params.X0
        n       = self.params.n
        delta_t = self.params.delta_t

        # Iniciar con la condición inicial  
        Xt = []
        Xt.append(X0)

        Xti_1 = X0

        # Aplicar Euler paso a paso  
        i = 1
        while i <= n:

            # Incremento browniano del paso i
            delta_B = lista_delta_B[i - 1]

            # Parte determinista
            a_por_Xti_1 = a * Xti_1

            a_por_Xti_1_mas_b = a_por_Xti_1 + b

            parte_determinista = a_por_Xti_1_mas_b * delta_t

            #  Parte estocástica

            c_por_Xti_1 = c * Xti_1

            c_por_Xti_1_mas_d = c_por_Xti_1 + d

            parte_estocastica = c_por_Xti_1_mas_d * delta_B

            #  Fórmula de Euler completa 
            Xti = Xti_1 + parte_determinista + parte_estocastica

            Xt.append(Xti)

            Xti_1 = Xti

            i = i + 1

        return Xt

    # Método 4: bucle completo de M trayectorias

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
