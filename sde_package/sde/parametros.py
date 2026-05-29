class ParametrosSDE:
    def __init__(self, a, b, c, d, X0, t_final, n, M):

        self.a = a
        self.b = b
        self.c = c
        self.d = d

        self.X0 = X0

        self.t_final = t_final
        self.n       = n
        self.M       = M

        self.delta_t = t_final / n


        self.mu_t_fijo = 1.0

    def validar(self):
        hay_error = False


        if self.a == 0.0:
            print("  [ERROR] El coeficiente 'a' no puede ser 0 (división b/a en valor medio).")
            hay_error = True


        if self.n <= 0:
            print("  [ERROR] n debe ser un entero positivo.")
            hay_error = True


        if self.M <= 0:
            print("  [ERROR] M debe ser un entero positivo.")
            hay_error = True


        if self.t_final <= 0.0:
            print("  [ERROR] t_final debe ser positivo.")
            hay_error = True

        return not hay_error

    def mostrar_resumen(self):
        print()
        print("  Parámetros cargados:")
        print(f"    Ecuación : dXt = ({self.a}·Xt + {self.b})dt "
              f"+ ({self.c}·Xt + {self.d})dBt")
        print(f"    X0       = {self.X0}")
        print(f"    Intervalo: (0, {self.t_final})")
        print(f"    n        = {self.n}  →  "
              f"delta_t = {self.t_final}/{self.n} = {self.delta_t}")
        print(f"    M        = {self.M} trayectorias")
        print(f"    mu(t)    = {self.mu_t_fijo} (fijo)")
        print()
