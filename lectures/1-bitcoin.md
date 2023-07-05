[↰ back](../../)

# What is Bitcoin?
### Contents
1. [A Brief History of Digital Cash](bitcoin.md#a-brief-history)
1. [Peer-to-Peer Networks & Consensus Mechanisms](bitcoin.md#peer-to-peer-networks--consensus-mechanisms)
1. [Proof-of-Work Mining & Network Security](bitcoin.md#proof-of-work-mining--network-security)
1. [Economic Incentives & Monetary Supply](bitcoin.md#economic-incentives--monetary-supply)
1. [Bitcoin Today](bitcoin.md#bitcoin-today)
1. [What did we miss?](bitcoin.md#what-did-we-miss)
1. [Further Reading - the very short list](bitcoin.md#further-reading---the-very-short-list)

# A brief history
What was the problem that Satoshi Nakamoto was looking to solve?
## Digital Cash (without the bank)
The 80's & 90's saw many attempts to create a digital version of money that could have a token, both private and untraceable, treated as a bearer instrument and not subject to the fragilities of third party issuers and verifiers. To name a few there was David Chaum's work on *Untraceable Electronic Cash*, Wei Dai's [*b-money*](http://www.weidai.com/bmoney.txt), and Nick Szabo's [*Bit Gold*](https://unenumerated.blogspot.com/2005/12/bit-gold.html).

Many technical challenges along the road were overcome by advances in cryptography such as digital signatures and hash functions. However, one problem always stood out: how to prevent someone from using a digital coin at one shop, copying it, and spending it again? Known as the *double-spend problem*, this is easily sovled using a centralized authority to check someone's balance and update it accordingly; by the time you arrive at the second retailer your card will be declined for insufficient funds. Here the bank is saying, "You can only spend your dollar once."

The decentralized approach removes the bank entirely from the transaction and is one of the revolutionary ideas put forward by Satoshi in his whitepaper.

# The Whitepaper
<p align="center"><img width="800" alt="header to the bitcoin whitepaper" src="https://user-images.githubusercontent.com/39792005/145146212-c35aff55-97ab-478a-8e10-de2977bc7a7f.PNG"></p>

There are many components to this system that will be introduced. Individually it can be difficult to see the connection between them and how they contribute to a peer-to-peer monetary system. This is intended to be an overview and if you are just learning about Bitcoin don't be disuaded if the pieces seem disjointed or don't fall into place quickly. *(Learning is hard!)*

## Peer-to-Peer Networks & Consensus Mechanisms
The key to the double-spend is to distribute the record of transactions to every participant in the network. In this manner every seller can verify independently that any buyer has the required unspent amount. Every new transaction is shared through the network with everyone else in a peer-to-peer (p2p) manner, rather than sending to a central server and having a gatekeeper update the accounts, this is handled at the individual level. The distributed ledger removes both the need for centralized accounting, and for trust between users. There is no reason for Alice to trust Bob because the network consensus says that Bob has the authority to spend his coins.

Practically speaking, each peer in the network listens for new blocks of transactions, verifies them, and adds them to their own local database. Should two nodes have conflicting information because they received new blocks at slightly different times, or with different transactions in them, then the state is said to fork, and for a short time *both* forks are valid. Resolving forks happens often, is expected, and is the job of the consensus mechanism. The way that Bitcoin does this is by a longest chain rule, meaning that whatever node has the longest chain of blocks is the most likely to receive a new block and therefore continue to be the canonical chain. If a node falls behind, then it abandons its chain and starts contributing to the longest. This method of distributed system consensus is now known as *Nakamoto* conseneus.
 
Because the chain is public you can do an inventory of nodes online at any given time. This also removes gatekeepers as anyone is free to join or leave whenever they want. At the end of 2021 the number of [bitcoin nodes](https://bitnodes.io/) globally was just under 15,000. (Compare this with centralized systems like Facebook that keep your data on anywhere from 3-5 nodes.)

## Proof-of-Work Mining & Network Security
The next major advance demonstrated in Bitcoin was using computational power through proof-of-work to act as a secure time-stamping service. This accomplished two things: first it keeps the network secure because it is very hard to alter the ledger (needs heaps of power) and secondly incentivses actors to behave honestly, or, in their economic best interest.

A hash is a cryptographic function that scrambles input data and outputs a fixed-length string that appears random. Any data of any size can be fed into a hash, such as a transaction, an image, or an entire block, and the result is a string of letters and numbers that can only be recreated using the original data. This makes hashing one-way, it cannot be reverse engineered, and if you have the original data the hash can be verified very quickly.

Bitcoin uses secure hash algorithm of length 256 bits (SHA256) to store pointers to the data in the blockchain. This has the advantage of being easy and fast to verify data, yet difficult (mathematically near impossible) to forge. The hashes in each new block include references to the previous block so if someone wanted to change or delete old data then hash pointers would all have to updated. 

In the table below the input data is changed just one character at a time, first by a lowercase B and then by removing the space. There is no discernable pattern in the output hashes which makes for a good hash function.
|Input data | SHA256 hash |
|:--|:--|
|`Blockchain NZ`|`5119f6c906773da2b05e423bfea20064c62cca75b3880bcff103b02025d510cd`|
|`blockchain NZ`|`3b0e845018217780828c6bdb0832789feb4504d5bea0534b28a58d69ed148f21`|
|`blockchainNZ`|`3f6008d2835912da5efecd62959f03fa98ffb25b14068a611a84756118a7ee22`|

Its a good place to pause and ask: why would someone agree to using their computer hardware for all this hashing and maintaining the ledger? What if the protocol had some form of built-in token to reward people for donating their finite computing power & electricity? 🤔

Proof-of-work (PoW) uses the same SHA256 algorithm to incentivise participants in the network by rewarding lucky ones with coins. Here is where the killer-app comes in. Bitcoin is a system to maintain a distributed ledger *and* the ledger's purpose is to keep track of its own coins! Every block includes some coins that are up for grabs to the miner that finds a lucky hash value. There is no way to game the system because the hashes are not reversible which means everyone is guessing[^hashing] and hoping their hash is a winner. 
[^hashing]: One misconception this author notes is the hashes are sometimes referred to as *complex math problems* or hash *puzzles*, both of which are incorrect. SHA256 is just a recipe to scramble bits of data and using the terms *math* and *puzzle* imply that there can be some optization or "correct" solution.

So, PoW is called mining because of the non-redeemable effort that goes into finding new new coins. Every ten minumtes on average a new block is  mined and with it the miner can redeem the block reward → freshly minted bitcoins.

## Economic Incentives & Monetary Supply
The economics of creating a new currency are tricky. There are many problems to consider such as: how is the money distributed? How much is there? How will the supply change over time? Bitcoin deviates from the textbook answers to these questions by setting a fixed upper limit on the number of bitcoin that will ever be produced in addition to a mathematical supply schedule. (Distribution is handled by mining.)

The fixed upper limit is set at 21 million bitcoin and is an aribtrary constant; as long as the money is divisible the unit amount does not matter. Bitcoin is divisible into 8 decimal places, so the smallest unit, a *satoshi*, is `0.000 000 01` BTC. Divisibility is a benefit of digital money as settlement of small amounts can be handled if fees are cheap enough.

Bitcoin's supply schedule is unique because its known in advance how many new coins are going to be produced and available to the market. Every four years there is a halving event where the new BTC rewarded each block are cut in half. Bitcoin is currently in its fouth epoch awarding 6.25 BTC every 10 minutes. This is a decreasing geometric series and thus the final amount of bitcoin won't be mined until the year 2140 (not a typo!).

<p align="center"><img width="800" alt="bitcoin_supply" src="https://user-images.githubusercontent.com/39792005/147862906-6537e8d0-aa4d-403d-825b-aefd1e31585a.png"></p>

The [CoinGecko chart](https://www.coingecko.com/en/explain/bitcoin_halving) shows bitcoin's total supply approaching 21 million (green) and the blockreward being cut in half every four years (red). After the final fraction of a bitcoin is mined the network will be incentivised entirely from transaction fees being awarded to the miners. 

# Bitcoin Today
Satoshi sent his whitepaper out to a [mailing list](https://satoshi.nakamotoinstitute.org/emails/cryptography/1/#selection-117.66-117.78) of like-minded cryptography cypherpunks on October 31, 2008. A few months later in January 2009 he started running the software and mined the genesis block. Since this time the Bitcoin network has been the most robust computing network humans have ever created. There has been almost no downtime, few bugs, no hacks, and exponential growth. 

With a total value of around $1 trillion USD, It is the 14th largest [currency](https://coinmarketcap.com/fiat-currencies/) next to the Russian Ruble and Swiss Franc. It is estimated that 1-2% of the global population have used or interacted with bitcoin, and [16% of Americans](https://www.pewresearch.org/fact-tank/2021/11/11/16-of-americans-say-they-have-ever-invested-in-traded-or-used-cryptocurrency/) have used or invested in cryptocurrency. There are reachable nodes running the core software in 87 countries. In El Salvador bitcoin is legal tender. 

What began as an experiment has bootstrapped an entire financial system with global settlement time in minutes and fees that are orders of magnitude cheaper and more secure than traditional banking infrastructure.

# What did we miss?
There are many topics not discussed here (trying to keep this as an overview) and so I encourage you, dear reader, to dig deeper into the following: 
* 

# Exercises
1. a
2. b
3. c

# Further Reading - the very short list
* The Whitepaper: [*Bitcoin: A Peer-to-Peer Electronic Cash System* ](https://bitcoin.org/bitcoin.pdf)
* On the Shoulder of Giants - History of the tech: [*Bitcoin's Academic Pedigree*, Communications of the ACM](https://cacm.acm.org/magazines/2017/12/223058-bitcoins-academic-pedigree/fulltext)

# Next Lecture
* :point_right: [Secret Writing (Cryptography)](2-cryptography.md)
