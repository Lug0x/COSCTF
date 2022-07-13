#!/usr/bin/env python
import argparse


class Decryptor(object):

    def xor(self, a, b):
        res = []
        for ac, bc in zip(a, b):
            res.append(ac^bc)
        return res

    def decrypt(self, cipherfile):
        while len(cipherfile)%16:
            cipherfile += b'\0'

        ctr = int("74639D71570D80F5170620FBDD72BCDA", 16)
        decrypted = bytes()

        for i in range(16, len(cipherfile), 16):
            decrypted += bytes(self.xor(cipherfile[i:i+16], ctr.to_bytes(16, 'big')))
            ctr += 1
        return decrypted

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file path to decipher')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    print('Welcome to Decryptor')
    print('Start decrypting')
    cipherfile = open(args.file, 'rb').read()
    plainfile = Decryptor().decrypt(cipherfile)

    ## Ecriture dans le fichier
    f = open("confidentiel.xlsx", 'wb')
    f.write(plainfile)
    f.close()
    print('Decrypt ok')