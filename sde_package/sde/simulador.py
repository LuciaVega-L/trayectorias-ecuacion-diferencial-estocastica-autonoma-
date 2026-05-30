from sde.menu_entrada     import MenuEntrada
from sde.browniano_euler  import BrownianoEuler
from sde.calculos_exactos import CalculosExactos
from sde.graficador       import Graficador


class SimuladorSDE:

    def ejecutar(self):

        menu   = MenuEntrada()
        params = menu.solicitar_parametros()

        es_valido = params.validar()
        if not es_valido:
            print("  Corrija los errores e intente de nuevo.")
            return

        params.mostrar_resumen()

        motor = BrownianoEuler(params)

        tiempos            = motor.construir_vector_tiempos()
        todas_trayectorias = motor.simular_M_trayectorias()

        calculos = CalculosExactos(params)

        lista_valor_medio_exacto          = calculos.calcular_lista_valor_medio(tiempos)
        lista_2do_momento, lista_varianza = calculos.calcular_lista_varianza(
            tiempos, lista_valor_medio_exacto
        )

        # ── Imprimir resumen de varianza exacta en t_final ─────────────────
        E_Xt_final   = lista_valor_medio_exacto[-1]
        E_Xt2_final  = lista_2do_momento[-1]
        Var_Xt_final = lista_varianza[-1]

        print()
        print("  ── Varianza exacta en t =", params.t_final, "──────────────────────")
        print(f"     Var(Xt) = E[Xt2]          -  (E[Xt])²")
        print(f"             = {E_Xt2_final:.6f}  -  ({E_Xt_final:.6f})²")
        print(f"             = {E_Xt2_final:.6f}  -  {E_Xt_final**2:.6f}")
        print(f"             = {Var_Xt_final:.6f}")
        print("  ──────────────────────────────────────────────────────────────")
        print()

        graficador = Graficador(params)
        graficador.graficar(
            tiempos,
            todas_trayectorias,
            lista_valor_medio_exacto,
            lista_2do_momento,
            lista_varianza
        )

        menu.mostrar_varianza_exacta(
            E_Xt2_final,
            E_Xt_final,
            Var_Xt_final,
            params.t_final
        )

        print()
        print("  Simulación completada.")