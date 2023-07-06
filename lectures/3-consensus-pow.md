[↰ back](../../..)
# Lecture 3: Consensus Part I: Proof of Work
## Contents
1. [BFT](#bft)
2. [Longest chain](#longest-chain)
3. [Mining/nodes](#miningnodes)
4. [51% attack](#51-attack)
5. [Selfish mining](#selfish-mining)
6. [Difficulty Adjustment](#difficulty-adjustment)
7. [Incentives](#incentives)
8. [What did we miss?](#what-did-we-miss)
9. [Further Reading - the very short list](#further-reading---the-very-short-list)
10. [Exercises](#exercises)

## BFT
### Databases
Codd (1970), working at IBM was thinking about how to solve the problem of databases growing in size and still be able to access data efficiently. His paper detailed what is now common practice: relational databases. This allows data to be accessed by linking different chunks of data within tables. Previously a programmer would have to write a program to find what was required in a DB. The benefits allowed reliable storage of data across multiple data centers that could maintain consistency between many users
(MacCormick, 2012).

This means that a bank could have a single database with customer data, and operate in different cities without any inconsistencies in a users’ account. This is a distributed computing model where resources are located in different geographic locations, however for traditional banking this falls under a centralised structure. More on centralisation later.


## Longest chain
The next major advance demonstrated in Bitcoin was using computational power through proof-of-work to act as a secure time-stamping service. This accomplished two things: first it keeps the network secure because it is very hard to alter the ledger (needs heaps of power) and secondly incentivses actors to behave honestly, or, in their economic best interest.

**review from lecture 2**
A hash is a cryptographic function that scrambles input data and outputs a fixed-length string that appears random. Any data of any size can be fed into a hash, such as a transaction, an image, or an entire block, and the result is a string of letters and numbers that can only be recreated using the original data. This makes hashing one-way, it cannot be reverse engineered, and if you have the original data the hash can be verified very quickly.

Bitcoin uses secure hash algorithm of length 256 bits (SHA256) to store pointers to the data in the blockchain. This has the advantage of being easy and fast to verify data, yet difficult (mathematically near impossible) to forge. The hashes in each new block include references to the previous block so if someone wanted to change or delete old data then hash pointers would all have to updated. 

In the table below the input data is changed just one character at a time, first by a lowercase B and then by removing the space. There is no discernable pattern in the output hashes which makes for a good hash function.
|Input data | SHA256 hash |
|:--|:--|
|`Blockchain NZ`|`5119f6c906773da2b05e423bfea20064c62cca75b3880bcff103b02025d510cd`|
|`blockchain NZ`|`3b0e845018217780828c6bdb0832789feb4504d5bea0534b28a58d69ed148f21`|
|`blockchainNZ`|`3f6008d2835912da5efecd62959f03fa98ffb25b14068a611a84756118a7ee22`|

Its a good place to pause and ask: why would someone agree to using their computer hardware for all this hashing and maintaining the ledger? What if the protocol had some form of built-in token to reward people for donating their finite computing power & electricity? 🤔





## Mining/nodes
So, PoW is called mining because of the non-redeemable effort that goes into finding new new coins. Every ten minumtes on average a new block is  mined and with it the miner can redeem the block reward → freshly minted bitcoins.

## 51% attack

## Selfish mining

## Difficulty Adjustment

## Incentives
Proof-of-work (PoW) uses the same SHA256 algorithm to incentivise participants in the network by rewarding lucky ones with coins. Here is where the killer-app comes in. Bitcoin is a system to maintain a distributed ledger *and* the ledger's purpose is to keep track of its own coins! Every block includes some coins that are up for grabs to the miner that finds a lucky hash value. There is no way to game the system because the hashes are not reversible which means everyone is guessing[^hashing] and hoping their hash is a winner. 
[^hashing]: One misconception this author notes is the hashes are sometimes referred to as *complex math problems* or hash *puzzles*, both of which are incorrect. SHA256 is just a recipe to scramble bits of data and using the terms *math* and *puzzle* imply that there can be some optization or "correct" solution.

#### Economic Incentives & Monetary Supply
The economics of creating a new currency are tricky. There are many problems to consider such as: how is the money distributed? How much is there? How will the supply change over time? Bitcoin deviates from the textbook answers to these questions by setting a fixed upper limit on the number of bitcoin that will ever be produced in addition to a mathematical supply schedule. (Distribution is handled by mining.)

The fixed upper limit is set at 21 million bitcoin and is an aribtrary constant; as long as the money is divisible the unit amount does not matter. Bitcoin is divisible into 8 decimal places, so the smallest unit, a *satoshi*, is `0.000 000 01` BTC. Divisibility is a benefit of digital money as settlement of small amounts can be handled if fees are cheap enough.

Bitcoin's supply schedule is unique because its known in advance how many new coins are going to be produced and available to the market. Every four years there is a halving event where the new BTC rewarded each block are cut in half. Bitcoin is currently in its fouth epoch awarding 6.25 BTC every 10 minutes. This is a decreasing geometric series and thus the final amount of bitcoin won't be mined until the year 2140 (not a typo!).

<p align="center"><img width="800" alt="bitcoin_supply" src="https://user-images.githubusercontent.com/39792005/147862906-6537e8d0-aa4d-403d-825b-aefd1e31585a.png"></p>

The [CoinGecko chart](https://www.coingecko.com/en/explain/bitcoin_halving) shows bitcoin's total supply approaching 21 million (green) and the blockreward being cut in half every four years (red). After the final fraction of a bitcoin is mined the network will be incentivised entirely from transaction fees being awarded to the miners. 

***

Lets now return to the question posed at the beginning: How can a blockchain protect against forged time-stamping? Each block contains a hash of the previous block, and \textit{that} block contains a hash the one before it, continuing back to the genesis block. So the hash of a single block is a digest or representation of the entire chain state up to that time. Any time a hash pointer is changed by a malicious actor all the subsequent blocks will also need to have their hash pointers updated. This process can require enormous amounts of computing power (energy and money) and incentivises nodes to act honestly according to the protocol.

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
* :point_right: [Proof-of-Stake Consensus](4-consensus-pos.md)


