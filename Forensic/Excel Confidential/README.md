# Excel Confidential
## Description :
Dans le dossier contenant les fichiers uploadés, nous avons trouvé un fichier excel.
Lise MITENER nous confirme que ce document ne lui appartient pas.
Le document est protégé par un mot de passe. Trouver un moyen d'accéder à l'information que contient ce tableur.

## Information complémentaire : 
Les documents excel ont tous une architecture semblable, il existe surement une méthode simple pour outrepasser la protection.

## Source :
CONFIDENTIEL.xlsx

---

## Resolution : 
Dans les informations complémentaires, l'auteur stipule qu'il existe une méthode simple pour outrepasser la protection du fichier excel.

J'ai donc mis le fichier "CONFIDENTIEL.xlsx" en "CONFIDENTIEL.zip", en ouvrant le zip j'obtiens plusieurs dossiers :
- docProps
- xl
- _rels
- [Content_Types].xml

Je m'intéresse donc à la partie "XL" et je vois un fichier "workbook.xml". En l'ouvrant, on peut voir :
```
<sheets>
	<sheet name="AVERTISSEMENT" sheetId="1" r:id="rId1"/>
    <sheet name="CONFIDENTIEL" sheetId="4" state="hidden" r:id="rId2"/>
</sheets>
```
J'ai supprimé le "state='hiden'", sauvagrdé le fichier puis je l'ai remis dans le zip.
J'ai remis l'extension original "xlsx" et en ouvrant le fichier j'ai bien l'onglet "CONFIDENTIEL" avec le flag. 

Voici le flag final : `HACK{3xcEl_R3al_Pr0TeCT10N?}`