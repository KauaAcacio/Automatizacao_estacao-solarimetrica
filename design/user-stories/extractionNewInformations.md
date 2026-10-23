# User Story - Realizar a extração das novas informações

## Descrição

Como usuário da Estação Solarimétrica, eu quero ter acesso as novas informações da estação compacta que chegam em um arquivo .txt a cada 10 segundos, para que eu possa colocar essas informações em um banco de dados.

## Critérios de aceitação

- A linha processada não pode ser o cabeçalho.
- A linha não pode ser um /n.
- Verificar se chegou no final do arquivo.
- Necessário armazenar os dados novos em um DataFrame do Pandas, por meio de uma classe.