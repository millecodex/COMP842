[↰ back](../../..)

# Lecture 7: Ethereum
## Contents
1. [Motivation](#first-some-brief-history)
2. [Smart Contracts](#smart-contracts)
3. [dApps](#dapps)
4. [Ethereum Virtual Machine](#evm)
5. [Consensus](#consensus)
7. [Characteristics and Quirks](#characteristics-and-quirks)
8. [What did we miss?](#what-did-we-miss)
9. [Further Reading - the very short list](#further-reading---the-very-short-list)
10. [Exercises](#exercises)

## First, some brief History
### What was the problem(s) that Vitalik Buterin was looking to solve?
Bitcoin provided a solution to the double-spend problem of creating digital cash by using proof-of-work mining to both maintain the state of the ledger and allow open participation in the network based on computing power. By assigning value to these digitally scarce coins the ledger can be used as a monetary system. This works great for money but comes up short when using Bitcoin's scripting language to make simple extensions such as a decentralized exchange -- how to determine the NZD/BTC rate? or how to do some arbitrary calculation, e.g. what is the probability that your game character encounters a villan?

In late 2013, While writing for *Bitcoin Weekly* and co-founding [*Bitcoin Magazine*](https://bitcoinmagazine.com/),  a nineteen-year-old Russian-Canadian computer science dropout, Vitalik saw the limitations in Bitcoin as an opportunity to create a new blockchain from scratch that can allow developers to build general applications. The first feature to include in this new blockchain was *Turing completness*. In computer programming this means it is possible to have loops in the code which would be necessary, for example, for calculating a probability or the value of π. Bicoin's *script* language is not considered Turing complete because it is stack-based and therefore anything that is needed by the program must be loaded onto the stack. (Also, by definition stacks cannot loop.) If you want to do something that isn't already available in the opcodes, then some very creative ad-hoc programming and second-layer work may be required. Turing-complete refers to a class of computers (programming languages) that can simulate another computer. Named after computer scientist Alan Turing[^Turing], a more practical way of thinking of Turing-completeness is that the language has loops; structures that allow for computation. HTML is not Turing-complete as it cannot calculate digits of π, whereas most programming languages are. Bitcoin's scripting language is not Turing-complete.

[^Turing]: The same namesake as the Turing test in which an artificial intelligence can convince a human they are human. Or, in other words, the human cannot tell if the terminal is answering on behalf of a human or AI.

The second feature was to use an account-based system. The benefit of this style is that each account (address) has a balance *and* the option of some code and storage. (This is in contrast to Bitcoin that uses a UTXO model that only keeps track of coins and not any additional data or code.)

The whitepaper for *Ethereum* was published online in 2013 and a year later a formal specification was written by Gavin Wood and the project raised funds through their initial coin offering. This was followed by the network launch in 2015.

Summarizing Ethereum from the whitepaper[^Buterin2014]:
> [Ethereum] is essentially the ultimate abstract foundational layer: a blockchain with a built-in Turing-complete programming language, allowing anyone to write smart contracts and decentralized applications where they can create their own arbitrary rules for ownership, transaction formats, and state transition functions.

[^Buterin2014]: Buterin, V. (2014). Ethereum: A next-generation smart contract and decentralized application platform.



## Initial Coin Offering
In order to fund their new proposed blockchain network, the founders embarked on a unique [fundraising scheme](https://blog.ethereum.org/2014/07/22/launching-the-ether-sale/) that laid down the template for future crowdfunding sales. An initial coin offering (ICO) seeks to bootstrap user adoption and funding by combining the style of an initial public offering (IPO) with a crowd fund model. A marked difference from the IPO model is that the token sale was open to anyone without geographic or regulatory restriction. All users had to do to participate was deposit bitcoin and receive *ether* tokens that represent their stake in the new network. The token sale was successful resulting in more than 50 million ether (the native currency of ethereum) being sold. Investors were aware of the token distribution from the beginning which included 9.9% of the tokens reserved for the founders (to fund development, salaries, bug bounties, etc.) and another 9.9% for a [foundation](https://ethereum.foundation/) that was set up to guide the long term mission of the network. These tokens didn't have to be purchased in a traditional sense; a practice now known as *pre-mining*.

### ICO Boom Times
The success of Ethereum's ICO and its smart contract capability combined with its open source code made it an ideal model for other founders to fund their projects. A new project could easily copy and modify smart contract code and host their own ICO and issue their own new ERC-20 tokens. (ERC-20 refers to the token standard that most coins that run on Ethereum use.) 2017--2018 was a boom period for ICOs with many projects and tokens launching. Unfortunately many of them had questionable products and practices or were outright scams and because there was no regulation in crypto (as there is for an IPO), there was no recourse for those that invested and lost their money. 

## Smart Contracts
The term *smart contract* refers to some executable code that lives on the blockchain. This code may be a snippet, small or large, it may be straightforward or complex, it may contain bugs, not compile, it may never even be executed. Ethereum allows for code to be stored on the blockchain in *contracts* which have a callable address that looks just like a user's address. All of these bits of code are generically called smart contracts. Pedants will like to tell you that they are not smart nor are they contractual and they might be right in a traditional sense, however, the term has come to be redefined in a blockchain context.

Earlier we mentioned that Ethereum is turing-complete, and here is where that comes in. A developer can write a program, say to issue crop insurance based on weather data, and store this program in a smart contract on the blockchain. As the blockchain is immutable this code will live there forever, it is also visible and thus can be easily verified or audited. The only limits to the applications that can be deployed on Ethereum come from the creativity & skill of the developer, and the amount of computation that program needs to do. Solidity is the name of most common high-level language used to write code that compiles to bytecode to be executed on the Ethereum virtual machine. Created by the co-founder of Ethereum, Gavin Wood, Solidity was intended to resemble JavaScript and be recognizable to web developers.

**Example Contract 1**
Here is an example from *Mastering Ethereum* (Antonopoulos, 2019) to create a faucet which will give out ether[^2] to anyone that interacts with it.

```solidity
// Our first contract is a faucet!
contract Faucet {
    // Give out ether to anyone who asks
    function withdraw(uint withdraw_amount) public {
        
        // Limit withdrawal amount
        require(withdraw_amount <= 100000000000000000);
        
        // Send the amount to the address that requested it
        msg.sender.transfer(withdraw_amount);
    }
    // Accept any incoming amount
    function () public payable {}
}
```

[^2]: Ether (ETH) is the currency used on the Ethereum platform. Gas is the name for the fees that the network will charge to execute contracts, this is priced in very small amounts of ETH.

**Example Contract 2**
A more substantial example is taken from the [solidity documentation](https://solidity.readthedocs.io/en/v0.4.24/introduction-to-smart-contracts.html) and details some functions of a simple cryptocurrency:

```solidity
pragma solidity ^0.4.21;

contract Coin {
    // The keyword "public" makes those variables
    // readable from outside.
    address public minter;
    mapping (address => uint) public balances;

    // Events allow light clients to react on
    // changes efficiently.
    event Sent(address from, address to, uint amount);

    // This is the constructor whose code is
    // run only when the contract is created.
    function Coin() public {
        minter = msg.sender;
    }

    function mint(address receiver, uint amount) public {
        if (msg.sender != minter) return;
        balances[receiver] += amount;
    }

    function send(address receiver, uint amount) public {
        if (balances[msg.sender] < amount) return;
        balances[msg.sender] -= amount;
        balances[receiver] += amount;
        emit Sent(msg.sender, receiver, amount);
    }
}
```

**Example Contract 3**
The Ethereum DAO hack took place in 2016 when a hacker drained US $50 million from a [fundraising account](https://daohub.org/). Here is some logic from the attack:

```solidity
contract donateDAO {
    mapping (address => uint256) public credit;

    // add funds to the contract
    function donate(address to) payable {
        credit[msg.sender] += msg.value;
    }

    // show ether credited to address
    function assignedCredit(address) returns (uint) {
        return credit[msg.sender];
    }

    // withdrawal ether from contract
    function withdraw(uint amount) {
        if (credit[msg.sender] >= amount) {
            msg.sender.call.value(amount)();
            credit[msg.sender] -= amount;
        }
    }
}
```

The problem is in the `withdraw()` function. In line 17, `call.value()` sends funds, in this case to the sender, before updating the balance. Here, the hacker can request their funds back, and then a fallback function triggers a recursive call that keeps sending funds back without updating the balance[^Humiston2018].

[^Humiston2018]: Humiston, I. (2018). Attacks and Incidents. In Ethereum Smart Contract Development (pp. 81-94). Apress.

### Gas
Computation occurs in the EVM (Ethereum virtual machine) and we will be light on details, but because its a blockchain, all the nodes need to have a copy of the data and verify any updates. This includes running *all* smart contracts and doing *any* calculation. A scenario could arise, either accidentally or maliciously, to halt the network by deploying a contract with an infinite loop:
```
int i=1
while i>0
  i=i+1
 ```
The simple code above continually updates the counter because the stop condition of i being less than or equal to 0 is never met. To avoid this scenario all computation in the EVM needs gas. As a contract is executed gas is consumed and if the contract runs out of the gas then the update fails. All gas is paid in ether (`ETH`) and goes to the nodes (miners) that perform the calculations. A follow up question is what if I am wealthy and have enough gas to spam the network in this manner? To prevent this there is a gas limit on all transactions that is calculated based on how busy the network is.
> The recent *London* upgrade to Ethereum changed the way that gas is distributed. Previously the miner would be compensated by receiving the entire gas fee in the transaction. Now, part of this fee is *burned*, and the miner gets the remainder. Burning some ETH reduces the overall issuance. More in the section on Proof-of-Work.

## dapps
Decentralised applications, or *dapps* just refer to smart contracts that are executed on a blockchain. When combined with a frontend these dapps can appear just like any other web application with the key difference being that that code and/or user data is stored on the blockchain. 

The [most used dapps](https://dappradar.com/rankings/protocol/ethereum) on Ethereum in 2023 ranked by Unique active wallets (UaW):

| App            | Category                | UaW (k/30 days) |
|:-------------  |:-----                   |-------:|
| Uniswap        |  Decentralised Exchange |    495 |
| MetaMask Swap  |  Decentralised Exchange |    85 |
| OpenSea        |  NFT Marketplace        |    81 |
| Simple FX    |  Decentralised Finance |  80    |
| Ox Protocol |Decentralised Exchange| 62 |

This list is dominated by DEX activity, so if we [rank](https://dappradar.com/rankings/defi?range=24h) by total value locked (TVL)[^caution]:
| App            | Category                | TVL ($B) |
|:-------------  |:-----                   |-------:|
| Lido        |  Ethereum Staking |   13.8  |
| Summer.fi        |    Decentralised Finance | 6.1    |
| Maker DAO        |  Stablecoin |   4.9  |
| Uniswap        |  Decentralised Exchange | 3.2    |
| Aave        |  Decentralised Lending |   2.6  |

[^caution]: Take these stats with some salt, I haven't looked into dappradar's methodology, and they are only representative as of August, 2023. Generally over the past few years, Maker, Uniswap, Aave, Curve have been relatively stable and popular protocols. 

### Stablecoins
Although not listed in the chart above, stable-value currencies were originally categorized as applications that can run on Ethereum. Now called *stablecoins*, it is hard to ignore their growth and popularity when looking at total value. The idea behind them is that to avoid the volatility present in the crypto markets, rather than using `ETH` there is the option to use a crypto token pegged to a common currency like the $USD. If you convert some $NZD to Tether today, then you can rely on the value being relatively stable to use it in the future. Some of the stablecoins that exist on Ethereum are Tether `USDT`, `USDC`, and `DAI`. Both Tether and USDC are issued privately, whereas DAI is a *Decentralized Autonomous Organization* (DAO) and maintains a US dollar peg.

<p align="center"><img width="800" alt="total-stablecoin-supply-daily" src="https://user-images.githubusercontent.com/39792005/147860382-00470018-aae5-46a7-8d7f-023a2b163a4f.png"></p>

Chart from [TheBlock](https://www.theblockcrypto.com/data/decentralized-finance/stablecoins) showing growth in stablecoins over the past four years. The total value of stablecoins rose in 2021 from ~$28B to $150B. Note that this chart includes other blockchains, not just Ethereum.

## EVM
Virtual machines (VMs) in computer science are emulations of a computer system that provide the functionality of a physical computer, operating on the basis of a host system and creating a separate environment known as the guest system. The main purpose of a VM is to enable multiple operating systems to share the same physical hardware resources, promoting flexibility and isolation for applications such as testing and development. 

```bash
VBoxHeadless --startvm "My_VM"
VBoxManage createvm --name "my_blockchain_vm" --register
VBoxManage modifyvm "my_blockchain_vm" --memory 1024 --acpi on --boot1 dvd
VBoxManage createhd --filename "my_blockchain_vm.vdi" --size 10000
VBoxManage storagectl "my_blockchain_vm" --name "IDE Controller" --add ide
VBoxManage storageattach "my_blockchain_vm" --storagectl "IDE Controller" --port 0 --device 0 --type hdd --medium "my_blockchain_vm.vdi"
VBoxManage storageattach "my_blockchain_vm" --storagectl "IDE Controller" --port 0 --device 1 --type dvddrive --medium /path/to/iso
VBoxHeadless --startvm "my_blockchain_vm"
```
> Bash script to spin up a VM in linux: register, allocate memory, disc space, and point to the OS

This concept of emulation is shared with the **Ethereum Virtual Machine** (EVM), although they serve different purposes. While regular VMs simulate physical hardware, the EVM is a virtual runtime environment designed specifically for executing smart contracts on the Ethereum blockchain. The EVM operates independently of the underlying hardware, ensuring deterministic computation that yields the same result across all network nodes. Each full node runs a copy of the EVM to verify transactions and smart contract executions, playing a crucial role in the decentralisation and security of the Ethereum network. Both regular VMs and the EVM are vital in their respective fields, with regular VMs being crucial in areas like cloud computing and virtualisation technologies, and the EVM translating the principles of virtualisation to the specific domain of blockchain technology.

![image](https://github.com/millecodex/COMP842/assets/39792005/9c3de5ff-de3f-44e9-bbb7-6a80abf43e4d)
> Figure: Ethereum EVM shown in the inner box (execution cycle) determines the next state. Source: https://github.com/4c656554/BlockchainIllustrations/ 

Visit the [EVM playground](https://www.evm.codes/playground?fork=shanghai)

## Consensus - I thought Ethereum was Proof-of-Stake?
Maintaining the database of accounts and smart contracts is done by the consensus algorithm and is a key component of any blockchain and often the first point of difference between blockchains. Bitcoin uses [proof-of-work](https://github.com/millecodex/BlockchainNZ_education/blob/main/articles/bitcoin.md#proof-of-work-mining--network-security) and relies on miners running purpose-built hardware to process transactions, and package and publish blocks. The incentive mechanism is a lottery based on the SHA256 (secure hash algorithm) result; when miners are lucky enough to find a winning hash they can publish a block and earn a reward.

The downside to Bitcoin's mining algorithm is that it is suceptible to hardware optimisation in the form of ASICs (application-specific integrated circuits) that can be manufactured purely for mining purposes and are otherwise superfluous. Ethereum's primary goal was to alleviate this by choosing an algorithm that required less pure processing power and relied more on general-purpose hardware like memory (RAM). The algorithm is called [ethash](https://eth.wiki/en/concepts/ethash/ethash) and requires random read access to a 1GB dataset making it suitable for PC graphics cards to be used as miners. As in Bitcoin, miners are incentivised by a block reward that is currently 2 ETH per block. In summary Ethereum is presently a proof-of-work blockchain that uses GPU miners.

### Where does proof-of-stake (PoS) come in?
It has always the ethos of the Ethereum community to transition the network to a fully stake-based validation mechanism and remove the need for expensive customized hardware. In a PoS system consensus is handled by validators that maintain skin in the game by contributing a stake in ether and are rewarded in a similar fashion to miners. A validator's rewards are proportional to their stake in the system. 

[Eth2](https://ethereum.org/en/eth2/) is the name of the upgrade[^eth2] which has been split into many sub phases. Presently the network is in the *final* stages of the upgrade and the merge may🤞 happen in 2022.
[^eth2]: As of early 2022 the Ethereum foundation decided [change the name](https://blog.ethereum.org/2022/01/24/the-great-eth2-renaming/) of Eth2 to *consensus layer* to prevent people from thinking that Eth1 and Eth2 are different blockchains. They aren't. Eth2 is just an upgrade that includes the present version.

Fact check this with regards to PoS. **Uncle Blocks**: Unlike other blockchain systems, Ethereum incorporates a mechanism to reward stale blocks, referred to as "uncle" blocks. These are blocks that are valid but not included in the main blockchain. This promotes network security and inclusiveness by providing incentives for miners even if their mined blocks are not included in the main chain.




# Characteristics and Quirks
* Difficulty Bomb: Also known as the "Ice Age," the Ethereum network has a built-in difficulty bomb designed to make mining exponentially more challenging over time. This was originally introduced to motivate the network to transition from Proof of Work (PoW) to Proof of Stake (PoS). It's a fascinating mechanic that's deeply rooted in the network's consensus strategy.
* Self-Destruct and Resurrection: A quirky feature in Solidity is the selfdestruct function. When a contract self-destructs, it can send its remaining Ether to another address. Interestingly, if someone sends Ether to a self-destructed contract's address, and a new contract is created at the same address, the new contract will have the Ether sent to the "dead" contract. This resurrection quirk has potential security implications.

# What did we miss?
* The **DAO hack** was an important event in Ethereum's history. There was a bug, and a lot of money was lost, but then the *immutable* blockchain was rolled back, the community split, now there still exists Ethereum Classic (ETC) and an ongoing question over the decentralised nature of Ethereum.
* Questions of Tokenomics: What is the total supply of ETH? Is ETH money?
* iii 

# Further Reading - the very short list
* [The Whitepaper by Vitalik Buterin](https://ethereum.org/en/whitepaper/)
* [The Yellowpaper by Gavin Wood](https://github.com/ethereum/yellowpaper), & [pdf](https://ethereum.github.io/yellowpaper/paper.pdf)
* [Extensive list of learning resources](https://ethereum.org/en/learn/)
* [EVM Illustrated (slides)](https://github.com/takenobu-hs/ethereum-evm-illustrated)

# Exercises
1. a
2. b
3. c

# Video
To be posted.

# Exercises
1. a
2. b
3. c
