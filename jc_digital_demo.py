"""JC Digital — demonstração de portfólio com dados sintéticos."""

import csv
from datetime import date, timedelta
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


CARTEIRAS = ("Aurora", "Horizonte", "Vértice")
STATUS = ("Pendente", "Em contato", "Concluído")
COLUNAS = ("Registro", "Carteira", "Status", "Vencimento", "Valor (R$)")


def dados_demo():
    base = date(2026, 1, 15)
    return [
        (f"DEMO-{i + 1:03}", CARTEIRAS[i % 3], STATUS[(i // 3) % 3],
         (base + timedelta(days=i)).strftime("%d/%m/%Y"), (i + 1) * 1375)
        for i in range(36)
    ]


def filtrar(registros, carteira="", status="", busca=""):
    busca = busca.strip().casefold()
    return [
        linha for linha in registros
        if (not carteira or linha[1] == carteira)
        and (not status or linha[2] == status)
        and (not busca or busca in linha[0].casefold())
    ]


def moeda(centavos):
    return f"{centavos // 100},{centavos % 100:02}"


def exportar_csv(caminho, registros):
    with open(caminho, "w", newline="", encoding="utf-8-sig") as arquivo:
        writer = csv.writer(arquivo, delimiter=";")
        writer.writerow(COLUNAS)
        writer.writerows((*linha[:-1], moeda(linha[-1])) for linha in registros)


class Aplicativo:
    def __init__(self, janela):
        self.registros = dados_demo()
        janela.title("JC Digital | Demonstração")
        janela.geometry("850x530")
        janela.minsize(690, 400)
        painel = ttk.Frame(janela, padding=20)
        painel.pack(fill="both", expand=True)

        ttk.Label(painel, text="JC Digital", font=("Segoe UI", 22, "bold")).pack(anchor="w")
        ttk.Label(painel, text="Acompanhamento de carteiras • Dados fictícios").pack(anchor="w")

        filtros = ttk.Frame(painel, padding=(0, 16))
        filtros.pack(fill="x")
        self.carteira = self.seletor(filtros, "Carteira", CARTEIRAS)
        self.status = self.seletor(filtros, "Status", STATUS)
        ttk.Label(filtros, text="Registro").pack(side="left", padx=(12, 5))
        self.busca = tk.StringVar()
        ttk.Entry(filtros, textvariable=self.busca, width=14).pack(side="left")
        for variavel in (self.carteira, self.status, self.busca):
            variavel.trace_add("write", self.atualizar)
        self.botao_exportar = ttk.Button(filtros, text="Exportar CSV", command=self.exportar)
        self.botao_exportar.pack(side="right")

        area_tabela = ttk.Frame(painel)
        area_tabela.pack(fill="both", expand=True)
        self.tabela = ttk.Treeview(area_tabela, columns=COLUNAS, show="headings")
        barra = ttk.Scrollbar(area_tabela, orient="vertical", command=self.tabela.yview)
        self.tabela.configure(yscrollcommand=barra.set)
        barra.pack(side="right", fill="y")
        self.tabela.pack(side="left", fill="both", expand=True)
        for coluna in COLUNAS:
            self.tabela.heading(coluna, text=coluna)
            self.tabela.column(coluna, width=120, anchor="center")
        self.resumo = ttk.Label(painel, padding=(0, 12, 0, 0))
        self.resumo.pack(anchor="w")
        self.atualizar()

    @staticmethod
    def seletor(painel, titulo, opcoes):
        ttk.Label(painel, text=titulo).pack(side="left", padx=(0, 5))
        variavel = tk.StringVar(value="Todas" if titulo == "Carteira" else "Todos")
        ttk.Combobox(painel, textvariable=variavel, values=(variavel.get(), *opcoes),
                     state="readonly", width=13).pack(side="left", padx=(0, 12))
        return variavel

    def atualizar(self, *_):
        carteira = self.carteira.get()
        status = self.status.get()
        self.visiveis = filtrar(self.registros, carteira if carteira in CARTEIRAS else "",
                               status if status in STATUS else "", self.busca.get())
        self.tabela.delete(*self.tabela.get_children())
        for linha in self.visiveis:
            self.tabela.insert("", "end", values=(*linha[:-1], moeda(linha[-1])))
        total = sum(linha[-1] for linha in self.visiveis)
        self.resumo.configure(text=f"{len(self.visiveis)} registro(s)  |  Total filtrado: R$ {moeda(total)}")
        self.botao_exportar.configure(state="normal" if self.visiveis else "disabled")

    def exportar(self):
        destino = filedialog.asksaveasfilename(
            defaultextension=".csv", initialfile="jc_digital_demo.csv",
            filetypes=[("Arquivo CSV", "*.csv")],
        )
        if destino:
            try:
                exportar_csv(destino, self.visiveis)
            except OSError as erro:
                messagebox.showerror("Erro ao exportar", str(erro))
            else:
                messagebox.showinfo("Relatório", f"{len(self.visiveis)} registro(s) exportado(s).")


if __name__ == "__main__":
    janela = tk.Tk()
    Aplicativo(janela)
    janela.mainloop()
