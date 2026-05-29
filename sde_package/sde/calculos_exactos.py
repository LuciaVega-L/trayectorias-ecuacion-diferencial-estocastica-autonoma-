
import math

from sde.parametros import ParametrosSDE


class CalculosExactos:
  
    def __init__(self, params):
     
        self.params = params

    # Método 1: valor medio exacto en un instante t

    def valor_medio_en_t(self, t):

        a    = self.params.a
        b    = self.params.b
        X0   = self.params.X0
        μₜ = self.params.μₜ_fijo

        if t == 0.0:
            return X0
        eᵃᵗ = math.exp(a * t)
        # [Fórmula: (b/a)*(e^(at) - 1) + X0*e^(at)]
        E_Xt = (b/a)*( (eᵃᵗ-1) + X0*eᵃᵗ )*μₜ
        return E_Xt

    # Método 2: valor medio en todos los instantes

    def calcular_lista_valor_medio(self, tiempos):
        print("  Calculando valor medio exacto...")

        lista_valor_medio_exacto = []

        i = 0
        while i <= self.params.n:

            t_actual = tiempos[i]


            EX_tᵢ = self.valor_medio_en_t(t_actual)

            lista_valor_medio_exacto.append(EX_tᵢ)

            i = i + 1

        return lista_valor_medio_exacto

    # Método 3: varianza empírica en un paso i

    def varianza_empirica_en_paso_i(self, todas_trayectorias, i, media_empirica_i):
       
        M = len(todas_trayectorias)

        suma_cuadrados = 0.0

        j = 0
        while j < M:


            Xtj_i = todas_trayectorias[j][i]

            diferencia = Xtj_i - media_empirica_i
            cuadrado   = diferencia * diferencia

            suma_cuadrados = suma_cuadrados + cuadrado

            j = j + 1

        varianza_i = suma_cuadrados / M

        return varianza_i

    # Método 4: varianza en todos los pasos

    def calcular_lista_varianza(self, todas_trayectorias):

        print("  Calculando varianza empírica...")

        lista_varianza = []

        i = 0
        while i <= self.params.n:

            suma_media = 0.0
            j = 0
            while j < self.params.M:
                suma_media = suma_media + todas_trayectorias[j][i]
                j = j + 1
            media_empirica_i = suma_media / self.params.M

            varianza_i = self.varianza_empirica_en_paso_i(
                todas_trayectorias, i, media_empirica_i
            )

            lista_varianza.append(varianza_i)

            i = i + 1

        return lista_varianza
