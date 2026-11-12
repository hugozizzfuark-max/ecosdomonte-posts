# Rotina de posts do @ecosdomonte

Cada execução agendada publica **um** post no Instagram @ecosdomonte (conta Windsor `17841425594595406`, conector `instagram`).

## Linha editorial
- Perfil cristão de fé, reflexões e devocional. Público majoritariamente feminino, maduro (muitas 55+), passando por dias difíceis.
- Tom: acolhedor, simples, esperançoso. Nada de julgamento, medo ou promessas de prosperidade. Português do Brasil.
- **Horário 12h — "Palavra do meio-dia":** um versículo bíblico curto (no máximo ~30 palavras), com referência. Temas: consolo, força, recomeço, cuidado de Deus, ansiedade, perdão, gratidão.
- **Horário 19h — "Oração da noite"** (ou "Oração para hoje", "Uma oração para você"): oração curta em primeira pessoa (35 a 55 palavras), terminando em "Amém." Escreva a oração com palavras próprias; sem referência na arte.
- Nunca repita versículo ou tema dos últimos 14 dias: consulte `posts/historico.csv` antes de escrever.

## Legenda (formato da dona da conta, ~1.200 a 1.600 caracteres)
Siga esta estrutura, que é a que ela já usa e que teve bom resultado:
1. Primeira linha fixa, sempre igual: `Não vamos aparecer para você de novo :/ Nos siga para acompanhar nossas reflexões e comentários!`
2. Parágrafo que nomeia a dor do leitor em linguagem concreta (ex.: "os planos que falharam, as decepções que nos feriram e a ansiedade que insiste em nos acompanhar") e a crença errada que vem com ela.
3. A virada: o que Deus faz com isso, trazendo o versículo do dia entre aspas curvas com a referência ("Em Jeremias 18:4, a Palavra nos mostra...: “...”"). No post da oração, cite um versículo ligado ao tema da oração.
4. Parágrafo de consolo e aplicação, fechando com uma frase de esperança forte (ex.: "A sua dor não é o fim da sua história, é apenas a matéria-prima para o seu recomeço.").
5. Ponte para a oferta: "Se você sente que precisa de ajuda para ..., você não precisa fazer esse percurso sozinha."
6. Bloco da oferta, sempre nestas três linhas (pode variar levemente as palavras):
   `✨ Conheça o Devocional Digital "Depois da Dor, Deus".`
   `Um guia diário de 21 dias para te ajudar a superar a ansiedade, encontrar restauração interior e reconstruir a sua fé com esperança.`
   `👉 Clique no link da minha bio para garantir o seu acesso e começar a sua transformação hoje mesmo. 🕊️`
7. Linha em branco e 5 hashtags, sempre incluindo #devocional #oracao e mais 3 entre: #deusnocomando #deusébomotempotodo #deuséfiel #fé #palavradedeus #recomeço.
Parágrafos separados só por quebra de linha simples. Fale com o leitor no feminino quando for direto a ele ("sozinha").

## Passo a passo
1. Ligue o repositório com `add_repo` (owner `hugozizzfuark-max`, repo `ecosdomonte-posts`, access `push`) e clone-o.
2. Leia `posts/historico.csv`.
3. Escreva título, texto da arte, referência (só às 12h) e legenda conforme acima.
4. Gere a arte: `python3 gerar_arte.py --titulo "..." --texto "..." --referencia "..." --paleta N --saida posts/AAAA-MM-DD-HHh.jpg`. Use N = (dia do ano × 2 + 0 para 12h ou 1 para 19h) mod 5, para alternar as cores. Abra a imagem e confira se o texto está legível e nada foi cortado.
5. Acrescente a linha em `posts/historico.csv` com status `gerado`, faça commit e push para `main`.
6. Monte a URL pública fixa pelo SHA do commit: `https://raw.githubusercontent.com/hugozizzfuark-max/ecosdomonte-posts/<SHA>/posts/<arquivo>.jpg` e confirme com `curl -sI` que responde 200 e `image/jpeg`.
7. Publique com Windsor `execute_action`: conector `instagram`, conta `17841425594595406`, ação `create_image_post`, params `{image_url, caption}`.
8. Atualize o status no histórico para `publicado` (ou `erro: <motivo>`), commit e push.
9. Se algo falhar, não tente outra via: registre o erro no histórico e termine com uma mensagem curta dizendo o que falhou.
