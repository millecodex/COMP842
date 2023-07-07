[↰ back](../../..)

# Lecture 4: Consensus Part II: Proof of Stake & Alternatives
## Contents
1. [Proof of Stake](#proof-of-stake)
2. [Scarce resource](#scarce-resource)
3. [PoX](#pox)
4. [Incentive structures](#incentive-structures)
5. [Decentralisation](#decentralisation)
6. [What is a blockchain?](#what-is-a-blockchain)
7. [Summary](#summary)
8. [What did we miss?](#what-did-we-miss)
9. [Further Reading - the very short list](#further-reading---the-very-short-list)
10. [Exercises](#exercises)

Recall the state diagram from Lecture 4. A distributed computing system has nodes that are geographically separated, may run different versions of the software, have varying latencies, and no minimum or maximum thresholds for participants. All nodes must agree on the state of the ledger without any authority figures. Just like playing recreational sports in the absence of a referee, there are generally agreed upon rules that when followed make the experience worthwhile. These are the consensus rules that are programmed into the software. Keep in mind that truly distributed systems have open source software that anyone can edit[^1].

[^1]: Governance in distributed open-source systems is another area of study. It is theoretically possible to change the rules of bitcoin by modifying the core client because anyone can do it. Distributing the `new' version and having it gain acceptance is another matter.

> <img width="800" alt="A state diagram for a distributed blockchain showing the hashing competition for the process of generating new blocks and updating the chain." src="https://github.com/millecodex/COMP842/assets/39792005/59aeb48c-3bcf-4a23-834e-ddab3de2c444">\
> Figure: A state diagram for a distributed blockchain showing the hashing competition for the process of generating new blocks and updating the chain.
\
> \
> \
> \
> \
> \
> \
> \
> \
> \
> \
> go through and arrange all this
>
> 
## Proof of Stake
Proof of stake assumes that participants with the most personal value in the system will have an interest in maintaining operations. It closely relates to shareholding in a public corporation whereby shareholders are entitled to certain rights and expect the corporation to maintain or increase the value of their shares. Stake holders may be awarded voting rights in governance decisions such as disbursement of community funds or changes of protocol. Users are incentivised to maintain their share in the project through block creation and reward, fees, and potential increases in token value.

Block creation in a proof of stake system is proportional to the fraction of tokens someone holds. If a single entity has 5% of the tokens at stake, they can expect 5% of the block rewards. To stake tokens, one must have them committed to the blockchain network and thus can not spend or transfer them.

Ethereum is the largest project that has proof of stake as a goal. Ethereum started with a proof of work system and is planning on upgrading at some point in the future to a staking system. This was by design as bootstrapping token distribution in a cryptocurrency is not straightforward.

Proof of stake is a lightweight system that does not require substantial hardware investment such as mining equipment and therefore also does not have the electricity consumption. There is a low barrier to entry as you simply need to acquire some of the coin to participate. However, this could also allow a large player to influence the network by purchasing their way in.

### Proof-of-Stake

Bitcoin uses an exceptional amount of hashpower and therefore electricity. Alternative methods look to ease this reliance on dedicated hardware and increasing power consumption. This was the prime motivation behind Proof-of-stake.

Tokens held by a user may be committed to maintaining a protocol. Proof-of-stake removes the thermodynamic inefficiency by allocating users a stake in the system proportional to their tokens. This stake can then be used to scale incentives for users that participate, generally by committing their tokens in a manner that incentivises honest behaviour. Proof of stake was the first proposed with *Peercoin* to remove the computational burden of finding hash targets by introducing an age metric: *coin age = amount × holding period*. In this case, seniority wins and allows for minting rewards based on the amount of coins being held and the length of time they've been inactive[^3]. Colloquially, proof of stake means any system where a user's puts up collateral and earns rewards proportional to their collateral.

A user's stake is different from a user's vote as they hold no utility other than determining a majority. Many present tokens employ a voting procedure to determine the block proposer. This is called *Delegated* Proof-of-stake operates similar to a democracy. Users vote for a leader that has authority to verify and publish transactions as well as collecting the reward for doing so[^4]. Delegate PoS is considered a hybrid system and relies on the reputation of the delegates. Various methods can be employed for electing leaders.

### Alternate consensus methods

Many alternative methods have been proposed in the literature and some have prototypes, but it is very early into this new field of research. Other methods include:

- **Proof of space** uses disk space as a resource. Most users have unused disk space on their machines; dedicating some of this to secure a blockchain would not require additional power or dedicated hardware. A proof of space system would require a network participant to hold a large file on their system. To prove they have dedicated the disc space, they might have to verify random parts of the file from time to time. The details can be found in [^5].

- **Proof of retrievability** is a modification of bitcoin, implemented in Permacoin[^6], that would allow for a large dataset such as the library of congress to be stored across individual participant's computers. This would ensure full data recoverability with high probability while limiting excess power consumption.

- **Proof of elapsed time** was developed by Intel in 2016 to take advantage of their new chip architecture instruction set. Blockchain consensus from PoET comes from being able to make trusted processors wait a random amount of time before mining a block[^7]. IBM's blockchain *Hyperledger* uses PoET to enforce random block selection[^8].

- **Proof of human work** is a puzzle that is moderately hard for humans to solve, easy for computers to generate, and hard for computers to solve[^9]. An example puzzle would be a CAPTCHA (Completely Automated Public Turing-Test to tell Computers and Humans Apart).

### Consensus Summary

In summary, consensus of nodes in a proof-of-work system like bitcoin emerges from an implicit agreement on the longest chain of blocks. The nodes are all agreeing that this blockchain represents the most computational effort via hashing. It is quick to validate the proof of work because the nonce for every block is published. As soon as a miner learns of a new block, they will abandon shorter chains to compete to build on the longer one to win the block reward. The transactions in this chain will have an increasing probability of being accepted over time as new blocks are mined on top of them. 

As of July 2019, the Bitcoin network alone was consuming more than 45.9 terawatt-hours of power, comparable to the consumption of a small country such as Jordan or Sri Lanka[^10]. For this reason researchers and developers have been looking for energy saving alternatives. The most promising is proof-of-stake which relies on a participants staking of tokens in the network. Ethereum is set to upgrade to a staking system later this year.









## Scarce resource

## PoX

## Incentive structures

## Decentralisation

## What is a blockchain?

## Summary

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

## What did we miss?

## Further Reading - the very short list

## Exercises

