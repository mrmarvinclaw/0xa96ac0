# Polymarket official token launch condition arbitration summary

## Proposition

Before January 1, 2027 at 00:00 PST, Polymarket launched an official fungible token: a fungible token officially released by Polymarket and publicly communicated through official Polymarket channels, excluding NFT launches, promotional offerings, tokenized point systems, and token launches in collaboration with other projects or communities.

## Inputs

- Case directory: `examples/polymarket-official-token-launch-condition`
- Mode: open-record/search-enabled.
- Attorney model: `openai://gpt-5?tools=search`.
- Run count requested: one.
- Initial packet: deliberately thin. It preserved the user-supplied rule text and unresolved gaps, but did not contain official Polymarket source captures before the run.

## Run results

- Output directory: `out/polymarket-official-token-launch-condition-gpt5-search-one-20260503-181128`
- Batch directory: `out/_batch-polymarket-official-token-launch-condition-gpt5-search-one-20260503-181128`
- Case status: completed.
- Resolution: `demonstrated`.
- Vote split: 3-2.
- Run id: `run-1777849888850174000`.

There was one earlier setup failure at `out/_batch-polymarket-official-token-launch-condition-gpt5-search-one-20260503-181107`: `error: parse situation: missing Proposition section`. That failed before a merits run. The input was corrected by adding the required `# Proposition` heading.

The successful arbitration completed, but the surrounding shell wrapper exited with code 1 after success because the wrapper referenced `PIPESTATUS` under zsh. The arbitration artifacts are complete.

## Aggregate outcome

One completed arbitration. Distribution: one `demonstrated`, zero `not_demonstrated` case resolutions.

## Vote/rationale coherence

Council:
- C1, `openrouter://google/gemini-3.1-flash-lite-preview`, `personas/persons/d715074-0.txt`: `demonstrated`.
- C2, `openrouter://openai/gpt-5.4`, `personas/persons/d715074-7.txt`: `demonstrated`.
- C3, `openrouter://openai/gpt-5.2-chat`, `personas/persons/d715074-2.txt`: `not_demonstrated`.
- C4, `openrouter://amazon/nova-premier-v1`, `personas/persons/e50e538-0.txt`: `not_demonstrated`.
- C5, `openrouter://google/gemini-2.5-flash`, `personas/persons/e50e538-1.txt`: `demonstrated`.

The vote labels matched the rationales. The two `not_demonstrated` votes were coherent burden-of-proof dissents, not apparent label inversions.

## Recurring factual theories

Plaintiff theory:
- Polymarket launched pUSD, Polymarket USD, as a standard ERC-20 token on Polygon.
- Official Polymarket docs identify pUSD as the collateral token used for all trading on Polymarket.
- Official Polymarket Contracts page lists the pUSD CollateralToken proxy at `0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB` and calls the page the single source of truth for platform contract addresses.
- Official Polymarket changelog and migration guide describe a CLOB V2 production upgrade, live April 28, 2026, shipping a new collateral token, pUSD.
- Polygonscan corroborates production-chain existence and activity.

Defense theory:
- The initial packet did not contain authenticated official-page captures or on-chain records, so counsel summaries and technical reports were insufficient.
- Even if pUSD exists, product documentation for a collateral instrument may not equal an outward launch of an official fungible token in the sense of the market rule.
- The case lacked server-dated captures, archive links, block numbers, block times, and full chain-control evidence.

Council pattern:
- The majority credited the attorney-discovered official Polymarket docs and found pUSD satisfied the rule.
- The dissenters focused on record incompleteness and the distinction between a technical collateral token and an official token launch.

## Evidence preservation after open-record run

The run relied on evidence not present in the initial packet. After the run, I captured the main discovered sources under `examples/polymarket-official-token-launch-condition/source-captures/` and updated `official-source-record.txt`, `primary-evidence.txt`, and `unresolved-record-gaps.txt`.

Captured files:
- `polymarket-docs-pusd.html` from `https://docs.polymarket.com/concepts/pusd`
- `polymarket-docs-contracts.html` from `https://docs.polymarket.com/resources/contracts`
- `polymarket-docs-changelog.html` from `https://docs.polymarket.com/changelog`
- `polymarket-docs-v2-migration.html` from `https://docs.polymarket.com/v2-migration`
- `polygonscan-pusd-token.html` from `https://polygonscan.com/address/0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB`
- `capture-manifest.txt`

## Operational issues

- First invocation failed before merits because `situation.md` lacked a `# Proposition` heading. Corrected.
- Successful run's shell wrapper used `PIPESTATUS`, which is not available under the default zsh shell. The wrapper failed after the arbitration had already returned `status: ok`. This affected wrapper status only, not case artifacts.
- No council or provider failure occurred in the completed run.

## Interpretation

This was a useful open-record evidence-discovery run. The council found `demonstrated` by 3-2, based on pUSD as an official Polymarket ERC-20 collateral token launched and publicly documented before the 2027 cutoff. The result is not a clean closed-record result because the decisive official documents were discovered during the run and captured afterward. A controlled closed-record replay should use the backfilled official captures and should sharpen the legal/factual distinction between "official token" and "technical collateral token."

## Artifact inventory

- `out/polymarket-official-token-launch-condition-gpt5-search-one-20260503-181128/run.json`
- `out/polymarket-official-token-launch-condition-gpt5-search-one-20260503-181128/state.json`
- `out/polymarket-official-token-launch-condition-gpt5-search-one-20260503-181128/digest.md`
- `out/polymarket-official-token-launch-condition-gpt5-search-one-20260503-181128/council.json`
- `out/polymarket-official-token-launch-condition-gpt5-search-one-20260503-181128/events.ndjson`
- `out/polymarket-official-token-launch-condition-gpt5-search-one-20260503-181128/transcript.md`
- `out/polymarket-official-token-launch-condition-gpt5-search-one-20260503-181128/run.log`
- `out/_batch-polymarket-official-token-launch-condition-gpt5-search-one-20260503-181128/logs/one.log`
- `out/_batch-polymarket-official-token-launch-condition-gpt5-search-one-20260503-181128/summary.md`
