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

            ti = i * self.params.Δt
            tiempos.append(ti)
            i = i + 1

        return tiempos

    # Método 2: una trayectoria del Browniano

    def simular_browniano(self):
    
        n = self.params.n
        Δt = self.params.Δt
        
        # Guardamos la raíz en una constante antes del bucle para no destruir Δt
        raiz_Δt = math.sqrt(Δt) 
        
        B = []
        lista_ΔB = []
        BX_tᵢ_1_1 = 0.0
        B.append(BX_tᵢ_1_1)
        i = 1
        while i <= n:

            Rand = random.gauss(0, 1)
            
            # Usamos raiz_Δt en lugar de modificar Δt directamente
            ΔB = raiz_Δt * Rand 
            Bₜᵢ = BX_tᵢ_1_1 + ΔB

            lista_ΔB.append(ΔB)
            B.append(Bₜᵢ)

            BX_tᵢ_1_1 = Bₜᵢ

            i = i + 1

        return lista_ΔB, B

    # Método 3: una trayectoria de Xt con Euler

    def euler_una_trayectoria(self, lista_ΔB):
        a       = self.params.a
        b       = self.params.b
        c       = self.params.c
        d       = self.params.d
        X0      = self.params.X0
        n       = self.params.n
        Δt = self.params.Δt


        Xt = []
        Xt.append(X0)

        X_tᵢ_1 = X0

        i = 1
        while i <= n:

            ΔB = lista_ΔB[i - 1]
            X_tᵢ = X_tᵢ_1 + ((a*X_tᵢ_1 + b)*Δt) + ((c*X_tᵢ_1 + d)*ΔB)

            

            Xt.append(X_tᵢ)

            X_tᵢ_1 = X_tᵢ

            i = i + 1

        return Xt

    # Método 4: bucle completo de M trayectorias

    def simular_M_trayectorias(self):
        M = self.params.M

        todas_trayectorias = []

        print(f"  Simulando {M} trayectorias con el método de Euler...")

        j = 1
        while j <= M:


            lista_ΔB, B = self.simular_browniano()

            trayectoria_Xt = self.euler_una_trayectoria(lista_ΔB)

            todas_trayectorias.append(trayectoria_Xt)

            j = j + 1

        print(f"  Trayectorias generadas: {len(todas_trayectorias)}")
        print()

        return todas_trayectorias