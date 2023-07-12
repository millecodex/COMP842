[↰ back](../../..)
# Lecture 3: Consensus Part I: Proof of Work
## Contents
1. [Introduction](#introduction)
2. [Longest chain](#longest-chain)
3. [Mining/nodes](#miningnodes)
6. [Difficulty Adjustment](#difficulty-adjustment)
7. [Incentives](#incentives)
8. [What did we miss?](#what-did-we-miss)
9. [Further Reading - the very short list](#further-reading---the-very-short-list)
10. [Exercises](#exercises)

## Introduction
Consensus broadly defines the process used by a network to reach a state of agreement. This process is a communication algorithm that allows nodes to determine what has happened and act accordingly. An activity initiated by a user (or by an autonomous process) needs to be recorded by the system which means that all participating nodes must be aware of the activity.

> <img width="800" alt="" src="https://github.com/millecodex/COMP842/assets/39792005/e4342bb3-f119-4836-8e53-8151f65dd89b">\
> Figure: Democratic parliaments work this way - a member proposes an update to the legislation, then through the course of debate (and perhaps incentivising favours) the house comes to agreement on updating the legislature. Source: https://www.parliament.nz/en/get-involved/features/parliament-s-debating-chamber-turns-100/

In the parliament-nodes metaphor, each MP needs to be aware of the proposed update, and then make an informed decision to support or deny the change. Not every citizen has equal influence as MPs represent a constituency. The same can be true in computing networks - not all nodes are equal. We can classify computing networks by three types: centralized, decentralized, and distributed. The centralized network has a main server that controls all the events. This is where the rules are implemented, and also where the off switch can be found. As organizations scale, this approach becomes more decentralized either due to computing resource constraints or organizational limits in the case of a global system, such as a bank. The tech giants we are used to todays are distributed - they have nodes, including data centers, in various jurisdictions while operating as a single entity.

> <img width="800" alt="" src="https://github.com/millecodex/COMP842/assets/39792005/ac182253-3850-4667-bc72-ed32550de671">\
> Figure: Degrees of decentralisation. The dots are nodes in the network and the graph edges are communication links. Source: Baran (1964) for an excellent overview of redundancy and vulnerability of digital communications networks.

On the right in the figure is a distributed (mesh) network which shows a high degree of decentralisation. If any node goes offline, the remainder of the network is largely unaffected. Compare with the middle figure where certain nodes can have large effects in the network should they be compromised or need to be repaired. 

### Centralized Consensus
Lets consider the case of withdrawing money from an ATM. The bank operates a network of ATM machines that maintain connection to a central server. A user requests \$100 from her local ATM. The machine must connect to the bank's server and query the database for an account balance, confirm that it is greater than the requested amount and respond to the ATM. The machine now sends a second request for withdrawal (step 3 in figure below) and the server will debit the users account, sending a message back to the ATM. It is only at this point that the \$100 can be dispensed; after the account has been debited. This is known as a two-phase commit; the first phase is a request, and the second phase is an action.

> <img width="800" alt="A single node simplified ATM network" src="https://github.com/millecodex/COMP842/assets/39792005/1fc47f55-f2d3-459a-8447-4a7f595eed3e">\
> Figure: A simplified ATM network and the steps required to withdraw money. This is an example of a client-server relationship. If communication fails at step 4 this could be a problem.

Adding a second ATM to the network complicates the process. If our user withdraws \$100 at the first ATM and then proceeds to another ATM the network needs to be updated about the state of her account. If our ATM dispensed money without updating the balance or if the message wasn't delivered, or if the write operation failed, then the ATM might think there is a different balance from the central server. This database would be inconsistent. The numerous components to a banking network are expected to fail at a prescribed rate, but the precise timing is unknown, and so the network must be robust against failure at any time. These systems are called *fault-tolerant*.

> <img width="800" alt="Multiple nodes in a simplified ATM network" src="https://github.com/millecodex/COMP842/assets/39792005/e9795dc1-f495-4a7d-af17-1363cdba6f59)">\
> Figure: Multiple nodes in the network. If a simultaneous request comes from 1 and 2, the server needs to order the events and make sure it has heard from every node before responding at 4. Additionally, information may be stuck at 3 if there is a fault or a delay in the network communication and 4 will have to wait.



### Distributed Consensus

The picture is different when the centralized server is removed; referred to as a peer-to-peer (p2p) network every participant is at the same level of the hierarchy. Now all the nodes (peers) must communicate with each other and decide on the true state of the blockchain. This is a circular process where all nodes must agree and some must propose updates which then need to be agreed upon.

> <img width="800" alt="A state diagram for a distributed blockchain showing the hashing competition for the process of generating new blocks and updating the chain." src="https://github.com/millecodex/COMP842/assets/39792005/59aeb48c-3bcf-4a23-834e-ddab3de2c444">\
> Figure: A state diagram for a distributed blockchain showing the hashing competition for the process of generating new blocks and updating the chain.

The process of all nodes agreeing is consensus, and the process of proposing updates is accomplished by mining, to be discussed in more detail next lecture. The algorithms for consensus must still be fault-tolerant, just like centralized systems, but they must also be resilient against malicious, or *Byzantine* adversaries.

### Byzantine Generals Problem

The *Byzantine Generals Problem*, is a famous computer science communication problem. Imagine three generals of the same army, all wanting to attack an enemy fortress at dawn the next morning. Each general knows their individual divisions cannot win the enemy fortress. Each general also knows that with the help of the other's forces they can win the position. So General *Alpha* sends a messenger to General *Beta* with the message "We attack at dawn." This is where the problems start. There are many scenarios that could play out. The messenger could be captured by the enemy; the messenger could be a double-agent; the messenger could get lost and not deliver the message; General Beta could double-cross Alpha, etc. To win the battle, the three generals must come to consensus and agree to attack at dawn. Practically speaking, each general must receive confirmation from each of the other generals that they received the message *and* are in agreement. This scenario maps nicely onto cryptography and message passing.

A decentralized blockchain application has many nodes in the network and each of them has a copy of the blockchain. If Bob wants to send Alice his tokens, the nodes in the network must first agree that Bob has available tokens to spend, and then update the state before Bob can double-spend his tokens. The network needs to be in a state of *consensus* for people to trust it. Consensus in the Byzantine Generals problem has been proven to be impossible if more than a third of the nodes are malicious~[Fischer1985].

Bitcoin does not exactly mirror the model of the Byzantine Generals and so is not impossible to reach consensus. In other words, bitcoin does achieve consensus despite Byzantine behaviour. More practically, bitcoin achieves a state of *emergent* consensus. This means that over time as blocks get added to the chain, a general state emerges that everyone agrees on. 

Consensus in bitcoin is referred to as emergent consensus indicating that agreement develops over time based on the longest chain. The longest chain is a representation of the most proof of computational effort that has been dedicated to the network, hence the name _proof of work_.

So how does this occur without clear rules? A closer look at the double-spend attack will illustrate how nodes come to agreement.



### Proof-of-Work
Here is an important distinction where bitcoin varies from other methods of reaching consensus. There are incentives for nodes to act honestly that are built into the protocol. The first is called the _coinbase_ transaction and awards freshly minted bitcoins to whoever added the block to the chain. This is how new bitcoins come into circulation. The second is from transaction fees. By listening to the network, validating transactions, and including them in a block, whoever is operating the node can choose to include transactions that offer an extra fee. Because bitcoin itself is designed to be digital money, this makes perfect sense and is why cryptocurrency is considered the killer app for blockchain. See (Antonopoulos 2017, p234-238) for details about collecting transactions into a block and validating them for addition to the chain.

Referring back to the Figure, who gets to propose these blocks and earn the block reward? How do we ensure the distribution is random? How are Sybil attacks prevented?

### Mining
A miner is a network participant that contributes their computing power in a demonstrable way. A fair way to allocate the incentives would be by some resource that can not be gamed or monopolized. One such way is by computing power as proposed by Dwork and Naor in 1993 in relation to email spam, and refined by Hashcash in 2002 for digital currency. Bitcoin miners participate by using their hardware to validate transactions and suggest new blocks. For this effort they receive rewards in proportion of their contribution to the network as a whole. A fair way to determine effort used by the miners is to have them search for a particular hash that meets a target. Bitcoin uses the `SHA256` hashing algorithm as the hash puzzle that miners have to find a solution for.

> “mining is the process of dedicating effort (working) to bolster one series of transactions (a block) over any other potential competitor block” (Wood, 2015)

### Mining/nodes
So, PoW is called mining because of the non-redeemable effort that goes into finding new new coins. Every ten minumtes on average a new block is  mined and with it the miner can redeem the block reward → freshly minted bitcoins.

To find a block, one must bundle the available transactions and apply the hashing algorithm such that:
```
Block = Hash(nonce||previousHash||tx||tx||...||tx) < target
````
The `Hash` output has a random distribution and so to find a block, your hash must be below a certain target level. The target level will be the hash size with a certain number of leading zero bits, for example:
```
000000000000000000117c467ab5336077cb04f7f70ea6ebcd68e0b3ef6cf909
```
was the successful hash of block `529283`. The only way to find a hash with a smaller value than the target is to change a nonce value and re-hash the bundle of transactions over and over. When a target is hit, the block is broadcast to the network as a proof of computational work done in solving the hash puzzle. Note this is a hex value and so every additional zero bit represents a 16x decrease in probability of meeting the target.

## Difficulty Adjustment
The bits here should be randomly distributed, like a lottery, to prevent gaming the system and earning more rewards than your proportion. Computing cycles in the bitcoin network are called _hashpower_ in reference to `SHA256`. As more miners come online, the total hashpower increases leading to greater overall probability of successfully hashing a value below the target. To keep the temporal distribution of blocks even, this target difficulty automatically adjusts according to the protocol every 2016 blocks, or approximately two weeks.

Figure is a plot of the mining difficulty showing an exponential increase. The slope roughly correlates to the growth of the network. As the bitcoin network has matured, dedicated hardware called ASICs (application specific integrated circuits) to solve the `SHA256` algorithm have dominated. It is no longer feasible for a single participant to mine bitcoin without dedicated hardware.

> <img width="800" alt="Bitcoin mining difficulty plotted on a logarithmic scale." src="https://github.com/millecodex/COMP842/assets/39792005/a877855a-795f-431d-8d82-2c45b6b9cfe8">\
> Bitcoin mining difficulty plotted on a logarithmic scale. Source: https://www.blockchain.com/explorer/charts/difficulty


Consider a simulation using an Intel Core i5 6400 looking for `SHA256` hashes with leading zeroes. The difficulty in this case is increasing by powers of 16. Five leading 0's were found in 8364 seconds and, as of writing this, six leading 0's are predicted to take `≈ 8364×16=133824` seconds, or 37 hours.

```
Difficulty: 1
Nonce: 43
Proof-of-work: 05b7e096306a10c850cd8fe6bf55b1cc97365538cadbe3dc89e1216298275a69
Elapsed time: 0.0009968280792236328

Difficulty: 2
Nonce: 22
Proof-of-work: 002fcd61b3f3188e0f7fdff849e8dd3ee5805a34e06f4c6a8fd4fb86d4577350
Elapsed time: 0.005983591079711914

Difficulty: 3
Nonce: 12489
Proof-of-work: 0003124c9428d9a1c6f2ef0a782a044bcfde374cf6dfef414b161f8594377246
Elapsed time: 0.7731056213378906

Difficulty: 4
Nonce: 224827
Proof-of-work: 0000d66a2b464413b4af3b52ffef44a714ced1c06a4471c389755bf2eca19cef
Elapsed time: 239.61160159111023

Difficulty: 5
Nonce: 1230021
Proof-of-work: 000004ab089b08c3ceed5622dbe1ea0a3d621295379d107707cf2b8f9ffc9098
Elapsed time: 8363.934648275375
```

> <img width="800" alt="A simplified ATM network" src="https://github.com/millecodex/COMP842/assets/39792005/676c6c14-d4e4-494e-b475-167c12b69c11">\
> A Bitmain Antminer S9, 13.5 terahash edition with power supply. Coffee mug for scale. Photo credit: Jeff Nijsse.

The Figure shows a dedicated SHA256 miner. The S9 is (was) the workhorse of the bitcoin network. It contains 189 individual chips that calculate a total of 13.5 trillion hashes per second. (Compare this to the hashrate of the i5 above!)


### Block Time

The difficulty adjustment aims to keep the time between blocks (successful hashes) at around ten minutes. In the early days, Satoshi and a few others could use their PC processors to find blocks every ten minutes. The hashpower has steadily increased and so has the difficulty target to keep the block time constant. Finding a hash of a block that is below the target size is a discrete event; it is either below or it is not. As with a lottery, it is only a matter of time before a hash is found, and the previous hash is independent of the current attempt. Statistically, this is a *Poisson* distribution. 

> <img width="800" alt="Block Time Poisson" src="[https://github.com/millecodex/COMP842/assets/39792005/676c6c14-d4e4-494e-b475-167c12b69c11](https://github.com/millecodex/COMP842/assets/39792005/e8c6651b-a33d-4371-9168-375721807172)">\
> Block Time Poisson
> 
From the graph[^1], you can see it's possible to find a block immediately after the last one, but unlikely. Similarly, it's possible that no block could be found for an hour or two, but unlikely. In practice, the average block time is just under ten minutes because as more miners join the network it is easier overall to find blocks, until the difficulty is reset. Block time is a design consideration; Ethereum adds a block approximately every 15 seconds.

### Fixed Supply
A brilliant idea that Satoshi incorporated into the bitcoin protocol is that the number of newly minted bitcoins decreases over time. Every 210,000 blocks (≈ four years) there is a halving event and the next block found is only allowed to pay out half the bitcoins. This defines a finite money supply. If you run the clock forward, assuming a new block is added every ten minutes, there will be no new bitcoins minted after the year 2140. Presently the coinbase transaction is for 12.5 BTC[^2] and at some point in May 2020 it will decrease










### The Double-Spend Attack
Solving the situation known as the *double spend problem*, is the final piece of the puzzle that was put in place for trustless decentralized digital cash to succeed. 

A dodgy actor, Eve, could manipulate the blockchain by sending some coins to Jeff and receiving a good or service. Then she could send those same coins to Bob's address whom she also controls. If the transaction involving Bob's address is validated on the blockchain, then Eve would have successfully double-spent the same coins. She now has the coins in Bob's address and the goods from the transaction with Jeff.

> <img width="800" alt="Double Spend Success" src="https://github.com/millecodex/COMP842/assets/39792005/3c5e1fdc-7521-4a0f-9b99-66e4f3d123b6">\
> Figure: For Eve to successfully double-spend in the blockchain she must take advantage of a fork in the chain. If the chain with the Eve to Bob transaction is the longest, representing the most cumulative proof of computation effort, she has double-spent.

How can Jeff avoid this scenario, especially when he does not know the other party he is transacting with? The solution is to wait. Over time as more blocks are added, say every ten minutes, the older blocks are more likely to be valid.[^1] Stated another way, as more blocks are added to the chain there is an exponential decrease in the probability of a block being rejected by other nodes. This is the method that secures the blockchain against malicious nodes attempting to double spend. 

[^1]: Standard confirmation time for bitcoin is six blocks, or one hour. The number of blocks to wait until considering a transaction to be confirmed is a personal preference.

> <img width="800" alt="Double Spend Solution" src="https://github.com/millecodex/COMP842/assets/39792005/2adf3b0c-9a8b-4b52-9353-60931659393d">\
> Figure: Jeff has waited to accept Eve's transaction. After six confirmations it is very unlikely that Eve's alternate chain will accepted as valid. Over time there is increasing probability that transactions are secure.

And what about Eve changing history? She would have to alter the block where the transaction is stored, as well as any subsequent blocks. The older the block is, the more computational effort is required because the hash pointers are linked. Consider that Eve is also competing against other nodes in the network that are honest. (We will return to the case of dishonest nodes when discussing a 51% attack.) 




## PoW Vulnerabilities
Two main weaknesses in proof of work cryptocurrencies will be briefly mentioned here and discussed further in the lecture on security.

### 51% attack
Should a single entity gain control of more than half of the hashpower in the network, this could lead to a 51% attack[^11]. The attacker can't steal coins directly as this involves subverting elliptic curve cryptography. The attacker can however user their majority status in some interesting ways. At >50% you have the ability to find more blocks and direct consensus of the blockchain. The attacker can censor transactions by refusing to add blocks containing someone's address. This would be akin to blacklisting certain addresses, but does not completely exclude these from being included in blocks mined by honest nodes (the 49%). As the proportion in control increases, it will be harder to get a blacklisted transaction published on the blockchain. With this majority, the attacker will now earn a larger proportion of block rewards, but still has to find `SHA256` hashes like everyone else. 

It is tempting at this point to ask: Can I change the block reward and earn more per block found? This will be rejected by the network because the block reward is hard-coded and so the malicious extra-reward transaction can never be spent. In a distributed system everyone has a version of the consensus rules that must agree with everyone else. A different block reward would have to be done as a software upgrade and falls under Community Level Security.

### Selfish mining
An adversary doesn't necessarily need 51% of the hashpower, but with a large number of nodes in the network they could gain an advantage. An interesting analysis was published in 2014 by~\citeA{Eyal2014} that showed a conglomerate of miners could form with as little as one-third of the hashpower. This mining cartel can continuously mine without broadcasting their blocks until some set time in the future. In the short term the miner is sacrificing the immediate block reward by not propagating their found blocks to neighbouring nodes. In the long run however, the result is that the honest miners are doing work that is not in competition with the selfish miners, increasing the attacker's expected rewards. The results of Eyal \& Sirer's study conclude a group can increase their mining payout with a little as $\frac{1}{3}$ of the network's hashpower.


### question
The next question is how to keep nodes honest? Especially when dealing with the medium of currency. Incentive structures need to be aligned from the beginning that discourage dishonest behaviour and scale well. One method is proof-of-stake.

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

# References
Baran, P. 1964. On distributed communications: I. introduction to distributed communications networks. Santa Monica, CA: RAND Corporation. https://www.rand.org/pubs/research_memoranda/RM3420.html 
