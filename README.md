# COMP2860 Semester 1 Week 9 Exercises

## Exercise 1: Vernam Cipher
The Vernam cipher has a structure similar to that of a stream cipher. However, for the Vernam cipher, the
keystream is a random byte sequence which is exactly as long as the plaintext and is only used once.

Open ```exercise1.py``` and complete the ```VernamCipher``` class by implementing the following class methods. De-
scriptions of what each method should do, its parameters and return value are given in the comments.
- ```encrypt```
- ```decrypt```

A unit test script, ```test_exercise1.py```, is supplied to test your implementation.

## Exercise 2: Cipher Block Chaining Mode of Encryption (Portfolio)
Open ```exercise2.py``` and complete the ```SAES_CBC``` class by implementing the following class methods. Descriptions
of what each method should do, its parameters and return value are given in the comments.
- ```encrypt```, which should implement the CBC mode encryption algorithm for the ```SimplifiedAES``` cipher.
- ```decrypt```, which should implement the CBC mode decryption algorithm for the ```SimplifiedAES``` cipher.

A unit test script, ```test_exercise2.py```, is supplied to test your implementation.

## Exercise 3: Alleged RC4
ARC4 (Alleged RC4) is a reverse engineered version of the RC4 stream cipher. ARC4 has two main
algorithms: the **key scheduling algorithm (KSA)** which initialises the keystream generator; and the **pseudorandom
generation algorithm (PRGA)** which outputs keystream bytes.

The pseudocode for the **key scheduling algorithm (KSA)** is given below:
```
for i from 0 to 255
    S[i] := i
endfor
j := 0
for i from 0 to 255
    j := (j + S[i] + key[i mod keylength]) mod 256
    swap values of S[i] and S[j]
endfor
```

The pseudocode for the **pseudorandom generation algorithm (PRGA)** is given below:
```
i := 0
j := 0
while GeneratingOutput:
    i := (i + 1) mod 256
    j := (j + S[i]) mod 256
    swap values of S[i] and S[j]
    t := (S[i] + S[j]) mod 256
    K := S[t]
    output K
endwhile
```

Open ```exercise3.py``` and complete the ```ARC4``` class by implementing the following class methods. Descriptions of
what each method should do, its parameters and return value are given in the comments.
- ```__init__```, the constructor, which implements the key scheduling algorithm
- ```prga```, which implements the pseudorandom generation algorithm
- ```encrypt```
- ```decrypt```

A unit test script, ```test_exercise3.py```, is supplied to test your implementation


