# DataCenter

## Description :
L’information est une ressource sensible. Une fuite des données peut provenir de zone insoupçonnable. Vérifiez s’il est possible d’extraire de la donnée depuis cette vidéo surveillance d’un datacenter

## Information complémentaire : 
Pour bien démarrer ce challenge vous devez télécharger la vidéo jointe au challenge.
Peut importe la forme que prend une donnée, elle peut être exploitée.

## Source :
datacenter.mp4

---

## Resolution : 
Indice mis à notre disposition :
- Peut importe la forme que prend une donnée, elle peut être exploitée.

En regardant la vidéo, je remarque que dans la première baie une diode clignote et que ça donne un message en morse qui faut décoder par la suite. 

J'ai analysé frame par frame la vidéo afin d'obtenir le code morse, voici le code morse obtenu : `.-.. ...-- ....- -.- ... .---- ... . ...- ...-- .-. -.-- .-- .... ...-- .-. .`.

J'ai donc utilisé le site [CyberChef](https://gchq.github.io/CyberChef/) et ajouter le module "From morse code", dans l'input j'ai mis le code morse obtenu ce qui m'a donné en output `L34KS1SEV3RYWH3RE`.

En lisant le mot, je remarque qu'il y'a plusieurs mots donnants : `L34K 1S EV3RYWH3RE`.

Voici le flag final : `HACK{L34K_1S_EV3RYWH3RE}`