# Crypto
## Description :
Vous avez réussi à obtenir l'accès au dossier où se situent les fichiers uploadés. Cependant, tous les fichiers sont chiffrés.
Fort heureusement, l'algorithme de chiffrement est présent dans le dossier, trouver un moyen de le déchiffrer.

## Information complémentaire : 
Essayez de vous attaquer à une partie de l'algorithme pour réduire le temps de calcul.

## Source :
encrypt.py et CONFIDENTIEL.xlsx.enc

---

## Resolution : 
Je tiens à remercier N00tice, pour ses explications qui m'ont permis de résoudre le challenge.
### Analyse du fichier encrypt.
Je commence à analyser la partie du "if __name__".
```
if __name__ == '__main__':
    args = parse_args()
    print('Welcome to Encryptor')
    print('Encrypting %s using :' % args.file, args.passphrase)
    plaintext = open(args.file, 'rb').read()
    passphrase = args.passphrase
    ciphertext = Encryptor(passphrase).encrypt(plaintext)
    if args.output_file:
        print("Cipher data saved in : %s" % args.output_file)
        f = open(args.output_file, 'wb')
        f.write(ciphertext)
        f.close()
    else:
        print('Your file after encryption is', ciphertext.hex())
```
Dans cette partie de code, il y a une variable qui attire mon attention est **ciphertext**.
Je remarque qu'elle utilise la classe Encryptor et lui passe en paramètre la passphrase, par la suite elle appelle la méthode encrypt et elle passe en paramètre le contenu du fichier.

Je passe donc à l'analyse de la classe Encryptor.
```
class Encryptor(object):
    def __init__(self, passphrase):
        self.key = passphrase.encode()

    def generateKey(self):
        self.key = hashlib.sha256(self.key).digest()[:6]
        return self.key

    def xor(self, a, b):
        res = []
        for ac, bc in zip(a, b):
            res.append(ac^bc)
        return res

    def encryptBlock(self, block):
        key = list(self.generateKey())
        l = list(block[:8])
        r = list(block[8:])
        for iround in range(6):
            keybyte = key.pop()
            for isubround in range(4):
                f = []
                for i in range(8):
                    f.append(sbox[l[i] ^ keybyte])
                    keybyte = (keybyte + 1) % 256
                f = [f[pbox[i]] for i in range(8)]
                l, r = self.xor(r, f), l
        return bytes(l+r)

    def encrypt(self, plaintext):
        while len(plaintext)%16:
            plaintext += b'\0'

        ctr = random.getrandbits(128)

        encrypted = ctr.to_bytes(16, 'big')
        for i in range(0, len(plaintext), 16):
            encryptedBlock = self.encryptBlock(ctr.to_bytes(16, 'big'))
            encrypted += bytes(self.xor(plaintext[i:i+16], ctr.to_bytes(16, 'big')))
            ctr += 1
        return encrypted 
```
La classe Encryptor possède plusieurs méthodes, mais celle qui m'intéresse est "encrypt". Dans celle-ci, je retrouve deux méthodes :
- encryptBlock
- xor

Avec un éditeur comme visual studio code, je remarque que la méthode encryptBlock n'est pas utilisé et que la méthode Xor est utilisé.
```
def encrypt(self, plaintext):
        while len(plaintext)%16:
            plaintext += b'\0'

        ctr = random.getrandbits(128)

        encrypted = ctr.to_bytes(16, 'big')
        for i in range(0, len(plaintext), 16):
            encryptedBlock = self.encryptBlock(ctr.to_bytes(16, 'big'))
            encrypted += bytes(self.xor(plaintext[i:i+16], ctr.to_bytes(16, 'big')))
            ctr += 1
        return encrypted 
```
Dans la méthode encrypt, je remarque qu'il y a une variable CTR qui génère aléatoirement qui retourne un entier avec 128 bits. Par la suite, je remarque que ce CTR est appelé dans la variable "encrypted". 

Dans cette variable, il prend le CTR qui met en 16 octets et place le byteorder en big qui signifie que l'octet le plus significatif est mis au début.

Je vois également une boucle for qui débute à 0, ce stop à la fin de la longueur du contenu du fichier et qui incrémente de 16 entre chaque élément de la liste.

Je remarque également qu'il ajoute à la variable encrypted qui utilise la méthode bytes permettant de convertir des objets en objets de type bytes. En effectuant un XOR du plaintext qui découpe en bloc de 16 octes et du CTR.

Puis il augmente le CTR de 1 à chaque fois.

### Solution.
Grâce à l'analyse de la méthode "Encrypt", je sais que la variable encrypted peut me servir à déchiffrer le fichier sachant que sa valeur sera le premier bloc d'octet présent dans le fichier. 

Avec un site comme [Hexed](https://hexed.it/) permettant d'analyser les octets d'un fichier en hexadecimal, je peux remarquer que la première ligne contient la valeur de la variable "encrypted".
```
00000000 74 63 9D 71 57 0D 80 F5 17 06 20 FB DD 72 BC DA
00000010 24 28 9E 75 43 0D 86 F5 1F 06 20 FB FC 72 69 F7
00000020 8E 68 01 70 57 0D 36 F3 17 06 33 FB D5 70 E7 98
```
J'ai donc repris la valeur du premier octet et repris le script "encrypt" que j'ai modifié afin d'obtenir le script "decrypt" disponible [ici](https://github.com/Lug0x/COSCTF/blob/main/Crypto/Crypto/decrypt.py).

Dans ce script, j'ai modifié le nom de la methode "Encrypt" par "Decrypt", remplacé le CTR par la valeur hexadecimal et remplacé le nom de la variable encrypted par decrypted avec bytes().
```
def decrypt(self, cipherfile):
        while len(cipherfile)%16:
            cipherfile += b'\0'

        ctr = int("74639D71570D80F5170620FBDD72BCDA", 16)
        decrypted = bytes()

        for i in range(16, len(cipherfile), 16):
            decrypted += bytes(self.xor(cipherfile[i:i+16], ctr.to_bytes(16, 'big')))
            ctr += 1
        return decrypted
```  
En exécutant le script decrypt.py, j'obtiens le fichier CONFIDENTIEL.xlsx déchiffré.

Voici le flag final : `HACK{ImplementationErrorBreaksCiphers}`