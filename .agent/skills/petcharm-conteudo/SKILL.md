---
name: petcharm-conteudo
description: Use para alterar textos, serviços, estilos de tosa, perguntas frequentes, telefones ou endereços das unidades no site da Pet Charm.
---

# Editar conteúdo do site Pet Charm

Leia antes `.agent/rules/03-conteudo.md`.

## Trocar telefone ou endereço
O site tem uma unidade só (Jardim Sevilha). Procure o número antigo no `index.html`
(com e sem formatação) e troque todos — JSON-LD no `<head>`, card em `#contato`,
rodapé e **todos os links `wa.me`** (formato `55` + DDD + número, só dígitos: `5511969010851`).

## Atualizar a nota e os comentários do Google
1. Abra https://share.google/drHGLipDYlrS1VbYZ e veja a nota e o total de avaliações.
2. Atualize em `#avaliacoes`: `.score__num`, o `style="--rate:4.4"` das estrelas e o texto "33 avaliações".
3. Atualize também `aggregateRating` no JSON-LD do `<head>`.
4. Para trocar/adicionar comentários, copie um `<li class="review">`. Use só avaliações de 5 estrelas,
   com o texto como está no Google (pode corrigir erro de digitação), nome e data.

## Mensagens prontas do WhatsApp
Cada botão tem um texto pré-preenchido em `?text=` (codificado para URL):
agendar, Táxi Pet e Clube VIP. Para mudar, codifique a frase (ex.: `encodeURIComponent` no console do navegador).

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
