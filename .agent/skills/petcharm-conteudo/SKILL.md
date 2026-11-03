---
name: petcharm-conteudo
description: Use para alterar textos, serviços, estilos de tosa, perguntas frequentes, telefones ou endereços das unidades no site da Pet Charm.
---

# Editar conteúdo do site Pet Charm

Leia antes `.agent/rules/03-conteudo.md`.

## Trocar telefone ou endereço de uma unidade
O dado aparece em **5 lugares** do `index.html`. Procure pelo número antigo (com e sem formatação) e troque todos:
1. JSON-LD no `<head>` (`"telephone"` e `"streetAddress"`)
2. Card da unidade em `#contato` (`.unit__addr`, `.unit__phone`, `href` do botão)
3. Seletor `#picker` (texto e `href`)
4. Rodapé "Como chegar" (texto e link do Google Maps)
5. Link `wa.me`: formato `55` + DDD + número, só dígitos. Ex.: `5511969010851`

## Adicionar um estilo de tosa
1. Prepare a foto (skill `petcharm-imagens`) como `img/web/tosa-NOME.webp`.
2. Copie um `<li class="cut">` dentro de `#cuts` e ajuste:
   - `data-tags`: um ou mais de `pratica`, `volume`, `raca` (separados por espaço)
   - `<h3>`: nome do estilo; `<p>`: para quem é; `<ul>`: 2–3 benefícios
3. Se criar uma categoria nova, adicione um `<button class="chip" data-filter="nova">` em `.chips`.

## Adicionar uma pergunta frequente
Copie um bloco `<details>` em `.faq__list`. Pergunta no `<summary>`, resposta num `<p>`.
Só a primeira pergunta fica com `open`.

## Adicionar um serviço
Copie um `<li class="svc__item">` em `.svc`. O ícone é um `<symbol>` no fim do `index.html`
(desenhe em `viewBox="0 0 32 32"`, traço `stroke-width="2"`, `currentColor`).
