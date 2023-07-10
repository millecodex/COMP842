[↰ back](../../..)

# Lecture 9: Security
## Contents
1. [Protocol Level Security](#protocol-level-security)
1. [Personal Security](#personal-security)
1. [Community Level Security](#community-level-security)
1. [](#)
1. [](#)
8. [What did we miss?](#what-did-we-miss)
9. [Further Reading - the very short list](#further-reading---the-very-short-list)
10. [Exercises](#exercises)

Divided into three pillars, security of a blockchain involves being prepared for many different attacks at the personal, community, and protocol levels. This list is not exhaustive and only represents some of the obvious security considerations that must be made when evaluating blockchains.

| Attacks          |                           |                          |                          | Security Considerations               |                          |                                                     |
|------------------------|-----------------------|----------------------|-----------------------|-----------------------------------|----------------------|-------------------------------------------------|
| Protocol Level                   |                           |                          |                          | Personal                                      |                          | Community                                    |
| DoS                           |                           |                          |                          | Keys                                          |                          | Developer Community                    |
| Sybil                         |                           |                          |                          | Multisig                                     |                          | Mining Community                          |
| Double Spend              |                           |                          |                          | Wallets                                        |                          | Smart Contracts                             |
| \textbf{PoW}                |                           | \textbf{PoS}          |                          |                                                   |                          | Exchanges                                          |
| 51\%                             |                           | Nothing at Stake   |                          |                                                   |                          | Scams                                               |
| Selfish Mining             |                           | Short Range           |                          |                                                   |                          |                                                     |
|                                     |                           | Long Range           |                          |                                                   |                          |                                                     |
|                                     |                           | Grinding                |                          |                                                   |                          |                                                     |

## Protocol Level Security

Denial of Service (DoS) and Sybil attacks are common to all networking systems. The consensus protocol itself handles these attacks by making it prohibitively expensive for an attacker to spam the network and create multiple identities. Spamming results in an immediate loss of funds through fees or resources spent such as electricity. In a PoW chain, multiple identities require splitting one's computing power and receiving proportionally less reward per identity. Similarly, a proof of stake proportion of tokens must be divvied up between Sybils.

A double spend attack, as previously discussed, must also be accounted for in some way. Some of the following attacks can result in double-spending if successful.

### 51% Attack

Should a single entity gain control of more than half of the hash power in the network, this could lead to a 51% attack (Nakamoto, 2008). The attacker can't steal coins directly as this involves subverting elliptic curve cryptography. The attacker can, however, use their majority status in some interesting ways. At >50%, they have the ability to find more blocks and direct the consensus of the blockchain. The attacker can censor transactions by refusing to add blocks containing someone's address. This would be akin to blacklisting certain addresses but does not completely exclude them from being included in blocks mined by honest nodes (the 49%). As the proportion in control increases, it will be harder to get a blacklisted transaction published on the blockchain. With this majority, the attacker will now earn a larger proportion of block rewards but still have to find SHA256 hashes like everyone else.

It is tempting at this point to ask: Can I change the block reward and earn more per block found? This will be rejected by the network because the block reward is hard-coded and so the malicious extra-reward transaction can never be spent. In a distributed system, everyone has a version of the consensus rules that must agree with everyone else. A different block reward would have to be done as a software upgrade and falls under Community Level Security.

### Selfish Mining

An adversary doesn't necessarily need 51% of the hash power, but with a large number of nodes in the network, they could gain an advantage. An interesting analysis was published in 2014[^eyal] by Eyal and Sirer that showed a conglomerate of miners could form with as little as one-third of the hash power. This mining cartel can continuously mine without broadcasting their blocks until some set time in the future. In the short term, the miner is sacrificing the immediate block reward by not propagating their found blocks to neighboring nodes. In the long run, however, the result is that the honest miners are doing work that is not in competition with the selfish miners, increasing the attacker's expected rewards. The results of Eyal and Sirer's study conclude a group can increase their mining payout with as little as 1/3 of the network's hash power.

[^eyal]: Eyal, I., & Sirer, E. G. (2014). Majority is not enough: Bitcoin mining is vulnerable.

### Nothing at Stake

Given a fork in a proof of stake system, the user is incentivized to build on every branch. In a proof of work system, the user has a finite amount of hashpower that is most profitable if used to build on the main chain. This constraint is gone in a pure proof of stake system as the user can bid for blocks on any and all branches. The probability of finding a block remains constant. Here, the blockchain may never reach consensus as everyone is scrambling to build blocks rather than maintain the longest chain (BitFury, 2015).

A simple solution is to penalize someone who publishes blocks on multiple branches. This is known as slashing and acts as a disincentive to build on non-consensus chains (Buterin, 2017).

### Short and Long Range Attacks

A Long Range attack involves rebuilding a blockchain from scratch with the intention of overtaking main-chain consensus. A user with enough computational power could accomplish this easier than the same attack on a proof of work chain. To prevent an attacker from building a long competing chain, milestones can be reached along the way that act as finality checkpoints. Going back in time before a checkpoint is not possible as any other branches, including the potential attack, would be pruned. Ethereum 2.0 (Serenity) uses validator nodes that vote on checkpoint blocks within an epoch.

In the short term, an attacker can attempt a double-spend by incentivizing participants to build on an orphaned chain as soon as a malicious transaction is broadcast. This is done secretly. If the alternate chain succeeds in overtaking the main chain, the double spend was successful. Basically, miners can be bribed to compete on the alternate chain, and this will be profitable up to the value of the double spend. Similar to the Nothing at Stake problem, a short-range attacker is penalized by slashing or revocation of validation privileges (Deirmentzoglou et al., 2019).

### Grinding

In a grinding attack, the attacker increases their probability of being selected for block minting. For example, a validator could iterate through many combinations of block parameters searching for a favorable one to get published. Given enough computing power, the attacker could always "find" a suitable block (Kiayias et al., 2019). A general mitigation measure for this is to use a source of randomness that cannot be known in advance, like a random function that uses seeds from a group of validators. Of course, the validators could work together and collude. Workarounds for this can be found in Ethereum's Proof of Stake FAQ.

## Personal Security
### Cryptographic Keys

As mentioned in the lecture on [Wallets & Tokens]() Contrary to popular belief, there is no standardized encryption in the Bitcoin protocol. As a decentralized system of exchange, there is no need for encryption. All the transactions are stored in the blockchain and accessible to everyone. Access to the private keys controlling addresses is maintained solely through personal security of the user. It is imperative that users keep their private keys secret, just as in any other cryptosystem. There are some added enhancements for encrypting passwords and wallets, but these are third-party additions and not built into the protocol.

### Key Storage
Storage of cryptocurrency is similar to storage of your online banking details. There are no actual coins or crypto-assets to keep safe; there is no `<bitcoin object>` to keep password protected. Remember, the blockchain is an open ledger of every transaction in the network. Bitcoin is cryptographically secured, and if you have the private keys to an address, then you control the funds that address references in the blockchain.

Cryptocurrencies are riskier than traditional online banking because if you lose your private keys, they are not recoverable. There is no password reset or government-issued ID verification to recover your account.

There are a number of ways to store your keys such as hot wallets, cold storage, it's important to note that for all these methods, including memorization, they are vulnerable to crises such as fire or theft and represent a single point of failure. Backing up your keys can solve the crisis issues, but someone could still steal the backup.



# Community Level Security
## Developer & Mining Communities
The main practical threat to a single entity controlling the majority of the hashpower is that it will lead to centralization and cause users to abandon the system altogether. Once hashpower gets close to this threshold it is also possible that developers will step in and update the software to limit this behaviour. It is unknown how this will play out in the future. Thus far the bitcoin network has been relatively decentralized, but a few mega mining pools have emerged. There have been some cases of 51% attacks on alternative cryptocurrencies such as Verge, Horizen, and Vertcoin. Smaller cryptocurrencies are more vulnerable to a large mining pool shifting their resources for this purpose.

## Smart Contracts
A list of known smart contract attacks is maintained at [here](https://consensys.github.io/smart-contract-best-practices/known_attacks/). We will discuss smart contracts in more detail in a future lecture.

## Exchanges & Scams
The list of hacks and breaches of cryptocurrency exchanges is long and colorful. A sampling can be found [here](https://www.saturn.network/blog/list-of-documented-exchange-hacks/) and includes a New Zealand (Christchurch based) company _Cryptopia_.

Outright scams are also prominent as Bitcoin becomes popular and increases in value, many 'alternatives' make the rounds promising massive gains and better features. The OneCoin scam was recently popularized in the excellent BBC podcast series _The Missing Queen_ by Jamie Bartlett. Episodes available [here](https://www.bbc.co.uk/programmes/p07nkd84/episodes/downloads).



## What did we miss?
* i
* ii
* iii 

## Further Reading - the very short list
* a
* B
* C

## Exercises
1. a
2. b
3. c
