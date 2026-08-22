# 🔒 Zero-Knowledge Mathematical Blind RAG Enclave

[![Security: Blind Computing](https://shields.io)](#)
[![Cryptography: Local Enclave Tokenization](https://shields.io)](#)

## 🚀 Overview

Exporting raw corporate intelligence matrices, sensitive PII, or internal ledger records to third-party public cloud vector databases introduces deep operational risk and compliance friction (SOC2, GDPR, HIPAA).

This module implements a pure-mathematical **Zero-Knowledge Blind Retrieval-Augmented Generation (RAG) Architecture**. Sensitive plain-text documentation is processed exclusively within local edge hardware boundaries. Text data nodes are scrubbed and assigned deterministic tracking hashes backed by a localized cryptographic master-salt vault. 

Crucially, the untrusted multi-tenant cloud storage array **executes semantic spatial similarity calculations exclusively using raw floating-point dot-product matrix equations over non-readable token references**. The cloud learns nothing about user query contexts, returning abstract index tokens to the edge for final safe hydration.

---

## 🏗️ Folder Architecture Blueprint

```text
blind-rag-enclave/
├── config/
│   └── crypto_vault.py   # Secure Edge Salt Engine & Token Dictionary Maps
├── core/
│   └── engine.py         # Pure Mathematical Vector Blinding & Sim Calculation
├── storage/
│   └── cloud_mock.py     # Untrusted External Data-Lake Store (Floats & Hashes only)
└── main.py               # Application Ingress Router & Encryption Pipeline
```

---

## ⚙️ How It Works (The 0.1% Differentiation)

1. **Local Enclave Scrubbing:** `config/crypto_vault.py` processes raw blocks on local hardware, creating opaque string representations (`[MEM_HASH_B64DA30786]`).
2. **Blind Matrix Operations:** `core/engine.py` computes raw scalar spatial similarity scoring over encrypted spaces without decrypting vector dimensions.
3. **Zero-Trace Index Hosting:** `storage/cloud_mock.py` holds purely floating-point coordinate structures and alphanumeric hashes, keeping public database contexts fully anonymized.

---

## 💻 Running the Verification Suite

Execute the blind execution script from the directory root:
```bash
python main.py
```

### Expected Architectural Trace Log:
* **Enclave Mapping:** Confirms records are successfully blind-uploaded to untrusted space.
* **Cloud Math Traversal:** Logs compute dot-product processing outputs matching against numeric reference coordinates without plain-text visibility.
* **Edge Reconciliation:** Resolves the matching hash back into pure text form inside localized memory boundaries.
