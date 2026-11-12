# Rotina de posts do @ecosdomonte

Cada execução agendada publica **um** post no Instagram @ecosdomonte (conta Windsor `17841425594595406`, conector `instagram`).

## Linha editorial
- Perfil cristão de fé, reflexões e devocional. Público majoritariamente feminino, maduro (muitas 55+), passando por dias difíceis.
- Tom: acolhedor, simples, esperançoso. Nada de julgamento, medo ou promessas de prosperidade. Português do Brasil.
- **Horário 12h — "Palavra do meio-dia":** um versículo bíblico curto (no máximo ~30 palavras), com referência. Temas: consolo, força, recomeço, cuidado de Deus, ansiedade, perdão, gratidão.
- **Horário 19h — "Oração da noite"** (ou "Oração para hoje", "Uma oração para você"): oração curta em primeira pessoa (35 a 55 palavras), terminando em "Amém." Escreva a oração com palavras próprias; sem referência na arte.
- Nunca repita versículo ou tema dos últimos 14 dias: consulte `posts/historico.csv` antes de escrever.

## Legenda (até ~900 caracteres)
1. Primeira linha forte que puxe a leitura (ex.: "Se hoje o seu coração está pesado, leia isto.").
2. Reflexão curta de 3 a 5 frases ligando o texto à vida real.
3. Convite simples para interação, sem pedir "comente Amém": ex. "Salve para reler quando precisar" ou "Envie para alguém que precisa ouvir isso hoje".
4. Chamada para o programa, em 1 a 2 frases, variando o texto: "✨ Se você está atravessando um tempo de dor, o recomeço de 21 dias *Depois da Dor, Deus* foi feito para você. Link na bio."
5. De 5 a 8 hashtags em português: misture amplas (#fé #deus #oração #devocional) e específicas (#oraçãodanoite #palavradedeus #recomeço #mulheresdefé).

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
