
import math

from sde.parametros import ParametrosSDE


class CalculosExactos:
  
    def __init__(self, params):
     
        self.params = params

    # ----------------------------------------------------------
    # Método 1: valor medio exacto en un instante t
    # ----------------------------------------------------------

    def valor_medio_en_t(self, t):

        a    = self.params.a
        b    = self.params.b
        X0   = self.params.X0
        mu_t = self.params.mu_t_fijo

        # Caso especial t = 0: E(X0) = X0
        if t == 0.0:
            return X0

        # Paso 1: e^(a*t)
        # [Fórmula: e^(at)]
        e_at = math.exp(a * t)

        # Paso 2: e^(a*t) - 1
        # [Fórmula: (e^(at) - 1)]
        e_at_menos_1 = e_at - 1

        # Paso 3: b / a
        # [Fórmula: b/a]
        b_sobre_a = b / a

        # Paso 4: (b/a) * (e^(at) - 1)
        # [Fórmula: (b/a)*(e^(at) - 1)]
        termino_1 = b_sobre_a * e_at_menos_1

        # Paso 5: X0 * e^(a*t)
        # [Fórmula: X0 * e^(at)]
        termino_2 = X0 * e_at

        # Paso 6: suma del paréntesis
        # [Fórmula: (b/a)*(e^(at) - 1) + X0*e^(at)]
        suma_parentesis = termino_1 + termino_2

        # Paso 7: multiplicar por mu(t)
        # [Fórmula: (...) * mu(t)]
        E_Xt = suma_parentesis * mu_t

        return E_Xt

    # ----------------------------------------------------------
    # Método 2: valor medio en todos los instantes
    # ----------------------------------------------------------

    def calcular_lista_valor_medio(self, tiempos):
        print("  Calculando valor medio exacto...")

        lista_valor_medio_exacto = []

        i = 0
        while i <= self.params.n:

            t_actual = tiempos[i]

            # Aplicar la fórmula exacta en t_actual
            E_Xt_i = self.valor_medio_en_t(t_actual)

            lista_valor_medio_exacto.append(E_Xt_i)

            i = i + 1

        return lista_valor_medio_exacto

    # ----------------------------------------------------------
    # Método 3: varianza empírica en un paso i
    # ----------------------------------------------------------

    def varianza_empirica_en_paso_i(self, todas_trayectorias, i, media_empirica_i):
       
        M = len(todas_trayectorias)

        # Acumulador de la suma de cuadrados
        suma_cuadrados = 0.0

        j = 0
        while j < M:

            # Valor de la trayectoria j en el paso i
            Xtj_i = todas_trayectorias[j][i]

            # (Xtj_i - media_i)^2
            diferencia = Xtj_i - media_empirica_i
            cuadrado   = diferencia * diferencia

            suma_cuadrados = suma_cuadrados + cuadrado

            j = j + 1

        # Dividir por M
        varianza_i = suma_cuadrados / M

        return varianza_i

    # ----------------------------------------------------------
    # Método 4: varianza en todos los pasos
    # ----------------------------------------------------------

    def calcular_lista_varianza(self, todas_trayectorias):

        print("  Calculando varianza empírica...")

        lista_varianza = []

        i = 0
        while i <= self.params.n:

            # Calcular la media empírica en el paso i
            suma_media = 0.0
            j = 0
            while j < self.params.M:
                suma_media = suma_media + todas_trayectorias[j][i]
                j = j + 1
            media_empirica_i = suma_media / self.params.M

            # Calcular la varianza empírica en el paso i
            varianza_i = self.varianza_empirica_en_paso_i(
                todas_trayectorias, i, media_empirica_i
            )

            lista_varianza.append(varianza_i)

            i = i + 1

        return lista_varianza
