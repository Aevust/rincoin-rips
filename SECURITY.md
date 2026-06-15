# Security Policy

## Official Rincoin Core Team

The following individuals are the current Core Role holders of the Rincoin protocol. **Only individuals listed here are authorized to represent the Rincoin Core Team.** Current role assignments are maintained in [`governance/core-role.md`](governance/core-role.md).

| Name | Role | Fingerprint |
|------|------|-------------|
| @ysmreg | Founder / Core Technical Lead | (to be added) |
| @Aevust | Core Authority Lead / Core Research Lead / Principal Architect | ED20 B635 4EE4 526D 01F8 3B53 8B6E 3BF4 5C71 4ECA |

Individuals not listed above are **not** members of the Rincoin Core Team, regardless of any claims made elsewhere.

---

## Reporting a Vulnerability

To report security issues send an email to info@rincoin.org (not for support).

Sensitive information may be encrypted using the public keys listed above.

### How to obtain our public key

You can import our public key directly from this repository:
`gpg --import security/aevust.asc`

Or fetch it from the keyserver (no clone required):
`gpg --keyserver hkps://keys.openpgp.org --recv-keys ED20B6354EE4526D01F83B538B6E3BF45C714ECA`

Viewable at: [keys.openpgp.org/vks/v1/by-fingerprint/ED20B6354EE4526D01F83B538B6E3BF45C714ECA](https://keys.openpgp.org/vks/v1/by-fingerprint/ED20B6354EE4526D01F83B538B6E3BF45C714ECA)

---

## Verifying Official Communications

Official Rincoin communications are characterized by:

- Signatures from keys listed in this document
- Publication via the official Discord server (owner: @Aevust)
- Publication on **rincoin.org** and **rincoin.com** (operated by @Aevust)
- For protocol-level changes: approval by the Founder (@ysmreg) and Core Strategic Authority as defined in RIP-0001 §Version Authority

Communications from individuals not listed above, even when claiming Core Team authority, should not be trusted. The Rincoin Core Team disclaims responsibility for content published outside official channels, as defined in RIP-0001 §Boundary of Official Support and Liability.

---

## Canonical Sources

- **Official RIPs**: [rips.rincoin.org](https://rips.rincoin.org)
- **Core Repository**: [github.com/Rin-coin/rincoin](https://github.com/Rin-coin/rincoin)
- **RIPs Repository (Development)**: [github.com/Aevust/rincoin-rips](https://github.com/Aevust/rincoin-rips)
- **Governance**: [RIP-0001](https://github.com/Aevust/rincoin-rips/blob/main/rip-0001/rip-0001.md)

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
