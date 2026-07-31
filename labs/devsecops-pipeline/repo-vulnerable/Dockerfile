# Dockerfile DELIBERADAMENTE MAL ESCRITO (objetivo de hadolint y trivy).
#
# Cada línea contiene al menos un antipatrón reconocible. El ejercicio es que
# hadolint te diga cuáles, con qué código de regla, y que tú decidas cuáles son
# un riesgo real de seguridad y cuáles son solo estilo o tamaño de imagen —
# distinguirlo es la mitad del trabajo.

# [DKR-1] Imagen base sin etiqueta de versión: hoy es una cosa, mañana otra.
FROM python:latest

# [DKR-2] apt-get upgrade dentro de la imagen: builds no reproducibles.
# [DKR-3] Sin --no-install-recommends y sin limpiar /var/lib/apt/lists.
# [DKR-4] Instala herramientas de red que no hacen falta en tiempo de ejecución
#         y que le sirven a un atacante si consigue ejecución en el contenedor.
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y curl wget netcat-openbsd vim sudo

# [DKR-5] Copia TODO el contexto, incluidos .git, credenciales y basura local.
COPY . /app

WORKDIR /app

# [DKR-6] Dependencias sin fijar y sin verificación de integridad.
RUN pip install -r requirements.txt

# [DKR-7] Secreto inyectado como variable de entorno en la propia imagen:
#         queda grabado en la capa y lo lee cualquiera con `docker history`.
ENV API_TOKEN="tok_live_000000000000000000000000EXAMPLE"

# [DKR-8] Sin instrucción USER: el proceso corre como root.
# [DKR-9] Puerto de depuración expuesto.
EXPOSE 8080
EXPOSE 5678

# [DKR-10] Forma shell del CMD: el proceso no recibe las señales del sistema.
CMD python app.py
