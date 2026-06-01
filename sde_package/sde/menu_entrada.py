import sys
import customtkinter as ctk
from sde.parametros import ParametrosSDE


# ── Fix DPI Windows (evita pixelado) ─────────────────────────────────────────
if sys.platform == "win32":
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(2)
    except Exception:
        try:
            windll.user32.SetProcessDPIAware()
        except Exception:
            pass


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class MenuEntrada:

    def solicitar_parametros(self):
        resultado = {}

        root = ctk.CTk()
        root.title("SDE Autónoma — Euler–Maruyama")
        root.resizable(True, True)   # redimensionable para pantallas pequeñas

        # ── Paleta ────────────────────────────────────────────────────────────
        C_BG      = "#F5F7FA"    # fondo principal
        C_CARD    = "#FFFFFF"    # tarjetas blancas
        C_BORDER  = "#D9DEE7"    # bordes suaves

        C_ACCENT  = "#2563EB"    # azul principal
        C_ACCENT2 = "#1D4ED8"    # azul hover

        C_TEXT    = "#1F2937"    # texto oscuro
        C_MUTED   = "#6B7280"    # texto secundario

        C_ENTRY   = "#F9FAFB"    # cajas de texto
        C_ERROR   = "#DC2626"    # rojo error

        FONT_TITLE = ctk.CTkFont(family="Segoe UI", size=20, weight="bold")
        FONT_SUB   = ctk.CTkFont(family="Segoe UI", size=11)
        FONT_EQ    = ctk.CTkFont(family="Consolas",  size=12)
        FONT_SEC   = ctk.CTkFont(family="Segoe UI", size=10, weight="bold")
        FONT_LABEL = ctk.CTkFont(family="Segoe UI", size=11)
        FONT_ENTRY = ctk.CTkFont(family="Consolas",  size=12)
        FONT_BTN   = ctk.CTkFont(family="Segoe UI", size=12, weight="bold")

        root.configure(fg_color=C_BG)
        vars_ = {}

        # ── Helpers ───────────────────────────────────────────────────────────
        def section(parent, text):
            ctk.CTkLabel(parent, text=text.upper(), font=FONT_SEC,
                         text_color=C_MUTED).pack(anchor="w", pady=(6, 2))

        def param_row(parent, symbol, desc, var_name, default):
            row = ctk.CTkFrame(parent, fg_color="transparent")
            row.pack(fill="x", pady=3)
            ctk.CTkLabel(row, text=symbol, font=FONT_EQ,
                         text_color=C_ACCENT, width=28,
                         anchor="w").pack(side="left", padx=(0, 6))
            ctk.CTkLabel(row, text=desc, font=FONT_LABEL,
                         text_color=C_MUTED, anchor="w",
                         width=210).pack(side="left")
            var = ctk.StringVar(value=default)
            ctk.CTkEntry(
                row, textvariable=var,
                width=90, height=30,
                font=FONT_ENTRY,
                fg_color=C_ENTRY,
                border_color=C_BORDER,
                border_width=1,
                text_color=C_TEXT,
                corner_radius=7,
            ).pack(side="right")
            vars_[var_name] = var

        def make_card(parent):
            card = ctk.CTkFrame(parent, fg_color=C_CARD, corner_radius=10,
                                border_width=1, border_color=C_BORDER)
            card.pack(fill="x", pady=(3, 10))
            inner = ctk.CTkFrame(card, fg_color="transparent")
            inner.pack(fill="x", padx=14, pady=10)
            return inner

        # ── Estructura principal: header fijo + scroll + footer fijo ──────────
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # — Header fijo —
        header = ctk.CTkFrame(root, fg_color=C_CARD, corner_radius=0)
        header.grid(row=0, column=0, sticky="ew")

        hinner = ctk.CTkFrame(header, fg_color="transparent")
        hinner.pack(padx=24, pady=16)
        ctk.CTkLabel(hinner, text="SDE Autónoma",
                     font=FONT_TITLE, text_color=C_TEXT).pack(anchor="w")
        ctk.CTkLabel(hinner,
                     text="Simulación por el método de Euler–Maruyama",
                     font=FONT_SUB, text_color=C_MUTED).pack(anchor="w", pady=(2, 8))
        eq_box = ctk.CTkFrame(hinner, fg_color=C_ENTRY, corner_radius=7,
                               border_width=1, border_color=C_BORDER)
        eq_box.pack(anchor="w")
        ctk.CTkLabel(eq_box,
                     text="  dXt = (a·Xt + b) dt  +  (c·Xt + d) dBt  ",
                     font=FONT_EQ, text_color=C_ACCENT).pack(padx=10, pady=7)

        # — Área scrollable —
        scroll = ctk.CTkScrollableFrame(root, fg_color="transparent",
                                         scrollbar_button_color=C_BORDER,
                                         scrollbar_button_hover_color=C_ACCENT)
        scroll.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)

        body = ctk.CTkFrame(scroll, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=24, pady=(12, 4))

        section(body, "Coeficientes")
        ci = make_card(body)
        param_row(ci, "a",  "Coef. de Xt en la parte dt",   "a",  "0.5")
        param_row(ci, "b",  "Término independiente en dt",   "b",  "0.2")
        param_row(ci, "c",  "Coef. de Xt en la parte dBt",  "c",  "0.3")
        param_row(ci, "d",  "Término independiente en dBt",  "d",  "0.1")

        section(body, "Condición inicial y tiempo")
        ti = make_card(body)
        param_row(ti, "X₀", "Valor inicial",         "X0", "1.0")
        param_row(ti, "T",  "Tiempo final t_final",  "T",  "1.0")

        section(body, "Simulación")
        si = make_card(body)
        param_row(si, "n", "Pasos de tiempo (subintervalos)", "n", "100")
        param_row(si, "M", "Número de trayectorias",          "M", "30")

        err_label = ctk.CTkLabel(body, text="", font=FONT_LABEL,
                                  text_color=C_ERROR, wraplength=400,
                                  justify="left")
        err_label.pack(anchor="w", pady=(4, 8))

        # — Footer fijo —
        footer = ctk.CTkFrame(root, fg_color=C_CARD, corner_radius=0)
        footer.grid(row=2, column=0, sticky="ew")
        ctk.CTkFrame(footer, height=1, fg_color=C_BORDER,
                     corner_radius=0).pack(fill="x")

        def on_simular():
            err_label.configure(text="")
            errores = []

            def rf(k, nombre):
                try:    return float(vars_[k].get())
                except: errores.append(f"{nombre} debe ser un número real."); return None

            def ri(k, nombre):
                try:    return int(vars_[k].get())
                except: errores.append(f"{nombre} debe ser un entero."); return None

            a  = rf("a",  "a")
            b  = rf("b",  "b")
            c  = rf("c",  "c")
            d  = rf("d",  "d")
            X0 = rf("X0", "X₀")
            T  = rf("T",  "T")
            n  = ri("n",  "n")
            M  = ri("M",  "M")

            if a  is not None and a == 0: errores.append("a no puede ser 0 (se usa b/a en E[Xt]).")
            if T  is not None and T <= 0: errores.append("T debe ser > 0.")
            if n  is not None and n <= 0: errores.append("n debe ser entero positivo.")
            if M  is not None and M <= 0: errores.append("M debe ser entero positivo.")

            if errores:
                err_label.configure(text="  ·  ".join(errores))
                return

            resultado["params"] = ParametrosSDE(a, b, c, d, X0, T, n, M)
            root.destroy()

        ctk.CTkButton(
            footer, text="▶   Simular",
            font=FONT_BTN, height=44, corner_radius=0,
            fg_color=C_ACCENT, hover_color=C_ACCENT2,
            text_color="#FFFFFF", command=on_simular,
        ).pack(fill="x")

        # ── Tamaño adaptado a la pantalla ─────────────────────────────────────
        root.update_idletasks()

        ancho    = 480
        sh       = root.winfo_screenheight()
        margen   = 80                          # deja espacio para la barra de tareas
        alto_max = sh - margen
        alto     = min(root.winfo_reqheight(), alto_max)

        x = (root.winfo_screenwidth()  - ancho) // 2
        y = (sh - alto) // 2
        root.geometry(f"{ancho}x{alto}+{x}+{y}")
        root.minsize(380, 400)                 # mínimo absoluto

        root.mainloop()

        if "params" not in resultado:
            print("  Simulación cancelada.")
            raise SystemExit(0)

        return resultado["params"]