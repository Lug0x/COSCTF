# Pour vivre secure vivons caché Part 2

## Description :
Nous avons réussi via la procédure de récupération de compte mail à accéder à sa messagerie.
Examinons tous ses messages à la recherche d'informations sensibles.

## Information complémentaire : 
Trouvez un moyen de s'authentifier sur les autres comptes de la cible afin de collecter encore plus d'informations.

## Source :
blog.challenge.operation-kernel.fr

---

## Resolution : 
Indice mis à notre disposition :
- Il faut trouver un moyen de se connecter à ses autres comptes pour obtenir des informations. 

### Gmail du futur
En analysant les mails qu'il a réçu, il y en a deux qui ont particulièrement attirés mon attention :
- "Account confirmation" de instafakegram.
- "Votre nouveau compte" de fakebank.

Dans le mail de instafakegram, je peux voir qu'il a reçu un récapitulatif de son compte contenant son adresse mail et son mot de passe :
- email : michel.aquemoi@challenge.operation-kernel.fr
- Mot de passe : MichelInstafakegram42!

Dans le mail de fakebank, il me donne juste l'identifiant de son compte qui est 3735928559 et un mot de passe qui a été généré aléatoirement pour la première connexion.

### Connexion aux autres comptes
J'ai donc essayé de me connecter sur ses autres comptes disponibles, j'ai remarqué que dans son mot de passe instragam il met le nom du site. J'en déduit donc que son mot de passe est en général Michel{Nom du site}42!.

- Fakebook : 
    - login : michel.aquemoi@challenge.operation-kernel.fr
    - Mot de passe : MichelFakebook42!
    - Connexion : OK !
- Blog :
    - login : michel.aquemoi@challenge.operation-kernel.fr
    - Mot de passe : MichelBlog42!
    - Connexion : OK ! 
- Linkedfakein : 
    - login : michel.aquemoi@challenge.operation-kernel.fr
    - Mot de passe : MichelLinkedfakein42!
    - Connexion : OK !
-Bank :
    - login : michel.aquemoi@challenge.operation-kernel.fr
    - Mot de passe : MichelFakeBank42!
    - Connexion : KO !

Je remarque que le mot de passe ne fonctionne pas sur le site de la banque et qu'en me connectant sur le compte fakebook de la victime, j'ai accès à ses messages !

Il a une conversation avec un Arnaud et il dit à Arnaud que son adresse dans 42 est découverte et qu'il va se faire discret dans le 69.

Je me suis rappelé qu'il habitait à Saint-Etienne dont le code postal est "42" qui sont présents à la fin de ses mots de passe donc, je me dis qu'il est possible qu'il a juste mis "69" à la place de "42" pour son mot de passe de banque.

Je test donc :

- Bank :
    - login : michel.aquemoi@challenge.operation-kernel.fr
    - Mot de passe : MichelFakebank69!
    - Connexion : OK !

Bingo ! Ca fonctionne et j'obtiens le flag final !

Voici le flag final : `HACK{M0r3_InF0_Y0u_H4v3_M0re_Y0u_C4n_G3T}`