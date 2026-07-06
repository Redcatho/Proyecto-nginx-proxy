# 1. Usamos una imagen ligera de Nginx como base
FROM nginx:alpine

# 2. Copiamos nuestro index.html local dentro del directorio por defecto donde Nginx busca los archivos web
COPY index.html /usr/share/nginx/html/

# 3. Exponemos el puerto 80 del contenedor
EXPOSE 80
