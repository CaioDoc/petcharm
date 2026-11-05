---
name: petcharm-publicar
description: Use para testar localmente e publicar o site Pet Charm em hospedagem estática, e para a checagem final antes de ir ao ar.
---

# Testar e publicar

## Testar localmente
Abra `index.html` no navegador, ou rode um servidor simples na pasta:
```bash
python -m http.server 8080
```
e acesse http://localhost:8080.

## Checklist antes de publicar
- [ ] Os botões de WhatsApp (agendar, Táxi Pet, Clube VIP) abrem (11) 96901-0851 com a mensagem certa
- [ ] QR code abre o Instagram @petcharmestetica
- [ ] Testado em celular de verdade (menu, galeria, rolagem das fotos do salão)
- [ ] Sem erros no console
- [ ] Pasta `img/web` presente; originais (`img/About` etc.) podem ficar fora do upload

## Publicar (Railway — produção)
Projeto na Railway ligado ao repositório `CaioDoc/petcharm`, branch `main`, com deploy automático.
O build usa o `Dockerfile` (Caddy servindo `index.html`, `css/`, `js/`, `img/web/` na porta 8080).
- Endereço Railway: https://petcharm-production.up.railway.app
- Domínio: petcharmestetica.com.br e www (DNS na Cloudflare; registros CNAME + TXT `_railway-verify` informados pela Railway)
- Se mudar a pasta de imagens ou criar arquivos públicos novos, inclua no `Dockerfile` (linhas `COPY`).

## GitHub Pages (espelho)
Repositório: https://github.com/CaioDoc/petcharm
Cada `git push` na branch `main` dispara `.github/workflows/deploy.yml`, que publica
em https://caiodoc.github.io/petcharm/ em 1–2 minutos. Acompanhe na aba **Actions**.
Se criar uma pasta nova usada pelo site, adicione-a ao passo "Montar pasta do site" do workflow.

## Outras opções gratuitas
- **Netlify Drop**: arraste a pasta do projeto em https://app.netlify.com/drop
- **GitHub Pages**: suba os arquivos num repositório e ative Pages na branch `main`
- **Vercel**: `vercel` na pasta, sem configuração

## Depois de publicar
Troque `og:image` no `<head>` por URL absoluta (`https://seudominio/img/web/og-image.jpg`)
para a prévia aparecer bonita ao compartilhar no WhatsApp.
