import math

from sde.parametros import ParametrosSDE


class CalculosExactos:

    def __init__(self, params):

        self.params = params

    # Método 1: valor medio exacto en un instante t

    def valor_medio_en_t(self, t):

        a  = self.params.a
        b  = self.params.b
        X0 = self.params.X0
        μₜ = self.params.μₜ_fijo

        if t == 0.0:
            return X0
        eᵃᵗ = math.exp(a * t)
        # [Fórmula: (b/a)*(e^(at) - 1) + X0*e^(at)]
        E_Xt = (b/a)*((eᵃᵗ) - 1) + (X0 * eᵃᵗ) * μₜ
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