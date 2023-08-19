[↰ back](../../..)

# Lecture 6: Wallets and Tokens
## Contents
1. [Wallets](#wallets)
2. [Seed Phrases](#seed-phrases)
3. [Multisig](#multisig)
4. [Multi-Party Computation](#multi-party-computation)
5. [Token standards](#token-standards)
6. [NFTs](#nfts)
7. [UTXO Model](#utxo-model)
8. [What did we miss?](#what-did-we-miss)
9. [Further Reading - the very short list](#further-reading---the-very-short-list)
10. [Exercises](#exercises)


Contrary to popular belief, there is no standardized encryption in the Bitcoin protocol. As a decentralized system of exchange, there is no need for encryption. All the transactions are stored in the blockchain and accessible to everyone. Access to the private keys controlling addresses is maintained solely through personal security of the user. It is imperative that users keep their private keys secret, just as in any other cryptosystem. There are some added enhancements for encrypting passwords and wallets, but these are third-party additions and not built into the protocol.



## Wallets
The term wallet is both a good name and a bad name to describe its purpose in the cryptocurrency lexicon. It's bad because there are no coins to store in a wallet, only keys that can sign transactions. Also, if you lose your wallet, it does not mean your crypto tokens can be used by whoever finds it. It is a good term because it fits into the metaphor of using a wallet to access the financial system similar to accessing credit card networks with a VISA card, trade with your neighbour using cash, and coffee via stamped vouchers.

Wallets have evolved past the point of storing randomly generated private keys and now use a master seed through which multiple child keys can be derived. HD, or hierarchical deterministic wallets do not need access to the private key to be able to spawn children. The child keys can then be used to generate grand-child keys, and so forth allowing multiple transactions to use different public addresses all derived from the same private key. This increases security because you can delete the private key from the device as long as you have a backup method to recreate it. Using common words as a seed phrase to derive a key is easier to backup than a sequence of characters.

The user experience for blockchain applications is an area for improvement. As an example, *Mycellium* has been in wallet development since 2009, switching their focus from secure hardware after bitcoin was released. From the figure below you get the sense that setting up a wallet and sending coins is not user-friendly.

> <img width="800" alt="The Mycelium bitcoin wallet interface." src="https://github.com/millecodex/COMP842/assets/39792005/7f6ef20d-451d-4ccc-8821-52204777631d">\
> The Mycelium bitcoin wallet interface (2019). The home screen (left); Adding a new account (middle); Sending a transaction (right).

## Seed Phrases
After selecting *backup now*, two warning messages are displayed and then a word list which you must write down (screenshots and copy/paste are disabled). The word list for this account is:

|   |   |   |
|---|---|---|
| 1. envelope | 2. motor | 3. heart |
| 4. circle   | 5. apple | 6. essay |
| 7. close    | 8. ranch | 9. powder |
| 10. cause   | 11. royal | 12. brass |
> Table: a backup seed phrase maps common words (in this case English) to bytes.

The list must be verified by the user after being displayed in the app. In the case of losing your device, the seed phrase can be used to import the wallet. Screenshots from Trustwallet, show a different approach. The home screen is much less cluttered and appears more like what you would expect from a wallet app. 

> <img width="800" alt="Screenshots from Trustwallet showing the recovery phrase" src="https://github.com/millecodex/COMP842/assets/39792005/8e708174-23a2-4ca3-8264-daac159180c6">\
> Figure: Screenshots from Trustwallet showing the recovery phrase. 

Trustwallet will let you export the 12-word seed phrase but will not let you dump your private keys to the screen as an added security measure[^1]. The Mycelium private key of the seed phrase is shown in Figure below.

[^1]: Using both Mycelium and Enjin wallets for Android, I could not screen-capture or share the screen with my PC.

> <img width="250" alt="The Mycelium bitcoin wallet interface." src="https://github.com/millecodex/COMP842/assets/39792005/efcb1db3-c720-4fc2-86c2-83f32696eac2">\
> Figure: Mycelium private key of the seed phrase shown above. Note the warning message: "whoever knows this code can spend all your current and future bitcion from this account."

### Key Storage
Storage of cryptocurrency is similar to storage of your online banking details. There are no actual coins or crypto-assets to keep safe; there is no `<bitcoin object>` to keep password protected. Remember, the blockchain is an open ledger of every transaction in the network. Bitcoin is cryptographically secured, and if you have the private keys to an address, then you control the funds that address references in the blockchain.

A Bitcoin address is the public key of a public-private key pair generated by a 256-bit elliptic curve function. The public key is encoded in base-58 to reduce errors in transcription by removing similar characters like `0`, `O`, `1`, and `l`.

Cryptocurrencies are riskier than traditional online banking because if you lose your private keys, they are not recoverable. There is no password reset or government-issued ID verification to recover your account.

There are a number of ways to store your keys:

- **Hot Wallet**: This is the most common method. It is a software application that stores your private keys so you can sign transactions, keeps track of your tokens, and may offer additional functionality like multiple addresses or multiple token support. The risk here is that if you lose your device, your private keys are gone with it. Day-to-day transactions using a smartphone would be done through a hot wallet.

- **Cold Storage**: For larger amounts, savings, investments, and custodial services, a cold or hardware wallet is recommended. This is a device that is not powered and has no connectivity and stores your private keys internally. When tokens are required, it can be plugged into a USB and connected to the network.

- **Paper Wallet**: Once a key pair has been generated and used to receive tokens, that private key will always have ownership of the tokens. The private key can be printed out or written down, sometimes as a QR code for easy scanning. After the memory has been cleared, there is no more digital record of the private keys.

- **Brain Wallet**: The most serious storage system is to remember your private keys and destroy all physical and digital evidence of them. Certain memory mnemonics and the use of common words as seed phrases can help with this.

It's important to note that for all these methods, including memorization, it is possible to receive tokens to your address without connecting the keys to the network. These transactions will be recorded by all the nodes running the blockchain and propagated accordingly. Private keys are only required to sign transactions (spend tokens). All of these methods are vulnerable to crises such as fire or theft and represent a single point of failure. Backing up your keys can solve the crisis issues, but someone could still steal the backup.



## Multisig
Multisignature (multisig) refers to the requirement of multiple private keys to authorise a cryptocurrency transaction. It's akin to a digital lock that needs multiple keys to be opened. Initially developed to enhance the security of Bitcoin[^multisig] transactions, multisig is now a well known key application. Imagine two out of three business owners needing to sign with their private keys to disburse funding, or a family that requires agreement among siblings and their lawyer to settle an estate, or a governance structure that needs majority voting to fund a proposal. A multiple-signature transaction requires more than one authorizing key. Sometimes referred to as an $M$ of $N$ system, if a minimum of $M$ private keys sign a transaction out of $N$ possible signatories, then the transaction can proceed.  

[^multisig]: *Multisig* is a useful feature in bitcoin although includes a bug requiring an extra item to be added to the script stack before execution. Although technically easy to fix, the bug has always been included in the reference implementation and is now a part of the consensus rules. At this stage it is considered too risky to fix because of unknown downstream effects. Antonopoulos (2017) details multisig transactions and the more advanced *pay-to-script-hash* functionality.

To enhance personal security you can arrange your funds in a 2 of 3 multisig (or more!) with private keys stored on different devices. This way, if one gets compromised, you can use the other two to move the funds. This additional layer provides enhanced protection against malware and phishing as the compromised device can't move your coins without at least one other signature.

Here's a pseudocode algorithm to create a multisig address:
```js
// Define Parameters
M = 2 // Minimum number of required signatures
N = 3 // Total number of possible signatures
publicKeys = [PublicKey1, PublicKey2, PublicKey3] 

// Create the Redeem Script
redeemScript = concatenate(M, publicKeys[0], publicKeys[1], publicKeys[2], N, "OP_CHECKMULTISIG")

// Compile Redeem Script to Bytecode (implementation varies based on the specific language and environment)
bytecode = compileToBytecode(redeemScript)

// Hash the Redeem Script to create a P2SH address
p2shHash = SHA256(RIPEMD160(bytecode))

// Add Network Information and Checksum, then encode into Base58Check for the final P2SH address
p2shAddress = Base58CheckEncode(p2shHash, networkPrefix, checksum)

// The P2SH address is now ready for use in transactions
```

Logically extending $M$ of $N$ signatures leads to transactions that can execute a small amount of instructions. Transactions are just data that is stored by all the nodes in the network, and there is no reason why this data could not be code -> *Smart Contracts*?

### Secret Sharing
In the scenario where someone eventually steals our private keys, secret sharing can provide an additional layer of security. The idea behind secret sharing is to split the key into multiple parts, or shares, such that a certain number of shares are required to reconstruct the key.

Let's consider a simple example with 2 shares ($N=2$) and a threshold of 2 shares ($K=2$). Suppose the secret $S$ is a 128-bit number, and we generate a random 128-bit number $R$. One share can be $R$, and the other share can be $S \oplus R$ (bitwise XOR). With only one share, $R$ is random and provides no information about $S$. The share $S \oplus R$ depends on knowing $R$, so it also provides no information about $S$. However, when both shares are combined, $R$ cancels out and the original secret $S$ can be reconstructed. This concept is similar to encrypting the secret with a one-time pad cipher where $R$ is the key.

Now, let's consider the case where we split the secret into four shares and require any two shares to reconstruct the secret. We can use some linear algebra to achieve this. We can think of the shares as points on a line. Any two points can construct a line, but if we introduce a third random point, it is unlikely to be collinear with the first two points. By generating $N$ shares along this line, any two of these shares can reconstruct the line and determine the $x$-intercept, which is the original secret $S$. However, any single share is useless because the slope of the line is unknown.

This approach of secret sharing provides a way to distribute the shares among trustworthy individuals. Even if one or more shares are compromised, they provide no useful information about the secret without the required threshold number of shares to reconstruct it.

> <img width="461" alt="image" src="https://github.com/millecodex/COMP842/assets/39792005/840adfd1-f4ee-40cc-9286-fbb0b0af1b45">\
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

## Multi-Party Computation
**The Millionaire's Problem** is a classic problem in the field of cryptography, specifically in the context of Multi-Party Computation (MPC). It was introduced by Andrew Yao (1986), and it forms the basis for understanding how privacy can be preserved during computation. Two millionaires, Alice and Bob, want to compare their wealth to find out who is richer without revealing the actual amount of their wealth to each other or anyone else. They want to know the result of the comparison but are unwilling to disclose any additional information.

The Millionaire's Problem can be seen as a special case of secure multi-party computation, where two parties wish to jointly compute a function over their inputs (in this case, a comparison function) while keeping those inputs private. Here, the answer is Max(Alice's Salary, Bob's Salary). An MPC protocol will take the private information (salaries), compute the function (max) and relay the information (Alice) without revealling the private info (salary). Also, the protocol is just that, a protocol, and not a trusted third party.

Multi-Party Computation (MPC) wallets are an innovation in cryptocurrency storage that leverages cryptographic protocols to securely distribute private keys among multiple parties. This distribution ensures that no single entity has control, enhancing security, and removing single points of failure.

Distinguishing MPC wallets from regular ones like single-key, multi-signature, or hardware wallets, MPC wallets are more secure, protocol-agnostic, and less cumbersome in authorization. They also overcome issues like damage to physical devices or the loss of private keys.

Benefits of MPC Wallets include:
* Decentralization: Elimination of trusted third parties for storing private keys.
* Data Privacy: No revealing of private information to other parties.
* Removal of Single Points of Failure: Distributing private keys among multiple parties.
* Scalability: Flexibility in adding or removing parties.

Risks of MPC Wallets include:
* High Communication Costs: Extensive communication can increase network latency and expose to attacks.
* Technical Complexity: Advanced cryptographic techniques might lead to vulnerabilities.
* Lack of Interoperability: Incompatibility with conventional wallets due to non-standardization.

Some popular MPC wallets are ZenGo, Fireblocks, Coinbase, and Qredo, each catering to different types of users with varying features and security levels.

## Token standards
Lorem ipsum dolor sit amet, consectetur adipiscing elit.

## NFTs
Lorem ipsum dolor sit amet, consectetur adipiscing elit.

## UTXO Model
Lorem ipsum dolor sit amet, consectetur adipiscing elit.

## What did we miss?
* i
* ii
* iii 

## Further Reading - the very short list
* Andrew Yao's Protocol for Secure Computations [pdf](https://github.com/millecodex/COMP842/blob/master/papers/yao1982-ocr.pdf)
* B
* C

## Exercises
1. a
2. b
3. c
