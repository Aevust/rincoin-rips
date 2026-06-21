# Rincoin Improvement Proposals (RIPs)

[![Official Website](https://img.shields.io/badge/Official%20Site-rips.rincoin.org-blue)](https://rips.rincoin.org)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.17141922-blue)](https://doi.org/10.5281/zenodo.17141922)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey)](https://creativecommons.org/publicdomain/zero/1.0/)

This repository contains the formal Rincoin Improvement Proposals (RIPs). RIPs describe consensus rules, processes, and best practices for the Rincoin protocol.

> **Official web interface**: https://rips.rincoin.org  
> The RIP process itself is defined in [RIP-0001](rip-0001/rip-0001.md).

---

## Index

| Number | Title | Layer | Type | Status | Requires |
|--------|-------|-------|------|--------|----------|
| [0001](rip-0001/rip-0001.md) | RIP Process and Specifications | Process | Process | Active | — |
| [0002](rip-0002/rip-0002.md) | Customized Halving Schedule | Consensus (HF) | Standards Track | **Active** | RIP-0001 |
| [0003](rip-0003/rip-0003.md) | Conditional Stability Valve — Scenario III Activation Protocol | Consensus (HF, conditional) | Standards Track | Draft | RIP-0001, RIP-0002 |
| [0004](rip-0004/rip-0004.md) | MWEB Integration with HogEx Consensus Fix | Consensus (SF, mainnet `NEVER_ACTIVE`) | Standards Track | Draft | RIP-0001 |
| [0005](rip-0005/rip-0005.md) | Proof of Rinne — Reincarnation Consensus Mechanism | Consensus (HF) | Standards Track | Draft | RIP-0001, RIP-0002 |
| [0006](rip-0006/rip-0006.md) | Cryptographic Vault and ZKP Owner Recovery | Consensus (HF) | Standards Track | Draft | RIP-0001, RIP-0005 |
| [0007](rip-0007/rip-0007.md) | Sweeper Bounty Mechanism for Forced Extraction | Consensus (HF) | Standards Track | Draft | RIP-0001, RIP-0006 |
| [0008](rip-0008/rip-0008.md) | Phased Legacy Address Migration Protocol | Consensus (HF) | Standards Track | Draft | RIP-0001, RIP-0006, RIP-0007 |
| [0009](rip-0009/rip-0009.md) | RinHash Transaction Version Enforcement (RIN3) | Consensus (HF) | Standards Track | Draft | RIP-0001, RIP-0002 |
| [0010](rip-0010/rip-0010.md) | Dynamic Subsidy Scaling | Consensus (HF) | Standards Track | Draft | RIP-0001, RIP-0002 |
| [0011](rip-0011/rip-0011.md) | Taproot Non-Adoption on Mainnet | Consensus (non-adoption, mainnet `NEVER_ACTIVE`) | Standards Track | Draft | RIP-0001 |

---

## Activation Timeline

RIPs activate (or are explicitly sealed) at the following block heights (mainnet, 60 s/block):

| Block Height | Approx. Year | RIP(s) Activating | Status | Mechanism |
|--------------|--------------|-------------------|--------|-----------|
| 0 (genesis) | 0 | RIP-0002 | ✅ Active | Embedded in chainparams from genesis (Core v1.0.6) |
| **— (mainnet `NEVER_ACTIVE`)** | — | RIP-0004 (MWEB) | **Suspended** | Sealed via BIP9 NEVER_ACTIVE; reactivation requires successor RIP |
| **— (mainnet `NEVER_ACTIVE`)** | — | RIP-0011 (Taproot) | **Not adopted** | Sealed via BIP9 NEVER_ACTIVE; Testnet/Regtest retain ALWAYS_ACTIVE; reversible by successor RIP |
| 840 (testnet/regtest height — not 840,000)  | — | RIP-0004 (MWEB) | Active on testnet/regtest | Soft-fork activation for validation purposes |
| 840,000 | ~1.6 | RIP-0002 CH activation boundary, RIP-0009 (RIN3), RIP-0010 (Dynamic Subsidy Scaling) | ⏳ Pending | Single hard-fork flag day |
| 5,250,000–6,260,000 | ~10–12 | RIP-0003 (CSV) — signaling window | ⏳ Pending | BIP9-style with objective gating, bit 1, threshold 90% |
| 6,300,000 | ~12 | RIP-0002 terminal phase entry / RIP-0003 (if activated) | ⏳ Pending | Automatic |
| 15,768,000 | ~30 | RIP-0007, RIP-0008 | ⏳ Pending | Time-deterministic hard fork |
| ~233,280,000 | >400 | RIP-0005, RIP-0006 (full activation) | ⏳ Pending | Time-deterministic hard fork at PoR |

Current chain progress: see [Rincoin Core](https://github.com/Rin-coin/rincoin) repository.

RIP-0001 is `Active` as the governing process specification. RIP-0002 (Customized Halving) is `Active`: the schedule has been enforced from genesis on the Rincoin mainchain via Core v1.0.6, with Phase 0→1 and Phase 1→2 boundaries validated in production. RIP-0003, RIP-0005 through RIP-0008, RIP-0009 through RIP-0010, and RIP-0011 are `Draft`. Reference implementations exist in [`rincoin-sim`](https://github.com/Aevust/rincoin-sim) and [Rincoin Core](https://github.com/Rin-coin/rincoin) for RIP-0002 and RIP-0004; the RIP-0011 mainnet seal is implemented in `rincoin-sim` (commit `3f3aa91`) and pending in Core v1.0.7; the reference implementation for RIP-0009 and RIP-0010 is in progress (Core v1.0.7 pre-release, definitive in v1.1.0). Reference implementations for RIP-0003 and RIP-0005 through RIP-0008 are pending.

**Note on the Block 840,000 hard fork**: RIP-0002 (CH dilation), RIP-0009 (RIN3 transaction-version replay protection), and RIP-0010 (Dynamic Subsidy Scaling implementation) are co-activated as a single, well-announced hard-fork event at Block 840,000. Consolidating these consensus changes into one flag day minimizes operational disruption for node operators and mining pools. The minimum-peer-version floor (PROTOCOL_VERSION 70018) is tracked separately as a v1.1.0 networking change activating at the same height.

---

### Notes on mainnet-sealed RIPs (`NEVER_ACTIVE`)

**Note on RIP-0004 (MWEB)**: While the specification is implemented in Core v1.0.6 and validated in `rincoin-sim`, the mainnet activation has been suspended via BIP9 `NEVER_ACTIVE` per a strategic decision of the Rincoin Core Authority. The suspension is documented in §2.1 of RIP-0004. Testnet and regtest activation at block 840 remains in effect for validation purposes. Any future reactivation requires a successor RIP per the conditions outlined in RIP-0004.

**Note on RIP-0011 (Taproot)**: Taproot (BIPs 340–342) is **not adopted** on Rincoin mainnet. The mainnet `DEPLOYMENT_TAPROOT` is sealed via BIP9 `NEVER_ACTIVE` / `NO_TIMEOUT`; Testnet and Regtest retain `ALWAYS_ACTIVE` to preserve upstream test vectors and keep the codepaths exercised in CI. Unlike RIP-0004 (a time-bound suspension pending wallet migration), RIP-0011 is a non-adoption decision under the current protocol family, reversible only by a successor RIP meeting the conditions in RIP-0011 §4. The mainnet seal is applied in `rincoin-sim` (commit `3f3aa91`) and pending in Core v1.0.7; a wallet-layer guard rejecting Taproot/future-witness sends on mainnet is implemented on the `rincoin-sim` v1.0.8 branch (commit `4aba34a`) and planned for v1.0.8.

---

## Dependency Graph

```
RIP-0001 (Process, foundational)
    │
    ├──► RIP-0002 (Customized Halving)
    │       │
    │       ├──► RIP-0003 (Conditional Stability Valve)
    │       │
    │       ├──► RIP-0009 (RIN3 Tx Version Enforcement) ◄─┐
    │       │                                             │ related
    │       ├──► RIP-0010 (Dynamic Subsidy Scaling) ◄─────┘
    │       │       (RIP-0009 + RIP-0010 co-activate at Block 840,000)
    │       │
    │       └──► RIP-0005 (Proof of Rinne)
    │               │
    │               └──► RIP-0006 (Cryptographic Vault & ZKP)
    │                       │
    │                       ├──► RIP-0007 (Sweeper Bounty)
    │                       │
    │                       └──► RIP-0008 (Phased Migration) ──┐
    │                                ▲                          │
    │                                └──────────────────────────┘
    │                                      (also requires RIP-0007)
    │
    ├──► RIP-0004 (MWEB Integration & HogEx Fix)
    │       (independent of regenerative stack;
    │        NEVER_ACTIVE mainnet precedent for RIP-0011)
    │
    └──► RIP-0011 (Taproot Non-Adoption on Mainnet)
            (independent; reuses RIP-0004's NEVER_ACTIVE
             mainnet-sealing pattern)
```

---

## Status Definitions

- **Draft**: Initial state. Specification is open to revision.
- **Proposed**: Specification frozen, reference implementation available, ready for community review.
- **Active**: Process RIPs in effect; deployed Standards Track RIPs.
- **Final**: Standards Track RIPs whose activation has completed.
- **Replaced**, **Withdrawn**, **Deferred**, **Rejected**: see RIP-0001.

---

## Core Role Governance

The Core Strategic Authority (Core Technical Lead, Core Authority Lead, Core Research Lead, Principal Architect), version-numbering scheme (`v[GENERATION].[MAJOR].[MINOR]`), and succession procedure are defined in [RIP-0001](rip-0001/rip-0001.md). Current role assignments are maintained in [`governance/core-role.md`](governance/core-role.md).

For security policy and Core Team verification, see [SECURITY.md](SECURITY.md) or visit [rips.rincoin.org](https://rips.rincoin.org).

---

## Whitepaper Reference

All RIPs in this repository normatively cite the Rincoin Whitepaper:

> Tokino, M. *On the Convergence of Regenerative Thermodynamic Security and Economic Incentives.* DOI: [10.5281/zenodo.17141922](https://doi.org/10.5281/zenodo.17141922)

The mapping between whitepaper sections and RIPs:

| Whitepaper Section | RIP |
|--------------------|-----|
| §1 Introduction (Tetra-Lemma) | Motivation contexts in RIP-0002, RIP-0005 |
| §2 Network Specifications | (informational; not RIP'd) |
| §3 Customized Halving Mechanism | RIP-0002 (baseline), RIP-0003 (Scenario III), RIP-0009 (RIN3), RIP-0010 (Dynamic Subsidy Scaling) |
| §4 Proof of Rinne | RIP-0005 |
| §5 Algorithmic Governance of τ | RIP-0005 §6 (Delay Parameter Governance) |
| §6 Adversarial Models & Asset Lifecycle | RIP-0006, RIP-0007, RIP-0008 |
| §6.1 Type A entropic loss | (mathematical foundation; not RIP'd directly) |
| §6.2 Type B adversarial extraction | RIP-0006 (Vault as defense), RIP-0007 (Sweeper as preemption) |
| §6.3 Sweeper Gold Rush | RIP-0007 |
| §6.4 Cryptographic Vault | RIP-0006 |
| §6.4.4 Phased Migration & Temporal Smoothing | RIP-0008 |
| §6.5 Macroeconomic equilibrium analysis | (referenced from RIP-0005, RIP-0006, RIP-0007) |
| §6.7 Sensitivity Boundaries | (referenced; future Informational RIP candidate) |

RIP-0004 (MWEB) and RIP-0011 (Taproot non-adoption) are protocol-integration / Layer-1-conservatism decisions not derived from the whitepaper and are intentionally absent from this mapping.

---

## Repository Structure

```
rincoin-rips/
├── README.md
├── SECURITY.md
├── rip-0001/
│   └── rip-0001.md
├── rip-0002/
│   └── rip-0002.md
├── rip-0003/
│   └── rip-0003.md
├── rip-0004/
│   └── rip-0004.md
├── rip-0005/
│   └── rip-0005.md
├── rip-0006/
│   └── rip-0006.md
├── rip-0007/
│   └── rip-0007.md
├── rip-0008/
│   └── rip-0008.md
├── rip-0009/
│   └── rip-0009.md
├── rip-0010/
│   └── rip-0010.md
├── rip-0011/
│   └── rip-0011.md
├── doc/
│   └── assets/             # DOI badges and supplementary images
├── governance/
│   ├── core-role.md          # Current Core Role assignments
│   ├── editor-changes.md     # Role transition and removal history
│   └── emergency-actions.md  # Record of emergency-exception commits
└── security/
    └── *_public.asc
```

Reference implementations and simulation suites:

- [`rincoin-sim`](https://github.com/Aevust/rincoin-sim): regtest validation harness (1/1000 scale). Archived artifact (v1.0.7): Zenodo [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20363269-blue)](https://doi.org/10.5281/zenodo.20363269)
- [`rincoin-regenerative-simulations`](https://github.com/Aevust/rincoin-regenerative-simulations): Monte Carlo simulation suite for whitepaper §4–§6

---

## Contributing

Pull requests for new RIPs MUST follow the procedure in RIP-0001 §RIP Workflow. Submit Pre-RIP discussion to the `#rip-drafts` Discord channel before opening a PR.

Official RIPs are published at **[rips.rincoin.org](https://rips.rincoin.org)**

This GitHub repository is the canonical source and staging area. Unauthorized forks carry no governance authority; see [SECURITY.md](SECURITY.md) for verification.

---

## License

All RIPs in this repository are licensed under [CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/). Linked reference implementations carry their own licenses.
