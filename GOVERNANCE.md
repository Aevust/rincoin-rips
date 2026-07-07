```
  Document: GOVERNANCE.md
  Title: Version Numbering and Core Role Governance
  Author: Aevust <edu@aevust.org>
  Status: Active (normative by incorporation into RIP-0001)
  Created: 2026-07-07
  Extracted-From: RIP-0001 (Created 2026-04-22)
  License: CC0-1.0
  Canonical-URL: https://rips.rincoin.org
  Repository: https://github.com/Aevust/rincoin-rips
```

---

## Authority and Amendment

This document specifies the governance framework for Rincoin Core releases and the human roles responsible for them: the Core Role structure, the Version Numbering Scheme and Version Authority, Network Ratification of Release Candidates, the Change Submission Discipline and Emergency Exception, Vacancy Determination, and Succession.

Its normative content was drafted and ratified as sections of RIP-0001 and was relocated to this file on 2026-07-07 without normative change, to keep RIP-0001 focused on the RIP process itself. This document is **incorporated by reference into RIP-0001** and carries the same normative force as that RIP. Amendments to this document follow the same process, submission discipline, and recording requirements as amendments to RIP-0001. Relocation does not alter the ratification status of any provision.

The terms **Founder**, **Core Role holder**, and **Core Strategic Authority** used throughout the RIP process are defined in this document.

---

## Version Numbering and Core Role Governance

Rincoin Core software releases and the human roles responsible for them are governed by an integrated scheme that links the protocol's long-horizon design philosophy (the ~400-year Proof of Rinne epoch) to practical software lifecycle management and personnel continuity.

---

### Core Roles

The following four roles constitute the Core Strategic Authority of Rincoin:

| Role | Responsibilities |
|------|------------------|
| **Core Technical Lead** | Lead protocol development; owner or administrator rights to the official Core repository; final technical reviewer and merger of Core software updates. Authority to approve consensus-affecting (MAJOR/GENERATION) changes is governed by the Version Authority table, not by this role individually. |
| **Core Authority Lead** | Responsible for official infrastructure (domains, servers, public-facing channels) and overall strategic direction. |
| **Core Research Lead** | Responsible for protocol research, academic output, and whitepaper maintenance. |
| **Principal Architect** | Cross-functional support for the above three roles in development, research, and strategic activities. |

A single individual MAY hold multiple roles simultaneously. Each individual casts exactly one vote in governance decisions regardless of the number of roles held. Vacant roles are excluded from both the numerator and denominator of any vote.

The title of **Founder** is held by the original creator of the Rincoin protocol. The Founder title by itself is not a Core Role for voting purposes; however, the Founder MAY concurrently hold one or more Core Roles, in which case the Founder casts a vote in their capacity as a Core Role holder.

---

### Current Role Holders

The current assignment of individuals to Core Roles is maintained in the authoritative file `governance/core-role.md` in the RIPs repository. Consult that file for the current record.

As a reference point, role assignments typically change infrequently. Whenever a Core Role assignment changes, the `governance/core-role.md` file MUST be updated, and the change MUST be recorded in `governance/editor-changes.md` for historical accountability.

The Core Role structure itself (the four roles and their responsibilities) is defined in this document and does not change except by RIP amendment.

---

### Version Numbering Scheme

Rincoin Core releases follow a three-component versioning scheme:

```
  v[GENERATION].[MAJOR].[MINOR]
```

- **GENERATION** — Incremented at each Proof of Rinne epoch boundary (approximately every 400 years, ~233,280,000 blocks). The current generation is `1`.
- **MAJOR** — Incremented for significant protocol upgrades, including consensus-layer changes (hard forks and soft forks) and substantial architectural modifications. MAJOR is an unsigned integer with no hard upper bound; implementations MUST NOT reject a version solely because MAJOR exceeds 255.
- **MINOR** — Incremented for routine maintenance, bugfixes, peer-services updates, and minor feature additions that do not require consensus changes. Analogous to Bitcoin Core's patch-version practice (e.g., 25.0 → 25.1).

Associated tools and simulation suites (e.g., `rincoin-sim`) MAY use an extended four-component scheme:

```
  v[GENERATION].[MAJOR].[MINOR].[PATCH]
```

where the first three components track the Core release the tool validates against, and PATCH increments for tool-internal fixes that do not correspond to a Core release change (e.g., `rincoin-sim` v1.0.6.1 is a sim-internal fix against Core v1.0.6).

---

### Version Authority

The authority required to increment each version component scales with the number of distinct individuals holding at least one Core Role:

| Distinct voters | MINOR | MAJOR / GENERATION |
|-----------------|-------|--------------------|
| 1               | ✅ permitted | ❌ prohibited |
| 2               | ✅ permitted | Unanimous (2/2) |
| 3               | ✅ permitted | Supermajority (2/3) |
| 4               | ✅ permitted | Supermajority (3/4) |

When only one Core Role holder exists, MAJOR and GENERATION increments are prohibited until a second role is filled. This prevents unilateral protocol capture while preserving the ability to maintain the network through MINOR releases.

This prohibition applies to the **increment** of an official version — the act of designating a release as an officially numbered MAJOR or GENERATION version under this table. It does NOT prohibit a Core Role holder from authoring, publishing, or distributing a **release candidate** for the network's evaluation, provided the candidate is clearly labeled as such and is not represented as an officially incremented release. Such a candidate becomes an officially incremented release only by satisfying this table; where the table cannot be satisfied, the candidate may instead become the network's recognized chain through network ratification, as described in *Network Ratification of Release Candidates*. Neither outcome follows from the author's assertion or the passage of time.

---

### Network Ratification of Release Candidates

The prohibition on single-holder MAJOR and GENERATION increments restricts the **unilateral** enactment of an official version; it does not restrict authoring, publishing, or distributing candidate software. A Core Role holder MAY develop a release candidate (for example, in a Development & Staging repository) and publish it for the network's evaluation, provided it is clearly labeled as a candidate and not represented as an officially incremented release.

Such a candidate acquires legitimacy only through **network ratification**: the sovereign decision of the economic network — miners, full-node operators, exchanges, and other economic actors — to run it. Ratification is established organically by whether the network converges on the candidate, in the same manner that Step 4 of the Succession procedure recognizes leadership through rough consensus. Where the Version Authority table cannot be satisfied (for example, when only one Core Role holder is available), network ratification is the legitimate path by which a consensus-layer change may nonetheless activate.

Network ratification is not an exception to the single-holder prohibition but a **satisfaction of its purpose**: authority derives not from one holder's declaration but from the network's sovereign adoption, which is more distributed than — not a bypass of — the authority the table requires. A candidate that the network declines to run does not become official by the passage of time or by the author's assertion.

---

### Change Submission Discipline and Emergency Exception

All changes to the official Rincoin Core repository — including those authored by the Founder or any Core Role holder — MUST enter through a reviewed pull request. No individual commits consensus-critical or protocol-level changes directly to the official repository, irrespective of the write access their role grants. Development and validation occur in a Core Role holder's working repository; the official repository is a verified record of reviewed changes, not a direct editing surface. This mirrors the established Bitcoin Core practice in which maintainers, despite holding commit access, do not self-merge and route all changes through peer review.

A single, narrowly scoped exception applies. When an actively exploited or imminently exploitable defect threatens network safety or user funds, and the normal review path cannot be completed in time, the Founder (or, in the Founder's absence, the available Core Role holders acting unanimously) MAY apply a direct emergency commit limited strictly to the minimum change required to mitigate the threat. The exception is constrained as follows:

1. **Scope** — Limited to the minimal fix necessary; it MUST NOT bundle unrelated changes, feature additions, or parameter changes beyond those required for mitigation.
2. **Authority unchanged** — The exception permits an expedited submission path only. It does NOT relax the Version Authority table: an emergency commit MUST NOT, by itself, effect a MAJOR or GENERATION increment, and MUST NOT introduce a hard fork or soft fork. Consensus-layer changes always require the authority specified above, with no emergency override.
3. **Retroactive review** — A corresponding pull request documenting the change MUST be opened within 72 hours, and the change MUST undergo the normal review it bypassed. If the review identifies defects, a follow-up correction is submitted through the standard process.
4. **Disclosure** — The emergency action, its justification, and its scope MUST be recorded in `governance/emergency-actions.md`, and disclosed to node operators through the official channels with appropriate timing relative to the underlying vulnerability.

Routine work — including non-urgent bugfixes, maintenance, and all feature development — is never eligible for this exception and proceeds exclusively through standard pull-request review.

---

### Vacancy Determination

A *pending matter* is a Core Role holder's requested participation in a specific governance action — a requested review or merge of a pull request, a requested concurrence, or a requested vote — recorded in `governance/editor-changes.md` and delivered through every channel listed in `SECURITY.md`.

A Core Role becomes vacant only through the procedure below, and not by inactivity, slowness, or absence alone.

1. **Trigger.** No substantive action on the pending matter within **14 days** of delivery.
2. **Cure notice.** A written notice is then delivered through every channel in `SECURITY.md` and recorded in `governance/editor-changes.md`, opening a **7-day cure period**.
3. **Deliberation (grace only).** Before the cure period expires, the remaining Core Role holders MAY convene and, by recorded decision stating their reasons, extend the cure period where they have good-faith grounds to believe the holder is reachable and will act. This deliberation may operate ONLY to extend grace; it confers no power to vacate a role whose conditions in (1)–(2) are not met, and it cannot shorten any period.
4. **Disposition.** If the cure period — as extended under (3), if at all — expires with no substantive action, the holder's operational Core Role(s) are recorded as vacant in `governance/core-role.md` and `governance/editor-changes.md`. Vacancy follows from this rule upon non-action; it is NOT a discretionary act of removal by the remaining holders.

**Substantive action** means a cryptographically signed concurrence, a signed objection on the merits, or performance of the specific role function the matter calls for. A bare acknowledgment, or a stated intention to act, is NOT substantive action and does not toll or reset any period.

This procedure is no-fault and is distinct from removal for cause. The following bounds apply:

- The title of **Founder** is not an operational Core Role and is unaffected by vacancy.
- Vacancy is **reversible**: a returning holder is reinstated per *Succession*, or, where the role has been reconstituted in the interim, through the normal appointment process.
- Vacancy **transfers no authority by itself**. Where it leaves a single Core Role holder, MAJOR/GENERATION increments remain prohibited and proceed only through *Network Ratification of Release Candidates*.
- For the purposes of *Succession*, the Founder is "unavailable" with respect to a pending matter when, and only when, conditions (1)–(4) are satisfied as to that matter.

---

### Succession

If one or more Core Roles become vacant, the following priority order applies.

**Founder priority**: If the Founder is available, vacant Core Roles are reconstituted by the Core Strategic Authority — the Founder together with all remaining Core Role holders — acting by consensus. The Founder convenes this deliberation, and the resulting appointment MUST be recorded in `governance/editor-changes.md` for historical accountability. If the Core Strategic Authority cannot reach consensus within **21 days** of the vacancy being recorded, the Founder MAY reconstitute the vacant role directly; any such unilateral decision MUST be recorded in `governance/editor-changes.md` together with its rationale.

If the Founder is unavailable, role succession follows this strict priority order:

1. **Designated successor (Deputy)** — Each role holder designates a successor in writing, cryptographically signed with their key listed in `SECURITY.md`. Role holders are strongly encouraged to maintain an active Deputy (e.g., Deputy Technical Lead) during normal operations to ensure a seamless transition.

2. **Core coordination** — Remaining Core Role holders convene and select a replacement by unanimous agreement. If unanimous agreement cannot be reached within **30 days**, the process escalates to Step 3.

3. **Infrastructure Custodian fallback** — If Step 2 fails or all formal Core Roles are vacant, the official **Infrastructure Custodians** — defined as the registered holders of the official domains (`rincoin.org`, `rincoin.com`, `rincoin.net`) and the primary GitHub Organization owner — act as an emergency anchor. The Custodians reconstitute the Core Authority by unanimous agreement among themselves, subject to a **14-day public notice period**. Individual verbal objections during this period do not block reconstitution. If, however, the majority of the network actively rejects the Custodians' authority — such as by converging on an alternative software fork — the process escalates to Step 4.

4. **Community consensus** — If infrastructure access is also lost, or the network explicitly rejects the Custodians' intervention, new leadership is recognized through rough consensus emerging from the network's established participants (miners, full-node operators, exchanges, and other economic actors). No formal voting mechanism is prescribed at this stage; legitimacy is determined organically by whether the network converges on the proposed leadership. This reflects the same trust model that Bitcoin employs in practice for analogous governance vacuums.

---

## Rationale

### Why integrate versioning with Core Role governance?

The version-numbering scheme deliberately encodes the protocol's long-horizon design philosophy. The `GENERATION` component links software releases to the Proof of Rinne ~400-year epoch, ensuring that the names of releases themselves remind operators and developers of the protocol's regenerative timescale.

The `MAJOR / GENERATION` prohibition under single-holder governance is a deliberate fail-safe: it ensures that no individual — including the original Founder — can unilaterally execute a hard fork. The network can be maintained through `MINOR` releases by a single holder, but substantive protocol evolution requires distributed authority. This design recognizes that the integrity of a cryptocurrency protocol depends not only on its cryptographic primitives but also on the resilience of the human authority that maintains it.

The MAJOR component carries no hard upper bound by design. Given Rincoin's philosophy of prioritizing correctness over speed, the expected rate of MAJOR increments within a single ~400-year GENERATION is far below any practical limit. Should the development pace ever approach an upper bound, the community may introduce a successor scheme via a Process RIP without altering the GENERATION component.

---

### Why one vote per individual rather than one vote per role?

A vote-per-role scheme would over-weight individuals who hold multiple roles, particularly during the early phases of the project when role consolidation is unavoidable. The vote-per-individual scheme ensures that as the project grows and roles are distributed across more people, governance naturally becomes more decentralized without requiring an amendment to this document.

---

### Why require Founder consultation when the Founder is available?

Earlier drafts granted the Founder unilateral authority to reconstitute vacant Core Roles. That rule guaranteed liveness but was inconsistent with the one-vote-per-individual principle and with the role of the Core Strategic Authority as the project's collective decision-making body. Requiring reconstitution by consensus with the remaining Core Role holders aligns succession with the same collective-authority model that governs version increments, while the 21-day timeout and Founder fallback preserve liveness: a single holdout cannot stall reconstitution indefinitely, yet reconstitution can no longer bypass the remaining authorities when consensus is reachable. This differs from the founder-unavailable chain below, which must resolve succession without the Founder's tie-breaking authority and therefore relies on four-stage escalation.

---

### Why the four-stage succession chain?

Each successive step corresponds to a degraded operational state and is designed to ensure liveness (the system cannot deadlock indefinitely) while preserving safety (no individual can unilaterally seize authority):

1. **Deputy** — Normal operations; succession is pre-planned and instantaneous.
2. **Core coordination** — Partial disruption; remaining authorities resolve internally, bounded by a 30-day timeout to prevent indefinite deadlock.
3. **Infrastructure Custodian fallback** — Catastrophic disruption; physical/digital asset control (domains, repository ownership) provides a concrete and verifiable anchor for emergency reconstitution.
4. **Community consensus** — Total loss of formal structure; the network falls back to the same informal rough-consensus model that Bitcoin employs when its leadership structures fail.

The distinction between "verbal objections" (which do not block reconstitution) and "active rejection by converging on an alternative software fork" (which does) is critical. This ensures that individual fear, uncertainty, and doubt (FUD) cannot weaponize the notice period as a denial-of-service attack against legitimate succession, while preserving the absolute sovereignty of the network's economic and thermodynamic majority.

---

## Backwards Compatibility

The Version Numbering scheme codifies practice already in effect for Rincoin Core releases (v1.0.1, v1.0.6) and does not retroactively rename prior releases. The four-component extension (`v[GENERATION].[MAJOR].[MINOR].[PATCH]`) for associated tools such as `rincoin-sim` is likewise compatible with existing tool releases (e.g., rincoin-sim v1.0.6.1).

---

## Security Considerations

The Core Role governance structure introduces additional security considerations beyond the RIP process itself:

- **Single-holder protocol capture**: Mitigated by the explicit prohibition on MAJOR and GENERATION increments under single-holder governance. A solitary Core Role holder cannot unilaterally introduce consensus-layer changes.
- **Sybil attacks on succession**: The Infrastructure Custodian fallback resists Sybil attacks by tying authority to verifiable physical/digital asset control (domain registrations, GitHub Organization ownership) rather than to claims that can be cheaply forged.
- **Denial-of-service via objection campaigns**: The "verbal objections do not block" rule in Step 3 of the Succession procedure prevents an adversary from weaponizing the notice period to indefinitely stall legitimate reconstitution.
- **Key compromise of Core Role holders**: Mitigated by the `SECURITY.md` key-rotation procedure, which is decoupled from this document so that key rotation does not require amending the governance specification.

---

### Boundary of Official Support and Liability

The Rincoin Core software is provided under the MIT License without warranty of any kind, and the Rincoin Core Team disclaims all liability for any network consensus failures, asset loss, or security breaches arising from the use of any release.

A protocol modification, software fork, or network parameter change is **unofficial** when it has achieved legitimacy through neither path recognized by this document — neither the formal approval required under the Version Authority table (including the requisite approval of the Founder and Core Strategic Authority) nor network ratification as described in *Network Ratification of Release Candidates*. The Core Team will not provide technical support, issue patches, or conduct emergency incident response for changes that are unofficial in this sense.

Node operators, miners, and users who adopt any change do so at their own risk; **the choice of which chain to run rests with the network.**

---

## Acknowledgments

The Version Numbering and Core Role Governance section was refined through structured deliberation with Gemini (Google DeepMind) and Claude (Anthropic) in an advisory capacity to the Core Strategic Authority, with successive iterations addressing Sybil resistance, deadlock avoidance, and the distinction between verbal objection and active network rejection.

---

## Copyright

This document is licensed under the Creative Commons CC0-1.0 license.
