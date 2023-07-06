[↰ back](../../..)
# Lecture 2: Cryptography
## Contents
1. [Introduction](#introduction)
2. [Hash Functions](#hash-functions)
3. [Symmetric Cryptography](#symmetric-cryptography)
4. [Asymmetric Cryptography](#asymmetric-cryptography)
5. [RSA](#rsa)
6. [ECC](#ecc)
7. [Digital Signatures](#digital-signatures)
8. [Merkle Trees](#merkle-trees)
9. [What did we miss?](#what-did-we-miss)
10. [Further Reading - the very short list](#further-reading---the-very-short-list)
11. [Exercises](#exercises)

## Introduction
### What is Cryptography?
Defined as the study of secret writing, cryptography has roots as old as history in message obfuscation. Traditional methods involve applying an algorithm or a key to a message to produce a cipher text. This process is known as encryption. The message recipient then applies secret knowledge to the ciphertext, decrypting it, to recover the original message. Curious eyes and self-serving couriers may intercept the cipher text before its destination and try to crack the code. This is the risk those take for secure communication. Cryptanalysis is the science of breaking codes to reveal messages without having knowledge of the key.

A basic encryption scheme is one used by school children where letters are substituted with an alternate according to a prescribed routine. Shifting letters by a set number of characters in the alphabet is known as a *Caesar cipher*. Without knowing how many letters were shifted, it would take an eavesdropper at most 25 attempts to decrypt an English message by brute force.

Other notable ciphers are the *Hill* cipher, *Vigenere* cipher, and *one-time pad* cipher (Singh, 1999). Hill and Vigenere both have weaknesses and can be broken; a well-constructed one-time-pad cipher can never be broken. The one-time works by transposing a message using a random key the same length as the message. This prevents repetition in both within key and from common phrases of speech, such as '*the*', or context such as '*Russians*'. If the key is sufficiently random, only someone with knowledge of the key can decrypt the message. Each new message requires a new key, and thus the name one-time pad. This poses many practical problems such as production and finding good sources of entropy (randomness). The primary limiting factor for this type of encryption is distribution of the keys to both parties. Long message require longer keys, and many messages require many keys.

## Diffie-Hellman (& Merkle) key exchange
The *Diffie-Hellman (& Merkle) key exchange* algorithm was devised so that two parties could use insecure communication channels to determine a common secret key (Diffie, 1976).

This algorithm starts with two public values that are pre-computed, a large prime number $p$ and an integer value $a$ with $1 < a < p $  for which:
$a, \quad a^2\mbox{ mod }p,\quad a^3\mbox{ mod }p,\quad \dots,\quad a^{p-1}\mbox{ mod }p$ are all distinct (yield a permutation of ${1,2,3,\dots, p-1}$)[^1]. If this is the case $a$ is called a *primitive root* of $p$.

Once a primitive root $a$ of a prime $p$ has been found, for any integer $b$ there is a unique power $i<p$ for which 
$b\mbox{ mod }p=a^i\mbox{ mod }p$
and $i$ is called the *discrete logarithm* or *index* of $b$ modulo $p$ for the base $a$.

**For example:** taking $p=7$ and $a=2$, determine $a^k\mod p$ for $k=\{1,2,\quad\dots\quad, p-1\}$.
[^1]: $\mbox{mod}$ is the modulo arithmetic operator.

| $2^1$ | $=2\mod7$ | $=2$ | |
|-------|----------------------|------|---|
| $2^2$ | $=4\mod7$ | $=4$ | |
| $2^3$ | $=8\mod7$ | $=1$ | |
| $2^4$ | $=16\mod7$ | $=\textbf{2}$ | |
| $2^5$ | $=32\mod7$ | $=\textbf{4}$ | repeated roots means 2 is not a primitive root of 7 |
| $2^6$ | $=64\mod7$ | $=\textbf{1}$ | |

Now for $a=3$:

| $3^1$ | $=3\mod7$ | $=3$ | |
|-------|-----------------------|------|---|
| $3^2$ | $=9\mod7$ | $=2$ | |
| $3^3$ | $=27\mod7$ | $=6$ | distinct roots up to $p-1$ means 3 is a primitive root of 7 |
| $3^4$ | $=81\mod7$ | $=4$ | |
| $3^5$ | $=243\mod7$ | $=5$ | |
| $3^6$ | $=729\mod7$ | $=1$ | |

Thus to find the discrete logarithm of an integer such as $b=1762$ we are looking for the $i$ value in the relation 
$1762\text{ mod } 7=3^i$
$1762\text{ mod } 7=5$
and from row 5 above, $3^5\text{ mod } 7=5$, and so $i=5$.

The security of the Diffie-Hellman key exchange relies on the difficulty of reversing this computation above. Given $b=a^i\mbox{ mod }p$, there is no pattern for relating $b$ to $i$. Stated another way: for any integer, $b$, there is a unique $i$ where $i$ is called the discrete logarithm and is computationally difficult to find.

So how do two people use this to exchange information publicly such that they each end up with a shared secret key that others can not deduce?

Alice and Jeff are going to agree on a large prime, $p$, and a base $a$. These values can be published. Each then selects their own secret number $x<p$. This will act as a private key. Both then calculate $y=a^x\mbox{ mod }p$ which is a quick calculation. After exchanging $y$ values, each can then calculate the same secret key, $k=y^x\mbox{ mod }p$. No secret information has been swapped, and both parties now have a common value, $k$, as a secret key.

Note that both Alice ($A$) and Jeff ($J$) calculate the same key ($k$):

```math
k_\text{Jeff}=
```

```math
k_\text{Jeff}=\left(y_{A}\right)^{x_J}\mbox{ mod }p

=\left(a^{x_A}\mbox{ mod }p\right)^{x_J} \mbox{ mod }p
=a^{x_A x_J}\mbox{ mod }p 
=\left(a^{x_J}\right)^{x_A}\mbox{ mod }p
=\left({y_J}\right)^{x_A}\mbox{ mod }p
\therefore k_\text{Jeff}=k_\text{Alice}
```

and a cryptanalyst cannot calculate $k$ without knowing either $x_A$ or $x_J$. Obtaining these values would require calculating the discrete logarithm of an intercepted $y_A$ or $y_J$. For large enough $p$, this is infeasible. In practice, $p$ should be at least 160 bits, and for contemporary standards 1024 is more comfortable[^2] (Hoffman, 2005).

[^2]: 160 bits is $\approx 49$ digit decimal number, and 1024 bits is $\approx 309$ digit decimal number.

One drawback of this system is that to communicate there has to be some back-and-forth between participants to agree on a secret key which can be particularly cumbersome if one participant is offline. If a third person wants to communicate, then a another pair of exchanges must take place. Every pair that needs to communicate needs their own secret key. A group of 40 students in this class requires 780 keys. What if instead each person had their own key and everyone else could use that same key to communicate with them?

## Hash Functions
A hash function takes a variable length input and produces a fixed length output with no discernible pattern. In this sense, the hash function is *one-way* which means that there is no decryption algorithm that can undo it[^2].

```plaintext
    +------------+         +-------------+
    |   message  |   --->  | hash function| ---> message digest
    |     (x)    |         |     H(x)     |
    +------------+         +-------------+
```
A good hash is easy to calculate (verify) but difficult to reverse. Given a hash, it should be computationally infeasible to both produce the data that created the hash or to find a message that produces the same hash. The figure below shows a simple hash function that takes characters as inputs and outputs 1 if the character is in the first half of the alphabet (a-m) and 0 otherwise.
```plaintext
    +------------+         +-----------------+
    |   `code`   |   --->  |   H(`code`)     | ---> `1011`
    +------------+         +-----------------+
```
If you begin with the hashed value of 1011, it is merely guesswork to try to determine the original string because 13 possible values could all produce a 1. After hashing more words, you realize that many other possibilities also produce 1011 as their hashed value, such as joke. If two or more different strings produce the same hash, this is called a collision. Finding a hash function that doesn't output collisions is trickier than it first appears because you can't test the entire solution space. For a blockchain to be secure, it should be built using a collision-resistant hash function.

### SHA-256
SHA-256 is a secure hashing algorithm that outputs a 256-bit message digest. It is part of a family of hash functions designed and tested by the National Institute of Standards and Technology[^3]. One of the key components is the bitwise XOR (exclusive-or) operation which outputs 0 if the two inputs are the same and 1 otherwise. The algorithm and notes can be found in [May2012]. SHA-256 has been used to hash the messages jeff and Jeff.
```plaintext
    +------------+         +---------------+
    |   `jeff`   |   --->  |   SHA-256     | ---> `2e0b8d61fa2a6959d254b6ff5d0fb512249329097336a35568089933b49abdde`
    +------------+         +---------------+

    +------------+         +---------------+
    |   `Jeff`   |   --->  |   SHA-256     | ---> `aea5a5ee6792fab36f3c60e62ef64e40061a8dac7d868b359aff7a4786a32e51`
    +------------+         +---------------+
```
If an adversary wishes to modify data in a block, such as financial transaction data, the resulting hash pointer will have changed and need to be updated. So rather than having to store the entire dataset for verification, we can store the hash pointers and easily see if they are correct. Our adversary that altered some data would have to change every subsequent hash pointer to the tip of the blockchain. Simply storing the most recent hash in a place that can't be modified is enough to verify the whole chain. This can be done by keeping multiple copies in different locations.

## Symmetric Cryptography

## Asymmetric Cryptography

## RSA

## ECC

## Digital Signatures

## Merkle Trees
The pages inside the books (data) can also be represented using hash pointers through a *Merkle tree*, named after computer scientist and cryptographer Ralph Merkle. The leaves of the binary tree structure[^1] are the data, and a hash pointer is created for every pair of leaves. When there are two pairs of leaves, the two hash pointers are combined and hashed into a third hash pointer. This continues until the root of the tree is a single hash representing all the data.

![An individual block contains a Merkle tree of all the transactions in the block. Note it also contains the transactions (pages) themselves. The Merkle root is quick to verify that none of the transactions have changed.][merkle]
![merkle](https://github.com/millecodex/COMP842/assets/39792005/3a827ffb-f4fc-4931-810c-af6898a7230e)

Following the tree in Figure [merkle], Page 1 is hashed as H(1), page 2 is hashed as H(2), and the two hashes are concatenated and hashed again as H(H₁+H₂). The hashing recurses until a single Merkle root is reached. The Merkle tree is secure in the same way as the blockchain -- if an adversary tries to modify some data, then the root hash pointer will change. Note that a block contains *two* separate hashes: one of the previous block and one of the transactions. See Chapter 9 in [Antonopoulos2017] for Bitcoin's block structure and an overview of Merkle trees. A Bitcoin block is output in Figure [bitcoin-block] showing the various metadata that is tracked.

A Merkle path from leaf to root takes $\log n$ time to traverse. If you need to verify a transaction in a block it must be found in a tree and any transaction path in a binary tree of $n$ nodes requires $\log n$ operations. Lightweight nodes do not need to store the entire data in the blockchain, they just keep the Merkle root and then can connect to a full node to verify the path. Simplified payment verification (SPV) clients work this way, for example in a mobile application, where it's impractical to store the entire chain. The trade off here is that the SPV node does not store a full copy of the blockchain and must trust the nodes it is verifying against.


[^1]: [Johnson2014] contains a good overview of tree structures.

[merkle]: (image link)
[bitcoin-block]: (image link)


## What did we miss?
[Text related to 'What did we miss?' here]

# Exercises
1. a
2. b
3. c

# Further Reading - the very short list
* The 
* On the

# Next Lecture
* :point_right: [Proof-of-Work Consensus](3-consensus-pow.md)

