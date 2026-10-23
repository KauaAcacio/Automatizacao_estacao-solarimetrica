# User Story - Abrir o arquivo das informações na última posição lida

## Descrição

Como usuário da Estação Solarimétrica, eu quero abrir o arquivo que contêm as informações da estação compacta na última posição lida anteriormente, e começar a leitura a partir dessa posição, para que não seja necessário processar novamente todas as informações de cada registro.

## Critérios de aceitação

- A posição anterior deve ficar armazenada em um arquivo .txt que guarda essa informação.
- A posição deve ser maior ou igual a 0.
- O programa deve ir direto para essa posição, se possível.
- Ao final de cada verificação, o programa deve atualizar a posição atual.