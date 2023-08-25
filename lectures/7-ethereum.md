[↰ back](../../..)

# Lecture 7: Ethereum
## Contents
1. [Motivation](#motivation)
2. [Smart Contract](#smart-contracts)

7. [Characteristics and Quirks](#characteristics-and-quirks)
8. [What did we miss?](#what-did-we-miss)
9. [Further Reading - the very short list](#further-reading---the-very-short-list)
10. [Exercises](#exercises)

## Motivation
A simple case that can't be handled by such scalability enhancements: suppose you have solar panels on your roof that generate electricity. When you are not home you would like to get paid for the excess electricity by selling it to your neighbors. This can be done through an agreement whereby generating electricity creates tokens that can be traded on the power network. Neighbors can buy your tokens at a discount to the local utility and you both benefit from the exchange.

Or suppose you want to raise money for your project, similar to a crowdfund. If people donate money to your project, in return you can promise them digitally unique tokens that can be used by the project. These are ideal reasons to use a blockchain as there is an exchange of a digital token that holds value.

In late 2013, a nineteen-year-old Russian-Canadian computer science dropout decided to create a system that could handle these use-cases. Vitalik Buterin wrote Ethereum as a response to Bitcoin's lack of programmability. It is the first Turing-complete blockchain and uses a javascript-esque language called Solidity to create blocks of code known as smart contracts. Let's unpack some of these statements and terms.

- **Bitcoin's lack of programmability** comes from the fact that Bitcoin uses a scripting language with very restricted functionality (see Appendix B in Antonopoulos, 2017). If you want to do something that isn't already available in the opcodes, then some very creative ad-hoc programming and second-layer work may be required.

- **Turing-complete** refers to a class of computers (programming languages) that can simulate another computer. Named after computer scientist Alan Turing[^1], a more practical way of thinking of Turing-completeness is that the language has loops; structures that allow for computation. HTML is not Turing-complete as it cannot calculate digits of π, whereas most programming languages are. Bitcoin's scripting language is not Turing-complete.

[^1]: The same namesake as the Turing test in which an artificial intelligence can convince a human they are human. Or, in other words, the human cannot tell if the terminal is answering on behalf of a human or AI.

- **Solidity** is the name of most common high-level language used to write code that compiles to bytecode to be executed on the Ethereum virtual machine. Created by the co-founder of Ethereum, Gavin Wood, Solidity was intended to resemble JavaScript and be recognizable to web developers.

Summarizing Ethereum from the whitepaper[^Buterin2014]:
> [Ethereum] is essentially the ultimate abstract foundational layer: a blockchain with a built-in Turing-complete programming language, allowing anyone to write smart contracts and decentralized applications where they can create their own arbitrary rules for ownership, transaction formats, and state transition functions.

[^Buterin2014]: Buterin, V. (2014). Ethereum: A next-generation smart contract and decentralized application platform.

## Smart Contracts
Smart contracts are blocks of code that reside on a blockchain. To be invoked, a transaction must be sent to the address of the code block, which may then cause other actions. Due to the nature of public decentralized blockchains like Bitcoin and Ethereum, once a smart contract is written to the blockchain, it permanently resides there lying dormant.

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

## Video
To be posted.

## Exercises
1. a
2. b
3. c
