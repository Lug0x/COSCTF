# AudioSpectre

## Description :

Un lecteur MP3 a été retrouvé à côté d’un serveur compromis lors d’une cyberattaque. Dessus, seul un fichier audio a été retrouvé. Prêt pour un interlude musical ?


## Information complémentaire : 
Même si un son a pour but premier d'être écouté, l'analyse de son spectre peut présenter tout autant d'intérêt et révéler des messages cachés.

## Source :
AudioSpectre.wav

---

## Resolution : 

Reprenons les indices mis à notre dispositions :
- Le nom du fichier qui est "Audi**Spectre**".
- Dans les informations complémentaires, nous pouvons remarquer cette partie : **l'analyse de son spectre peut présenter tout autant d'intérêt**
Par la suite dans les informations complémentaires, on nous dit qu'analyser le spectre peut donner des informations.

Donc il faut analyser le spectre du fichier pour cela, j'ai utilisé [Audacity](https://audacity.fr/) qui permet d'analyser le fichier audio.

En ouvrant Audacity, j'ai effectué les étapes suivantes : 
- File > Open > AudioSpectre.wav
- Clique droit sur l'audio > Spectogram

En effectuant ces étapes, j'ai eu le flag qui s'est affiché : `HACK{FuN_W1tH_AuD1o}`
