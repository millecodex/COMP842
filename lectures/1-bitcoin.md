[↰ back](../../..)

# Lecture 1: Money & Bitcoin
## Contents
1. [Money](#money)
2. [P2P digital cash](#p2p-digital-cash)
3. [The Double-Spend Problem](#the-double-spend-problem)
4. [Distributed Systems](#distributed-systems)
5. [Bitcoin](#bitcoin)
6. [Chain of blocks](#chain-of-blocks)
7. [Characteristics and Quirks](#characteristics-and-quirks)
8. [What did we miss?](#what-did-we-miss)
9. [Further Reading - the very short list](#further-reading---the-very-short-list)
10. [Exercises](#exercises)

## Money
#### History of the Blockchain
Many areas had to be developed, invented, and refined before the blockchain could come to fruition and encompass the widespread mania it has today. Many of the sections that follow may seem disjunct, or even irrelevant upon first reading, but all have had some influence that led to the development of cryptocurrencies and blockchains.

The two main sources of motivation on the road to bitcoin are Finance and Computing. The finance portion traces right back to early human civilisation and the development of money.

### Early Trading Systems
Early humans could barter with their neighbours using goods or services on offer, but this quickly becomes cumbersome as values often do not align. In small tribes and families this is not a problem because the members trust each other. As societies or tribes get larger, inevitably there is interaction with another tribe whose members you do not trust. To resolve this peacefully elders of one tribe would negotiate with elders of another tribe, essentially keeping accounts of each other’s debt (Graeber, 2011). Thus arise two concepts that allow us to trust a neighbour: units of account and debt (Ferguson, 2008). There is still a problem with our early business environment though, what do you do with a tribe you’ve never encountered before? In the case that the elders have no previous history, how can they be trusted?

### Cash
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

### Finance
Finance could only evolve once stable systems for credit and debt and value transfer (cash) were widely accepted. In the fifteenth century in Italy, the Medici family were money changers that revolutionised banking. They were meticulous bookkeepers and adopted the new practice called double-entry bookkeeping where account debits were maintained in one column and credits in a separate column. Their success caused this style of banking to be the standard throughout Europe in the fifteenth and sixteenth century and is still standard today (Ferguson, 2008). Recording all account activity in a ledger is a core property of blockchain systems, including bitcoin.

It’s not just the idea of a permanent ledger that bitcoin borrowed, but rather the motivation to create a system outside of the one the Medici’s of 15th century Italy pioneered, and hold to this day. Next we will look at the computing branch.

## Traditional Banking System
The banking system we use today has capitalised on the internet infrastructure and computing ideas such as relational databases using an atomic transaction model, to truly become global. With relevance to blockchain development, this system:

- Uses digital double-entry accounting
- Has a centralised hierarchy and often distributed infrastructure
- Maintains a permanent record of transactions that are opaque to the public.

The bank is the middle-man, or final arbiter, of all transactions. The centralised architecture allows the bank to choose its customers and set fees. Among other monopolistic behaviours, this leads to censorship and in the digital age, hacks and breeches are increasingly common. Also, one may not want the bank to know exactly how and with whom you are transacting. As we learn more about the blockchain it will become apparent that bitcoin transactions are not anonymous, rather they are considered pseudonymous. Although your name is not attached to a transaction, the address and activity associated with it is permanently recorded in the blockchain. Digital privacy will be one of the most important consequences of the blockchain era.




## Digital Cash (without the bank)
The 80's & 90's saw many attempts to create a digital version of money that could have a token, both private and untraceable, treated as a bearer instrument and not subject to the fragilities of third party issuers and verifiers. To name a few there was David Chaum's work on *Untraceable Electronic Cash*, Wei Dai's [*b-money*](http://www.weidai.com/bmoney.txt), and Nick Szabo's [*Bit Gold*](https://unenumerated.blogspot.com/2005/12/bit-gold.html).

Many technical challenges along the road were overcome by advances in cryptography such as digital signatures and hash functions. However, one problem always stood out: how to prevent someone from using a digital coin at one shop, copying it, and spending it again? Known as the *double-spend problem*, this is easily sovled using a centralized authority to check someone's balance and update it accordingly; by the time you arrive at the second retailer your card will be declined for insufficient funds. Here the bank is saying, "You can only spend your dollar once."

The decentralized approach removes the bank entirely from the transaction and is one of the revolutionary ideas put forward by Satoshi in his whitepaper.

### Digital Cash *check continuity*
Chaum, Fiat and Naor (1988) came up with a scheme for issuing unique digital coins that could be redeemed by a centralised authority in a way that conceals the user’s identity. Anonymous digital cash. His scheme used what are called blind signatures and are clever because it means you can not reuse a digital coin. This is referred to as the double-spending problem because it’s easy to copy a digital object and then turn around and offer it to many people while claiming it’s unique. Chaum et al. commercialized his company, calling it DigiCash but it never caught on (Narayanan, 2016). One of the reasons was that it wasn’t a truly peer-to-peer system.


## The Double-Spend Problem
[Text related to 'The Double-Spend Problem' here]

## Distributed Systems
The key to the double-spend is to distribute the record of transactions to every participant in the network. In this manner every seller can verify independently that any buyer has the required unspent amount. Every new transaction is shared through the network with everyone else in a peer-to-peer (p2p) manner, rather than sending to a central server and having a gatekeeper update the accounts, this is handled at the individual level. The distributed ledger removes both the need for centralized accounting, and for trust between users. There is no reason for Alice to trust Bob because the network consensus says that Bob has the authority to spend his coins.

Practically speaking, each peer in the network listens for new blocks of transactions, verifies them, and adds them to their own local database. Should two nodes have conflicting information because they received new blocks at slightly different times, or with different transactions in them, then the state is said to fork, and for a short time *both* forks are valid. Resolving forks happens often, is expected, and is the job of the consensus mechanism. The way that Bitcoin does this is by a longest chain rule, meaning that whatever node has the longest chain of blocks is the most likely to receive a new block and therefore continue to be the canonical chain. If a node falls behind, then it abandons its chain and starts contributing to the longest. This method of distributed system consensus is now known as *Nakamoto* conseneus.
 
Because the chain is public you can do an inventory of nodes online at any given time. This also removes gatekeepers as anyone is free to join or leave whenever they want. At the end of 2021 the number of [bitcoin nodes](https://bitnodes.io/) globally was just under 15,000. (Compare this with centralized systems like Facebook that keep your data on anywhere from 3-5 nodes.)

## Bitcoin
[Text related to 'Bitcoin' here]
### The Whitepaper
<p align="center"><img width="800" alt="header to the bitcoin whitepaper" src="https://user-images.githubusercontent.com/39792005/145146212-c35aff55-97ab-478a-8e10-de2977bc7a7f.PNG"></p>

There are many components to this system that will be introduced. Individually it can be difficult to see the connection between them and how they contribute to a peer-to-peer monetary system. This is intended to be an overview and if you are just learning about Bitcoin don't be disuaded if the pieces seem disjointed or don't fall into place quickly. *(Learning is hard!)*

### Cryptocurrencies and the Blockchain
The Global Financial Crisis in the mid-2000’s created significant hardship and the blame was put clearly on the banking sector. While changes were called for in how banks managed risk, there was also social disquiet amongst those that felt that banks controlled too much financial and therefore, societal resource. In particular, libertarians called for an economic system free of the banking sector.

A person named Satoshi Nakamoto (Nakamoto, 2008b) designed a technological solution as a cryptocurrency, Bitcoin. While digital cash systems have a long history, with some successes such as PayPal, most have failed to ignite support. Bitcoin’s success seems in part to derive from its decentralised peer-to-peer system that provides complete transactions without a singular or centralised banking system.

The Bitcoin cryptocurrency architecture combines functions that provide money or coin creation, transactional cryptographic validation, and a highly redundant storage system that is publicly available but relatively anonymous (Brikman, 2014). An important measure that ensures cryptographically sound identification and verification of ownership is the use of SHA public/private key cryptography. This also provides a degree of anonymity, transactional integrity, and non-repudiation (Peteanu, 2014). The blockchain is a read-only public ledger of all transactions that have occurred within the cryptocurrency ecosystem and consists of a series of blocks that are created through proofing methods, such as Proof ofWork (Nakamoto, 2008b), Proof of Stake (Buterin, 2013; Larimer, 2013), plus any other proofs that may be required. To limit the number of transactions, Bitcoin transactions are completed every 10 minutes, each transaction returns a block that is added to the chain. Thus, each block contains the outputs of transactions, and with a cryptographic hash, they are added to a sequence, or chain, of blocks. The hash then provides ameans of referencing individual blocks (Wood, 2015).

In an accounting or economic sense, the chain represents a journaling system, although due to size constraints, the journal does not contain the final state. The transaction series is punctuated with “incentives” for nodes to mine, where “mining is the process of dedicating effort (working) to bolster one series of transactions (a block) over any other potential competitor block” (p.2, (Wood, 2015)). A cryptocurrency ecosystem is comprised of nodes, where a node is defined as any device that is running on or creates transaction or block data to the blockchain network (Community, 2014). Thus, a node may exhibit a variety of behaviours depending on context and function. Each cryptocurrency defines the purpose and functionality of nodes on its network, but, in general, the nodes are used to mine and validate blocks. They may also be used to provide defence mechanisms, such as limitations on the number of transactions processed per minute to prevent denial of service attacks.


## The Blockchain Data Structure
In Lecture 1 it was mentioned that [Haber1991] described a method to use one-way hash functions to digitally time-stamp documents. This creates an ordered list of the documents that itself is useful enough to act as a time-stamp. If document A appears in the list before document B, then it can be concluded that A was published to the list earlier (in time) than document B. This is important because digital items such as timestamps can be forged. It is only in relation to the other documents in the list that we pinpoint a window in time when document A came into existence. An isolated document or moment in history is not nearly as valuable without the context in which that event happened. The blockchain doesn't just provide context, it provides the entire history. How can a blockchain do this without being vulnerable to forged timestamps? First we must describe how data is organized on disc and the structures that allow its retrieval.

### Where are objects stored in memory?
When a program writes to disc or to memory there will be a predetermined area it is allowed to use. Usually this is allocated by the operating system at runtime. Because programs require lots of writing and rewriting to disc the data ends up being disorganized, or in seemingly sporadic locations. Thus, one item is probably not stored physically beside its related item. Data structures track where their items are located in memory and possibly other important information like the location of the last element or the maximum number allowed. Described here will be two data structures: a linked-list, and a tree. Both have simple diagrams to visualize how they work, but in practice can be tricky to implement. For this reason, all useful programming languages come with built-in data structure operations.



### Linked Time-stamping *CHECK*
The blockchain itself, as the name suggests, is a chain of blocks that are linked together using cryptographic hash functions. The idea was not unique to cryptocurrencies. Haber and Stornetta (1991) describe a method to use one-way hash functions to digitally time-stamp documents and maintain privacy. This hashing system is used to order the blocks in a blockchain while maintaining block integrity and security over time.


### Linked Lists
A linked list is a sequence of data that has a reference to previous or subsequent item. Figure [list] shows a schematic for integer elements that are linked to a subsequent item in their list. A key property of lists is that there is no absolute reference to individual elements. To find an element in the middle, say 99, you have to start at the beginning (12) and then traverse the list. Additionally in this manner it is easiest to append elements to the end of the list and much more difficult to insert elements part way through. For an introduction to lists and their programmatic implementation, see [Johnson2014] (available on Blackboard).
![Various linked lists. Top: a standard implementation with a reference pointer to the next element. Middle: a doulble-linked list with previous and subsequent pointers. Bottom: a circular linked list with reference back to the first element. Source: [source].][list]
![linkedLists](https://github.com/millecodex/COMP842/assets/39792005/468aafe3-f855-478e-80c9-adcd5139dd7e)

![blockchain](https://github.com/millecodex/COMP842/assets/39792005/34e431d1-4a41-42cc-9828-ea4d6385fd2f)


### Chains of Blocks
A blockchain is a data structure whereby a single block of data contains a hashed reference to a previous block. The chain of blocks can represent a chronological ordering of data as mentioned above. If blocks are appended regularly then the time-stamping effect can be as good as an actual time-stamp. When a new block is created it must include a reference pointer to the previous block in the chain. An ordinary linked list would contain a pointer referencing the object in memory. A blockchain reference is known as a *hash pointer* because it also includes a hash of the previous block.

> <p align="center"><img width="800" alt="blockchain data structure resembles ledger books" src="https://user-images.githubusercontent.com/39792005/152084209-bbde7db2-ddef-4f1b-bc98-354c0bc2e2ed.PNG"></p>
> 
> Each individual ledger is analagous to a block. When one book is full a new one begins with the account balances being copied over, thus linking the 'blocks'. The ledger is an accounting system that starts all the way back in the 1400's when the Medici family in Florence popularized double-entry accounting. The blockchain can be thought of as triple-entry accounting, where the third entry is the distributed copies that maintain consensus. Here, the second block has a cryptographic hash of the first block, and the third block has a hash of the second block, which, by definition includes the hash of the first block. This is how the chain maintains its integrity.

**Check text continuity**
The blockchain must be created one block at a time and mass deletion or appending of new blocks is not possible while maintaining the correct hash linking. If there are multiple new blocks to be added to the data structure,

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
		  "9d6e152ab00bd22c4803a5cb2d393ac72cbf81d2d708802a52da2236f4a8f658",
		  "16e53bf67ccec6cd30460dd721a9a940791aa327a50ac99bcdb7a6bd7949fe54",
		  "e406e599aeb4974473bf9a4bcdcc5de35d15fac296acceb217779680ae927d91",
		  "d55c96ce6ccf995035338f4ded57850f307299b0756b44c61b2fe5e5c2c89a51",
		  ,
		  ...truncated...,
		  ,
	 	  "22ba973e71869d1e64cdd8572fa94754429d52d84bce61b2374f082606e02ec5",
		  "35525a4db6c1fdea573780c9726ceebcd71788db66d05b83e661d864820b59c6",
		  "8a2d96492dc0be984e5ee5d8641ff599f63cfbedc0041e3343fc7b76f4d75de0",
		  "c996d69ba1d780de851422cf27b7bf65bcfe1e77631d86fb508d79fd57a58ff5"
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

The fields of block `620229` mined on March 05, 2020 in the Bitcoin blockchain. The transaction list has been truncated; this block has 350 transactions in total. The block ID is called *height* as if blocks are built on top of each other. Details of a block can be found at http://chainquery.com/bitcoin-api/getblock .
	

### Other pieces
### Cryptography
The 1980s saw a lot of research into the idea of being able to send a private digital message. Historically, this meant creating a cipher that converts a plaintext message into a ciphertext (encrypted message), sending the encrypted version, and the recipient has a matching cipher to enable them to decrypt the message. The key hurdle to this setup is that the cipher has to be transported to the recipient among eavesdroppers. A digital cryptosystem also involves distributing your cipher through any number of third-party servers that could have spies monitoring the connection.

Public key cryptography is the solution to this problem and will be covered more in Lecture 3. Although neither a blockchain nor bitcoin is a crypto-system, they both utilize elements of cryptography: hash functions, and cryptographic keys.

### Email
The Simple Mail Transfer Protocol (SMTP) was defined in 1982 (Postel, 1982). As a standard, this would allow anyone to write an email client according to the SMTP guidelines and be able to send messages to anyone else that also followed the protocol. It is still used today and has undergone many updates, however SMTP has two problems: all text is sent as plaintext, and it is easy to spoof from addresses and generate spam.

Email spam is an issue that was considered by Dwork and Naor (1993) when they wrote a paper describing the computational cost incurred by a spammer before sending an email. Titled Pricing via Processing, the idea is that your computer has to solve some computational puzzle before being permitted to send an email. For the average user this would take seconds
and not be a nuisance but for a spam emailer, this would slow down their operation. A few years later in 1997, Back (2002) created Hashcash in a similar vein. Although Back was unaware of the previous work by Dwork and Naor, Back also implemented the idea of a cost function that has an easily verifiable solution. This is now known as Proof-of-Work and used by Bitcoin miners (Nakamoto, 2008a).

## Characteristics and Quirks
* fixed supply
* block reward
* difficulty adjustment

## Bitcoin Today
Satoshi sent his whitepaper out to a [mailing list](https://satoshi.nakamotoinstitute.org/emails/cryptography/1/#selection-117.66-117.78) of like-minded cryptography cypherpunks on October 31, 2008. A few months later in January 2009 he started running the software and mined the genesis block. Since this time the Bitcoin network has been the most robust computing network humans have ever created. There has been almost no downtime, few bugs, no hacks, and exponential growth. 

With a total value of around $1 trillion USD, It is the 14th largest [currency](https://coinmarketcap.com/fiat-currencies/) next to the Russian Ruble and Swiss Franc. It is estimated that 1-2% of the global population have used or interacted with bitcoin, and [16% of Americans](https://www.pewresearch.org/fact-tank/2021/11/11/16-of-americans-say-they-have-ever-invested-in-traded-or-used-cryptocurrency/) have used or invested in cryptocurrency. There are reachable nodes running the core software in 87 countries. In El Salvador bitcoin is legal tender. 

What began as an experiment has bootstrapped an entire financial system with global settlement time in minutes and fees that are orders of magnitude cheaper and more secure than traditional banking infrastructure.

## What did we miss?
[Text related to 'What did we miss?' here]

# Exercises
1. a
2. b
3. c

# Further Reading - the very short list
* The Whitepaper: [*Bitcoin: A Peer-to-Peer Electronic Cash System* ](https://bitcoin.org/bitcoin.pdf)
* On the Shoulder of Giants - History of the tech: [*Bitcoin's Academic Pedigree*, Communications of the ACM](https://cacm.acm.org/magazines/2017/12/223058-bitcoins-academic-pedigree/fulltext)

# Next Lecture
* :point_right: [Secret Writing (Cryptography)](2-cryptography.md)
