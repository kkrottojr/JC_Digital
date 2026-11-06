# JC Digital

Demonstração de portfólio de um aplicativo desktop para acompanhar carteiras, consultar registros e gerar relatórios. Os registros, nomes de carteiras e valores desta edição são fictícios. A demonstração funciona localmente com dados gerados pelo próprio programa.

## O que você pode testar

- Filtrar os registros por carteira e status.
- Buscar um registro pelo código, como `DEMO-001`.
- Conferir a quantidade de registros e o valor total da seleção.
- Exportar os registros filtrados para um arquivo CSV.

## Como executar

Use Python 3.10 ou superior com Tkinter. No Windows, a instalação padrão do Python inclui Tkinter. Baixe ou clone o repositório, abra um terminal na pasta e execute:

```bash
python jc_digital_demo.py
```

O CSV usa ponto e vírgula como separador e UTF-8 com BOM. O relatório pode ser aberto no Excel.

## Como o código está organizado

- `dados_demo` gera os registros sintéticos.
- `filtrar` aplica os critérios de seleção.
- `exportar_csv` grava o relatório.
- `Aplicativo` monta a interface em Tkinter e conecta os filtros à tabela.
