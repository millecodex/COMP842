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
Consensus broadly defines the process used by a network to reach a state of agreement. This process is a communication algorithm that allows nodes to determine what has happened. An activity initiated by a user (or by an autonomous process) needs to be recorded by the `system` which means that all participating nodes must be aware of the activity. Recall from lecture 1 the three types of networks: centralized, decentralized, and distributed. The centralized network has a server that controls all the events. As organizations scale, this approach becomes more decentralized either due to computing resource constraints or organizational limits in the case of a global system, such as a bank. 

Lets consider the case of withdrawing money from an ATM. The bank operates a network of ATM machines that maintain connection to a central server. A user requests \$100 from her local ATM. The machine must connect to the bank's server and query the database for an account balance, confirm that it is greater than the requested amount and respond to the ATM. The machine now sends a second request for withdrawal (step 3 in figure below) and the server will debit the users account, sending a message back to the ATM. It is only at this point that the \$100 can be dispensed; after the account has been debited. This is known as a two-phase commit; the first phase is a request, and the second phase is an action.

> <img width="800" alt="A single node simplified ATM network" src="https://github.com/millecodex/COMP842/assets/39792005/1fc47f55-f2d3-459a-8447-4a7f595eed3e">\
> Figure: A simplified ATM network and the steps required to withdraw money. This is an example of a client-server relationship. If communication fails at step 4 this could be a problem.

Adding a second ATM to the network complicates the process. If our user withdraws \$100 at the first ATM and then proceeds to another ATM the network needs to be updated about the state of her account. If our ATM dispensed money without updating the balance or if the message wasn't delivered, or if the write operation failed, then the ATM might think there is a different balance from the central server. This database would be inconsistent. The numerous components to a banking network are expected to fail at a prescribed rate, but the precise timing is unknown, and so the network must be robust against failure at any time. These systems are called *fault-tolerant*.

> <img width="800" alt="Multiple nodes in a simplified ATM network" src="https://github.com/millecodex/COMP842/assets/39792005/e9795dc1-f495-4a7d-af17-1363cdba6f59)">\
> Figure: Multiple nodes in the network. If a simultaneous request comes from 1 and 2, the server needs to order the events and make sure it has heard from every node before responding at 4. Additionally, information may be stuck at 3 if there is a fault or a delay in the network communication and 4 will have to wait.



### Distributed Consensus

The picture is different when the centralized server is removed; referred to as a peer-to-peer (p2p) network every participant is at the same level of the hierarchy. Now all the nodes (peers) must communicate with each other and decide on the true state of the blockchain. This is a circular process where all nodes must agree and some must propose updates which then need to be agreed upon.

> <img width="800" alt="A simplified ATM network" src="https://github.com/millecodex/COMP842/assets/39792005/59aeb48c-3bcf-4a23-834e-ddab3de2c444">\
> Figure: A state diagram for a distributed blockchain showing the hashing competition for the process of generating new blocks and updating the chain.

The process of all nodes agreeing is consensus, and the process of proposing updates is accomplished by mining, to be discussed in more detail next lecture. The algorithms for consensus must still be fault-tolerant, just like centralized systems, but they must also be resilient against malicious, or *Byzantine* adversaries.

### Byzantine Generals Problem

The *Byzantine Generals Problem*, is a famous computer science communication problem. Imagine three generals of the same army, all wanting to attack an enemy fortress at dawn the next morning. Each general knows their individual divisions cannot win the enemy fortress. Each general also knows that with the help of the other's forces they can win the position. So General *Alpha* sends a messenger to General *Beta* with the message "We attack at dawn." This is where the problems start. There are many scenarios that could play out. The messenger could be captured by the enemy; the messenger could be a double-agent; the messenger could get lost and not deliver the message; General Beta could double-cross Alpha, etc. To win the battle, the three generals must come to consensus and agree to attack at dawn. Practically speaking, each general must receive confirmation from each of the other generals that they received the message *and* are in agreement. This scenario maps nicely onto cryptography and message passing.

A decentralized blockchain application has many nodes in the network and each of them has a copy of the blockchain. If Bob wants to send Alice his tokens, the nodes in the network must first agree that Bob has available tokens to spend, and then update the state before Bob can double-spend his tokens. The network needs to be in a state of *consensus* for people to trust it. Consensus in the Byzantine Generals problem has been proven to be impossible if more than a third of the nodes are malicious~[Fischer1985].

Bitcoin does not exactly mirror the model of the Byzantine Generals and so is not impossible to reach consensus. In other words, bitcoin does achieve consensus despite Byzantine behaviour. More practically, bitcoin achieves a state of *emergent* consensus. This means that over time as blocks get added to the chain, a general state emerges that everyone agrees on. 

So how does this occur without clear rules? A closer look at the double-spend attack will illustrate how nodes come to agreement.


### The Double-Spend Attack
Solving the situation known as the *double spend problem*, is the final piece of the puzzle that was put in place for trustless decentralized digital cash to succeed. 

A dodgy actor, Eve, could manipulate the blockchain by sending some coins to Jeff and receiving a good or service. Then she could send those same coins to Bob's address whom she also controls. If the transaction involving Bob's address is validated on the blockchain, then Eve would have successfully double-spent the same coins. She now has the coins in Bob's address and the goods from the transaction with Jeff.

> <img width="800" alt="Double Spend Success" src="https://github.com/millecodex/COMP842/assets/39792005/3c5e1fdc-7521-4a0f-9b99-66e4f3d123b6">\
> Figure: For Eve to successfully double-spend in the blockchain she must take advantage of a fork in the chain. If the chain with the Eve to Bob transaction is the longest, representing the most cumulative proof of computation effort, she has double-spent.

How can Jeff avoid this scenario, especially when he does not know the other party he is transacting with? The solution is to wait. Over time as more blocks are added, say every ten minutes, the older blocks are more likely to be valid.[^1] Stated another way, as more blocks are added to the chain there is an exponential decrease in the probability of a block being rejected by other nodes. This is the method that secures the blockchain against malicious nodes attempting to double spend. 

> <img width="800" alt="Double Spend Solution" src="https://github.com/millecodex/COMP842/assets/39792005/2adf3b0c-9a8b-4b52-9353-60931659393d">\
> Figure: Jeff has waited to accept Eve's transaction. After six confirmations it is very unlikely that Eve's alternate chain will accepted as valid. Over time there is increasing probability that transactions are secure.

And what about Eve changing history? She would have to alter the block where the transaction is stored, as well as any subsequent blocks. The older the block is, the more computational effort is required because the hash pointers are linked. Consider that Eve is also competing against other nodes in the network that are honest. (We will return to the case of dishonest nodes when discussing a 51% attack.) 



[^1]: Standard confirmation time for bitcoin is six blocks, or one hour. The number of blocks to wait until considering a transaction to be confirmed is a personal preference.





## Mining/nodes
So, PoW is called mining because of the non-redeemable effort that goes into finding new new coins. Every ten minumtes on average a new block is  mined and with it the miner can redeem the block reward → freshly minted bitcoins.

## 51% attack
text here

## Selfish mining
text here

## Difficulty Adjustment
text here

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


