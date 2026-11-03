# Regra 02 — Código e qualidade

## Stack
- HTML5 semântico + CSS puro + JavaScript vanilla (IIFE em `js/main.js`). Sem build.
- Fontes do Google Fonts são o único recurso externo.

## CSS
- Use os tokens de `:root`; não escreva hex soltos fora dele (exceto `#fff` e o verde do WhatsApp).
- Classes no padrão BEM leve: `.bloco`, `.bloco__elemento`, `.bloco--variante`.
- Mobile-first na prática: todo layout novo precisa funcionar em 360px sem rolagem horizontal.
- Breakpoints usados: 1020, 960, 900, 860, 760, 640, 600, 560, 420px.

## Acessibilidade (obrigatório)
- Toda `<img>` de conteúdo tem `alt` descritivo em português; decorativas usam `alt=""`.
- Toda imagem tem `width`/`height` reais e `loading="lazy"` (exceto a primeira do hero).
- Botões que só têm ícone precisam de `aria-label`.
- Foco visível (`:focus-visible`) nunca pode ser removido.
- Contraste mínimo AA (4.5:1 para texto normal).

## Contato
- **O site não tem formulário.** Todo contato vai para o WhatsApp da unidade.
- Links de WhatsApp: `https://wa.me/55DDDNUMERO?text=...` com mensagem pré-preenchida (URL-encoded).
- Todos os botões de agendar são links diretos `wa.me` para (11) 96901-0851 (não há seletor de unidade).
- O Instagram aparece como QR code (`img/web/qr-instagram.svg`) + link de texto.

## Testes antes de entregar
1. Abrir no navegador em 1366px e 390px de largura.
2. Conferir: menu mobile, links do WhatsApp, filtros de tosa, galeria (setas, teclado, deslizar).
3. Console sem erros.
