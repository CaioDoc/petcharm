# Servidor estático do site Pet Charm (Railway)
FROM caddy:2.8-alpine

COPY Caddyfile /etc/caddy/Caddyfile

# Somente os arquivos públicos (fotos originais ficam fora da imagem)
COPY index.html /srv/
COPY css /srv/css
COPY js /srv/js
COPY img/web /srv/img/web

# A Railway define a variável PORT; 8080 é o padrão local
ENV PORT=8080
EXPOSE 8080
