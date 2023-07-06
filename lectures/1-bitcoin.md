[↰ back](../../..)

# Lecture 1: Money & Bitcoin
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

# History of the Blockchain
Many areas had to be developed, invented, and refined before the blockchain could come to fruition and encompass the widespread mania it has today. Many of the sections that follow may seem disjunct, or even irrelevant upon first reading, but all have had some influence that led to the development of cryptocurrencies and blockchains.

The two main sources of motivation on the road to bitcoin are Finance and Computing. The finance portion traces right back to early human civilisation and the development of money.

## Early Trading Systems
Early humans could barter with their neighbours using goods or services on offer, but this quickly becomes cumbersome as values often do not align. In small tribes and families this is not a problem because the members trust each other. As societies or tribes get larger, inevitably there is interaction with another tribe whose members you do not trust. To resolve this peacefully elders of one tribe would negotiate with elders of another tribe, essentially keeping accounts of each other’s debt (Graeber, 2011). Thus arise two concepts that allow us to trust a neighbour: units of account and debt (Ferguson, 2008). There is still a problem with our early business environment though, what do you do with a tribe you’ve never encountered before? In the case that the elders have no previous history, how can they be trusted?

## Cash
Cash allows one person to transact with someone whom they don’t know, and therefore can’t trust. Myriad items throughout history have been used as cash such as: gold, cowrie shells, woodpecker scalps, stone discs, and NZ$20 notes (Agha, 2017).

To be considered cash only two things need to hold true:

1. Someone must be willing to accept your token, and
2. The token must last long enough to be transacted again.

To be an eligible NZ$20 note, a few more characteristics must hold true (Graeber, 2011):

- affordable
- available
- durable
- fungible
- portable
- reliable

Any token that has these properties in addition to being issued by the state is called fiat money. Aside from the convenience that comes with a standard cash transacting system is the benefit of it being anonymous. You don’t know the history of your cowrie shell, or who previously used your $20 note.

## Finance
Finance could only evolve once stable systems for credit and debt and value transfer (cash) were widely accepted. In the fifteenth century in Italy, the Medici family were money changers that revolutionised banking. They were meticulous bookkeepers and adopted the new practice called double-entry bookkeeping where account debits were maintained in one column and credits in a separate column. Their success caused this style of banking to be the standard throughout Europe in the fifteenth and sixteenth century and is still standard today (Ferguson, 2008). Recording all account activity in a ledger is a core property of blockchain systems, including bitcoin.

It’s not just the idea of a permanent ledger that bitcoin borrowed, but rather the motivation to create a system outside of the one the Medici’s of 15th century Italy pioneered, and hold to this day. Next we will look at the computing branch.

## Databases
Codd (1970), working at IBM was thinking about how to solve the problem of databases growing in size and still be able to access data efficiently. His paper detailed what is now common practice: relational databases. This allows data to be accessed by linking different chunks of data within tables. Previously a programmer would have to write a program to find what was required in a DB. The benefits allowed reliable storage of data across multiple data centers that could maintain consistency between many users
(MacCormick, 2012).

This means that a bank could have a single database with customer data, and operate in different cities without any inconsistencies in a users’ account. This is a distributed computing model where resources are located in different geographic locations, however for traditional banking this falls under a centralised structure. More on centralisation later.

## Traditional Banking System
The banking system we use today has capitalised on the internet infrastructure and computing ideas such as relational databases using an atomic transaction model, to truly become global. With relevance to blockchain development, this system:

- Uses digital double-entry accounting
- Has a centralised hierarchy and often distributed infrastructure
- Maintains a permanent record of transactions that are opaque to the public.

The bank is the middle-man, or final arbiter, of all transactions. The centralised architecture allows the bank to choose its customers and set fees. Among other monopolistic behaviours, this leads to censorship and in the digital age, hacks and breeches are increasingly common. Also, one may not want the bank to know exactly how and with whom you are transacting. As we learn more about the blockchain it will become apparent that bitcoin transactions are not anonymous, rather they are considered pseudonymous. Although your name is not attached to a transaction, the address and activity associated with it is permanently recorded in the blockchain. Digital privacy will be one of the most important consequences of the blockchain era.

## Cryptography
The 1980s saw a lot of research into the idea of being able to send a private digital message. Historically, this meant creating a cipher that converts a plaintext message into a ciphertext (encrypted message), sending the encrypted version, and the recipient has a matching cipher to enable them to decrypt the message. The key hurdle to this setup is that the cipher has to be transported to the recipient among eavesdroppers. A digital cryptosystem also involves distributing your cipher through any number of third-party servers that could have spies monitoring the connection.

Public key cryptography is the solution to this problem and will be covered more in Lecture 3. Although neither a blockchain nor bitcoin is a crypto-system, they both utilize elements of cryptography: hash functions, and cryptographic keys.

## Digital Cash
Chaum, Fiat and Naor (1988) came up with a scheme for issuing unique digital coins that could be redeemed by a centralised authority in a way that conceals the user’s identity. Anonymous digital cash. His scheme used what are called blind signatures and are clever because it means you can not reuse a digital coin. This is referred to as the double-spending problem because it’s easy to copy a digital object and then turn around and offer it to many people while claiming it’s unique. Chaum et al. commercialized his company, calling it DigiCash but it never caught on (Narayanan, 2016). One of the reasons was that it wasn’t a truly peer-to-peer system.

## Email
The Simple Mail Transfer Protocol (SMTP) was defined in 1982 (Postel, 1982). As a standard, this would allow anyone to write an email client according to the SMTP guidelines and be able to send messages to anyone else that also followed the protocol. It is still used today and has undergone many updates, however SMTP has two problems: all text is sent as plaintext, and it is easy to spoof from addresses and generate spam.

Email spam is an issue that was considered by Dwork and Naor (1993) when they wrote a paper describing the computational cost incurred by a spammer before sending an email. Titled Pricing via Processing, the idea is that your computer has to solve some computational puzzle before being permitted to send an email. For the average user this would take seconds
and not be a nuisance but for a spam emailer, this would slow down their operation. A few years later in 1997, Back (2002) created Hashcash in a similar vein. Although Back was unaware of the previous work by Dwork and Naor, Back also implemented the idea of a cost function that has an easily verifiable solution. This is now known as Proof-of-Work and used by Bitcoin miners (Nakamoto, 2008a).

## Linked Time-stamping
The blockchain itself, as the name suggests, is a chain of blocks that are linked together using cryptographic hash functions. The idea was not unique to cryptocurrencies. Haber and Stornetta (1991) describe a method to use one-way hash functions to digitally time-stamp documents and maintain privacy. This hashing system is used to order the blocks in a blockchain while maintaining block integrity and security over time.

## Cryptocurrencies and the Blockchain
The Global Financial Crisis in the mid-2000’s created significant hardship and the blame was put clearly on the banking sector. While changes were called for in how banks managed risk, there was also social disquiet amongst those that felt that banks controlled too much financial and therefore, societal resource. In particular, libertarians called for an economic system free of the banking sector.

A person named Satoshi Nakamoto (Nakamoto, 2008b) designed a technological solution as a cryptocurrency, Bitcoin. While digital cash systems have a long history, with some successes such as PayPal, most have failed to ignite support. Bitcoin’s success seems in part to derive from its decentralised peer-to-peer system that provides complete transactions without a singular or centralised banking system.

The Bitcoin cryptocurrency architecture combines functions that provide money or coin creation, transactional cryptographic validation, and a highly redundant storage system that is publicly available but relatively anonymous (Brikman, 2014). An important measure that ensures cryptographically sound identification and verification of ownership is the use of SHA public/private key cryptography. This also provides a degree of anonymity, transactional integrity, and non-repudiation (Peteanu, 2014). The blockchain is a read-only public ledger of all transactions that have occurred within the cryptocurrency ecosystem and consists of a series of blocks that are created through proofing methods, such as Proof ofWork (Nakamoto, 2008b), Proof of Stake (Buterin, 2013; Larimer, 2013), plus any other proofs that may be required. To limit the number of transactions, Bitcoin transactions are completed every 10 minutes, each transaction returns a block that is added to the chain. Thus, each block contains the outputs of transactions, and with a cryptographic hash, they are added to a sequence, or chain, of blocks. The hash then provides ameans of referencing individual blocks (Wood, 2015).

In an accounting or economic sense, the chain represents a journaling system, although due to size constraints, the journal does not contain the final state. The transaction series is punctuated with “incentives” for nodes to mine, where “mining is the process of dedicating effort (working) to bolster one series of transactions (a block) over any other potential competitor block” (p.2, (Wood, 2015)). A cryptocurrency ecosystem is comprised of nodes, where a node is defined as any device that is running on or creates transaction or block data to the blockchain network (Community, 2014). Thus, a node may exhibit a variety of behaviours depending on context and function. Each cryptocurrency defines the purpose and functionality of nodes on its network, but, in general, the nodes are used to mine and validate blocks. They may also be used to provide defence mechanisms, such as limitations on the number of transactions processed per minute to prevent denial of service attacks.


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
