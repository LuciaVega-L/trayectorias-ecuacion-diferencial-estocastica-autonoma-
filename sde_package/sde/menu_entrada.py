
from sde.parametros import ParametrosSDE


class MenuEntrada:
    
    def mostrar_encabezado(self):
        print("=" * 60)
        print("  SIMULACIÓN SDE AUTÓNOMA - MÉTODO DE EULER")
        print("  dXt = (a*Xt + b)dt + (c*Xt + d)dBt")
        print("  Universidad de los Llanos - Procesos Estocásticos")
        print("=" * 60)

    def leer_float(self, mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                return valor
            except ValueError:
                print("  [AVISO] Ingrese un número válido.")

    def leer_entero_positivo(self, mensaje):
        while True:
            try:
                valor = int(input(mensaje))
                if valor > 0:
                    return valor
                else:
                    print("  [AVISO] El valor debe ser mayor que 0.")
            except ValueError:
                print("  [AVISO] Ingrese un número entero válido.")

    def solicitar_parametros(self):
        self.mostrar_encabezado()

        print()
        print("--- Coeficientes de la ecuación ---")

        a = self.leer_float(
            "  Ingrese a (coeficiente de Xt en la parte dt): "
        )

        b = self.leer_float(
            "  Ingrese b (término independiente en la parte dt): "
        )

        c = self.leer_float(
            "  Ingrese c (coeficiente de Xt en la parte dBt): "
        )

        d = self.leer_float(
            "  Ingrese d (término independiente en la parte dBt): "
        )

        print()
        print("--- Condición inicial ---")

        X0 = self.leer_float(
            "  Ingrese X0 (condición inicial): "
        )

        print()
        print("--- Parámetros de simulación ---")

        t_final = self.leer_float(
            "  Ingrese t_final (extremo derecho del intervalo (0, t)): "
        )

        n = self.leer_entero_positivo(
            "  Ingrese n (número de subintervalos/pasos): "
        )

        M = self.leer_entero_positivo(
            "  Ingrese M (número de trayectorias a simular): "
        )

        print("=" * 60)

        params = ParametrosSDE(a, b, c, d, X0, t_final, n, M)
        return params
