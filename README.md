Un simple repositorio donde publico soluciones a problemas resueltos cuando tengo tiempo libre.

# Plataformas

## InfoSec
* [hackthebox](https://www.hackthebox.com/)
* [tryhackme](https://tryhackme.com)
* [picoctf](https://picoctf.org/)
* [cryptohack](https://cryptohack.org/)
* [kontra](https://application.security/free/owasp-top-10)
* [gameofhacks](www.gameofhacks.com)
* [bofhle](https://sysarmy.com/bofhle/)

## Dev
* [Beecrowd (ex URI Online Judge)](https://www.beecrowd.com.br/judge/es/profile/427859)
* [SoloLearn](https://www.sololearn.com/profile/8636629)
* [Frontedn Mentor](https://www.frontendmentor.io/)
* [Advent of Code](https://adventofcode.com/2020/about)
* [OmegaUp](https://omegaup.com/)
* [Mumuki](https://mumuki.io/)
* [RetosDeProgramacion](https://retosdeprogramacion.com/)

## Keyboard
* [TypingClub](https://www.typingclub.com/)
* [TypingStudy](https://www.typingstudy.com/es-latin_american-2/)
* [Vim Adventures](https://vim-adventures.com/)
* [Dvorak Programmers](https://www.npmjs.com/package/dvorak-programmers-tutorial)
* [Ktouch](https://apps.kde.org/ktouch/)

# ¿Qué es GIT?
[GIT](https://git-scm.com/) es un [Sistema de Control de Versiones](https://es.wikipedia.org/wiki/Control_de_versiones) (CVS), su utilidad se encuentra en cómo el mismo gestiona proyectos logrando que puedas volver en el tiempo a determinados estados y coordinar tu proyecto entre varias personas.

## ¿Cómo usar GIT?
GIT consta de 3 estados:
1. Working Directory.
2. Staging Area.
3. Repository.

## Instrucciones:
1. Configurar GIT:
    ``` bash
    git config --global user.name "Nombre Apellido"
    git config --global user.email tucorreo@dominio.com
    ```
2. Clonar repositorio:
    ``` bash
    git clone https://github.com/c05m4r/desafios.git
    ```
3. Pasar del Working Directory a Staging Area:
    ``` bash
    git add .
    ```
4. Pasar del Staging Area al repositorio local:
    ``` bash
    git commit -m "descripción"
    ```
5. Subir archivos al repositorio remoto:
    ``` bash
    git push origin master
    ```

## Recomendaciones
1. Realizar el "clone" por única vez
2. Para ver el estado de nuestros archivos:
    ``` bash
    git status
    ```
3. Para ver el registro de "commits" realizados:
    ``` bash
    git log
    ```
4. Si queremos arreglar el commit antes de hacer "push":
    ``` bash
    git commit --amend -m "Este es el mensaje correcto"
    ```
4. Si queremos arreglar el commit despues de hacer "push":
    ``` bash
    git reset --hard HEAD~1
    ```
5. Si deseamos actualizar el fork con los nuevos contenidos del repo original [LEER](https://medium.com/@sahoosunilkumar/how-to-update-a-fork-in-git-95a7daadc14e).
