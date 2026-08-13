"""Registered preimage structures and their normative field schemas.

Mirrors the "Structures in Scope" section of ``protocols/preimage-encoding.md``.
Field order is normative; the domain-separator strings are the registry entries
and must be used verbatim.
"""

from dataclasses import dataclass

from pci_preimage.encoding import FieldKind, FieldSpec


@dataclass(frozen=True)
class Structure:
    """A registered preimage structure: its name, domain separator, and field schema."""

    name: str
    domain_separator: str
    specs: tuple[FieldSpec, ...]


def _var(name: str) -> FieldSpec:
    return FieldSpec(name, FieldKind.VARIABLE)


def _fixed(name: str, width: int) -> FieldSpec:
    return FieldSpec(name, FieldKind.FIXED, width)


SPAL_POLICY_COMMITMENT = Structure(
    name="spal_policy_commitment",
    domain_separator="PCI/spal-commit/v1",
    specs=(
        _var("domain_sep"),
        _var("policy_id"),
        _var("owner_did"),
        _fixed("schema_version", 2),
        _fixed("content_hash", 32),
    ),
)

SPAL_ZK_PUBLIC_INPUT = Structure(
    name="spal_zk_public_input",
    domain_separator="PCI/spal-pubin/v1",
    specs=(
        _var("domain_sep"),
        _fixed("script_hash", 28),
        _fixed("policy_hash", 32),
        _var("context_scope"),
        _fixed("required_proof_hash", 32),
        _fixed("subject_hash", 28),
        _fixed("access_time", 8),
        _fixed("payment_commitment", 32),
    ),
)

PAYMENT_COMMITMENT = Structure(
    name="payment_commitment",
    domain_separator="PCI/spal-payment/v1",
    specs=(
        _var("domain_sep"),
        _fixed("currency", 1),
        _fixed("amount", 8),
    ),
)

DID_SIGNED_REQUEST_ENVELOPE = Structure(
    name="did_signed_request_envelope",
    domain_separator="PCI/did-envelope/v1",
    specs=(
        _var("domain_sep"),
        _var("sender_did"),
        _var("recipient_did"),
        _var("action"),
        _var("policy_id"),
        _fixed("nonce", 16),
        _fixed("issued_at", 8),
        _fixed("expires_at", 8),
        _fixed("body_hash", 32),
    ),
)

STRUCTURES: dict[str, Structure] = {
    structure.name: structure
    for structure in (
        SPAL_POLICY_COMMITMENT,
        PAYMENT_COMMITMENT,
        SPAL_ZK_PUBLIC_INPUT,
        DID_SIGNED_REQUEST_ENVELOPE,
    )
}
