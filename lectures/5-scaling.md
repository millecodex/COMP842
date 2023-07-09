[↰ back](../../..)

# Lecture 5: Scaling
## Contents
1. [Blockchain Stack](#blockchain-stack)
2. [The Trilemma](#the-trilemma)
3. [Scalability](#scalability)
4. [Storage](#storage)
5. [State Channels](#state-channels)
6. [Side Chains](#side-chains)
7. [What did we miss?](#what-did-we-miss)
8. [Further Reading - the very short list](#further-reading---the-very-short-list)
9. [Exercises](#exercises)

## Blockchain Stack
A technology stack is a model to represent the sections and subsections of a complex system. A classic example can be seen in the internet. Underneath the application that we interface with there are many sub-layers to the entire technology. The internet standard defines four layers: application, transport, internet, and link[^1^]. Contrast this with the stack from[^2^] that has five divisions. There is no first-principles based ordering to the stack, and one may have more or fewer layers if sufficient to describe the system. This has been inspired by the OSI model (Open Systems Interconnection, see [link](https://en.wikipedia.org/wiki/OSI_model)).

> [^1^]: Braden1989
> [^2^]: Stallings2007

|   | Internet STD 3 |   |   | Stallings (text) |   | Example            |
|---|----------------|---|---|------------------|---|---------------------|
| 4 | Application    |   | 5 | Application      |   | HTTP/FTP           |
| 3 | Transport      |   | 4 | Transport        |   | TCP/UDP            |
| 2 | Internet       |   | 3 | Internet         |   | IPv6               |
| 1 | Link           |   | 2 | Network Access   |   | MAC addressing     |
|   |                |   | 1 | Physical         |   | Integrated circuit |
> Table: The internet standard technology stack as defined by the Internet Engineering Task Force has 4 layers. Others could have different layers, Stallings includes Physical as Level 1.

The blockchain stack also has various definitions with many of them excluding the base layers 1 and 2 of internet; these are assumed. At Level 1 sits consensus, the rules that maintain the ledger. Some kind of network infrastructure is required for consensus to run atop, such as HTTP gateway access and gossip protocol message passing. Level 2 has broad usage and could refer to payment channels such as the lightning network, storage optimisation like sharding, or secondary chains that interact with a main chain. Beyond this is even more diffuse, but generally there must be an application layer on top.

| Bitcoin |   | Ethereum |     | Example          |
|---------|---|----------|-----|------------------|
|         |   | Dapps    | 4   | Stable Coins     |
| Appl    |   | ication  | 3   | Smart Contracts  |
| `Layer 2` |   |          | 2   | Payment Channels |
| Consen  |   | sus      | 1   | Proof of Work    |
| Network |   |          | 0   | Gossip Protocol  |
| Physical |  |          | -1  | ASICs            |
> Table: The blockchain technology stack generally begins with consensus as the base, layer 2 has various scaling improvements, and applications are on top.

The main criticism of Bitcoin is that the network has a limit on throughput; the number of transactions that get recorded in the ledger is difficult to scale. Good security and decentralisation come at the expense of scalability.

> **Note:** The image input provided is a graphical illustration which cannot be converted into Markdown text directly. But you can include images in your markdown file using the following ![Placeholder](<URL TO IMAGE>) syntax along with a caption or text that describes the image.

Figure: The blockchain trilemma: pick any two ideal properties at the risk of sacrificing the third.

## The Trilemma

## Scalability

## Storage

## State Channels

## Side Chains

## What did we miss?

## Further Reading - the very short list

## Exercises

