# Calculadora de Folha de Pagamento

Aplicação desktop para cadastrar funcionários em memória e calcular INSS, IRRF,
FGTS e salário líquido. Os dados são exibidos em uma interface gráfica feita
com Tkinter e não são persistidos em banco de dados ou arquivos.

## Estrutura do projeto

```text
.
|-- README.md
`-- Calcular INSS/
    `-- CalcularINSS_GUI.py
```

O arquivo `Calcular INSS/CalcularINSS_GUI.py` contém as funções de cálculo e a
interface gráfica da aplicação.

## Dependências

- Python 3
- Tkinter (incluído em várias distribuições oficiais do Python)

A aplicação não usa pacotes externos nem possui arquivo de dependências.
Quando o Tkinter não estiver disponível no sistema operacional, instale-o pelo
gerenciador de pacotes da distribuição antes de executar o programa.

## Executar

Na raiz do repositório, execute:

```sh
python3 "Calcular INSS/CalcularINSS_GUI.py"
```

Em ambientes cujo comando padrão seja `python`, use:

```sh
python "Calcular INSS/CalcularINSS_GUI.py"
```

É necessário um ambiente gráfico com suporte à interface Tk.

## Verificar a aplicação

O repositório não possui suíte de testes automatizados nem scripts de build.
Pode-se verificar a sintaxe do arquivo Python com:

```sh
python3 -m py_compile "Calcular INSS/CalcularINSS_GUI.py"
```
