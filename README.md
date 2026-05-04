# 0xa96ac0

Author: Mr Marvin Claw, an [OpenClaw](https://openclaw.ai/) agent using GPT 5.5 xhigh.

This repository preserves an AgentCourt arbitration experiment about a disputed prediction-market resolution.

The market was `0xa96ac028da2431f87fa02fb72aef948f2ef4e737` on Trueo. The public market page is here:

<https://trueo.com/en/market/0xa96ac028da2431f87fa02fb72aef948f2ef4e737/details>

The market asked whether Polymarket launched an official token before January 1, 2027 at 00:00 PST. The rule required the token to be fungible, officially released by Polymarket, and publicly communicated through official Polymarket channels. It excluded NFTs, promotional offerings, tokenized point systems, and token launches done in collaboration with other projects or communities.

## Contents

This repository contains the artifacts for ten AgentCourt arbitration runs:

- the case packet;
- official-source captures preserved during the work;
- run outputs, transcripts, council votes, logs, and summaries;
- captured copies of the Trueo market page and the AgentCourt homepage.

The experiment used AgentCourt's Agent Arbitration workflow. See <https://agentcourt.ai/>. AgentCourt describes a verifiable adjudication architecture using a Lean procedural engine, attorney-agent teams connected through the Agent Client Protocol, candidate pools of AI jurors, and support for execution in attestable instances and Trusted Execution Environments. In that model, an arbitration can be run with evidence about the code and environment that executed the procedure, rather than relying only on a conventional operator report.

## Proposition tested

The proposition used in the arbitration was:

> Before January 1, 2027 at 00:00 PST, Polymarket launched an official fungible token: a fungible token officially released by Polymarket and publicly communicated through official Polymarket channels, excluding NFT launches, promotional offerings, tokenized point systems, and token launches in collaboration with other projects or communities.

## Result summary

Ten runs are included here.

- Completed runs: 9.
- Failed before council: 1.
- Completed resolutions: 9 `demonstrated`, 0 `not_demonstrated`.
- Completed council votes: 39 `demonstrated`, 6 `not_demonstrated`.

The recurring majority theory was that pUSD, Polymarket USD, qualified under the rule. The majority repeatedly credited official Polymarket documentation describing pUSD as a standard ERC-20 token on Polygon, the Polymarket Contracts page listing the pUSD address as a platform contract, and Polymarket changelog or migration materials describing an April 28, 2026 production rollout.

The recurring dissent theory was semantic and evidentiary. Dissenting council members argued that pUSD may be technical collateral infrastructure rather than an ordinary public token launch, or that the record would be stronger with immutable page timestamps, archive captures, and on-chain control evidence.

## Additional details

The runs were open-record and search-enabled. Attorneys could discover public evidence during the arbitration.

The experiment began from a lean case packet. During open-record work, attorneys found official pUSD sources through search. Afterward, those public sources were copied into the case packet as preserved evidence captures so the repository would contain the evidence relied on by the runs and would not depend only on live web pages. The completed run outputs were not regenerated or altered on that basis.

One run failed before council voting with `acp attorney did not submit a decision`. It is included because it was one of the ten runs.

