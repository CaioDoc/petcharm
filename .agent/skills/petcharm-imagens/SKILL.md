---
name: petcharm-imagens
description: Use para adicionar, trocar ou otimizar fotos do site Pet Charm (estúdio, salão, estilos de tosa, logo) e para regenerar o QR code do Instagram.
---

# Imagens do site Pet Charm

Originais ficam em `img/About`, `img/Logo`, `img/Picture`, `img/Studio` e **não** são usados direto.
O site usa apenas `img/web/`, com nomes sem espaço e sem acento.

## Padrões
| Tipo | Nome | Largura máx. | Formato |
|---|---|---|---|
| Estúdio (quadrada) | `estudio-NN.webp` | 900px | WebP q80 |
| Salão (retrato 3:4) | `salao-NN.webp` | 720px | WebP q80 |
| Estilo de tosa | `tosa-NOME.webp` | 800px | WebP q80 |

Fotos de estilo vêm dos posts em `img/About`: **recorte a parte de cima com o texto** e
mantenha só o cachorro (o texto é escrito em HTML no card).

## Converter com Python + Pillow
```python
from PIL import Image
im = Image.open("img/Studio/dog_ (17).jpeg").convert("RGB")
im.thumbnail((900, 900))
im.save("img/web/estudio-17.webp", "WEBP", quality=80, method=6)
```
Recorte de post (ex.: remover os 500px de cima): `im.crop((0, 500, im.width, im.height))`.

## Adicionar foto ao Estúdio
1. Gere `img/web/estudio-NN.webp`.
2. Em `#board`, copie um `<li>` e ajuste `data-index` (sequencial, começando em 0), `src` e `alt`.
3. O alt descreve o pet: raça/cor + acessório. Ex.: "Spitz laranja com babador rosa".

## QR code do Instagram
```bash
python tools/qr.py "https://www.instagram.com/petcharmestetica/" img/web/qr-instagram.svg
```
O script gera SVG na cor chocolate da marca e (se o OpenCV estiver instalado) confere a leitura.
Sempre teste o QR com a câmera do celular depois de trocar.
