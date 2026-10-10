"""Evidence sealing with cryptographic digests."""

from __future__ import annotations

import hashlib
import json
from typing import Any, Dict


def canonical_json(obj: Any) -> str:
    """Deterministic JSON serialization for digesting."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str)


def seal_evidence(payload: Dict[str, Any] | Any) -> str:
    """
    Produce a SHA-256 digest of the canonical form of the payload.
    The digest is the sealed identity of the evidence.
    """
    canonical = canonical_json(payload)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def verify_digest(payload: Any, expected_digest: str) -> bool:
    return seal_evidence(payload) == expected_digest
