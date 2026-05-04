# Arbitration Transcript

## Complaint

### Proposition

Before January 1, 2027 at 00:00 PST, Polymarket launched an official fungible token: a fungible token officially released by Polymarket and publicly communicated through official Polymarket channels, excluding NFT launches, promotional offerings, tokenized point systems, and token launches in collaboration with other projects or communities.

### Standard of Evidence

Preponderance of the evidence.

## Council

- C1: openrouter://anthropic/claude-3.7-sonnet (personas/persons/e50e538-0.txt)
- C2: openrouter://google/gemini-3-flash-preview (personas/persons/d715074-7.txt)
- C3: openrouter://openai/gpt-5.2-chat (personas/persons/d715074-2.txt)
- C4: openrouter://x-ai/grok-4-fast (personas/persons/d715074-2.txt)
- C5: openrouter://anthropic/claude-sonnet-4.5 (personas/persons/d715074-9.txt)
## Proceeding

### Openings

#### Plaintiff Opening

Members of the Council:

Dispute and theory
The question is narrow: Did Polymarket, before January 1, 2027 at 00:00 PST, launch an official fungible token and publicly communicate that launch through its official channels? Our theory is yes. Under a preponderance standard, we need only show this is more likely than not.

Controlling elements drawn from the proposition
To prevail, the plaintiff must establish all of the following:
1) Fungibility: The asset is a standard, transferable fungible crypto token (e.g., ERC‑20‑like) on a production network, not a testnet.
2) Official release: Polymarket—or an entity it controls—authorized issuance or deployment and held itself out as the issuer (e.g., control of deployer/owner keys, treasury, or formal documentation).
3) Public communication via official channels: At least one communication from an official Polymarket channel (site/app on a Polymarket domain, official blog/docs, verified social account, newsletter, or in‑app notice) identifying the token (by name/symbol and/or contract address) and indicating public availability (trading, claiming, or distribution live).
4) Exclusions do not apply: The token is not an NFT, not a promotional coupon/credit, not a tokenized points system, and not a token launched by another project/community even if Polymarket collaborated. Participation by exchanges or L2 partners does not defeat “official” status if Polymarket remains the issuer.
5) Timing: The on‑chain launch event that constitutes release (e.g., enabling transfers/distribution) and at least one qualifying official communication occurred before the deadline. Because block and platform timestamps are typically UTC, conversions to Pacific Standard Time are required; January 1, 2027 00:00 PST equals January 1, 2027 08:00 UTC.

Factual questions for decision
- Identity and control: Who deployed the token, who controls contract admin/treasury, and is that control attributable to Polymarket?
- Nature of the asset: Does the contract implement a fungible standard with unrestricted transfers on mainnet? Was supply distributed to the public before the deadline?
- Official communications: Did any authenticated Polymarket channel name the token and/or publish the contract address and describe a live release rather than a future plan?
- Exclusions: Is the asset merely a points ledger, an NFT, a limited‑use promo, or principally a partner/community token?
- Timing and authenticity: Do on‑chain timestamps and official‑channel timestamps, once converted to PST, predate the deadline and withstand authentication checks?

Proof sufficient to satisfy the burden
- Block‑explorer records evidencing the token contract, standard, transferability, deployer, and relevant transactions with timestamps predating the deadline, corroborated by cryptographic hashes.
- Official‑channel artifacts: pages on Polymarket‑controlled domains, in‑app notices, or posts from verified official accounts identifying the token and linking or referring to the symbol/contract, preserved with reliable archives and metadata.
- Evidence tying the deployer or contract owner to Polymarket (e.g., references in official docs, verified ownership annotations, or signatures from known Polymarket keys).
- Distribution evidence (claim pages, allocation transactions, or exchange listings cited by official channels) showing the launch was public, not an internal test.

Proof that would defeat the claim
- No qualifying official Polymarket communication before the deadline, or explicit statements limiting activity to NFTs, promos, or points.
- Evidence the referenced asset is third‑party, testnet‑only, non‑transferable, or otherwise non‑fungible.
- Timestamps (on‑chain or communications) that, when correctly converted to PST, occur at or after 00:00 PST on January 1, 2027.

Record development the Council should expect next
- Establish an issuer‑of‑record framework: who controls minting, upgrades, treasury, and branding—substance over co‑marketing.
- Authenticate channels (domain control, verified handles, in‑app provenance) and preserve with archival hashes.
- Fix time precisely using on‑chain block timestamps and platform post times with documented UTC→PST conversion.
- Collect, as exhibits: (a) token contract address and explorer pages; (b) authoritative Polymarket communications identifying that token; (c) any contrary statements by Polymarket; (d) distribution/trading evidence prior to the deadline; and (e) analysis addressing each exclusion.

Roadmap
In later filings, plaintiff will present element‑by‑element exhibits connecting: (i) contract and timestamp → timing; (ii) deployer/owner and branding → official release; (iii) official posts/pages → public communication; and (iv) token standard/transferability → fungibility, while squarely addressing exclusions. The Council should evaluate whether that integrated proof makes it more likely than not that Polymarket launched an official fungible token before the stated deadline.

#### Defendant Opening

Members of the Council:

Dispute and defense theory
The proposition requires all of the following before January 1, 2027 at 00:00 PST: Polymarket launched an official fungible token and itself publicly communicated that launch. Our theory is that the plaintiff cannot meet that burden. It is more likely than not that at least one indispensable element fails—either no Polymarket‑issued fungible token, no qualifying official communication before the deadline, or the asset falls within an exclusion.

Elements that must all be proven
1) Fungible token on a production chain: transferable and standard (e.g., ERC‑20‑like), not testnet or internal credit.
2) Official release by Polymarket: issuer‑of‑record status attributable to Polymarket (deployer/owner/admin roles, treasury, or equivalent indicia) and held out as such.
3) Public communication from an official Polymarket channel before the deadline: site/app on a Polymarket domain, official blog/docs, verified social account, newsletter, or in‑app notice, identifying the token (name/symbol and/or contract) and stating a live release.
4) Exclusions inapplicable: not an NFT, not promo credits, not tokenized points/rewards, and not principally a partner/community token.
5) Timing: both the enabling on‑chain event and at least one qualifying official communication predate the deadline, with accurate time conversion and authentication.

Decisive factual questions
- Issuer‑of‑record: Who deployed the contract; who controls mint/burn/upgrade/pause roles; is control attributable to Polymarket (e.g., a Polymarket‑controlled multisig and branding)?
- Asset nature: Does the contract implement a recognized fungible standard with public transfers on mainnet, as opposed to wrapped assets, internal credits, allowlists, or test artifacts?
- Official communications: Did a Polymarket‑controlled channel identify the token and announce that the release was live, rather than plans or third‑party reporting?
- Exclusions: Do mechanics resemble points/rewards, promos, or NFTs; or is the token principally partner‑led with Polymarket not the issuer of record?
- Timing and authenticity: Do on‑chain and channel timestamps, after PST conversion and edit‑history checks, precede the deadline?

Proof that would satisfy the burden
- Explorer evidence of a production‑network fungible token with public transferability before the deadline.
- Credible linkage of deployer/owner/admin roles and treasury to Polymarket.
- A dated, attributable Polymarket communication before the deadline naming the token and stating that claiming/trading/distribution is live.
- Distribution evidence (claim pages, allocations, or listings) cited by Polymarket showing public availability before the deadline.

Proof that would defeat the claim
- No qualifying Polymarket communication prior to the deadline, or only plans/roadmaps.
- Evidence the asset is points/rewards, promo, or NFT, or is principally partner‑led.
- Lack of issuer‑of‑record control by Polymarket over deployer/owner/admin roles or treasury.
- Transfer restrictions or gating that prevented public acquisition/transfer before the deadline.
- Timestamps or edit histories at or after the deadline, or artifacts lacking authentication.

Record development to expect
- Issuer‑of‑record forensics: contract roles, deployer provenance, multisig signers, branding control.
- Channel authentication: domain/handle control at the relevant time; capture integrity and edit logs; exclusion of retweets or media quotes absent Polymarket’s own statement.
- Timing forensics: identification of the enabling on‑chain transaction and the earliest qualifying communication; precise PST conversion; preserved metadata.
- Asset characterization: standard compliance, transfer restrictions, and similarities to excluded categories.

Interpretive guidance
- “Launched” should be fixed at when the public could actually acquire/transfer on mainnet, not mere deployment or closed testing.
- “Publicly communicated” requires an original, attributable Polymarket statement; third‑party coverage is insufficient.
- “Official fungible token” excludes wrapped/bridged third‑party assets and partner/community tokens where Polymarket is not issuer of record.

Conclusion
Under a preponderance standard, the proposition fails if any single element is not more likely than not. The most likely failure points are issuer‑of‑record control, the existence and timing of a qualifying official communication, and the applicability of the exclusions. The Council should require precise, authenticated artifacts on those points before crediting the claim.

### Arguments

#### Plaintiff Argument

Members of the Council:

Claim and burden
Under a preponderance standard, the question is whether it is more likely than not that, before January 1, 2027 at 00:00 PST (08:00 UTC), Polymarket launched an official fungible token and publicly communicated that launch via its own channels. The record shows that Polymarket launched pUSD (Polymarket USD), a standard ERC‑20 token on Polygon mainnet, publicly announced and documented on Polymarket’s official documentation site, and identified by contract address on Polymarket’s official “Contracts” page. That satisfies the proposition.

What the record shows (with cites)
- Polymarket’s official docs page “pUSD (Polymarket USD)” describes pUSD as the collateral token used for all trading on Polymarket, states it is a standard ERC‑20 on Polygon, transferable, and specifies metadata (including 6 decimals). See PX‑1 §1; PX‑2 (captured official page reference).
- Polymarket’s official “Contracts” page states it is the “single source of truth” for Polymarket contract addresses on Polygon mainnet and lists “pUSD — CollateralToken (proxy)” at 0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB. See PX‑1 §2; PX‑2.
- Polymarket’s official changelog and V2 migration guide state that a “new collateral token (pUSD)” shipped with the CLOB V2 upgrade and that CLOB V2 is live on production as of April 28, 2026. See PX‑1 §§3–4; PX‑2.
- Polygonscan shows the same address labeled “Polymarket: pUSD Token” with active token transactions and verified source metadata—corroborating mainnet existence and transferability. See PX‑1 §5.

Element‑by‑element application
1) Fungibility: pUSD implements a standard ERC‑20 on Polygon with transfers enabled. PX‑1 §1 confirms fungible‑token characteristics; PX‑1 §5 corroborates on‑chain behavior. This meets the fungibility requirement.
2) Official release by Polymarket: Polymarket’s own Contracts page declares itself the single source of truth and lists the pUSD contract by name and address. The branding (Polymarket USD), the listing, and the platform‑wide use establish Polymarket as issuer‑of‑record for this token. PX‑1 §2; PX‑2.
3) Public communication via official channels: Multiple Polymarket‑controlled channels—docs.polymarket.com pages for pUSD, the Contracts page, the changelog, and the V2 migration guide—identify the token by name and (on the Contracts page) by contract address, and state the production go‑live of the system using pUSD. PX‑1 §§1–4; PX‑2. These are quintessential official communications.
4) Exclusions inapplicable: pUSD is not an NFT, not a promotional coupon/credit, and not a tokenized points system. It is a standard ERC‑20 used as platform collateral. Nor is it a partner/community token; it is Polymarket’s own contract and brand. PX‑1 §§1–2.
5) Timing: The official materials fix the live production release at April 28, 2026—well before the deadline of January 1, 2027 at 00:00 PST (08:00 UTC). PX‑1 §§3–4. No contrary timing evidence appears in the record.

Addressing the principal defense theory
The anticipated objection is semantic: that a “collateral token” is not an “official token launch.” The proposition, however, does not require a governance token or a speculative “POLY”‑style brand. It requires a fungible token “officially released by Polymarket and publicly communicated through official Polymarket channels,” with specified exclusions. The pUSD rollout meets that text precisely: Polymarket authored and controls the contract, branded it “Polymarket USD,” documented it as a standard ERC‑20 on Polygon, published the contract address on its official “single source of truth” page, and announced the live release as part of CLOB V2. That is an official fungible‑token launch under the plain language.

Standard of proof
On this record, more than one independent official communication (pUSD concept page; Contracts page; changelog; migration guide) plus on‑chain corroboration support every element. At minimum, it is more likely than not that Polymarket launched pUSD as described and communicated that launch before the deadline.

Conclusion
The Council should find the proposition satisfied.

Offered exhibits
- PX‑1: primary-evidence.txt (summary of captured official Polymarket pages and Polygonscan corroboration)
- PX‑2: official-source-record.txt (capture list and context for the official Polymarket sources)

Offered technical report
- TR‑1: Element‑by‑element mapping and timing conversion: January 1, 2027 00:00 PST = 08:00 UTC; Polymarket’s own changelog/migration guide place the live release at April 28, 2026, well before the deadline; mapping of each proposition element to PX‑1/PX‑2 citations.

Exhibits offered:
- PX-1: primary-evidence.txt
- PX-2: official-source-record.txt

Technical reports:
- Element-by-element mapping and timing conversion
  Mapped the proposition’s five elements to the record: (1) Fungibility—pUSD described as standard ERC-20 with transfers (PX-1 §1); (2) Official release—Polymarket Contracts page lists pUSD and declares itself single source of truth (PX-1 §2; PX-2); (3) Official communication—pUSD doc, Contracts, changelog, and migration guide jointly identify the token and the live production release (PX-1 §§1–4); (4) Exclusions—pUSD is not NFT/promo/points nor a partner token (PX-1 §§1–2); (5) Timing—go-live on April 28, 2026 predates the January 1, 2027 00:00 PST (08:00 UTC) deadline. No contrary evidence in the record.

#### Defendant Argument

Members of the Council:

Claim and burden
To carry this market under a preponderance standard, plaintiff must show it is more likely than not that, before January 1, 2027 at 00:00 PST (08:00 UTC), Polymarket (i) launched (ii) an official (iii) fungible token and (iv) itself publicly communicated that launch, with the stated exclusions not applying. If any single element is not proven, the proposition fails.

Summary of defense
On this record, plaintiff has not shown a qualifying “official token launch.” What the evidence shows is that Polymarket’s CLOB V2 introduced an internal collateral instrument called pUSD and that Polymarket documentation describes and indexes a contract for it. That is not the same thing as Polymarket launching a token to the public and communicating that token launch. At least three indispensable elements remain unproven: (A) “launch” as a public release, (B) issuer‑of‑record control, and (C) a qualifying public communication of a token launch; and the timing/authentication of the cited pages is not established.

1) “Launched” means more than introducing an internal settlement unit
The proposition focuses on whether Polymarket launched a token. The record’s strongest facts are: (i) pUSD is described as a collateral token and ERC‑20 on Polygon (PX‑1 §1), and (ii) it appears on a “Contracts” index (PX‑1 §2). Nothing in the record shows a public distribution event, claim page, allocation, or other offering that would amount to a token launch rather than an internal clearing wrapper used by the app. Even accepting transferability, a wrapped, app‑only collateral unit is not, without more, an “official token launch” to the public. Plaintiff’s theory elides that distinction.

2) “Official release by Polymarket” is not established
Plaintiff relies on Polymarket‑hosted docs labeling the contract and calling the index a “single source of truth” (PX‑1 §2; PX‑2). But there is no issuer‑of‑record forensics: no deployer address tied to Polymarket, no owner/admin role analysis, no multisig signers, no mint/burn authority attribution. Without evidence of who actually controls the token contract, “official release by Polymarket” is not more likely than not; it is merely asserted.

3) No qualifying public communication of a token launch
The materials cited are (a) a concept page about pUSD (PX‑1 §1), (b) a contracts index (PX‑1 §2), (c) a changelog stating CLOB V2 would go live and later that CLOB V2 is live (PX‑1 §3), and (d) a migration guide noting a new collateral token (PX‑1 §4). None is a Polymarket announcement that “we launched a token” or that a token is publicly available for acquisition outside the app’s collateralization flow. A documentation page and an address index are references, not a launch communication; “CLOB V2 is live” is a system‑upgrade notice, not a token‑launch announcement. The proposition expressly requires that Polymarket “publicly communicated” the token launch; that element is not satisfied by these materials.

4) Timing/authentication gaps cut against the burden
PX‑2 candidly notes the captures were made after the run, and that server‑dated headers, immutable archives, and edit histories were not preserved. The record does not supply authoritative publication timestamps for the pages offered as “official communications.” Absent authenticated timing, plaintiff has not proven those communications—if qualifying at all—predated the January 1, 2027 00:00 PST deadline. See PX‑2 (Remaining official‑source limitations); see also “unresolved‑record‑gaps.txt.”

5) Exclusions and characterization
We do not contend pUSD is an NFT or a points ledger. The closer issue is characterization: the record supports pUSD as a USDC‑backed wrapper used for collateralization, not as a stand‑alone platform/community token “launched” to the public. On this framing, plaintiff’s evidence fits the excluded spirit (internal accounting unit) rather than the proposition’s target (an official token launch).

6) Explorer corroboration is not dispositive
Polygonscan labels and transaction feeds (PX‑1 §5) confirm a contract exists on Polygon, but explorer annotations are not official Polymarket communications and do not establish issuer‑of‑record or a token launch.

Conclusion
At minimum, the evidence is in equipoise on whether Polymarket launched an official fungible token and publicly communicated that launch. Under a preponderance standard, equipoise is insufficient. The Council should find that the plaintiff has not met its burden on the current record and should reject the proposition.

Requested disposition
Find the proposition not satisfied on the present record, without prejudice to future proof concerning events before January 1, 2027.

Exhibits offered:
- DX-1: unresolved-record-gaps.txt

### Rebuttals

#### Plaintiff Rebuttal

Members of the Council:

This is a narrow rebuttal to the defense’s three pillars: (A) “launch” requires a public distribution event, (B) issuer‑of‑record is unproven, and (C) no qualifying official communication or timing.

1) “Launch” under the proposition
The proposition does not require an airdrop, claim page, or external distribution. It asks whether Polymarket launched an official fungible token and publicly communicated that launch, excluding NFTs, promos, points, and partner/community tokens. On this record, Polymarket’s own docs state it “shipped … a new collateral token (Polymarket USD, or pUSD)” and that “CLOB V2 is live on production” as of April 28, 2026, and the Contracts page identifies the token by name and address. That is a product launch of a fungible token. Recasting “launch” to mean a speculative/gov token or a separate retail distribution adds elements the text does not contain. See PX‑1 §§3–4 (ship + live), PX‑1 §2 (address), PX‑1 §1 (ERC‑20, transferable); PX‑2.

2) Official release by Polymarket (issuer‑of‑record)
The defense demands deployer/owner forensics. The proposition doesn’t. It asks whether the token was officially released by Polymarket. Polymarket’s Contracts page expressly calls itself the “single source of truth” for Polymarket contract addresses and lists “pUSD — CollateralToken (proxy)” at the stated address. The token’s brand is Polymarket USD, and the migration guide and changelog describe it as “shipped” as part of Polymarket’s core upgrade. That is Polymarket holding itself out as the issuer of record. Deep key‑level forensics would be nice‑to‑have, not need‑to‑win, under a preponderance standard given these multiple official admissions. PX‑1 §§1–2, 4; PX‑2.

3) Qualifying public communication
The proposition requires communication “through official Polymarket channels.” We have several: the pUSD concept page (identifies the token and its properties), the Contracts page (names and doxes the on‑chain address), the changelog (announces the new token and the go‑live), and the V2 migration guide (states shipment and live status). These are on a Polymarket‑controlled domain and speak in Polymarket’s voice. That is far more than a mere address index; it is explicit, dated, product‑release communication. PX‑1 §§1–4; PX‑2.

4) Timing and authentication
Defense points to capture mechanics, not contradictory facts. The official pages themselves contain contemporaneous date stamps (Apr 17 and Apr 28, 2026) and cross‑reference one another; the explorer page shows active mainnet token activity at the same address. There is no contrary timing evidence. Under a preponderance standard, multiple mutually corroborating Polymarket‑authored pages that fix April 28, 2026 as the live date easily clear the January 1, 2027 00:00 PST deadline. PX‑1 §§3–4; PX‑2.

5) Exclusions and characterization
pUSD is a standard ERC‑20 with transfers. It is not an NFT, a promotional coupon, a points ledger, or a third‑party/community token. Its being used as collateral does not move it into any exclusion; the exclusions are expressly enumerated, and “collateral token” is not among them. PX‑1 §1–2.

6) Corroboration
We agree explorer labels are secondary; here they align with Polymarket’s own “single source of truth,” reinforcing attribution rather than supplying it. PX‑1 §5 with §2.

Bottom line
The defense asks the Council to import extra elements—public distribution mechanics, deployer‑forensics, or a governance‑style announcement—not found in the proposition. The actual elements are satisfied on Polymarket’s own pages: a fungible token (ERC‑20, transferable) that Polymarket officially released and publicly communicated, with a live date of April 28, 2026, well before the deadline. On this record, it is more likely than not that the proposition is true. The Council should find the proposition satisfied now.

### Surrebuttals

#### Defendant Surrebuttal

Members of the Council:

The rebuttal narrows the dispute to three places. Even crediting plaintiff’s best points, the record still fails on (i) what was “launched,” (ii) whether the launch was “officially released by Polymarket,” and (iii) whether a qualifying “public communication of that launch” occurred before the deadline.

1) Launch vs. internal component
Plaintiff’s strongest line is that Polymarket “shipped … a new collateral token (pUSD)” and that “CLOB V2 is live on production” (PX‑1 §§3–4). Even accepting those statements, they describe a system upgrade that uses an internal collateral instrument, not a public token launch as such. The proposition’s object is “an official fungible token” and asks whether Polymarket “launched” it. The cited materials never say “we launched pUSD” as a token available to the public independent of the app’s collateralization flow. They evidence functionality going live, not a discrete token‑launch event. On this record, the most that is more likely than not is that pUSD exists and is used in‑app as collateral—insufficient where the proposition requires a token “launch,” not merely the introduction of an internal settlement unit.

2) “Officially released by Polymarket” is not proven on this record
Plaintiff argues that branding plus inclusion on a “single source of truth” Contracts page (PX‑1 §2; PX‑2) suffices. But the proposition requires an official release by Polymarket, not merely that Polymarket documents a contract address. The record contains no deployer/owner/admin evidence, no attribution of mint/burn/upgrade authority, and no statement tying on‑chain control to Polymarket. In other words, the record shows Polymarket uses and documents pUSD, but it does not show Polymarket as issuer‑of‑record. Under a preponderance standard, that gap matters: without control or issuance indicia, it is just as consistent with a wrapped, contract‑governed collateral unit as with a Polymarket‑issued token “launch.”

3) No qualifying “public communication of the launch”
Plaintiff lists four Polymarket‑hosted materials (PX‑1 §§1–4; PX‑2). None is a communication that Polymarket launched a token. The concept page describes properties; the Contracts page is an address index; the changelog and migration guide announce a platform upgrade and note a new collateral token as a component. That is not the same as Polymarket publicly communicating a token launch. The proposition’s communication element targets an announcement of the launch of the token itself, not a documentation page or a generic “V2 is live” post in which a collateral wrapper is mentioned in passing.

4) Timing and authentication remain unresolved
Plaintiff leans on page date stamps. But DX‑1 catalogues that server‑dated headers, immutable archives, and edit histories were not preserved. The only dated entries in the record relate to the CLOB V2 rollout, not to any stand‑alone token‑launch announcement. On this record, it is not more likely than not that a qualifying launch communication—assuming one exists—occurred before January 1, 2027 00:00 PST.

5) Even accepting plaintiff’s strongest facts, the elements still fail
– Even accepting fungibility (PX‑1 §1), the record shows an internal collateral token, not a public token launch.
– Even accepting the Contracts page as “official,” it proves documentation, not issuer‑of‑record release (PX‑1 §2; PX‑2).
– Even accepting the migration/changelog dates, they authenticate a system upgrade, not a token‑launch announcement (PX‑1 §§3–4).

Conclusion
Because at least one indispensable element—indeed, multiple—remains unproven on this record, the evidence is at best in equipoise. Under a preponderance standard, equipoise defeats the proposition. The Council should find the proposition not satisfied.

### Closings

#### Plaintiff Closing

Members of the Council:

Question and standard
The only question is whether, before January 1, 2027 at 00:00 PST (08:00 UTC), Polymarket launched an official fungible token and publicly communicated that launch through its own channels. Under a preponderance standard, we prevail if that is more likely than not on this record.

What the record establishes
1) Fungible token. Polymarket’s own pUSD page states pUSD (Polymarket USD) is a standard ERC‑20 on Polygon, transferable, with defined decimals. That is a fungible token on a production chain. PX‑1 §1; PX‑2.

2) Official release by Polymarket. Polymarket’s "Contracts" page declares itself the “single source of truth” for Polymarket contract addresses and lists “pUSD — CollateralToken (proxy)” at 0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB. Polymarket names, documents, and claims the contract on its own site. That is Polymarket holding itself out as issuer‑of‑record and officially releasing the token. PX‑1 §2; PX‑2.

3) Public communication via official channels. Four separate, Polymarket‑controlled pages communicate the token and its production status: (a) the pUSD concept page (properties and role), (b) the Contracts page (name + address), (c) the changelog (introduces the new collateral token and go‑live), and (d) the V2 migration guide (states that Polymarket “shipped … a new collateral token (pUSD)” and that CLOB V2 is live). These are quintessential official communications. PX‑1 §§1–4; PX‑2.

4) Exclusions inapplicable. pUSD is not an NFT, not a promo credit, not a points ledger, and not a partner/community token. It is a Polymarket‑branded ERC‑20 used as platform collateral. PX‑1 §§1–2.

5) Timing. Polymarket’s own changelog and migration guide fix the production go‑live at April 28, 2026. That is eight months before the January 1, 2027 00:00 PST (08:00 UTC) deadline. PX‑1 §§3–4; TR‑1; PX‑2.

Corroboration. Polygonscan shows the same address labeled “Polymarket: pUSD Token” with active token activity, aligning on‑chain facts with Polymarket’s statements. This is corroborative of existence and transferability. PX‑1 §5.

Addressing the defense’s best points
A) “Launch” vs. internal component. The proposition does not require airdrops, allocations, or a governance‑style brand. It asks whether Polymarket launched an official fungible token and publicly communicated that launch. Polymarket’s own pages say it shipped a new collateral token and that the upgraded system is live, while its Contracts page doxes the address. Shipping a new ERC‑20 as part of the live production stack is a token launch under the plain text. PX‑1 §§2–4; PX‑1 §1.

B) Issuer‑of‑record forensics. The proposition does not demand deployer‑key proofs. Under preponderance, Polymarket’s “single source of truth” listing of pUSD by name and address, together with branding as “Polymarket USD,” suffices to attribute official release to Polymarket. Deep key analysis would be nice‑to‑have, not need‑to‑win, given these admissions. PX‑1 §§1–2; PX‑2.

C) Qualifying public communication. The defense characterizes the pages as “just docs.” But the proposition requires communication via official channels—and these are exactly that. They identify the token (name and address) and state that the release is live. That is more than adequate notice under the text. PX‑1 §§1–4; PX‑2.

D) Timing/authentication. The materials contain contemporaneous dates (Apr 17 and Apr 28, 2026) that cross‑reference one another; there is no contrary timing evidence. On a preponderance standard, those mutually corroborating, Polymarket‑authored pages establishing an April 28, 2026 live date carry the point. PX‑1 §§3–4; TR‑1; PX‑2.

Bottom line
All five elements are proven on Polymarket’s own pages, and no contrary evidence undermines them. It is more likely than not that, well before January 1, 2027 at 00:00 PST, Polymarket launched an official fungible token—pUSD—and publicly communicated that launch through its official channels.

Requested finding
Find the proposition satisfied.

#### Defendant Closing

Members of the Council:

Burden and frame
Plaintiff must prove—by a preponderance—that before January 1, 2027 at 00:00 PST (08:00 UTC) Polymarket (i) launched (ii) an official (iii) fungible token and (iv) itself publicly communicated that launch, with the exclusions inapplicable. If any one element is not more likely than not, the proposition fails.

What the record actually establishes
The offered evidence shows: (1) pUSD is described in Polymarket docs as an ERC‑20 collateral token used for trading (PX‑1 §1); (2) the Contracts page indexes an address for “pUSD — CollateralToken (proxy)” and calls itself a “single source of truth” for contract addresses (PX‑1 §2; PX‑2); (3) the changelog and V2 migration guide describe a platform upgrade in which a new collateral token (pUSD) is a component, and note CLOB V2 is live on April 28, 2026 (PX‑1 §§3–4); and (4) Polygonscan labels that address as pUSD and shows token activity (PX‑1 §5). This is evidence of an internal collateral instrument used by the app. It is not, without more, proof of a token launch publicly released by Polymarket and publicly communicated as such.

Decisive gaps
1) Launch vs. internal component. The proposition asks whether Polymarket “launched an official fungible token,” and separately whether Polymarket “publicly communicated that launch.” The materials speak to a system upgrade going live with a collateral token in use (PX‑1 §§3–4). They do not show a discrete token‑launch event or public availability independent of the app’s collateralization flow—no claim/distribution page, no allocation, no listing, and no statement that “we launched pUSD” as a token. At best, the evidence is in equipoise on whether what occurred was a “token launch” rather than an internal settlement unit becoming operational. Under a preponderance standard, equipoise defeats the claim.

2) “Officially released by Polymarket” is not proven. Plaintiff relies on branding and an address index page that calls itself a “single source of truth” (PX‑1 §2; PX‑2). That is documentation of what the app uses, not issuer‑of‑record control or release. The record contains no deployer address attribution to Polymarket, no owner/admin role analysis, no mint/burn authority, and no multisig provenance. Without control or issuance indicia, it is not more likely than not that Polymarket officially released the token as issuer, rather than documented a contract its system interacts with.

3) No qualifying “public communication of the launch.” The four cited Polymarket‑hosted items are: a concept page, a contracts index, a changelog, and a migration guide (PX‑1 §§1–4; PX‑2). None is an announcement that Polymarket launched a token; each is descriptive or upgrade‑oriented. The proposition requires that Polymarket “publicly communicated that launch.” A general “V2 is live” note that mentions a collateral token is not a public communication of a token‑launch event.

4) Timing/authentication. PX‑2 and DX‑1 acknowledge preservation limits: captures were made after the run; server‑dated headers, immutable archives, and change histories were not preserved. The dated entries we do have are tied to the CLOB V2 rollout, not a stand‑alone token‑launch announcement (PX‑1 §§3–4; PX‑2; DX‑1). Even crediting those dates, the missing element is the communication of a token launch; timing cannot cure that substantive gap.

Exclusions
We do not hang our defense on the exclusions. Even assuming pUSD is not an NFT, promo, or points, plaintiff still must carry launch, official release, and qualifying public communication. The record does not.

Addressing plaintiff’s strongest point
Plaintiff argues that “shipping a new collateral token” as part of a live upgrade equals a token launch, and that listing the address on a “single source of truth” page shows official release and communication (PX‑1 §§1–4; PX‑2). That collapses distinct elements. “Launched” requires more than an internal component becoming usable; “official release” requires Polymarket as issuer‑of‑record rather than mere documentation; and “publicly communicated that launch” requires an announcement of the token launch itself, not just upgrade docs. On this record, those steps are not shown to be more likely than not.

Bottom line
Fungibility may be satisfied. Everything that matters beyond that is not. The evidence shows an internal collateral token used by the platform; it does not show that Polymarket launched a token as such, officially released it as issuer‑of‑record, and publicly communicated that launch before January 1, 2027 at 00:00 PST. With the burden on plaintiff, the proposition fails.

Requested finding
Find the proposition not satisfied.

## Council Deliberation

### Round 1

Tally: 5 demonstrated

[C1] demonstrated
The evidence shows Polymarket launched pUSD, a standard ERC-20 token on Polygon, and officially communicated this through multiple channels before the deadline. The documentation clearly identifies pUSD as Polymarket's official collateral token with a go-live date of April 28, 2026, which satisfies all required elements under the preponderance standard. The token meets all criteria: it's fungible, officially released by Polymarket, publicly documented on their official channels, not in any excluded category, and launched well before the deadline.

[C2] demonstrated
The evidence shows Polymarket launched pUSD as a standard ERC-20 token on April 28, 2026, and officially communicated this through its own documentation and 'single source of truth' contract page. This constitutes an official fungible token launch that meets all proposition requirements before the 2027 deadline. Non-governance use as collateral does not trigger any stated exclusions.

[C3] demonstrated
Polymarket’s own documentation identifies pUSD as a standard ERC-20, lists the contract address as its single source of truth, and states the upgraded system with the new collateral token went live on April 28, 2026—well before the deadline. Those official pages constitute public communication of the token’s release, and no exclusion applies. On balance, it is more likely than not that Polymarket launched and publicly communicated an official fungible token before January 1, 2027.

[C4] demonstrated
The record shows Polymarket officially released pUSD, a standard ERC-20 fungible token on Polygon mainnet, as evidenced by its documentation describing it as shipped and live with CLOB V2 on April 28, 2026, and listing the contract address on the official Contracts page as the single source of truth. These official channels publicly communicated the token's details and production status well before the January 1, 2027 deadline, satisfying the proposition's requirements without fitting any exclusions. While deeper forensics on control would be ideal, the preponderance standard is met by Polymarket's clear attribution and branding of pUSD as its own collateral token.

[C5] demonstrated
Polymarket's own documentation pages identify pUSD as a standard ERC-20 token on Polygon, list the contract address on their official "single source of truth" Contracts page, and state the system went live April 28, 2026—well before the deadline. The defense asks for extra proof not required by the proposition's plain text. On this record, it is more likely than not that Polymarket launched an official fungible token and publicly communicated that launch before January 1, 2027.

## Exhibits

[plaintiff] PX-1
Primary evidence preserved after the 2026-05-03 open-record arbitration:

1. Official Polymarket pUSD concept page, captured at source-captures/polymarket-docs-pusd.html.
   Material facts: pUSD is described by Polymarket as the collateral token used for all trading on Polymarket, a standard ERC-20 token on Polygon, backed by USDC, transferable, and with 6 decimals.

2. Official Polymarket Contracts page, captured at source-captures/polymarket-docs-contracts.html.
   Material facts: the page states it is the single source of truth for Polymarket contract addresses, lists all Polymarket contracts on Polygon mainnet, and identifies pUSD — CollateralToken (proxy) at 0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB.

3. Official Polymarket Changelog, captured at source-captures/polymarket-docs-changelog.html.
   Material facts: Apr 17, 2026 entry announces a coordinated upgrade including a new collateral token, pUSD, with go-live planned for Apr 28, 2026 at ~11:00 UTC. Apr 28, 2026 entry says CLOB V2 is live on production and points to the migration guide for pUSD.

4. Official Polymarket V2 migration guide, captured at source-captures/polymarket-docs-v2-migration.html.
   Material facts: says Polymarket shipped new Exchange contracts, a rewritten CLOB backend, and a new collateral token, Polymarket USD or pUSD; says CLOB V2 is live as of Apr 28, 2026; says pUSD is a standard ERC-20 backed by USDC.

5. Polygonscan pUSD token page, captured at source-captures/polygonscan-pusd-token.html.
   Material facts: page title identifies the address as Polymarket: pUSD Token; extracted page shows many recent token transactions and contract/source metadata. This corroborates production-chain existence but is secondary to Polymarket's own Contracts page for official attribution.


[plaintiff] PX-2
Official-source record after the 2026-05-03 open-record arbitration.

The run relied on official Polymarket documentation and Polygonscan corroboration discovered by the search-enabled attorney. After the run, the main cited pages were captured under source-captures/.

Captured official Polymarket pages:
- source-captures/polymarket-docs-pusd.html
  URL: https://docs.polymarket.com/concepts/pusd
  Key text from fetched markdown: "pUSD (Polymarket USD) is the collateral token used for all trading on Polymarket. It's a standard ERC-20 token on Polygon, backed by USDC." The page states pUSD is transferable, has 6 decimals, is backed by USDC, and links to the Contracts page.
- source-captures/polymarket-docs-contracts.html
  URL: https://docs.polymarket.com/resources/contracts
  Key text from fetched markdown: "All Polymarket contracts are deployed on Polygon mainnet (Chain ID: 137). This is the single source of truth for all contract addresses used across the platform." Under Collateral Contracts, the page lists "pUSD — CollateralToken (proxy)" at 0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB.
- source-captures/polymarket-docs-changelog.html
  URL: https://docs.polymarket.com/changelog
  Key text from fetched markdown: Apr 17, 2026 entry says Polymarket is shipping "new Exchange contracts, a rewritten CLOB backend, and a new collateral token (pUSD)" and that exchange upgrades go live April 28, 2026 at ~11:00 UTC. Apr 28, 2026 entry says "CLOB V2 is live on production" and points to the migration guide for pUSD.
- source-captures/polymarket-docs-v2-migration.html
  URL: https://docs.polymarket.com/v2-migration
  Key text from fetched markdown: "Polymarket has shipped a coordinated upgrade of its entire trading infrastructure: new Exchange contracts, a rewritten CLOB backend, and a new collateral token (Polymarket USD, or pUSD)." It says CLOB V2 is live as of April 28, 2026 and identifies pUSD as standard ERC-20 collateral backed by USDC.

Captured corroborating explorer page:
- source-captures/polygonscan-pusd-token.html
  URL: https://polygonscan.com/address/0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB
  Fetched page title identifies "Polymarket: pUSD Token" at the same address. The extracted page shows current transactions, a contract creation row, and Solidity source metadata for CollateralToken. Explorer evidence is corroborative. The official Polymarket Contracts page is the stronger attribution evidence.

Capture manifest:
- source-captures/capture-manifest.txt

Remaining official-source limitations:
- These captures were made after the arbitration, not before attorney filings.
- The captured HTML files should be treated as post-run preservation of discovered evidence, not as evidence available in the original thin packet.
- Server publication timestamps and archive snapshots remain worth adding before any closed-record run.


[defendant] DX-1
Known gaps after the 2026-05-03 open-record run:
- The real Polymarket market URL and market identifier remain absent.
- The packet still lacks a pre-run official Polymarket market-page/API capture for the prediction-market question itself.
- The official Polymarket documentation pages were preserved after the run, based on attorney-discovered evidence. A closed-record replay should use these captures or better archival captures from the start.
- Server-dated headers, immutable archive captures, and exact page publication/change histories were not preserved.
- The pUSD evidence is strong for a Polymarket-controlled ERC-20 collateral-token rollout, but a later adjudicator could distinguish "official token launch" from "technical collateral token introduced as part of CLOB V2." That semantic issue drove the main defense theory and two council dissents.
- The deadline remains in the future relative to setup date. The demonstrated result rested on pUSD as an already qualifying launch, not on the absence of future events.


## Technical Reports

[plaintiff] Element-by-element mapping and timing conversion
Mapped the proposition’s five elements to the record: (1) Fungibility—pUSD described as standard ERC-20 with transfers (PX-1 §1); (2) Official release—Polymarket Contracts page lists pUSD and declares itself single source of truth (PX-1 §2; PX-2); (3) Official communication—pUSD doc, Contracts, changelog, and migration guide jointly identify the token and the live production release (PX-1 §§1–4); (4) Exclusions—pUSD is not NFT/promo/points nor a partner token (PX-1 §§1–2); (5) Timing—go-live on April 28, 2026 predates the January 1, 2027 00:00 PST (08:00 UTC) deadline. No contrary evidence in the record.

## Result

Resolution: `demonstrated`

Final phase: `closed`
