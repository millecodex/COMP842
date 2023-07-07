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

## Symmetric Cryptography
### Diffie-Hellman (& Merkle) key exchange
The *Diffie-Hellman (& Merkle) key exchange* algorithm was devised so that two parties could use insecure communication channels to determine a common secret key (Diffie, 1976).

This algorithm starts with two public values that are pre-computed, a large prime number $p$ and an integer value $a$ with $1 < a < p $  for which:
$a, \quad a^2\mbox{ mod }p,\quad a^3\mbox{ mod }p,\quad \dots,\quad a^{p-1}\mbox{ mod }p$ are all distinct (yield a permutation of ${1,2,3,\dots, p-1}$)[^1]. If this is the case $a$ is called a *primitive root* of $p$.

Once a primitive root $a$ of a prime $p$ has been found, for any integer $b$ there is a unique power $i < p$ for which 
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

Alice and Jeff are going to agree on a large prime, $p$, and a base $a$. These values can be published. Each then selects their own secret number $x < p$. This will act as a private key. Both then calculate $y=a^x\mbox{ mod }p$ which is a quick calculation. After exchanging $y$ values, each can then calculate the same secret key, $k=y^x\mbox{ mod }p$. No secret information has been swapped, and both parties now have a common value, $k$, as a secret key.

Note that both Alice ($A$) and Jeff ($J$) calculate the same key ($k$):

$$
\begin{align}
k_\text{Jeff}  &=\left(y_{A}\right)^{x_J}\text{ mod }p \\
  &=\left(a^{x_A}\text{ mod }p\right)^{x_J} \text{ mod }p \\
  &=a^{x_A x_J}\text{ mod }p  \\
&=\left(a^{x_J}\right)^{x_A}\text{ mod }p \\
&=\left({y_J}\right)^{x_A}\text{ mod }p \\
\therefore k_\text{Jeff}&=k_\text{Alice}
\end{align}
$$



and a cryptanalyst cannot calculate $k$ without knowing either $x_A$ or $x_J$. Obtaining these values would require calculating the discrete logarithm of an intercepted $y_A$ or $y_J$. For large enough $p$, this is infeasible. In practice, $p$ should be at least 160 bits, and for contemporary standards 1024 is more comfortable[^2] (Hoffman, 2005).

[^2]: 160 bits is $\approx 49$ digit decimal number, and 1024 bits is $\approx 309$ digit decimal number.

One drawback of this system is that to communicate there has to be some back-and-forth between participants to agree on a secret key which can be particularly cumbersome if one participant is offline. If a third person wants to communicate, then a another pair of exchanges must take place. Every pair that needs to communicate needs their own secret key. A group of 40 students in this class requires 780 keys. What if instead each person had their own key and everyone else could use that same key to communicate with them?


## Asymmetric Cryptography
### Public-Key Cryptography
The search for a personal key involves finding a one-way function that some insider information can quickly reverse. This is the foundation of public-key cryptography. A user has a key that they can share and use to encrypt messages, called the public-key. They also have a *trapdoor* into that one-way function to decrypt messages, called the private-key. Sometimes the term *backdoor* is used to indicate insider access unknown to users. This is different from a trapdoor as it introduces a deliberate weakness into the cryptosystem, whereas a trapdoor is simply information that is easy to compute one-way.

### RSA
In 1977, Ron Rivest came up with a scheme to deliver exactly this: a key-pair system that allows universal encryption with some additional information to allow the owner (and only that owner) to decrypt messages. Rivest and his colleagues Adi Shamir and Leonard Adleman's system is simply referred to eponymously as RSA encryption[^3] (Rivest, 1978). The details will be skipped here, but in brief, RSA uses the properties of large prime numbers to generate encryption keys that are hard to reverse engineer. It is easy to multiply two prime numbers and calculate the output (semi-prime), but given a large semi-prime it is much more difficult to determine the two factors. 

[^3]: Rivest, R., Shamir, A., & Adleman, L. (1978). A method for obtaining digital signatures and public-key cryptosystems. Communications of the ACM, 21(2), 120-126.

### ECC
### Elliptic Curve Cryptography
Due to progress in calculating prime factorizations RSA public keys need to be at least 1024 bits to provide adequate security. *Elliptic Curve Cryptography* (ECC) is a promising alternative to RSA for public-key encryption, allowing a much shorter key to be used with far less computational overhead, yet providing the same level of security as RSA against a cryptanalysis attack.

For instance, in order to provide roughly the same level of security as a 128-bit AES[^4] key, RSA requires a 3072-bit key, which places a computational burden on any devices using RSA. Worse still, to be equivalent to a 256-bit AES key, RSA requires a 15360-bit key, which is infeasible on devices with limited power and computation such as mobile phones. ECC however requires just double the number of bits than an AES key, making it particularly attractive for public-key encryption on limited devices. It has begun to challenge RSA and Diffie-Hellman key exchange as the preferred public-key cryptographic algorithm, since the difficulty of cryptanalysis against ECC gets harder for longer keys much faster than for either RSA or Diffie-Hellman[^5] (Stallings, 2017).

[^4]: AES is Advanced Encryption Standard, published by the NIST in 2001.
[^5]: Stallings, W. (2017). Cryptography and Network Security: Principles and Practice. Pearson.

| AES | RSA   | ECC  |
|-----|-------|------|
| --- | 512   | 112  |
| --- | 1024  | 160  |
| --- | 2048  | 224  |
| 128 | 3072  | 256  |
| 192 | 7680  | 384  |
| 256 | 15360 | 512  |

### Elliptic Curves
An *elliptic curve* over a field consists of the set of points $(x,y)$ where $x$ and $y$ are elements of the field that satisfy an equation of the form:

$$y^2 + a_1xy+a_3y = x^3+a_2x^2+a_4x+a_6\,.$$

If $a_1=a_2=a_3=0$, this general form can be simplified to:

$$y^2 = x^3+ax+b.$$

Further, if $a=0$ and $b=7$, we get $y^2=(x^3+7)$ taken over a field of primes $\mathbb{Z}_p$ as seen in[^6] (Antonopoulos, 2017). This can be plotted as a series of points similar to Figure 1. Compare to Figure 2 on Page 2 which is plotted over the real numbers. 

> ![Plot of a field of primes up to 17 (Antonopoulos, 2017). ECC operates on integers and when plotted appear as distinct points.](fieldOfPrimes.png)
> Figure: Plot of a field of primes up to 17 (Antonopoulos, 2017). ECC operates on integers and when plotted appear as distinct points.*

> ![Plot of $y^2=(x^3+7)$ over real numbers for visualization only; the same theory applies.](fieldOfReals.png)
> Figure: Plot of $y^2=(x^3+7)$ over real numbers for visualization only; the same theory applies.*

ECC can be utilized for key exchange by making public the chosen field ($p$ or $2^m$), the curve ($a$ and $b$ values in the field), and a generator point $G$ for which there are many multiples $G, 2G, 3G, \dots, nG$ that are all distinct. These distinct multiples are related to the discrete logarithm problem describe above. In this manner the security of an elliptic curve cryptosystem relies on the difficulty in finding the discrete logarithm. This is the method that Bitcoin uses for generating public-private key-pairs; the public part which are used as addresses. Selection of the curve (equation 1) is very important as there may be case-by-case weaknesses. [^7] (Brown, 2010) outlines the standards for curve `secp256k1` that is used by Bitcoin.

[^6]: Antonopoulos, A. M. (2017). Mastering Bitcoin: Unlocking digital cryptocurrencies. O'Reilly Media, Inc.
[^7]: Brown, D. R. L. (2010). SEC 2: Recommended elliptic curve domain parameters. Standards for Efficient Cryptography (SEC) (Certicom Research).


## Digital Signatures
A digital signature arises as a consequence of public-key cryptosystems such as RSA & ECC. It allows a user to do three things:
1. Verify the authenticity of the sender of a message; e.g. if Jacinda Ardern posts a message it is helpful to trust the source,
2. Prevent a sender from denying they sent the message; this is called non-repudiation and prevents someone from saying they were not responsible, and
3. Validate the integrity of the message to ensure it wasn't tampered with during transport; e.g. if a general sends a scout to deliver a message the recipient can be sure the scout did not change the content.

Any standard public-key encryption algorithm such as RSA or ECC combined with a cryptographic hash function such as SHA-1[^8] can be used to create a digital signature, so long as recipients are aware of which encryption algorithm and hash function have been chosen and the correct public key is available to the recipients. Bitcoin and Ethereum both use the elliptic curve digital signature algorithm (ECDSA). 

If a sender encrypts a message with their *private* key, anyone with the public key can decrypt the message. Since the public key is available, anyone has the ability to quickly verify that a message or transaction came from the holder of the private key. This is all done without exposing the private keys and so is as secure as having someone encrypt a message with your public key.

[^8]: SHA-1 is a cryptographic hash function which takes an input and produces a 160-bit (20-byte) hash value known as a message digest – typically rendered as a hexadecimal number, 40 digits long. It was designed by the United States National Security Agency and published by the NIST.






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







## Merkle Trees
The pages inside the books (data) can also be represented using hash pointers through a *Merkle tree*, named after computer scientist and cryptographer Ralph Merkle. The leaves of the binary tree structure[^leaves] are the data, and a hash pointer is created for every pair of leaves. When there are two pairs of leaves, the two hash pointers are combined and hashed into a third hash pointer. This continues until the root of the tree is a single hash representing all the data.

![An individual block contains a Merkle tree of all the transactions in the block. Note it also contains the transactions (pages) themselves. The Merkle root is quick to verify that none of the transactions have changed.][merkle]
![merkle](https://github.com/millecodex/COMP842/assets/39792005/3a827ffb-f4fc-4931-810c-af6898a7230e)

Following the tree in Figure [merkle], Page 1 is hashed as H(1), page 2 is hashed as H(2), and the two hashes are concatenated and hashed again as H(H₁+H₂). The hashing recurses until a single Merkle root is reached. The Merkle tree is secure in the same way as the blockchain -- if an adversary tries to modify some data, then the root hash pointer will change. Note that a block contains *two* separate hashes: one of the previous block and one of the transactions. See Chapter 9 in [Antonopoulos2017] for Bitcoin's block structure and an overview of Merkle trees. A Bitcoin block is output in Figure [bitcoin-block] showing the various metadata that is tracked.

A Merkle path from leaf to root takes $\log n$ time to traverse. If you need to verify a transaction in a block it must be found in a tree and any transaction path in a binary tree of $n$ nodes requires $\log n$ operations. Lightweight nodes do not need to store the entire data in the blockchain, they just keep the Merkle root and then can connect to a full node to verify the path. Simplified payment verification (SPV) clients work this way, for example in a mobile application, where it's impractical to store the entire chain. The trade off here is that the SPV node does not store a full copy of the blockchain and must trust the nodes it is verifying against.


[^leaves]: [Johnson2014] contains a good overview of tree structures.



## Summary
Today encryption is ubiquitous in digital communication. An inspection of the certificate of a secure website will often reveal one of two cryptosystems at work: RSA, or ECC. WhatsApp uses ECDH for key exchange and AES256 symmetric encryption for message sessions[^9]. Telegram uses 2048 bit RSA encryption and Diffie-Hellman key exchange with a symmetric protocol based on AES256[^10]. WeChat does not use end-to-end encryption and has been criticised for its lack of privacy features.

Contrary to popular belief there is no standardized encryption in the Bitcoin protocol. As a decentralized system of exchange, there is no need for encryption. All the transactions are stored in the blockchain, open and accessible to everyone. Access to the private keys controlling addresses is maintained solely through personal security of the user. 

So can someone steal my coins? Not by hacking. Elliptical curve cryptography keeps keys safe from cryptanalysis via the difficulty in solving the discrete logarithm problem. The standard curve `secp256k1` was chosen by the designer of the Bitcoin protocol. This is a choice unique to Bitcoin, as the more common `secp256r1` is used in Transport Layer Security (TLS) for web browsing, email, etc. ECC was chosen because it provides the same level of relative security with smaller keys compared to RSA.

As in any cryptosystem, it is imperative that users keep their private keys secret. There are some added enhancements for encrypting passwords and wallets but these are third party additions and not built in to the protocol. This will be discussed further in a future lecture.

Digital signatures allow a blockchain user to transfer ownership of a token by verifying they have the authority to do so. Tokens are mapped to addresses and to transfer a token the owner must sign a transaction to the recipient's address. Additionally this allows the recipient to verify the message has not been altered at any time. Every transaction on a blockchain is digitally signed by the parties involved; this means they have used their private key to attest to the transaction. 



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

