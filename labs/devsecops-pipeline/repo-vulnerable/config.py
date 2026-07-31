"""Configuración de la aplicación de laboratorio.

TODOS los valores de este archivo son FALSOS y están escritos a propósito para
que un escáner de secretos los encuentre. No sirven para autenticarse contra
ningún servicio real: son cadenas con el formato correcto y contenido inventado.

El fallo que ilustra este archivo no es "tener una contraseña": es tenerla
EN EL CÓDIGO, es decir, en el historial de git para siempre, replicada en cada
clon del repositorio y visible para cualquiera con acceso de lectura.
"""

# Credenciales de base de datos embebidas (patrón clásico).
DB_HOST = "db.interno.lab"
DB_USER = "app_produccion"
DB_PASSWORD = "P4ssw0rd-Sup3r-S3cret4-2024"

# Clave de acceso con formato de AWS (inventada).
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Tokens de servicios de terceros.
#
# NEUTRALIZADOS A PROPÓSITO. En la versión original de este archivo aquí había
# un webhook de Slack y una clave de Stripe con el formato exacto del proveedor.
# GitHub los RECHAZÓ al subir el laboratorio, con su "push protection": un
# control del lado del servidor que analiza cada push y bloquea los patrones de
# secreto de alta confianza — aunque el valor sea inventado y aunque el
# repositorio tenga una allowlist local que los excluya.
#
# Es una lección del laboratorio, no un contratiempo: la protección de la
# plataforma NO respeta tu configuración local, y esa es exactamente su virtud.
# Ver la capa 3 en SOLUCION.md.
SLACK_WEBHOOK = "https://hooks.slack.invalid/services/EJEMPLO/DE/LABORATORIO"
STRIPE_API_KEY = "clave-de-pasarela-de-pago-EJEMPLO-NO-VALIDA"

# Token de API interno: sin prefijo de proveedor conocido, así que ningún
# detector lo reconoce por patrón. Solo lo delata su ENTROPÍA — y ese es
# justamente el tipo de secreto que más se escapa en un caso real.
INTERNAL_API_TOKEN = "f4c9a71e8b2d6350af17c9e4d8b25a06"

# Clave de firma de sesiones: fija, corta y predecible.
SECRET_KEY = "dev"

DEBUG = True
