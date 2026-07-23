# Security Policy

## Official Rincoin Core Team

The following individuals are the current Core Role holders of the Rincoin protocol. **Only individuals listed here are authorized to represent the Rincoin Core Team.** Current role assignments are maintained in [`governance/core-role.md`](governance/core-role.md); this table is the authoritative record of their verification keys.

| Name | Role | Fingerprint |
|------|------|-------------|
| @ysmreg | Founder / Core Technical Lead | (to be added) |
| @Aevust | Core Authority Lead / Core Research Lead / Principal Architect | ED20 B635 4EE4 526D 01F8 3B53 8B6E 3BF4 5C71 4ECA |

Individuals not listed above are **not** members of the Rincoin Core Team, regardless of any claims made elsewhere.

---

## Reporting a Vulnerability

To report security issues, send an email to **info@rincoin.org** (not for general support).

Please do **not** open a public GitHub issue for security-sensitive reports.

Sensitive information may be encrypted using the key identified above.

### How to obtain our public key

Any of the three channels below serves the same key. Import from whichever is available and verify the fingerprint against the table above.

From the public keyserver (no clone required):

```
gpg --keyserver hkps://keys.openpgp.org --recv-keys ED20B6354EE4526D01F83B538B6E3BF45C714ECA
```

Via WKD, when rincoin.org is reachable:

```
gpg --auto-key-locate clear,wkd --locate-keys info@rincoin.org
```

From this repository, if you already have a clone:

```
gpg --import security/aevust.asc
```

Then verify:

```
gpg --fingerprint ED20B6354EE4526D01F83B538B6E3BF45C714ECA
```

The three channels may serve byte-different copies of the same key — the keyserver and the copy in this repository carry a superseded self-signature that the WKD response does not. **Verify the fingerprint, not a file digest.** The same fingerprint is pinned in the signed provenance certificate and in `llms.txt` on rincoin.org.

Signatures made since 2026-06-26 come from a signing subkey (0ED9 9C46 B219 2E37 5381 EF4A C5BE F8A9 FA06 C16F); gpg resolves this automatically once the primary key is imported. A copy of the key imported before that date will fail to verify current signatures and must be refreshed.

The key is also viewable at
- [keys.openpgp.org/vks/v1/by-fingerprint/ED20B6354EE4526D01F83B538B6E3BF45C714ECA](https://keys.openpgp.org/vks/v1/by-fingerprint/ED20B6354EE4526D01F83B538B6E3BF45C714ECA)

---

## Verifying Official Communications

Official Rincoin communications are characterized by:

- Signatures from keys listed in this document
- Publication via the official Discord server (owner: @Aevust)
- Publication on **rincoin.org** and **rincoin.com** (operated by @Aevust)
- For protocol-level changes: approval by the Founder (@ysmreg) and Core Strategic Authority as defined in [GOVERNANCE.md §Version Authority](GOVERNANCE.md#version-authority)

Communications from individuals not listed above, even when claiming Core Team authority, should not be trusted. The Rincoin Core Team disclaims responsibility for content published outside official channels, as defined in [GOVERNANCE.md §Boundary of Official Support and Liability](GOVERNANCE.md#boundary-of-official-support-and-liability).

---

## Canonical Sources

- **Official RIPs**: [rips.rincoin.org](https://rips.rincoin.org)
- **Core Repository (canonical)**: [github.com/Rin-coin/rincoin](https://github.com/Rin-coin/rincoin)
- **Core Repository (development and staging)**: [github.com/rincoin-core/rincoin](https://github.com/rincoin-core/rincoin)
- **RIPs Repository (canonical)**: [github.com/Aevust/rincoin-rips](https://github.com/Aevust/rincoin-rips)
- **Governance framework**: [GOVERNANCE.md](https://github.com/Aevust/rincoin-rips/blob/main/GOVERNANCE.md)
- **RIP process**: [RIP-0001](https://github.com/Aevust/rincoin-rips/blob/main/rip-0001/rip-0001.md)

The staging repository carries no governance authority of its own; changes reach the canonical Core repository only as reviewed pull requests.

---

## Independent DNS Verification

The canonical RIPs repository and official web endpoint are declared in DNS TXT records on the official Rincoin domains. These records can be independently verified without trusting any single document.

**Verified domains** (operated by @Aevust):

| Domain | DNS query |
|--------|-----------|
| rincoin.org | `dig TXT rincoin.org +short`|
| rips.rincoin.org | `dig TXT rips.rincoin.org +short`|

Expected TXT record content:

```
v=rincoin1; canonical-rips=https://github.com/Aevust/rincoin-rips; web=https://rips.rincoin.org; controller=@Aevust
```

**Note:** `rincoin.net` is owned by the Core Authority Team but its DNS management is currently delegated. It is not authoritative for verification purposes and MUST NOT be used to verify official Core Team communications.
