# Regra 01 — Identidade visual Pet Charm

A marca é delicada, carinhosa e "fofa", mas profissional. Rosa + chocolate, nunca cores frias dominantes.

## Cores (definidas em `css/style.css` → `:root`)

| Token | Hex | Uso |
|---|---|---|
| `--pink` | `#EC4D97` | rosa do logo: ícones, detalhes, marcadores |
| `--pink-ink` | `#D62A7B` | fundo de botões com texto branco (contraste AA) |
| `--pink-deep` | `#B01C64` | rosa para **texto** sobre fundo claro |
| `--petal` | `#F8C9DA` | fitas adesivas, chips, bordas suaves |
| `--blush` | `#FDEEF3` | fundo principal (mesmo tom do estúdio de fotos) |
| `--milk` | `#FFFAFB` | papel das polaroids, seções alternadas |
| `--cocoa` | `#4A2416` | marrom do logo: títulos, texto, seções escuras |
| `--cocoa-soft` | `#7A5143` | texto secundário |

- Nunca use `--pink` (#EC4D97) como cor de texto pequeno sobre fundo claro: use `--pink-deep`.
- Botão principal = rosa (`.btn--pink`). Botão secundário = contorno chocolate (`.btn--ghost`).
- Verde `#25D366` só no botão flutuante do WhatsApp.

## Tipografia

- **Fraunces** (Google Fonts, eixo `SOFT` 100): títulos. Lembra as serifas arredondadas dos posts.
- **Nunito**: textos, botões, menus.
- Não acrescente uma terceira família.

## Elemento-assinatura: polaroid com fita adesiva

Vem dos próprios posts da marca (fotos com fita rosa). Use em: hero e mural do Estúdio.
Não espalhe polaroids pelo site todo — é o detalhe memorável justamente por ser pontual.

## Logo

- `img/web/logo-horizontal.png` (fundo transparente): header e rodapé.
- `img/web/logo-selo.webp` (selo redondo): carimbo decorativo no hero e no Estúdio.
- Não distorcer, não recolorir, não colocar sobre fundo chocolate sem área de respiro clara.

## Movimento

Um único momento orquestrado: as polaroids do hero "caindo" na mesa ao carregar.
Não adicione animações de entrada em cada seção. Sempre respeite `prefers-reduced-motion`.
