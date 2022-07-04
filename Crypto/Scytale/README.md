# Scytale

## Description :

En fouillant une planque utilisée par des cyber-attaquants, la Police a retrouvé de curieuses bandelettes de papier sur lesquelles sont inscrites des lettres. A quoi peuvent-elles bien servir ?

## Information complémentaire : 
Les chiffrements de transposition sont les plus anciens dispositifs de cryptographie militaire connue.

## Source :
message.txt

---

## Resolution : 

Indices mis à notre disposition :
- Le nom du challenge est "Scytale" qui fait référence à une méthode de chiffrement.
- L'information complémentaire qui donne un grand indice également "dispositifs de cryptographie militaire connue".

Afin de résoudre de challenge, je suis allé sur le site [Decode](https://www.dcode.fr/chiffre-scytale) qui a une page dédiée au chiffrement et au déchiffrement en Scytale.
J'ai rentré le contenu présent dans "message.txt" `Bj.lsC1_T!iolatKsSA.eueg.{_PA.né..HT14}..efeAhSR..` dans l'input "Déchiffrement" et coché la case "Conserver la ponctuation et les espaces".

En cliquant sur "Déchiffrer la scytale", le site nous affiche les résultats à gauche. Celui qui nous intéresse est le premier résultat qui donne `Bien.jouée.le.flag.est.HACK{Th1s_1S_SP4RTAA}.!....`.

Voici le flag final : `HACK{Th1s_1S_SP4RTAA}'