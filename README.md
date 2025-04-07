# ProvidenceScript
Programming Language created based off of ShadowScript (Additional comments for myself mostly.)

ProvidenceScript este un limbaj de programare simplificat, creat de mine de la zero in Python, ca proiect de invatare folosind ghidul acesta: https://www.youtube.com/watch?v=1WpKsY9LBlY.

Totul este impartit in 4 componente esentiale:

# Lexer – traducerea textului in tokeni

Ce face: Ia textul scris in ProvidenceScript si il imparte in unitati de baza numite tokeni (cuvinte cheie, numere, simboluri, etc).

Practic, parcurge codul caracter cu caracter si identifica:

numere intregi sau reale

variabile (siruri de litere)

cuvinte cheie rezervate (ex: make, if, while)

operatori matematici si logici (+, -, =, >, ?=, etc)

Tokenii sunt reprezentati de clase simple: Integer, Float, Variable, Operation, Boolean, Comparison, Declaration, Reserved.

# Parser – constructia arborelui de sintaxa

Ce face: Primeste lista de tokeni de la Lexer si o transforma intr-un arbore de sintaxa (parse tree), adica o structura care reflecta ordinea logica a operatiilor.

Se ocupa de:

expresii matematice (ordine corecta a operatiilor)

expresii logice (ex: and, or, not)

instructiuni if, elif, else, while

atribuiri de variabile (make x = ...)

Exemplu: make z = (x + y) * 2 se transforma intr-o structura de tip arbore unde operatia de baza este =, iar partea dreapta este un calcul matematic organizat logic (intai x + y, apoi inmultit cu 2).

# Interpreter – executia logicii din arbore

Ce face: Primeste arborele construit de Parser si il parcurge pentru a executa efectiv operatiile.

Aici se intampla evaluarea:

Se citesc valorile variabilelor

Se efectueaza calculele matematice

Se evalueaza conditii

Se executa ramuri conditionale si bucle

Interpreterul poate lucra cu:

operatii binare (+, -, *, >, etc.)

operatii unare (-x, not x)

expresii conditionale si bucle (if, while)

atribuiri (make x = ...)

Toate variabilele sunt stocate si gestionate printr-o clasa Data, care are metode de citire si scriere.

# Shell – bucla principala de executie

Ce face: Este interfata care preia inputul de la utilizator (cod scris in ProvidenceScript), il trimite prin cele trei componente anterioare si afiseaza rezultatul final.

Fluxul este urmatorul:

Se primeste inputul de la utilizator

Inputul este trecut prin Lexer → Parser → Interpreter

Se afiseaza rezultatul (daca exista)

Acesta este practic un REPL (Read, Eval, Print Loop) interactiv.

Sintaxa de baza in ProvidenceScript

make x = 5 # declara o variabila make y = 10

make z = (x + y) * 2 # expresii cu paranteze

if x > 3 do make x = x + 1

while x < 10 do make x = x + 1

# Reguli:

Toate variabilele trebuie declarate inainte de a fi folosite.

make este cuvantul cheie pentru initializare.

do marcheaza inceputul blocului de instructiuni pentru if si while.

Nu se folosesc acolade sau indentare stricta; limbajul este guvernat de o structura logica simplificata.

# Concluzie

ProvidenceScript este un proiect prin care am invatat cum se construieste un limbaj de programare de la zero. Am inteles cum functioneaza fazele de lexing, parsing si interpretare, si am creat o structura modulara care poate fi extinsa usor.

Este un limbaj simplu, dar complet functional, cu suport pentru variabile, expresii, conditii si bucle. Cel mai important, a fost construit integral de mine si reflecta stilul meu de gandire si invatare.
