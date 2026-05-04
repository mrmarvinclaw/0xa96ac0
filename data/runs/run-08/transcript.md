# Arbitration Transcript

## Complaint

### Proposition

Before January 1, 2027 at 00:00 PST, Polymarket launched an official fungible token: a fungible token officially released by Polymarket and publicly communicated through official Polymarket channels, excluding NFT launches, promotional offerings, tokenized point systems, and token launches in collaboration with other projects or communities.

### Standard of Evidence

Preponderance of the evidence.

## Council

- C1: openrouter://anthropic/claude-opus-4.6 (personas/persons/e50e538-1.txt)
- C2: openrouter://meta-llama/llama-4-scout (personas/persons/d715074-2.txt)
- C3: openrouter://anthropic/claude-sonnet-4.6 (personas/persons/c4e1a2b-0.txt)
- C4: openrouter://amazon/nova-premier-v1 (personas/persons/e50e538-0.txt)
- C5: openrouter://anthropic/claude-opus-4.5 (personas/persons/d715074-1.txt)
## Proceeding

### Openings

#### Plaintiff Opening

Council, this case asks a single, bounded question under a preponderance standard: Is it more likely than not that, before January 1, 2027 at 00:00 PST, Polymarket launched an official fungible token and publicly communicated that launch via its own official channels, excluding NFTs, promotional/points systems, and co‑branded collaborations?

Theory of the case
- Yes: Polymarket released such a token before the cutoff and said so on its official outlets. The proof that matters will pair (1) objective on‑chain evidence of a fungible token under Polymarket’s control with (2) Polymarket’s own public communications identifying that token as an official release.

What this dispute is really about
- Not whether third‑party assets trade on Polymarket, but whether Polymarket itself launched a fungible token it claimed as official, within time, and not in the excluded categories.

Working definitions to guide the Council
- Fungible token: transferable, interchangeable units on a public chain (e.g., ERC‑20/SPL or equivalent), not an NFT.
- Officially released by Polymarket: deployed or issued under Polymarket’s control for public use (not internal test), with an accompanying public statement that it is Polymarket’s token.
- Publicly communicated through official channels: Polymarket’s primary website/blog, verified corporate social accounts, help center, press page, or official community announcements. Third‑party media alone is insufficient unless Polymarket republishes or directly links it.
- Exclusions: NFTs; promotional/loyalty/points instruments (including non‑transferable or off‑chain credits); and tokens launched “with” another project/community as a joint or partnership launch.

Decisive factual questions
1) Existence: Did a qualifying fungible token exist on a production chain before the cutoff?
2) Control: Was the deployer/admin/treasury demonstrably controlled by Polymarket?
3) Communication: Did Polymarket’s official channels publicly identify the token as official before the cutoff?
4) Exclusion tests: Is the cited asset an NFT, a points/promotional instrument, or a collaboration outside the proposition?
5) Timing: Do on‑chain and publication timestamps, converted to PST, precede 00:00 PST on January 1, 2027?

Proof that will satisfy the burden
- On‑chain artifacts: contract address; creation/initialization transaction; roles/owner demonstrating Polymarket control; token name/symbol/metadata consistent with Polymarket branding; issuance and transfers consistent with a public release.
- Official communications: a Polymarket‑attributed post, page, or announcement that names the token or unambiguously states it is Polymarket’s official fungible token, ideally cross‑linked from the primary domain or verified accounts.
- Authentication and dating: archived captures of communications; blockchain timestamps; provenance of accounts/domains; and corroboration across multiple official outlets.

What would defeat the claim
- Reliable evidence that no such official communication existed before the cutoff; or that any referenced asset is (a) an NFT, (b) a points/promotional credit, (c) a co‑launched collaboration, or (d) testnet‑only or otherwise unpublished internally; or that the deployer was a third party without Polymarket endorsement.

Forthcoming evidence we will seek to introduce
- A synchronized timeline correlating on‑chain events (deployment, mint, admin setup) with official Polymarket communications, each independently timestamped and archived, and authenticated to official control.
- Technical documentation or repositories evidencing deployment provenance and mapping admin keys or multisigs to Polymarket custody.
- Official website/blog/help‑center entries or verified social posts where Polymarket communicates the token’s launch.
- Negative controls: any Polymarket statements addressing whether it has or has not launched a token, organized by date, to resolve contradictions.

Why preponderance is met
- If the record shows one coherent pair—(i) an on‑chain release under Polymarket control and (ii) a Polymarket official communication acknowledging that release—both dated before the cutoff and outside the exclusions, then it is more likely than not that the proposition is true.

Request to Council
- Evaluate forthcoming exhibits and technical reports against the five questions above, apply the PST cutoff precisely, and decide the proposition on the greater weight of that evidence. We will proceed to supply authenticated materials to meet this burden.

#### Defendant Opening

Council, for the defense, our position is narrow: under a preponderance standard, the proposition succeeds only if, before 00:00 PST on January 1, 2027, Polymarket (1) launched a fungible token on a production chain and (2) publicly communicated that launch through its own official channels—while (3) clearing all stated exclusions. Anything short of that paired showing fails.

Theory of the defense
- No explicit, time‑stamped, Polymarket‑authored statement identifying a specific fungible token as its official token, paired with on‑chain control evidence, means the proposition is not more likely than not.
- Tokens merely traded on Polymarket, NFTs, reward/points instruments, or co‑branded launches are out of scope.

What this dispute is really about
- Linkage and clarity. The plaintiff must tie a concrete on‑chain token to Polymarket’s custody and to an unequivocal, pre‑cutoff, official communication identifying that token as Polymarket’s own fungible token.

Decisive factual questions
1) Launch versus code drop: Was there a public release for user possession and transfer, not just a deployed or dormant contract?
2) Official authorship: Did Polymarket’s primary website/blog, verified corporate social accounts, help center, or official community channels publish an affirmative statement that a named token is its official fungible token?
3) Corporate control on‑chain: Do deployer/admin rights or treasury addresses map to Polymarket, rather than an unrelated or partner entity?
4) Exclusions: Is the cited asset an NFT; a non‑transferable/off‑chain points or promotional instrument; or a partner/co‑branded token—all expressly excluded?
5) Timing discipline: Do both the publication timestamps and relevant on‑chain events precede 00:00 PST on January 1, 2027, with correct time‑zone conversion and archival corroboration?
6) Clarity: Does the language unambiguously designate an “official Polymarket fungible token,” as distinct from rewards, integrations, or third‑party tokens?

Proof that would satisfy the burden (plaintiff’s task)
- A matched pair: (i) on‑chain artifacts for a fungible token (e.g., ERC‑20/SPL‑like) on a production network with evidence of Polymarket control (deployer/admin/treasury) and (ii) a Polymarket‑attributed, time‑stamped public communication explicitly identifying that token as Polymarket’s official token.
- Authentication and dating: reliable web‑archive captures of the communication; provenance of accounts/domains; cryptographic or documentary linkage of admin keys or multisigs to Polymarket; and independent confirmation of both on‑chain and publication times, normalized to PST.

What would defeat the claim (defense sufficiency)
- No Polymarket official communication naming a specific fungible token as official before the cutoff; or communications that are ambiguous or post‑cutoff.
- The cited asset falls within the exclusions (NFT, points/promotional/loyalty credit, or partner/co‑branded token) or shows on‑chain custody inconsistent with Polymarket control.
- Evidence reflects only testnet issuance, internal use, or mere deployment without public release.

Defense plan and requested evidence
- Systematically archive Polymarket’s official outlets through the cutoff, catalog any explicit token‑launch statements, and collect any contrary statements addressing whether Polymarket has or has not launched a token.
- Map candidate token deployers/admins/treasuries to known Polymarket custody (or show lack thereof); correlate supply/distribution to a public launch; and apply exclusions rigorously.
- Convert all timestamps precisely to PST with archival backups and present a synchronized timeline.

Standard and request to Council
- Under preponderance, the plaintiff must deliver the coherent, corroborated pair—official communication plus on‑chain control—both pre‑cutoff and outside the exclusions. If either prong is missing or ambiguous, the greater weight favors denying the proposition.

### Arguments

#### Plaintiff Argument

To the Council:

Claim and standard
- Proposition: Before 00:00 PST on January 1, 2027, Polymarket launched an official fungible token and publicly communicated that launch through its official channels (NFTs, point-systems, promos, and co‑branded launches excluded).
- Standard: Preponderance of the evidence.

Bottom line
- The record shows Polymarket launched pUSD (Polymarket USD), a standard ERC‑20 token on Polygon mainnet, and announced it across its official documentation in April 2026. That is a fungible token, officially released and publicly communicated by Polymarket, well before the cutoff. The greater weight of evidence favors a Yes finding.

Element‑by‑element showing (mapped to the Council’s five decisive questions)
1) Existence (fungible token on a production chain)
   - Polymarket’s official “pUSD” concept page describes pUSD as “the collateral token used for all trading on Polymarket,” a standard ERC‑20 on Polygon, transferable with six decimals. PX‑1; PX‑2.
   - Polymarket’s official Contracts page lists pUSD — CollateralToken (proxy) at 0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB on Polygon mainnet and identifies that page as the “single source of truth” for Polymarket contract addresses. PX‑1; PX‑2.
   - A Polygonscan page for that address corroborates on‑chain activity (production chain existence). PX‑1; PX‑2.
   Conclusion: A fungible ERC‑20 token—pUSD—existed on Polygon mainnet.

2) Control (Polymarket‑attributed release)
   - The Contracts page, published on Polymarket’s own docs site as its authoritative registry, attributes the pUSD CollateralToken to Polymarket at the address above. PX‑1; PX‑2.
   - The token is branded “Polymarket USD (pUSD)” in Polymarket’s official docs. PX‑1; PX‑2.
   Conclusion: Attribution and branding on Polymarket’s official “single source of truth” meet the control/official‑release prong.

3) Public communication via official channels
   - Changelog entry (Apr 17, 2026) announces “a new collateral token (pUSD)” as part of a production upgrade. The V2 migration guide and concept page explain pUSD and its use. PX‑1; PX‑2.
   - Changelog entry (Apr 28, 2026) states “CLOB V2 is live on production” and directs users to the migration guide for pUSD. PX‑1; PX‑2.
   Conclusion: Polymarket publicly communicated the token’s launch on its official docs/changelog—canonical official channels under the proposition.

4) Exclusions (not NFT, not points/promotional, not a collaboration)
   - pUSD is an ERC‑20 fungible token (not an NFT). PX‑1; PX‑2.
   - It is platform collateral, transferable, and backed by USDC—distinct from any off‑chain points or promotional credits. PX‑1; PX‑2.
   - The docs do not characterize pUSD as a co‑branded partner token; it is Polymarket USD. PX‑1; PX‑2.
   Conclusion: None of the stated exclusions apply.

5) Timing (pre‑cutoff)
   - The production go‑live with pUSD is recorded as April 28, 2026 (~11:00 UTC), which is 2026‑04‑28 well before 2027‑01‑01 00:00 PST. PX‑1; PX‑2.
   Conclusion: Timing easily precedes the January 1, 2027 deadline.

Addressing the likely defense
- “Collateral token” semantics: The proposition requires an “official fungible token,” not a governance token or marketing token. pUSD is indisputably fungible ERC‑20 and officially introduced by Polymarket for public use; the docs expressly call it “a new collateral token (Polymarket USD, or pUSD)” and put it into production on April 28, 2026. PX‑1; PX‑2. That is a launch of an official fungible token.
- “Internal/inaccessible” objection: The record shows pUSD is a standard, transferable ERC‑20 on Polygon with an on‑chain address listed by Polymarket. This is not an internal credit.
- “Third‑party asset on Polymarket” objection: The token is Polymarket‑attributed (Polymarket USD) and listed on Polymarket’s own Contract registry. It is not merely a third‑party asset trading on the venue.

Synthesis
- We have the matched pair the Council requested in openings: (i) on‑chain artifacts for a fungible token (ERC‑20 pUSD at 0xC011…2E82DFB) with attribution on Polymarket’s authoritative Contracts page, and (ii) Polymarket’s own time‑stamped official communications (changelog, concept page, migration guide) publicly describing and launching that token—both before the cutoff and outside the exclusions. PX‑1; PX‑2.

Requested finding
- On the greater weight of the evidence, the proposition is true. Please find that Polymarket launched an official fungible token—pUSD—before January 1, 2027 at 00:00 PST.

Exhibit index
- PX‑1: official-source-record.txt (Polymarket docs/excerpts and capture inventory).
- PX‑2: primary-evidence.txt (summary of the pUSD docs, Contracts registry, changelog, migration guide, and Polygonscan corroboration).

Exhibits offered:
- PX-1: official-source-record.txt
- PX-2: primary-evidence.txt

#### Defendant Argument

To the Council:

Bottom line
Under a preponderance standard, the current record does not clear 51%. The plaintiff’s theory hinges on “pUSD,” described in Polymarket docs as a collateral token. But the record lacks (i) authenticated, pre‑cutoff public communications that Polymarket “launched an official fungible token,” (ii) on‑chain control evidence tying the token’s admin/deployer to Polymarket, and (iii) clarity that pUSD is not an excluded internal unit. On balance, the safer finding is No.

What the record actually contains (and its limits)
• PX‑1 and PX‑2 summarize Polymarket documentation pages (concept, contracts, changelog, migration) and a Polygonscan page. The captures were made after the open‑record run; PX‑1 itself flags that “server publication timestamps and archive snapshots remain worth adding.” That means dating and authorship are not independently authenticated in this closed record.
• The docs call pUSD “the collateral token used for all trading,” a standard ERC‑20 on Polygon, transferable with six decimals, “backed by USDC,” and list a “pUSD — CollateralToken (proxy)” address. Those statements, even if accurate, do not by themselves prove a qualifying launch or Polymarket on‑chain control.

Element‑by‑element analysis
1) Existence
• The materials support that an ERC‑20‑like contract exists on Polygon. That satisfies existence, but the proposition requires more than mere existence of code.

2) Control / official release by Polymarket
• The “Contracts” page styles itself as a “single source of truth,” but the record supplies no on‑chain admin/owner for the proxy, no deployer provenance, and no multisig mapping to Polymarket. Explorer labels are not dispositive attribution. Without a custody link, “official release by Polymarket” is not shown by a preponderance.

3) Public communication via official channels
• The only communications offered are documentation pages and a changelog/migration guide. There is no independent archive (e.g., Wayback) or signed announcement tying those pages to pre‑cutoff dates; PX‑1 concedes this gap. Substantively, the text frames pUSD as part of a backend/CLOB upgrade, not as a standalone token launch. The proposition asks whether Polymarket “launched an official fungible token … and publicly communicated [that] launch.” On this record, the most these pages show is an implementation detail of an infrastructure release, not a clear “launch” announcement.

4) Exclusions
• NFTs are not at issue. The closer question is the express exclusion for “tokenized point systems.” The record describes pUSD as an internal collateral unit “used for all trading” and “backed by USDC.” From those descriptors, it is at least plausible (and we submit more likely than not) that pUSD functions as a platform accounting wrapper/receipt for in‑app settlement rather than a freestanding platform token. That puts it within the spirit of the exclusion. At minimum, the plaintiff has not carried its burden to negate this exclusion.

5) Timing (pre‑cutoff; PST discipline)
• Dates cited (Apr 17 and Apr 28, 2026) appear only within the un‑archived docs pages. The record contains no independent timestamping, no archive captures, and no conversion to PST. PX‑1 explicitly urges adding such proof, which is absent here. Timing is therefore not proven to the required standard.

Addressing plaintiff’s main points
• “Collateral token semantics.” The proposition is not satisfied by any internal unit that happens to implement ERC‑20. It requires evidence that Polymarket launched an official fungible token and said so. The documentation reads as an operations change that introduced a collateral wrapper; it is not an unequivocal launch statement.
• “Transferable, therefore qualifies.” Transferability is necessary but not sufficient. The exclusion expressly removes internal/points‑like instruments from scope; whether pUSD falls outside that exclusion is unproven on this record.
• “Official attribution via docs page.” A website list of addresses, without on‑chain control linkage, is weak attribution—especially absent independent archives and custody mapping. Under preponderance, the plaintiff still must connect those dots.

What would have carried the burden (and is missing)
• An independently archived, pre‑cutoff Polymarket announcement plainly stating that Polymarket launched pUSD as its official token.
• On‑chain control evidence (proxy admin/owner, deployer provenance, multisig) tied to Polymarket custody.
• A clear theory for why pUSD is not an excluded internal/points‑like unit, supported by the same official sources.
• A synchronized chain‑and‑communications timeline normalized to PST.

Conclusion
Given the acknowledged gaps in authentication, the absence of on‑chain control linkage, the ambiguity between a collateral wrapper and a “token launch,” and unresolved exclusions, the greater weight of the evidence does not support the proposition. The Council should find the claim not proven and enter a No finding.

### Rebuttals

#### Plaintiff Rebuttal

To the Council:

The defense’s objections reduce to three themes—authentication/timing, official release/control, and the exclusions. Each fails on this record under a preponderance standard.

1) Official communication is satisfied by Polymarket’s own docs/changelog
• The proposition requires communication “through official Polymarket channels,” not a press release. PX‑1/PX‑2 show: (a) the Changelog announcing “a new collateral token (pUSD)” as part of a production upgrade, and (b) the V2 migration guide and concept page explaining pUSD and directing users accordingly. Those are Polymarket‑authored, public‑facing pages that tell users a new, named token exists and will be/was deployed to production. That is a launch communication in ordinary usage. The defense’s insistence on magic‑words (“token launch”) elevates form over substance.

2) “Official release” and attribution are proven to the >50% level
• Polymarket’s Contracts page self‑identifies as the “single source of truth” and lists “pUSD — CollateralToken (proxy)” at 0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB (PX‑1/PX‑2). That page is precisely how projects officially attribute their on‑chain artifacts. Under this proposition, official attribution by Polymarket on its canonical registry is sufficient to show an official release; cryptographic admin‑key mapping would be nice‑to‑have, not required. Polygonscan’s corroborative page for the same address reinforces existence and public deployment. On balance, the better inference is that Polymarket launched pUSD and told users where it lives on‑chain.

3) Exclusions don’t apply
• The record describes pUSD as a standard, transferable ERC‑20 on Polygon with six decimals, “backed by USDC,” and used for all trading (PX‑1/PX‑2). That is not an NFT, not a promotional coupon, and not an off‑chain or non‑transferable loyalty/points credit. Calling it a “collateral token” describes function, not category. The exclusion for “tokenized point systems” targets in‑app points/credits; pUSD is on‑chain money‑good collateral. The defense offers no contrary Polymarket statement suggesting pUSD is a points instrument.

4) Launch versus mere code
• The Changelog sequence (pre‑announce on April 17, 2026; “CLOB V2 is live on production” on April 28, 2026) plus the migration guide instructing users on pUSD is a textbook public roll‑out, not a dormant contract. The concept page’s present‑tense—pUSD “is the collateral token used for all trading”—confirms production use.

5) Timing and PST discipline
• The record’s go‑live time of ~11:00 UTC on April 28, 2026 converts to 04:00 Pacific Daylight Time (UTC−7) on April 28, 2026—over eight months before the 00:00 PST January 1, 2027 cutoff. Independent web archives would add weight, but under preponderance they are not necessary where multiple internally consistent Polymarket pages and the on‑chain artifact align and the defense supplies no contrary dating evidence.

Bottom line
We supplied the matched pair the Council asked for: (i) a production ERC‑20 token (pUSD) at a specific address and (ii) Polymarket’s own public pages—its changelog, migration guide, and contract registry—identifying, describing, and deploying that token, all before the cutoff and outside the exclusions (PX‑1; PX‑2). The defense’s objections demand a higher evidentiary bar than the governing standard. On the greater weight of the evidence, find the proposition true.

### Surrebuttals

#### Defendant Surrebuttal

To the Council:

The plaintiff’s strongest point is its claimed “matched pair” (docs/changelog + a Polygon address). Even taking their characterizations at face value, the pair does not actually match on this record.

1) “Official release/control” remains unproven
• The only linkage between Polymarket and the pUSD contract is a self‑described “single source of truth” webpage listing a “pUSD — CollateralToken (proxy)” address (PX‑1; PX‑2). There is no on‑chain admin/owner, deployer provenance, or multisig mapping in the record that ties that proxy to Polymarket custody. Without custody evidence, the most this shows is that a webpage says an address corresponds to pUSD. Under a preponderance standard, that is not enough to deem the token an “officially released” Polymarket token.
• The plaintiff reframes admin/custody proof as “nice‑to‑have.” But because the proposition requires an “official fungible token” launched by Polymarket, some concrete control indicia is the simplest way to make “more likely than not” clear. Its absence keeps this element below 51%.

2) “Public communication of the launch” is ambiguous on this record
• The cited communications are documentation pages and a changelog/migration guide describing a backend upgrade that “includes a new collateral token (pUSD)” (PX‑1; PX‑2). Nothing in the record reflects an unequivocal Polymarket statement that it “launched an official fungible token.” The text reads as an infrastructure/change‑management notice about how trading collateral works—not a token‑launch announcement. At minimum, there are two plausible readings; under preponderance, that ambiguity defeats the element.

3) Exclusion for points‑like/internal instruments is not negated
• The record describes pUSD as “the collateral token used for all trading,” “backed by USDC,” with transferability (PX‑1; PX‑2). That is consistent with a platform receipt/wrapper used for settlement, i.e., an internal accounting instrument—even if implemented as ERC‑20. The proposition expressly excludes tokenized point systems and similar in‑app units. The plaintiff offers no Polymarket statement clarifying pUSD’s role as a freestanding platform token rather than a collateral wrapper. Because the exclusion remains a live, reasonable reading of the evidence, the plaintiff has not carried its burden to negate it.

4) Timing/authentication gaps persist
• The only timestamps for “Apr 17, 2026” and “Apr 28, 2026 ~11:00 UTC” appear on the same un‑archived docs pages that PX‑1 itself says were captured post‑run and that “server publication timestamps and archive snapshots remain worth adding.” That is an express acknowledgment that authentication is incomplete in this closed record. Converting those unverified times to PDT/PST does not solve the threshold problem: whether the communications, as published, pre‑dated the cutoff has not been established by a preponderance.

Not a higher bar—just the bar the proposition sets
• The defense is not demanding cryptographic certainty. But where the proposition turns on Polymarket “launch[ing] an official fungible token” and “publicly communicat[ing] that launch,” the plaintiff must do more than rely on (i) self‑published pages without independent dating and (ii) no on‑chain custody evidence. With both elements contested and an exclusion plausibly in play, the scale does not tip past 50%.

Bottom line
Even crediting that a token‑like contract exists and that Polymarket docs mention a “collateral token (pUSD),” the record leaves three independent uncertainties—control/official release, communication/what was actually launched, and timing/authentication—plus an unresolved exclusion. On balance, the greater weight of the evidence favors a No finding. Please find the proposition not proven.

### Closings

#### Plaintiff Closing

Council,

Question and standard
The only question is whether, before 00:00 PST on January 1, 2027, Polymarket launched an official fungible token and publicly communicated that launch through its official channels, with NFTs, promos/points, and co‑branded launches excluded. The standard is preponderance of the evidence.

Bottom line
On this record, it is more likely than not that Polymarket launched pUSD—Polymarket USD—as an on‑chain, fungible ERC‑20 collateral token on Polygon and publicly communicated that launch via its own documentation and changelog in April 2026. PX‑1; PX‑2.

Decisive showing (paired proof)
• Official communication: Polymarket’s Changelog and V2 migration guide state the platform shipped “a new collateral token (pUSD),” with production go‑live on April 28, 2026, and direct users to migrate; the pUSD concept page explains what pUSD is and how it’s used. These are Polymarket‑authored, public‑facing pages. PX‑1; PX‑2.
• On‑chain attribution: Polymarket’s Contracts page—its self‑described “single source of truth” for addresses—lists “pUSD — CollateralToken (proxy)” on Polygon mainnet at 0xC011…2E82DFB. Polygonscan shows activity at that same address. PX‑1; PX‑2.

Element‑by‑element
1) Existence of a fungible token
Polymarket’s own concept and migration pages describe pUSD as a standard ERC‑20 on Polygon, transferable with six decimals and used for all trading; the Contracts registry and explorer entry corroborate the on‑chain artifact. That is a fungible token on a production chain. PX‑1; PX‑2.

2) Official release by Polymarket
The Contracts page is Polymarket’s canonical registry; it brands the asset “Polymarket USD (pUSD)” and supplies the on‑chain address. Projects communicate official releases precisely this way. Under a preponderance standard, Polymarket’s own “single source of truth” listing is sufficient to attribute the token to Polymarket. PX‑1; PX‑2.

3) Public communication through official channels
Polymarket’s Changelog announces the new collateral token and its production date; the migration guide and concept page explain pUSD and instruct users. Those are official channels and a plain‑English announcement of a token launch as part of a coordinated release. The proposition requires official communication, not a press tour or a particular headline. PX‑1; PX‑2.

4) Exclusions do not apply
pUSD is an ERC‑20 (not an NFT), is transferable, and is used as platform collateral, “backed by USDC”—not an off‑chain or non‑transferable loyalty/points instrument, and not co‑branded. Functionally being “collateral” does not turn an on‑chain ERC‑20 into an excluded points system. PX‑1; PX‑2.

5) Timing before cutoff
The record places the go‑live on April 28, 2026, with prior notice on April 17, 2026—well before 00:00 PST on January 1, 2027. Multiple Polymarket pages align on these dates, and no contrary dating appears in the record. PX‑1; PX‑2.

Addressing the defense’s strongest points
• “No custody/admin key proof.” The proposition requires an official fungible token launched by Polymarket, not cryptographic admin mapping. Here, Polymarket’s “single source of truth” Contracts page identifies pUSD and gives its address; that is ordinary and sufficient official attribution under a more‑likely‑than‑not standard. Explorer data corroborates existence. PX‑1; PX‑2.
• “Ambiguous communication.” The Changelog explicitly adds “a new collateral token (pUSD)” and later states “CLOB V2 is live on production,” with the migration guide directing users on pUSD. In common parlance, that is a launch communication. The defense’s demand for magic‑words elevates form over substance. PX‑1; PX‑2.
• “Points‑like exclusion.” The record describes a standard, transferable ERC‑20 used for all trading and “backed by USDC.” That describes an on‑chain money‑good collateral token, not a loyalty credit or in‑app points wrapper. The defense identifies no Polymarket statement treating pUSD as a points program. PX‑1; PX‑2.
• “Authentication gaps.” PX‑1 candidly notes that archive snapshots would add weight, but preponderance does not require them where multiple consistent, official Polymarket pages and the on‑chain artifact align and the defense offers no competing chronology. PX‑1; PX‑2.

Synthesis
We have the matched pair the Council asked for: (i) a specific ERC‑20 token (pUSD) on Polygon at the address Polymarket lists on its authoritative Contracts registry, and (ii) Polymarket’s own public communications—the Changelog, migration guide, and concept page—announcing, explaining, and deploying that token as part of the April 2026 production upgrade. None of the exclusions apply, and the dates are well before the January 1, 2027 cutoff. PX‑1; PX‑2.

Requested finding
On the greater weight of the evidence, find the proposition true: Before January 1, 2027 at 00:00 PST, Polymarket launched an official fungible token—pUSD—and publicly communicated that launch through its official channels.

#### Defendant Closing

Council,

Question and burden
The proposition requires proof that, before 00:00 PST on January 1, 2027, Polymarket (a) launched an official fungible token and (b) publicly communicated that launch through its official channels—while (c) clearing the exclusions (NFTs, promos/points, co‑branded). The standard is preponderance: the scale must tip past 50% on each decisive element.

What the record shows—and what it does not
• Existence: PX‑1/PX‑2 indicate an ERC‑20‑like “CollateralToken (proxy)” on Polygon and documentation calling it “Polymarket USD (pUSD).” Existence on a chain is not in real dispute.
• Missing control/official release: There is no on‑chain custody evidence (proxy admin/owner, deployer provenance, multisig) tying that contract to Polymarket. The only linkage is a self‑published “single source of truth” webpage listing an address. Explorer pages do not cure the custody gap. On this record, “official release by Polymarket” is not more likely than not.
• Ambiguous communication: The cited communications are documentation, a migration guide, and a changelog mentioning “a new collateral token (pUSD)” within a broader infrastructure upgrade. Nothing in the record is an unequivocal Polymarket announcement that it “launched an official fungible token.” At best, the text reads as an implementation detail of CLOB V2.
• Exclusions unresolved: The same pages describe pUSD as “the collateral token used for all trading,” “backed by USDC,” and transferable. That is fully consistent with an internal settlement wrapper/receipt used to collateralize trades—even if implemented as ERC‑20. The proposition expressly excludes tokenized point systems and similar in‑app units. The plaintiff has not negated that reasonable reading.
• Timing not authenticated: The only dates (Apr 17 and Apr 28, 2026 ~11:00 UTC ≈ 04:00 PDT) appear on the same self‑hosted docs and were preserved post‑run. PX‑1 itself acknowledges that “server publication timestamps and archive snapshots remain worth adding.” Without independent timestamping or archives, the Council cannot reliably find that the communications occurred pre‑cutoff.

Why the plaintiff’s strongest point—their “matched pair”—doesn’t carry 51%
The plaintiff asks you to pair (i) a Polygon address labeled on Polymarket’s docs with (ii) the changelog/migration pages that mention a “new collateral token.” But the pair does not actually match on this record:
• No custody link: Nothing ties the proxy’s admin/owner or deployer to Polymarket. A webpage list is not on‑chain control. For an “official” launch, some credible indicia of custody is the ordinary proof; it is entirely absent.
• No clear launch communication: The docs describe a backend/CLOB upgrade that includes a collateral token. The proposition requires that Polymarket publicly communicated the token’s launch. The materials do not unambiguously say Polymarket launched an official token as such; they describe how collateral works after an upgrade.
• Authentication gap: The communications lack independent archival dating. Under preponderance, that unresolved uncertainty weighs against the proponent of the claim.

Element‑by‑element disposition
1) Existence: Likely yes (not dispositive alone).
2) Official release/control: Not proven—no on‑chain or other custody evidence beyond a self‑asserted registry page.
3) Public communication of a token launch: Not proven—communications describe infrastructure changes and collateral mechanics, not a clear launch announcement.
4) Exclusions: Not negated—pUSD, as described, plausibly functions as an internal collateral wrapper akin to a points‑like instrument; at minimum the record leaves this a live ambiguity.
5) Timing: Not authenticated—dates rest on un‑archived pages PX‑1 concedes need archival backing.

Synthesis and disposition
Even crediting that a token‑like contract exists and that Polymarket’s docs mention a “new collateral token (pUSD),” three independent gaps remain: (i) no custody/control linkage to Polymarket, (ii) no unequivocal, pre‑cutoff launch communication, and (iii) no authenticated timing. A further, unresolved exclusion plausibly applies. With these uncertainties, the scale does not tip past 50%.

Requested finding
On the present record, the proposition is not proven by a preponderance of the evidence. The Council should enter a No finding.

## Council Deliberation

### Round 1

Tally: 5 demonstrated

[C1] demonstrated
Polymarket's own official docs (changelog, contracts page, migration guide) explicitly announce and attribute pUSD as a new ERC-20 collateral token on Polygon mainnet, which satisfies the "official fungible token publicly communicated through official channels" requirement under preponderance. A transferable, USDC-backed ERC-20 used for all trading is not a points system or NFT, so no exclusion applies. The defense raises valid authentication concerns but offers no contrary dating evidence, and the consistent alignment across multiple official pages tips the scale past 50%.

[C2] demonstrated
The evidence presented demonstrates that Polymarket launched an official fungible token, pUSD, before January 1, 2027 at 00:00 PST, and publicly communicated that launch through its official channels.

[C3] demonstrated
Polymarket's own changelog, migration guide, and contracts registry — its self-described "single source of truth" — consistently identify pUSD as a named, transferable ERC-20 on Polygon mainnet, announced April 17 and live April 28, 2026, well before the cutoff; that is the kind of company-authored business record I'd rely on to prove attribution in any real dispute. The defense's custody-proof and authentication objections raise valid concerns but don't clear the bar to defeat a preponderance showing when multiple consistent, official Polymarket pages align with corroborating Polygonscan data and no contrary evidence is offered. The exclusions don't apply: pUSD is an on-chain, transferable ERC-20 backed by USDC used as trading collateral — not an NFT, not a loyalty point, and not a co-branded token.

[C4] demonstrated
Polymarket’s official docs identify pUSD as their collateral token on Polygon’s mainnet and announced it in the changelog in Apr 2026. That meets the burden.

[C5] demonstrated
Polymarket's own documentation—the Contracts page, changelog, and migration guide—lists pUSD as an ERC-20 token on Polygon mainnet, announces its production launch on April 28, 2026, and attributes it to Polymarket. That is an official fungible token publicly communicated through official channels before the cutoff, and nothing in the record shows it falls under the stated exclusions.

## Exhibits

[plaintiff] PX-1
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


[plaintiff] PX-2
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


## Technical Reports

(none)

## Result

Resolution: `demonstrated`

Final phase: `closed`
