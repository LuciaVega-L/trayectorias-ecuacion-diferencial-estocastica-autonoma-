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
        E_Xt = (b/a)*( ((eᵃᵗ)-1)) + ((X0)*(eᵃᵗ ))*μₜ
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

    # Método 3: varianza exacta en todos los pasos
    # Var(Xt) = E[Xt2]  -  (E[Xt])²
    #           └─ 2do Momento ─┘   └─ Media² ─┘

    def calcular_lista_varianza(self, tiempos, lista_valor_medio_exacto):

        print("  Calculando varianza exacta  Var(Xt) = E[Xt2] - (E[Xt])² ...")

        lista_2do_momento = []
        lista_varianza    = []

        a  = self.params.a
        b  = self.params.b
        c  = self.params.c
        d  = self.params.d
        X0 = self.params.X0
        Δt = self.params.Δt

        # Integración Euler del EDO del 2do momento paso a paso
        EX2_tᵢ = X0 * X0
        lista_2do_momento.append(EX2_tᵢ)

        i = 0
        while i < self.params.n:

            EX_tᵢ = lista_valor_medio_exacto[i]

            # d/dt E[Xt2] = (2a + c²)·E[Xt2] + 2(b + c·d)·E[Xt] + d²
            derivada_EX2_tᵢ = (
                (2*a + c*c) * EX2_tᵢ
                + 2*(b + c*d) * EX_tᵢ
                + d*d
            )

            EX2_tᵢ = EX2_tᵢ + derivada_EX2_tᵢ * Δt

            lista_2do_momento.append(EX2_tᵢ)

            i = i + 1

        # Var(Xt) = E[Xt2] - (E[Xt])²
        i = 0
        while i <= self.params.n:

            E_Xt2         = lista_2do_momento[i]
            media_al_cuad = lista_valor_medio_exacto[i] ** 2

            Var_Xtᵢ = E_Xt2 - media_al_cuad

            lista_varianza.append(Var_Xtᵢ)

            i = i + 1

        return lista_2do_momento, lista_varianza