[↰ back](../../..)
# Lecture 2: Cryptography
## Contents
1. [Introduction](#introduction)
2. [Hash Functions](#hash-functions)
3. [Merkle Trees](#merkle-trees)
4. [Symmetric Encryption](#symmetric-encryption)
5. [Asymmetric Encryption](#asymmetric-encryption)
6. [Digital Signatures](#digital-signatures)
7. [Summary](#summary)
8. [What did we miss?](#what-did-we-miss)
9. [Readings](#readings)
10. [Exercises](#exercises)

## Introduction
Defined as the study of secret writing, cryptography has roots as old as history in message obfuscation. Traditional methods involve applying an algorithm or a key to a message to produce a cipher text. This process is known as encryption. The message recipient then applies secret knowledge to the ciphertext, decrypting it, to recover the original message. Curious eyes and self-serving couriers may intercept the cipher text before its destination and try to crack the code. This is the risk those take for secure communication. Cryptanalysis is the science of breaking codes to reveal messages without having knowledge of the key.

A basic encryption scheme is one used by school children where letters are substituted with an alternate according to a prescribed routine. Shifting letters by a set number of characters in the alphabet is known as a *Caesar cipher*. Without knowing how many letters were shifted, it would take an eavesdropper at most 25 attempts to decrypt an English message by brute force.

Other notable ciphers are the *Hill* cipher, [*Vigenere* cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher), and *one-time pad* cipher (Singh, 1999). Hill and Vigenere both have weaknesses and can be broken; a well-constructed one-time-pad cipher can never be broken. The one-time works by transposing a message using a random key the same length as the message. This prevents repetition in both within key and from common phrases of speech, such as '*the*', or context such as '*Russians*'. If the key is sufficiently random, only someone with knowledge of the key can decrypt the message. Each new message requires a new key, and thus the name one-time pad. This poses many practical problems such as production and finding good sources of entropy (randomness). The primary limiting factor for this type of encryption is distribution of the keys to both parties. Long message require longer keys, and many messages require many keys.

## Hash Functions
Cryptographic hash functions are a fundamental tool in the field of cryptography, serving as the basis of numerous information security applications. These deterministic algorithms take an arbitrary (variable) amount of input data and convert it into a fixed-size string of bytes, typically in the form of a *hash digest*. Uniquely, any minor alteration in the input data results in a drastically different output, a property known as the avalanche effect. Moreover, cryptographic hash functions exhibit essential security attributes including pre-image resistance, second pre-image resistance, and collision resistance.

A hash function takes a variable length input and produces a fixed length output with no discernible pattern. In this sense, the hash function is *one-way* which means that there is no decryption algorithm that can undo it. (In fact, there's no encryption here at all, as encryption implies the message can be decrypted.)

```plaintext
    +------------+         +-------------+
    |   message  |   --->  | hash function| ---> message digest
    |     (x)    |         |     H(x)     |
    +------------+         +-------------+
```
A good hash is easy to calculate (verify) but difficult to reverse. Given a hash, it should be computationally infeasible to both produce the data that created the hash (pre-image resistance) or to find a message that produces the same hash (2nd pre-image resistance). The figure below shows a simple hash function that takes characters as inputs and outputs 1 if the character is in the first half of the alphabet (a-m) and 0 otherwise.
```plaintext
    +------------+         +-----------------+
    |   `code`   |   --->  |   H(`code`)     | ---> `1011`
    +------------+         +-----------------+
```
If you begin with the hashed value of 1011, it is merely guesswork to try to determine the original string because 13 possible values could all produce a 1. After hashing more words, you realize that many other possibilities also produce 1011 as their hashed value, such as joke (or lame, lone, male, mine, etc.). If two or more different strings produce the same hash, this is called a collision. Finding a hash function that doesn't output collisions is trickier than it first appears because you can't test the entire solution space. For a blockchain to be secure, it should be built using a collision-resistant hash function.

### SHA-256
SHA-256 is a secure hashing algorithm that outputs a 256-bit message digest. It is part of a family of hash functions designed and tested by the National Institute of Standards and Technology (see required reading). One of the key components is the bitwise XOR (exclusive-or) operation which outputs 0 if the two inputs are the same and 1 otherwise. 
```plaintext
    +------------+         +---------------+
    |   `jeff`   |   --->  |   SHA-256     | ---> `2e0b8d61fa2a6959d254b6ff5d0fb512249329097336a35568089933b49abdde`
    +------------+         +---------------+

    +------------+         +---------------+
    |   `Jeff`   |   --->  |   SHA-256     | ---> `aea5a5ee6792fab36f3c60e62ef64e40061a8dac7d868b359aff7a4786a32e51`
    +------------+         +---------------+
```
> Figure: SHA-256 has been used to hash the messages `jeff` and `Jeff`. There should be no way to link the two hashes.

Recall that the links between blocks are called hash pointers. If an adversary wishes to modify data in a block, such as financial transaction data, the resulting hash pointer will have changed and need to be updated. So rather than having to store the entire dataset for verification, we can store the hash pointers and easily see if they are correct. Our adversary that altered some data would have to change every subsequent hash pointer to the tip of the blockchain. Simply storing the most recent hash in a place that can't be modified is enough to verify the whole chain. A good way to do this is by keeping multiple copies in different locations.

SHA-256 is used in various places in Bitcoin (and blockchains) such as: address generation, block pointers, Merkle trees, and proof-of-work mining. 

### A quick note about Email
The Simple Mail Transfer Protocol (SMTP) was defined by [Jon Postel](https://www.rfc-editor.org/rfc/rfc821) in 1982. As a standard, this would allow anyone to write an email client according to the SMTP guidelines and be able to send messages to anyone else that also followed the protocol. It is still used today and has undergone many updates, however SMTP has two problems: all text is sent as plaintext, and it is easy to spoof from addresses and generate spam.

Email spam is an issue that was considered by Dwork and Naor (1993) when they wrote a paper describing the computational cost incurred by a spammer before sending an email. Titled Pricing via Processing, the idea is that your computer has to solve some computational puzzle before being permitted to send an email. For the average user this would take seconds and not be a nuisance but for a spam emailer, this would slow down their operation. A few years later in 1997, Back (2002) created Hashcash in a similar vein. Although Back was unaware of the previous work by Dwork and Naor, Back also implemented the idea of a cost function that has an easily verifiable solution. This is now known as Proof-of-Work and used by Bitcoin miners.


## Merkle Trees
Recall our ledger consisting of pages (transaction data) that is bundled into entire books (blocks) and linked by a numbering system (hash pointer). The pages inside the books can also be represented using hash pointers through a *Merkle tree*, named after computer scientist and cryptographer [Ralph Merkle](https://en.wikipedia.org/wiki/Ralph_Merkle). The leaves of the binary tree structure are the data, and a hash pointer is created for every pair of leaves. When there are two pairs of leaves, the two hash pointers are combined and hashed into a third hash pointer. This continues until the root of the tree is a single hash representing all the data.

> <img width="300" alt="Merkle Tree" src="https://github.com/millecodex/COMP842/assets/39792005/3a827ffb-f4fc-4931-810c-af6898a7230e">\
> Figure: An individual block contains a Merkle tree of all the transactions in the block. Note it also contains the transactions (pages) themselves. The Merkle root is quick to verify that none of the transactions have changed.

Following the tree in the Figure, Page 1 is hashed as $H(1)$, page 2 is hashed as $H(2)$, and the two hashes are concatenated and hashed again as $H(H₁+H₂)$. The hashing recurses until a single Merkle root is reached. The Merkle tree is secure in the same way as the blockchain -- if an adversary tries to modify some data, then the root hash pointer will change. Note that a block contains *two* separate hashes: one of the previous block and one of the transactions. See Chapter 9 in Antonopoulos (2017) for Bitcoin's block structure and an overview of Merkle trees. A Bitcoin block is output below showing the various metadata that is tracked.

```json
	"hash": "00000000000000000000534d3d2c7758fab39dabb98d23b954813379f053c580",
	"confirmations": 1,
	"strippedsize": 130543,
	"size": 174555,
	"weight": 566184,
	"height": 620229,
	"version": 536928256,
	"versionHex": "2000e000",
	"merkleroot": "cdfc01a6d3a9f037670be9c17dba180e6b281764cb402ead941b2a439c1d801d",
	"tx": [
		  "d55c96ce6ccf995035338f4ded57850f307299b0756b44c61b2fe5e5c2c89a51",
		  "...truncated...",
	 	  "22ba973e71869d1e64cdd8572fa94754429d52d84bce61b2374f082606e02ec5",
	],
	"time": 1583366597,
	"mediantime": 1583365586,
	"nonce": 4225421315,
	"bits": "17122cbc",
	"difficulty": 15486913440292.87,
	"chainwork": "00000000000000000000000000000000000000000d4bf930c8adffc9b1a4b136",
	"nTx": 350,
	"previousblockhash": "000000000000000000070be3e6873e60481b5e3c71322c8ced8315f6e44edd6e"
```
> Figure: block header info in Bitcoin, note the `merkleroot`.

A Merkle path from leaf to root takes $\log n$ time to traverse. If you need to verify a transaction in a block it must be found in a tree and any transaction path in a binary tree of $n$ nodes requires $\log n$ operations. Lightweight nodes do not need to store the entire data in the blockchain, they just keep the Merkle root and then can connect to a full node to verify the path. Simplified payment verification (SPV) clients work this way, for example in a mobile application, where it's impractical to store the entire chain. The trade off here is that the SPV node does not store a full copy of the blockchain and must trust the nodes it is verifying against.

![merkle](merkle.gif)
> Figure: Objects `A` to `P` stored as leaf nodes in a Merkle tree. Tracing a path to verify a letter is present should occur in $\log n$ time. Note: *.gif doesn't play.

## Symmetric Encryption
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


## Asymmetric Encryption
### Public-Key Cryptography
The search for a personal key involves finding a one-way function that some insider information can quickly reverse. This is the foundation of public-key cryptography. A user has a key that they can share and use to encrypt messages, called the public-key. They also have a *trapdoor* into that one-way function to decrypt messages, called the private-key. Sometimes the term *backdoor* is used to indicate insider access unknown to users. This is different from a trapdoor as it introduces a deliberate weakness into the cryptosystem, whereas a trapdoor is simply information that is easy to compute one-way.

### RSA
In 1977, Ron Rivest came up with a scheme to deliver exactly this: a key-pair system that allows universal encryption with some additional information to allow the owner (and only that owner) to decrypt messages. Rivest and his colleagues Adi Shamir and Leonard Adleman's system is simply referred to eponymously as RSA encryption (Rivest, 1978). The details will be skipped here, but in brief, RSA uses the properties of large prime numbers to generate encryption keys that are hard to reverse engineer. It is easy to multiply two prime numbers and calculate the output (semi-prime), but given a large semi-prime it is much more difficult to determine the two factors. 

### Elliptic Curve Cryptography
Due to progress in calculating prime factorizations RSA public keys need to be at least 1024 bits to provide adequate security. *Elliptic Curve Cryptography* (ECC) is a promising alternative to RSA for public-key encryption, allowing a much shorter key to be used with far less computational overhead, yet providing the same level of security as RSA against a cryptanalysis attack.

For instance, in order to provide roughly the same level of security as a 128-bit AES[^4] key, RSA requires a 3072-bit key, which places a computational burden on any devices using RSA. Worse still, to be equivalent to a 256-bit AES key, RSA requires a 15360-bit key, which is infeasible on devices with limited power and computation such as mobile phones. ECC however requires just double the number of bits than an AES key, making it particularly attractive for public-key encryption on limited devices. It has begun to challenge RSA and Diffie-Hellman key exchange as the preferred public-key cryptographic algorithm, since the difficulty of cryptanalysis against ECC gets harder for longer keys much faster than for either RSA or Diffie-Hellman (Stallings, 2017).

[^4]: AES is Advanced Encryption Standard, published by the NIST in 2001.


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

Further, if $a=0$ and $b=7$, we get $y^2=(x^3+7)$ taken over a field of primes $\mathbb{Z}_p$ as seen in Antonopoulos (2017). This can be plotted as a series of points similar to Figure 1. Compare to Figure 2 on Page 2 which is plotted over the real numbers. 

> <img width="346" alt="fieldOfReals" src="https://github.com/millecodex/COMP842/assets/39792005/2bca0a05-c619-4219-9b7c-3b15ada4758e">\
> Figure: Plot of a field of primes up to 17 (Antonopoulos, 2017). ECC operates on integers and when plotted appear as distinct points.*

> <img width="346" alt="fieldOfReals" src="https://github.com/millecodex/COMP842/assets/39792005/341f93cb-e46f-4fcc-9964-45570fde9633">\
> Figure: Plot of $y^2=(x^3+7)$ over real numbers for visualization only; the same theory applies.

ECC can be utilized for key exchange by making public the chosen field ($p$ or $2^m$), the curve ($a$ and $b$ values in the field), and a generator point $G$ for which there are many multiples $G, 2G, 3G, \dots, nG$ that are all distinct. These distinct multiples are related to the discrete logarithm problem describe above. In this manner the security of an elliptic curve cryptosystem relies on the difficulty in finding the discrete logarithm. This is the method that Bitcoin uses for generating public-private key-pairs; the public part which are used as addresses. Selection of the curve (equation 1) is very important as there may be case-by-case weaknesses. Brown (2010) outlines the standards for curve `secp256k1` that is used by Bitcoin.





## Digital Signatures
A digital signature arises as a consequence of public-key cryptosystems such as RSA & ECC. It allows a user to do three things:
1. Verify the authenticity of the sender of a message; e.g. if Jacinda Ardern posts a message it is helpful to trust the source,
2. Prevent a sender from denying they sent the message; this is called non-repudiation and prevents someone from saying they were not responsible, and
3. Validate the integrity of the message to ensure it wasn't tampered with during transport; e.g. if a general sends a scout to deliver a message the recipient can be sure the scout did not change the content.

Any standard public-key encryption algorithm such as RSA or ECC combined with a cryptographic hash function such as SHA-1[^8] can be used to create a digital signature, so long as recipients are aware of which encryption algorithm and hash function have been chosen and the correct public key is available to the recipients. Bitcoin and Ethereum both use the elliptic curve digital signature algorithm (ECDSA). 

If a sender encrypts a message with their *private* key, anyone with the public key can decrypt the message. Since the public key is available, anyone has the ability to quickly verify that a message or transaction came from the holder of the private key. This is all done without exposing the private keys and so is as secure as having someone encrypt a message with your public key.

[^8]: SHA-1 is a cryptographic hash function which takes an input and produces a 160-bit (20-byte) hash value known as a message digest – typically rendered as a hexadecimal number, 40 digits long. It was designed by the United States National Security Agency and published by the NIST.


## Summary
Today encryption is ubiquitous in digital communication. An inspection of the certificate of a secure website will often reveal one of two cryptosystems at work: RSA, or ECC. WhatsApp uses ECDH for key exchange and AES256 symmetric encryption for message sessions[^9]. Telegram uses 2048 bit RSA encryption and Diffie-Hellman key exchange with a symmetric protocol based on AES256[^10]. WeChat does not use end-to-end encryption and has been criticised for its lack of privacy features.

Contrary to popular belief there is no standardized encryption in the Bitcoin protocol. As a decentralized system of exchange, there is no need for encryption. All the transactions are stored in the blockchain, open and accessible to everyone. Access to the private keys controlling addresses is maintained solely through personal security of the user. 

So can someone steal my coins? Not by hacking. Elliptical curve cryptography keeps keys safe from cryptanalysis via the difficulty in solving the discrete logarithm problem. The standard curve `secp256k1` was chosen by the designer of the Bitcoin protocol. This is a choice unique to Bitcoin, as the more common `secp256r1` is used in Transport Layer Security (TLS) for web browsing, email, etc. ECC was chosen because it provides the same level of relative security with smaller keys compared to RSA.

As in any cryptosystem, it is imperative that users keep their private keys secret. There are some added enhancements for encrypting passwords and wallets but these are third party additions and not built in to the protocol. This will be discussed further in a future lecture.

Digital signatures allow a blockchain user to transfer ownership of a token by verifying they have the authority to do so. Tokens are mapped to addresses and to transfer a token the owner must sign a transaction to the recipient's address. Additionally this allows the recipient to verify the message has not been altered at any time. Every transaction on a blockchain is digitally signed by the parties involved; this means they have used their private key to attest to the transaction. 



## What did we miss?
* Zero-knowledge proofs are an applied branch of cryptography. We will return to these (at a high level) in our lecture on Privacy.

# Exercises
1. a
2. b
3. c

# Readings
* New Directions in Cryptography by Whitfield Diffie and Martin Hellman [(pdf)](https://www-ee.stanford.edu/~hellman/publications/24.pdf)
* WhatsApp Encryption Overview - Technical white paper [(pdf)](https://github.com/millecodex/COMP842/blob/master/papers/WhatsApp-Security-White-paper.pdf)
* NIST specification for SHA-1 [(pdf)](https://github.com/millecodex/COMP842/blob/master/papers/NIST.FIPS.180-4.pdf) (download for proper font rendering)

# Next Lecture
* :point_right: [Proof-of-Work Consensus](3-consensus-pow.md)

# References
Antonopoulos, A. 2017. Mastering Bitcoin: Unlocking digital cryptocurrencies. O'Reilly Media, Inc.
Back, A. 2002. *Hashcash: A denial of service counter-measure*. http://www.hashcash.org/
Brown, D. R. L. 2010. SEC 2: Recommended elliptic curve domain parameters. Standards for Efficient Cryptography (SEC) (Certicom Research). https://www.secg.org/sec2-v2.pdf

Diffie, W., Hellman, M. 1976. "New Directions in Cryptography." *IEEE Transactions on Information Theory*. 22 (6): 644–654.
5. Dwork, C., Naor, M. 1993. *Pricing via processing or combatting junk mail*. http://www.wisdom.weizmann.ac.il/~naor/PAPERS/pvp.pdf

Hoffman, P. 2005. "Algorithms for Internet Key Exchange (IKEv2)." RFC 4109. Internet Engineering Task Force. https://tools.ietf.org/html/rfc4109


Postel, J. 1982. "Simple Mail Transfer Protocol." RFC 821. Internet Engineering Task Force. https://www.rfc-editor.org/rfc/rfc821

Rivest, R., Shamir, A., & Adleman, L. 1978. "A Method for Obtaining Digital Signatures and Public-Key Cryptosystems." *Communications of the ACM*. 21(2), 120-126.

Singh, S. 1999. "The Code Book." *Doubleday*.

Stallings, W. 2017. Cryptography and Network Security: Principles and Practice. Pearson.

