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

Contrary to popular belief, there is no standardized encryption in the Bitcoin protocol. As a decentralized system of exchange, there is no need for encryption. All the transactions are stored in the blockchain and accessible to everyone. Access to the private keys controlling addresses is maintained solely through personal security of the user. It is imperative that users keep their private keys secret, just as in any other cryptosystem. There are some added enhancements for encrypting passwords and wallets, but these are third-party additions and not built into the protocol.

### Key Storage

Storage of cryptocurrency is similar to storage of your online banking details. There are no actual coins or crypto-assets to keep safe; there is no `<bitcoin object>` to keep password protected. Remember, the blockchain is an open ledger of every transaction in the network. Bitcoin is cryptographically secured, and if you have the private keys to an address, then you control the funds that address references in the blockchain.

A Bitcoin address is the public key of a public-private key pair generated by a 256-bit elliptic curve function. The public key is encoded in base-58 to reduce errors in transcription by removing similar characters like `0`, `O`, `1`, and `l`.

Cryptocurrencies are riskier than traditional online banking because if you lose your private keys, they are not recoverable. There is no password reset or government-issued ID verification to recover your account.

There are a number of ways to store your keys:

- Hot Wallet: This is the most common method. It is a software application that stores your private keys so you can sign transactions, keeps track of your tokens, and may offer additional functionality like multiple addresses or multiple token support. The risk here is that if you lose your device, your private keys are gone with it. Day-to-day transactions using a smartphone would be done through a hot wallet.

- Cold Storage: For larger amounts, savings, investments, and custodial services, a cold or hardware wallet is recommended. This is a device that is not powered and has no connectivity and stores your private keys internally. When tokens are required, it can be plugged into a USB and connected to the network.

- Paper Wallet: Once a key pair has been generated and used to receive tokens, that private key will always have ownership of the tokens. The private key can be printed out or written down, sometimes as a QR code for easy scanning. After the memory has been cleared, there is no more digital record of the private keys.

- Brain Wallet: The most serious storage system is to remember your private keys and destroy all physical and digital evidence of them. Certain memory mnemonics and the use of common words as seed phrases can help with this.

It's important to note that for all these methods, including memorization, it is possible to receive tokens to your address without connecting the keys to the network. These transactions will be recorded by all the nodes running the blockchain and propagated accordingly. Private keys are only required to sign transactions (spend tokens). All of these methods are vulnerable to crises such as fire or theft and represent a single point of failure. Backing up your keys can solve the crisis issues, but someone could still steal the backup.

### Secret Sharing
In the scenario where someone eventually steals our private keys, secret sharing can provide an additional layer of security. The idea behind secret sharing is to split the key into multiple parts, or shares, such that a certain number of shares are required to reconstruct the key.

Let's consider a simple example with 2 shares ($N=2$) and a threshold of 2 shares ($K=2$). Suppose the secret $S$ is a 128-bit number, and we generate a random 128-bit number $R$. One share can be $R$, and the other share can be $S \oplus R$ (bitwise XOR). With only one share, $R$ is random and provides no information about $S$. The share $S \oplus R$ depends on knowing $R$, so it also provides no information about $S$. However, when both shares are combined, $R$ cancels out and the original secret $S$ can be reconstructed. This concept is similar to encrypting the secret with a one-time pad cipher where $R$ is the key.

Now, let's consider the case where we split the secret into four shares and require any two shares to reconstruct the secret. We can use some linear algebra to achieve this. We can think of the shares as points on a line. Any two points can construct a line, but if we introduce a third random point, it is unlikely to be collinear with the first two points. By generating $N$ shares along this line, any two of these shares can reconstruct the line and determine the $x$-intercept, which is the original secret $S$. However, any single share is useless because the slope of the line is unknown.

This approach of secret sharing provides a way to distribute the shares among trustworthy individuals. Even if one or more shares are compromised, they provide no useful information about the secret without the required threshold number of shares to reconstruct it.

> <img width="461" alt="image" src="https://github.com/millecodex/COMP842/assets/39792005/840adfd1-f4ee-40cc-9286-fbb0b0af1b45">
> Figure: The point $(0,S)$ represents the secret, a large random number less than a large prime, $P$. The shares are linear combinations modulo $P$, up to $N$, where any 2 of them will recover the secret.

$$
\begin{align}
x=0,\quad y&=S\\
x=1,\quad y&=(S+R)\mod P\\
x=2,\quad y&=(S+2R)\mod P\\
x=3,\quad y&=(S+3R)\mod P\\
\vdots\\
x=N,\quad y&=(S+NR)\mod P\\
\end{align}
$$

What if you require more than 2 shares necessary to reconstruct the key? If we increase the degree of our share-reconstruction function from linear to parabolic, then we have $K=3$ is necessary to find $S$ because 3 points can uniquely define a parabola. This can be continued up to $K=N-1$ shares. Since multiple people can store portions of an individuals private key it would be convenient if a similar setup was in place for specific transactions or sets of transactions.

### Multisig
Imagine two out of three business owners needing to sign with their private keys to disburse funding, or a family that requires agreement among siblings and their lawyer to settle an estate. A multiple signature transaction requires more than one authorizing key. Sometimes referred to as an $M$ of $N$ system, if a minimum of $M$ private keys sign a transaction out of $N$ possible signatories, then the transaction can proceed.  *Multisig* is a useful feature in bitcoin although includes a bug requiring an extra item to be added to the script stack before execution. Although technically easy to fix, the bug has always been included in the reference implementation and is now a part of the consensus rules. At this stage it is considered too risky to fix because of unknown downstream effects. Antonopoulos (2017) details multisig transactions and the more advanced *pay-to-script-hash* functionality.

Logically extending $M$ of $N$ signatures leads to transactions that can execute a small amount of instructions. Transactions are just data that is stored by all the nodes in the network, and there is no reason why this data could not be code -> *Smart Contracts*?

## Wallets
The term wallet is both a good name and a bad name to describe its purpose in the cryptocurrency lexicon. It's bad because there are no coins to store in a wallet, only keys that can sign transactions. Also, if you lose your wallet, it does not mean your crypto tokens can be used by whoever finds it. It is a good term because it fits into the metaphor of using a wallet to access the financial system similar to accessing credit card networks with a VISA card, trade with your neighbour using cash, and coffee via stamped vouchers.

Wallets have evolved past the point of storing randomly generated private keys and now use a master seed through which multiple child keys can be derived. HD, or hierarchical deterministic wallets do not need access to the private key to be able to spawn children. The child keys can then be used to generate grand-child keys, and so forth allowing multiple transactions to use different public addresses all derived from the same private key. This increases security because you can delete the private key from the device as long as you have a backup method to recreate it. Using common words as a seed phrase to derive a key is easier to backup than a sequence of characters.

The user experience for blockchain applications is an area for improvement. As an example, *Mycellium* has been in wallet development since 2009, switching their focus from secure hardware after bitcoin was released. From the figure below you get the sense that setting up a wallet and sending coins is not user-friendly.

> <img width="800" alt="The Mycelium bitcoin wallet interface." src="https://github.com/millecodex/COMP842/assets/39792005/7f6ef20d-451d-4ccc-8821-52204777631d">
> The Mycelium bitcoin wallet interface. The home screen (left); Adding a new account (middle); Sending a transaction (right).

After selecting *backup now*, two warning messages are displayed and then a word list which you must write down (screenshots and copy/paste are disabled). The word list for this account is:

|   |   |   |
|---|---|---|
| 1. envelope | 2. motor | 3. heart |
| 4. circle   | 5. apple | 6. essay |
| 7. close    | 8. ranch | 9. powder |
| 10. cause   | 11. royal | 12. brass |
> Table: a backup seed phrase maps common words (in this case English) to bytes.

The list must be verified by the user after being displayed in the app. In the case of losing your device, the seed phrase can be used to import the wallet. 

Screenshots from Enjin's wallet, which has concentrated on the user experience, show a different approach. The Enjin home screen is much less cluttered and appears more like what you would expect from a wallet app. Enjin will let you export the 12-word seed phrase but will not let you dump your private keys to the screen as an added security measure[^1]. The Mycelium private key of the seed phrase is shown in Figure below.

[^1]: Using both Mycelium and Enjin wallets for Android, I could not screen capture or share the screen with my PC.

> <img width="250" alt="The Mycelium bitcoin wallet interface." src="https://github.com/millecodex/COMP842/assets/39792005/efcb1db3-c720-4fc2-86c2-83f32696eac2">
> Figure: Mycelium private key of the seed phrase shown above. Note the warning message: "whoever knows this code can spend all your current and future bitcion from this account."

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
