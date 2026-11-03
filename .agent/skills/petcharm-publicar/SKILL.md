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

## Publicar (GitHub Pages — já configurado)
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
