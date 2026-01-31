# musica2

Descrição do projeto
--------------------

Este repositório contém uma pequena aplicação Streamlit que simula e exibe rankings do Billboard Hot 100 entre 2020 e 2025. A aplicação permite ao usuário selecionar ano e mês, navegar pelo Top 10 e baixar os dados como CSV.

Arquivos principais
-------------------

- `app1.py`: Interface Streamlit com geração de dataset fictício (com alguns hits reais) e opções de filtro por ano/mês. Exibe posição, música, artista e link para ouvir no Spotify. Também contém botões para baixar o CSV do mês selecionado ou o CSV completo.
- `billboard-app/`: pasta com experimentos adicionais e scripts auxiliares (ex.: `app.py` e `main.py`) que usam a biblioteca `billboard` para buscar rankings reais quando disponível.

Como usar
---------

1. Instale dependências (ex.: `streamlit`, `pandas`, `billboard.py` quando necessário):

```bash
pip install streamlit pandas billboard.py
```

2. Execute a aplicação Streamlit:

```bash
streamlit run app1.py
```

3. Na interface, selecione o `Ano` e `Mês` desejados. O Top 10 será exibido com posição, música, artista e um botão que direciona para busca/track no Spotify.

4. Use os botões de download para obter o CSV do mês selecionado ou o CSV completo (2020–2025).

Notas técnicas
--------------

- O dataset usado em `app1.py` é gerado dinamicamente por `generate_billboard_csv()` e mistura entradas fictícias com alguns hits reais para dar contexto.
- O botão de download gera arquivos CSV codificados em UTF-8.
- Há uma subpasta `billboard-app/billboard-app` que aparece como repositório Git aninhado; isso pode ser intencional (submódulo) ou um artefato. Se não desejar, remova do índice com:

```bash
git rm --cached billboard-app/billboard-app
```

Sugestões futuras
------------------

- Conectar a API do Spotify para exibir capas e links diretos aos tracks.
- Substituir dados fictícios por pulls regulares da API do Billboard para histórico mais preciso.
- Adicionar testes básicos e `requirements.txt` para garantir instalação reprodutível.

Licença
-------

Coloque aqui sua licença preferida (ex.: MIT).

