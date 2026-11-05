# Pet Charm Estética Animal — Landing page

Site one-page da **Pet Charm Estética Animal** (banho e tosa em Bragança Paulista, SP).
HTML + CSS + JavaScript puros, sem build, sem dependências. Basta abrir `index.html`
no navegador ou enviar a pasta para qualquer hospedagem estática
(Netlify, Vercel, GitHub Pages, Hostinger etc.).

## Estrutura

```
index.html            página única (todas as seções)
css/style.css         estilos + tokens da marca (variáveis :root)
js/main.js            menu mobile, escolha de unidade, filtro de tosas, galeria
img/web/              imagens otimizadas usadas pelo site (WebP / PNG / SVG)
img/About|Logo|...    originais (não são carregadas pelo site)
tools/qr.py           gera o QR code do Instagram em SVG
.agent/rules/         regras do projeto (marca, código, conteúdo)
.agent/skills/        skills: como editar conteúdo, imagens e publicar
AGENTS.md             ponto de entrada para agentes de IA
```

## Publicação

### Railway (produção)
O site roda na Railway com um container **Caddy** (`Dockerfile` + `Caddyfile`), na porta 8080.
Cada push na `main` gera um novo deploy automaticamente. A imagem leva só `index.html`, `css/`, `js/` e `img/web/`.
Endereços: https://petcharm-production.up.railway.app (Railway) e
https://petcharmestetica.com.br / https://www.petcharmestetica.com.br (domínio próprio, DNS na Cloudflare).

### GitHub Pages (espelho)

O site é publicado automaticamente no **GitHub Pages** a cada push na branch `main`
(workflow em `.github/workflows/deploy.yml`). Só `index.html`, `css/`, `js/` e `img/web/`
vão para o ar — as fotos originais ficam apenas no repositório.

Endereço: https://caiodoc.github.io/petcharm/

## Seções

1. **Início** — headline, botão de agendamento e polaroids do estúdio
2. **Nosso jeito** (`#cuidado`) — princípios de atendimento
3. **Serviços** (`#servicos`) — banho, hidratação, tosas, higiênica, carding, desembolo
   + **Táxi Pet** e **Clube VIP** (`#taxi-vip`), com botões para o WhatsApp
4. **Estilos de tosa** (`#estilos`) — 10 estilos com filtro
5. **Estúdio** (`#estudio`) — mural de polaroids com galeria ampliada
6. **Direto do salão** — fotos reais de celular (rolagem lateral)
7. **Avaliações** (`#avaliacoes`) — nota do Google (4,4 · 33 avaliações) e comentários 5 estrelas
8. **Como agendar** (`#agendar`) — 3 passos (pet → serviços → horário)
9. **Dúvidas** (`#duvidas`) — critérios, Táxi Pet, pagamento, filhotes
10. **Contato** (`#contato`) — WhatsApp + QR code do Instagram

## Dados usados no site

- **Unidade:** Jardim Sevilha — Av. Norte e Sul (Av. Dr. Tancredo de Almeida Neves), 207, sala 4, CEP 12914-160
- **WhatsApp:** (11) 96901-0851
- **Táxi Pet:** segunda a sexta, das 8h às 17h
- **Google:** nota 4,4 com 33 avaliações (conferido em 03/11/2026) — https://share.google/drHGLipDYlrS1VbYZ
- **Instagram:** [@petcharmestetica](https://www.instagram.com/petcharmestetica/)

## Pendências sugeridas

- Horário de funcionamento (não informado nos materiais — não foi inventado)
- Domínio próprio e `og:image` com URL absoluta após publicar
- Atualizar a nota e os comentários do Google de tempos em tempos (seção `#avaliacoes` e JSON-LD no `<head>`)
- Valores/condições do Clube VIP, se a dona quiser divulgar
