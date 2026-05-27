from sde.menu_entrada     import MenuEntrada
from sde.browniano_euler  import BrownianoEuler
from sde.calculos_exactos import CalculosExactos
from sde.graficador       import Graficador


class SimuladorSDE:
    

    def ejecutar(self):

        # ── Paso 1: Leer parámetros desde consola ──────────────
        menu   = MenuEntrada()
        params = menu.solicitar_parametros()

        # ── Paso 2: Validar parámetros ─────────────────────────
        es_valido = params.validar()
        if not es_valido:
            print("  Corrija los errores e intente de nuevo.")
            return

        params.mostrar_resumen()

        # ── Paso 3: Construir tiempos y simular trayectorias ───
        # [Documento: partición t0 < t1 < ... < tn  y  M trayectorias]
        motor = BrownianoEuler(params)

        tiempos            = motor.construir_vector_tiempos()
        todas_trayectorias = motor.simular_M_trayectorias()

        # ── Paso 4: Valor medio exacto y varianza empírica ─────
        # [Fórmulas exactas del documento]
        calculos = CalculosExactos(params)

        lista_valor_medio_exacto = calculos.calcular_lista_valor_medio(tiempos)
        lista_varianza           = calculos.calcular_lista_varianza(todas_trayectorias)

        # ── Paso 5: Generar gráficas ───────────────────────────
        # [Documento: "graficar trayectorias, valor medio y varianza"]
        graficador = Graficador(params)
        graficador.graficar(
            tiempos,
            todas_trayectorias,
            lista_valor_medio_exacto,
            lista_varianza
        )

        print()
        print("  Simulación completada.")
