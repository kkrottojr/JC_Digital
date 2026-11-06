# JC Digital

O **JC Digital é um orquestrador de réguas de acionamento**. Ele combina regras predefinidas com os retornos dos contatos, registrados nas tabulações, para determinar o próximo passo de cada registro.

## Como a régua funciona

1. As **regras** definem os critérios para acionar, aguardar ou encerrar uma etapa.
2. As **tabulações** registram o resultado de cada tentativa de contato.
3. Os **follows** definem a continuidade a partir desse resultado, como encaminhar o registro para uma nova tentativa ou aguardar o prazo previsto antes de seguir.

Por exemplo, uma tentativa sem resposta pode gerar um novo contato após o intervalo definido na regra. Um contato concluído pode encerrar a sequência daquele registro.

## Demonstração de portfólio

A edição pública mostra a consulta de registros e a geração de relatórios com carteiras, status e valores fictícios. O motor de regras e follows, as integrações e as configurações operacionais ficam na versão de uso interno.

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

Se aparecer um erro mencionando `init.tcl`, repare a instalação do Python com a opção **Tcl/Tk and IDLE** habilitada.

O CSV usa ponto e vírgula como separador e UTF-8 com BOM. O relatório pode ser aberto no Excel.

## Como o código está organizado

- `dados_demo` gera os registros sintéticos.
- `filtrar` aplica os critérios de seleção.
- `exportar_csv` grava o relatório.
- `Aplicativo` monta a interface em Tkinter e conecta os filtros à tabela.
