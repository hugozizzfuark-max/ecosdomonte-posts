"""Gera a arte diária do @ecosdomonte (1080x1350 JPEG, formato 4:5).

Uso:
  python3 gerar_arte.py --titulo "Oração do meio-dia" \
      --texto "Senhor, ..." --referencia "Salmos 34:18" \
      --paleta 0 --saida posts/2026-11-12-12h.jpg
"""
import argparse
import os
import textwrap

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1080, 1350
AQUI = os.path.dirname(os.path.abspath(__file__))
FONTES = os.path.join(AQUI, "fontes")

# (fundo topo, fundo base, cor do texto, cor de destaque)
PALETAS = [
    ((247, 239, 228), (232, 214, 192), (58, 44, 34), (166, 120, 72)),   # areia
    ((236, 241, 238), (202, 219, 210), (36, 56, 48), (92, 128, 108)),   # sálvia
    ((244, 235, 236), (226, 204, 206), (66, 40, 46), (158, 96, 104)),   # rosa antigo
    ((34, 40, 58), (58, 54, 82), (246, 238, 226), (214, 182, 128)),     # noite
    ((240, 236, 246), (214, 206, 230), (48, 40, 70), (122, 100, 160)),  # lavanda
]


def fonte(nome, tamanho):
    caminho = os.path.join(FONTES, nome)
    if not os.path.exists(caminho):
        caminho = os.path.join("/usr/share/fonts/truetype/google-fonts", nome)
    return ImageFont.truetype(caminho, tamanho)


def fundo(topo, base):
    img = Image.new("RGB", (W, H), topo)
    px = img.load()
    for y in range(H):
        t = y / (H - 1)
        cor = tuple(int(topo[i] + (base[i] - topo[i]) * t) for i in range(3))
        for x in range(W):
            px[x, y] = cor
    # brilho suave no alto, como luz entrando
    luz = Image.new("L", (W, H), 0)
    ImageDraw.Draw(luz).ellipse((W * 0.15, -H * 0.35, W * 0.85, H * 0.35), fill=70)
    luz = luz.filter(ImageFilter.GaussianBlur(160))
    branco = Image.new("RGB", (W, H), (255, 255, 255))
    return Image.composite(branco, img, luz)


def quebrar(texto, f, largura_max, draw):
    linhas = []
    for paragrafo in texto.split("\n"):
        palavras, atual = paragrafo.split(), ""
        for p in palavras:
            teste = (atual + " " + p).strip()
            if draw.textlength(teste, font=f) <= largura_max:
                atual = teste
            else:
                linhas.append(atual)
                atual = p
        linhas.append(atual)
    return linhas


def gerar(titulo, texto, referencia, paleta, saida):
    topo, base, cor_txt, cor_dest = PALETAS[paleta % len(PALETAS)]
    img = fundo(topo, base)
    d = ImageDraw.Draw(img)
    margem = 120
    largura = W - 2 * margem

    # título pequeno no alto
    f_tit = fonte("Poppins-Medium.ttf", 34)
    tit = titulo.upper()
    espac = " ".join(tit)  # letras espaçadas
    if d.textlength(espac, font=f_tit) > largura:
        espac = tit
    d.text((W / 2, 170), espac, font=f_tit, fill=cor_dest, anchor="mm")
    d.line((W / 2 - 40, 215, W / 2 + 40, 215), fill=cor_dest, width=3)

    # texto principal: maior fonte que caiba (legível para público maduro)
    area_h = H - 2 * 300
    for tam in range(78, 39, -2):
        f_txt = fonte("Lora-Variable.ttf", tam)
        linhas = quebrar(texto, f_txt, largura, d)
        alt_linha = int(tam * 1.42)
        if len(linhas) * alt_linha <= area_h:
            break
    total = len(linhas) * alt_linha
    y = (H - total) / 2 + alt_linha / 2 - 10
    for linha in linhas:
        d.text((W / 2, y), linha, font=f_txt, fill=cor_txt, anchor="mm")
        y += alt_linha

    # referência
    if referencia:
        f_ref = fonte("Lora-Italic-Variable.ttf", 40)
        d.text((W / 2, y + 40), "— " + referencia, font=f_ref, fill=cor_dest, anchor="mm")

    # assinatura
    f_ass = fonte("Poppins-Regular.ttf", 30)
    d.text((W / 2, H - 110), "@ecosdomonte", font=f_ass, fill=cor_dest, anchor="mm")

    os.makedirs(os.path.dirname(os.path.abspath(saida)), exist_ok=True)
    img.save(saida, "JPEG", quality=92, optimize=True)
    return saida


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--titulo", required=True)
    ap.add_argument("--texto", required=True)
    ap.add_argument("--referencia", default="")
    ap.add_argument("--paleta", type=int, default=0)
    ap.add_argument("--saida", required=True)
    a = ap.parse_args()
    print(gerar(a.titulo, a.texto, a.referencia, a.paleta, a.saida))
