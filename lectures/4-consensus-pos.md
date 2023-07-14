[↰ back](../../..)

# Lecture 4: Consensus Part II: Proof of Stake & Alternatives
## Contents
1. [Proof of Stake](#proof-of-stake)
2. [Digital Scarcity](#digital-scarcity)
3. [Proof-of-X (PoX)](#pox)
4. [Incentive Structures](#incentive-structures)
5. [Decentralisation](#decentralisation)
6. [What is a Blockchain?](#what-is-a-blockchain)
7. [Summary](#summary)
8. [What did we miss?](#what-did-we-miss)
9. [Readings](#readings)
10. [Exercises](#exercises)

Recall the state diagram from Lecture 3. A distributed computing system has nodes that are geographically separated, may run different versions of the software, have varying latencies, and no minimum or maximum thresholds for participants. All nodes must agree on the state of the ledger without any authority figures. Just like playing recreational sports in the absence of a referee, there are generally agreed upon rules that when followed make the experience worthwhile. These are the consensus rules that are programmed into the software. Keep in mind that truly distributed systems have open source software that anyone can edit[^oss].

[^oss]: Governance in distributed open-source systems is another area of study. It is theoretically possible to change the rules of bitcoin by modifying the core client because anyone can fork the [repo](https://github.com/bitcoin/bitcoin) and make changes. Distributing the `new' version and having it gain acceptance is another matter.

### ⏸️🕐 
Its worth a pause here to think about **How can you chose someone (a node) to make updates?**

> <img width="800" alt="" src="https://github.com/millecodex/COMP842/assets/39792005/031d091a-5329-48f7-a9aa-4e37019d79e6">\
> Figure: A state diagram for a distributed blockchain involves continually proposing and processing updates to the state

If your network is distributing rewards such as a coinbase then its imperative that (a) people think the distribution is fair and (b) it can't be gamed. If your network is not distributing obvious financial rewards, then do the same questions apply? And if your network is permissioned (perhaps an Amazon datacenter) then do these questions matter?

## Proof of Stake
Shortly after Bitcoin started people were looking at alternate ways to achieve decentralised consensus by varying the rewards, hashing mechanism, and mechanics of winning a block to append to the chain. One of the primary criticisms of Bitcoin is the mining aspect which seems to incentise more and more miners and specialized hardware coming online just to try and win the block reward.

> "Proof-of-work helped to give birth to Nakamoto’s major breakthrough, however the nature of proof-of-work means that the crypto-currency is dependent on energy consumption, thus introducing significant cost overhead in the operation of such networks, which is borne by the users via a combination of inflation and transaction fees."\
> Sunny King, Scott Nadal, [PPCoin Whitepaper](./papers/peercoin-paper.pdf), Aug. 2012.

First outlined by King and Nadal, they suggested a mechanism where users put up a stake of their coins to validate transactions and earn rewards proportional to their stake in the network. The [Peercoin](peercoin.net) design still uses a proof-of-work hash system for users to earn the block proposing right by lottery (in combination with a property called *coin age* $=$ days $\times$ stake), but it is in a limited capacity. In this case, seniority wins and allows for minting rewards based on the amount of coins being held and the length of time they've been inactive. The network can be classified as a hybrid PoW/PoS system.

2014 saw a bloom of research and projects into proof-of-staking style blockchain systems. A proof-of-stake-only system will use staking both for network security and for minting of new tokens. 
* Nxt is a "100% proof-of-stake cryptocurrency"
* Bitshares introduced Delegated Proof-of-Stake
* Tendermint: Consensus without Mining is published

Motivation for the switch to a staking-type blockchain is primarily mining centralisation risk, but also resource consumption, and an element of intellecual curiousity - Can we do this without mining?

[Casper](https://arxiv.org/abs/1710.09437) is published in 2017 by Vitalik Buterin and Virgil Griffith as the groundwork for a transition for Ethereum to proof-of-stake. 

> "Proof-of-stake underlies certain consensus mechanisms used by blockchains to achieve distributed consensus. In proof-of-work, miners prove they have capital at risk by expending energy. Ethereum uses proof-of-stake, where validators explicitly stake capital in the form of ETH into a smart contract on Ethereum. This staked ETH then acts as collateral that can be destroyed if the validator behaves dishonestly or lazily. The validator is then responsible for checking that new blocks propagated over the network are valid and occasionally creating and propagating new blocks themselves."\
> Quote: From the [ethereum.org](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/) website describing Proof-of-Stake

Colloquially, proof of stake means any system where a user puts up collateral and earns rewards proportional to their collateral. Proof of stake assumes that participants with the most personal value in the system will have an interest in maintaining operations. It closely relates to shareholding in a public corporation whereby shareholders are entitled to certain rights and expect the corporation to maintain or increase the value of their shares. Stake holders may be awarded voting rights in governance decisions such as disbursement of community funds or changes of protocol. Users are incentivised to maintain their share in the project through block creation and reward, fees, and potential increases in token value.

Proof of stake is lightweight compared to Bitcoin by not requiring substantial hardware investment such as mining equipment and therefore also does not have the electricity consumption. There is a low barrier to entry as you simply need to acquire some of the coin to participate. However, this could also allow a large player to influence the network by purchasing their way in. We will cover more staking-specific issues in the Lectures on Ethereum, and Security.

## Digital Scarcity
So far we have two categories of blockchain consensus: proof of computational work, and proof of token-value. We can extend this to other categories as long as the network is allocating a scarce resource. In the case of PoW miners this is the amount of bit-flipping the ASICs can do. For PoS it is the guarantee that tokens-staked are scarce and therefore have value to users of the network. There are other methods of consensus scarcity, votes for example are a scarce resource because one person is entitled to one vote, and only one vote. The same can be said if a node or processor is allocated a single vote.

The table shows various consensus methods classified by the scarce resource that is occupied. Note the resource doesn't have to be universally scarce, just within the bounds of the network and its participants.

## PoX
Many alternative methods have been proposed in the literature and some have prototypes, but it is very early into this new field of research. Other methods include:

- **Proof of space** uses disk space as a resource. Most users have unused disk space on their machines; dedicating some of this to secure a blockchain would not require additional power or dedicated hardware. A proof of space system would require a network participant to hold a large file on their system. To prove they have dedicated the disc space, they might have to verify random parts of the file from time to time. The details can be found in [^5].

- **Proof of retrievability** is a modification of bitcoin, implemented in Permacoin[^6], that would allow for a large dataset such as the library of congress to be stored across individual participant's computers. This would ensure full data recoverability with high probability while limiting excess power consumption.

- **Proof of elapsed time** was developed by Intel in 2016 to take advantage of their new chip architecture instruction set. Blockchain consensus from PoET comes from being able to make trusted processors wait a random amount of time before mining a block[^7]. IBM's blockchain *Hyperledger* uses PoET to enforce random block selection[^8].

- **Proof of human work** is a puzzle that is moderately hard for humans to solve, easy for computers to generate, and hard for computers to solve[^9]. An example puzzle would be a CAPTCHA (Completely Automated Public Turing-Test to tell Computers and Humans Apart).

A user's stake is different from a user's vote as they hold no utility other than determining a majority. Many present tokens employ a voting procedure to determine the block proposer. This is called *Delegated* Proof-of-stake operates similar to a democracy. Users vote for a leader that has authority to verify and publish transactions as well as collecting the reward for doing so. Delegate PoS is considered a hybrid system and relies on the reputation of the delegates. Various methods can be employed for electing leaders.

## Incentive structures

## Decentralisation
| | Centralized | Distributed (p2p) |
|---|---|---|
| Structure | Top-down; rules based | 1-node at a time; protocol based |
| Membership | Gatekeepers allow you to join and can expel/blacklist | Anyone can join (and leave) based on the protocol |
| Consensus | Voting and elections; democracy | Proofing methods: proof-of-work, proof-of-stake, etc.; meritocracy |
| Robustness | Fault-tolerant; no expected Byzantine actors | Fault and Byzantine tolerant |
| Incentive structure | Honesty enforced by legal structure of the corporation and therefore the state in which it operates | Honesty incentivised by some kind of reward (monetary, token, social, etc.) |
| Examples | Banks, Facebook, governments | Bit-torrent, email, wikis* & the internet* |
| Blockchain examples | Enterprise blockchains: Hyperledger (IBM/Linux), Azure (Microsoft), Quorum (JP Morgan) | Bitcoin, Ethereum, many other cryptocurrencies |
> Table: Centralized versus decentralized organizations and some of their features. *depending on your perspective



## What is a blockchain?
We are now in a position to pose a definition of a blockchain.

A blockchain is a distributed architecture that has a mechanism to handle:
* a fork-choice rule; how does the blockchain resolve forks?
* sybil attack mitigation method


### Summary
In summary, consensus of nodes in a proof-of-work system like bitcoin emerges from an implicit agreement on the longest chain of blocks. The nodes are all agreeing that this blockchain represents the most computational effort via hashing. It is quick to validate the proof of work because the nonce for every block is published. As soon as a miner learns of a new block, they will abandon shorter chains to compete to build on the longer one to win the block reward. The transactions in this chain will have an increasing probability of being accepted over time as new blocks are mined on top of them. 

As of July 2019, the Bitcoin network alone was consuming more than 45.9 terawatt-hours of power, comparable to the consumption of a small country such as Jordan or Sri Lanka[^10]. For this reason researchers and developers have been looking for energy saving alternatives. The most promising is proof-of-stake which relies on a participants staking of tokens in the network. Ethereum is set to upgrade to a staking system later this year.



# What did we miss?
* We have yet to get into the security element of blockchains

# Exercises
1. How does 

# Readings
* PPCoin: Peer-to-Peer Crypto-Currency with Proof-of-Stake ([pdf](./papers/peercoin-paper.pdf))
* Ethereum's Whitepaper ([2014 pdf, historical](https://ethereum.org/669c9e2e2027310b6b3cdce6e1c52962/Ethereum_Whitepaper_-_Buterin_2014.pdf), current: https://ethereum.org/en/whitepaper/)
* Tendermint: Consensus without Mining ([pdf](./papers/tendermint.pdf))

# Next Lecture
* :point_right: [Network Scaling](5-scaling.md)

# References
1. 
