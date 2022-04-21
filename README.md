Actividad 2 - Hito 3 Criptografia y seguridad en redes
===============
- En este Hito, el/la estudiante deberá auditar la implementación de los sistemas de creación, actualización, acceso, transmisión y recuperación de contraseñas de 2 los dos sitios elegidos en los hitos anteriores (uno de uso exclusivo para usuarios chilenos y uno para usuarios pertenecientes a la comunidad europea), automatizando el proceso mediante el uso del lenguaje de programación a su elección.

- Para esto, deberá implementar un código en el lenguaje que usted estime conveniente, para automatizar lo siguiente:
>
> - Creación de una cuenta
> - Inicio de sesión (permitirá hacer ataques por fuerza bruta contra su cuenta de usuario).
> - Restablecimiento de contraseña (no requiere login del usuario).
> - Modificación de contraseña (requiere login del usuario).
> 
_________________

## Desarrollo del Hito
- Para la creación de la automatizacion se utilizo `python` junto con una libreria llamanda `selenium`.
- Gracias a esta libreria, se puede lograr ejectuar una version de prueba de `Google Chrome`y controlarla mediante codigo.

### Pagina Chilena 
- La pagina chilena utilizada en este ejercicio es [Dust2](https://dust2.gg/), la que nos permite la creacion de un usuario, modificar la contraseña posterior al inicio de sesion, cambiar la contraseña via Mail sin ningun mayor problema.
- En cuanto a la ejecucion del codigo se tiene
  - Primero se debe ejecutar el archivo 
