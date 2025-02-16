**Conversor de Números Decimais para Binário com Selenium e Pandas**

Descrição

Este script automatiza a conversão de números decimais para binário utilizando o site Calculadora Online. Ele faz a leitura de uma lista de números a partir de um arquivo CSV, insere os valores no campo de entrada do site e extrai os resultados convertidos automaticamente. O resultado é salvo em um novo arquivo CSV.

Requisitos

Python 3 instalado

Google Chrome instalado

Bibliotecas Python:

selenium

pandas

Caso alguma biblioteca esteja ausente, instale com:

pip install selenium pandas

Como Executar

Preparar o arquivo CSV: Certifique-se de que o arquivo n decimais.csv está na mesma pasta do script e contém uma coluna com números decimais.

Executar o script:

python nome_do_script.py

O script abrirá o navegador automaticamente, inserirá os números no site e salvará os resultados em resultados_binarios.csv.

Estrutura do CSV de Entrada (n decimais.csv)

Decimal
42
89
5
76
...

Estrutura do CSV de Saída (resultados_binarios.csv)

Decimal,Binário
42,101010
89,1011001
5,101
76,1001100
...

Possíveis Problemas e Soluções

Erro de SSL ou Lentidão na Inicialização

Se ocorrer um erro relacionado ao SSL (handshake failed), tente:

Atualizar o Chrome para a última versão.

Atualizar o ChromeDriver automaticamente usando Selenium Manager (já embutido no Selenium 4.6+).

Certificar-se de que não há restrições de rede ou firewall bloqueando o acesso ao site.

Caso precise de mais ajustes, edite o script ou entre em contato!

Desenvolvido por: Amanda 🚀
