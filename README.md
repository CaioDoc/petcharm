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

O site é publicado automaticamente no **GitHub Pages** a cada push na branch `main`
(workflow em `.github/workflows/deploy.yml`). Só `index.html`, `css/`, `js/` e `img/web/`
vão para o ar — as fotos originais ficam apenas no repositório.

Endereço: https://caiodoc.github.io/petcharm/

## Seções

1. **Início** — headline, botão de agendamento e polaroids do estúdio
2. **Nosso jeito** (`#cuidado`) — princípios de atendimento
3. **Serviços** (`#servicos`) — banho, hidratação, tosas, higiênica, carding, desembolo
4. **Estilos de tosa** (`#estilos`) — 10 estilos com filtro
5. **Estúdio** (`#estudio`) — mural de polaroids com galeria ampliada
6. **Direto do salão** — fotos reais de celular (rolagem lateral)
7. **Como agendar** (`#agendar`) — 3 passos
8. **Dúvidas** (`#duvidas`) — critérios, pagamento, filhotes
9. **Contato** (`#contato`) — WhatsApp de cada unidade + QR code do Instagram

## Contatos usados no site

| Unidade | Endereço | WhatsApp |
|---|---|---|
| Jardim Sevilha | Av. Norte e Sul, 207 | (11) 96901-0851 |
| Jardim do Sul | Av. Sebastião Silvério, 169 (em frente à Clínica Santa Helena) | (11) 93385-3563 |

Instagram: [@petcharmestetica](https://www.instagram.com/petcharmestetica/)

## Pendências sugeridas

- Horário de funcionamento (não informado nos materiais — não foi inventado)
- Domínio próprio e `og:image` com URL absoluta após publicar
- Depoimentos reais de clientes (Google / Instagram), se a dona quiser
