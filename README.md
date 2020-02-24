# LeGeneralDeBot

Code Python qui génère la grammaire Tracery pour le bot twitter @LeGeneralDeBot, de façon à mimer sa célèbre anaphore énoncée lors de la libération de Paris en 1944.

## Grammaire

L'idée et de choisir au hasard 4 participes passés des verbes du premier groupe. Comme corpus, j'utilise le repository [Verbes Français Conjugués](https://github.com/Drulac/Verbes-Francais-Conjugues).

Pour ne pas avoir de répétition de verbe, je coupe cette liste en 4 parties égales (4 verbes à placer).

```
liste1, liste2, liste3, liste4
```

Comme je souhaite placer tous les verbes à toutes les places possibles, ma grammaire racine se compose de toutes les permutation de ces listes.

La première permutation étant évidemment:

```
"Paris! Paris #liste1#! Paris #liste2#! Paris #liste3#! Mais Paris #liste4#!
```

Il suffit juste de générer les 23 autres permutations (c'est à dire la factorielle de 4: `4!`)