# Solución — El cliente que mandaba demasiado

El servidor convirtió claims del cliente en estado canónico. La corrección es ignorar salud/munición
declaradas y aceptar acciones (`fire`, `pickup`, `damage_event`) cuyas precondiciones verifica el
servidor. La regresión envía los mismos claims en modo SECURE y comprueba salud 100, munición 30 y
rechazo o indiferencia explícita, además de un disparo normal aceptado.

`FLAG{servidor-autoridad}`
