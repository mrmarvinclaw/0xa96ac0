# Polymarket official token launch condition nine-more arbitration summary

## Proposition

Before January 1, 2027 at 00:00 PST, Polymarket launched an official fungible token: a fungible token officially released by Polymarket and publicly communicated through official Polymarket channels, excluding NFT launches, promotional offerings, tokenized point systems, and token launches in collaboration with other projects or communities.

## Inputs

- Case directory: `examples/polymarket-official-token-launch-condition`
- Mode: open-record/search-enabled.
- Attorney model: `openai://gpt-5?tools=search`.
- Requested additional runs: 9 sequential attempts.
- Batch directory: `out/_batch-polymarket-official-token-launch-condition-gpt5-search-nine-more-20260503-183500`.

The case packet had been backfilled after the first open-record run with official Polymarket pUSD, Contracts, Changelog, and CLOB V2 migration captures, plus Polygonscan corroboration.

## Run results

| Run | Output directory | Status | Resolution | Vote split |
| --- | --- | --- | --- | --- |
| 1 | `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r1-20260503-183500` | completed | `demonstrated` | 5-0 |
| 2 | `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r2-20260503-184607` | completed | `demonstrated` | 5-0 |
| 3 | `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r3-20260503-185517` | completed | `demonstrated` | 5-0 |
| 4 | `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r4-20260503-190913` | failed before council | none | none |
| 5 | `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r5-20260503-191501` | completed | `demonstrated` | 4-1 |
| 6 | `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r6-20260503-192814` | completed | `demonstrated` | 4-1 |
| 7 | `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r7-20260503-193906` | completed | `demonstrated` | 5-0 |
| 8 | `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r8-20260503-194746` | completed | `demonstrated` | 3-2 |
| 9 | `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r9-20260503-195613` | completed | `demonstrated` | 5-0 |

Run 4 failed before council with `acp attorney did not submit a decision`. It produced `events.ndjson` and `run.log`, but no `run.json`, `state.json`, `digest.md`, or council vote.

## Aggregate outcome

Nine requested additional attempts:
- Completed: 8.
- Failed before council: 1.
- Completed-case resolution distribution: 8 `demonstrated`, 0 `not_demonstrated`.
- Completed vote totals: 36 `demonstrated`, 4 `not_demonstrated`.
- Vote-split distribution among completed runs:
  - 5-0: 5 runs.
  - 4-1: 2 runs.
  - 3-2: 1 run.

Including the first earlier run (`out/polymarket-official-token-launch-condition-gpt5-search-one-20260503-181128`), the experiment now has:
- Attempts: 10.
- Completed: 9.
- Failed before council: 1.
- Completed-case resolution distribution: 9 `demonstrated`, 0 `not_demonstrated`.
- Council vote total across completed runs: 39 `demonstrated`, 6 `not_demonstrated`.

## Vote/rationale coherence

I did not find vote-label inversions in the completed additional runs. The `demonstrated` votes credited the same pUSD theory. The `not_demonstrated` votes were coherent dissents based on either:

1. semantic narrowness: pUSD is infrastructure/collateral plumbing, not an ordinary "official token launch"; or
2. burden/record sufficiency: official docs and explorer corroboration were not enough without stronger immutable timestamps, on-chain control proof, or launch-style announcement evidence.

Dissent locations:
- Run 5 C4: semantic dissent; collateral-token references did not meet ordinary meaning of an official token launch.
- Run 6 C2: burden dissent; gaps in immutable timestamps and organizational control.
- Run 8 C1: semantic dissent; pUSD looked like infrastructure update rather than standalone platform token launch.
- Run 8 C5: general insufficiency dissent; terse but coherent.

## Recurring factual theories

Majority theory:
- Polymarket's official documentation identifies pUSD, Polymarket USD, as a standard ERC-20 token on Polygon.
- Polymarket's Contracts page lists the pUSD CollateralToken proxy at `0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB` and describes the page as the single source of truth for platform contract addresses.
- Polymarket's Changelog and CLOB V2 migration guide say Polymarket shipped a new collateral token, pUSD, with the April 28, 2026 production upgrade.
- April 28, 2026 is before the January 1, 2027 00:00 PST deadline.
- The exclusions do not apply: pUSD is not an NFT, promotional offering, tokenized point system, or partner/community token.

Dissent theory:
- The rule phrase "official token launch" may imply something more like a public token product, governance/airdrop/tokenomics launch, or ordinary public launch announcement.
- A platform collateral token introduced as part of CLOB V2 may be official infrastructure without being the kind of official token launch contemplated by the market.
- More rigorous closed-record proof would include immutable archive captures, server/publication timestamps, explicit contract-control linkage, and first-mint/first-transfer block-time analysis.

## Operational issues

- Run 4 failed before council with `acp attorney did not submit a decision`. No retry was performed.
- The batch wrapper had a manifest parser bug: it wrote `parse_error` for successful runs because its Python one-liners referenced unquoted dict keys. I ignored the manifest's parsed fields and inspected `run.json` and `state.json` directly for the results above.
- While diagnosing a premature completion notice, I started and then stopped an accidental duplicate continuation. It produced an extra incomplete events-only directory: `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r6-20260503-191633`. It is not counted in the nine requested additional attempts.
- No OpenClaw configuration changes, gateway restarts, or git commits were made.

## Interpretation

The pUSD theory became more stable after the official Polymarket source captures were backfilled. The initial run was `demonstrated` 3-2. The eight completed additional runs all resolved `demonstrated`, with five unanimous councils and only four dissenting votes out of forty completed additional council votes.

The remaining dispute is not whether pUSD exists. The record repeatedly established that point. The remaining dispute is semantic: whether Polymarket's official ERC-20 collateral token counts as an "official token launched by Polymarket" under the market rule, or whether the rule should be read as excluding technical collateral infrastructure even though that exclusion is not stated.

A closed-record replay should preserve stronger source authentication and separate the key semantic issue directly: whether an official platform collateral ERC-20 qualifies as an official token launch under the rule's plain language.

## Artifact inventory

Batch:
- `out/_batch-polymarket-official-token-launch-condition-gpt5-search-nine-more-20260503-183500/summary.md`
- `out/_batch-polymarket-official-token-launch-condition-gpt5-search-nine-more-20260503-183500/logs/r1.log` through `r9.log`
- `out/_batch-polymarket-official-token-launch-condition-gpt5-search-nine-more-20260503-183500/manifest.tsv`
- `out/_batch-polymarket-official-token-launch-condition-gpt5-search-nine-more-20260503-183500/DONE`

Completed outputs:
- `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r1-20260503-183500`
- `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r2-20260503-184607`
- `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r3-20260503-185517`
- `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r5-20260503-191501`
- `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r6-20260503-192814`
- `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r7-20260503-193906`
- `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r8-20260503-194746`
- `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r9-20260503-195613`

Failed/incomplete outputs:
- `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r4-20260503-190913`
- accidental duplicate, not counted: `out/polymarket-official-token-launch-condition-gpt5-search-nine-more-r6-20260503-191633`
