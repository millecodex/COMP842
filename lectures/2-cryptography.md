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

