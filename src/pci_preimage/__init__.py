"""Reference implementation of the PCI canonical preimage encoding.

The encoding is specified in ``protocols/preimage-encoding.md`` and guarantees
injectivity: no two distinct field tuples serialize to the same bytes. It is
deliberately hash-agnostic — this package produces the bytes that are hashed,
never a digest.
"""

from pci_preimage.encoding import (
    MAX_VARIABLE_FIELD_LENGTH,
    DecodeError,
    Field,
    FieldKind,
    FieldSpec,
    FieldTooLongError,
    FixedField,
    FixedWidthError,
    PreimageError,
    VariableField,
    decode,
    encode,
)
from pci_preimage.structures import (
    DID_SIGNED_REQUEST_ENVELOPE,
    PAYMENT_COMMITMENT,
    SPAL_POLICY_COMMITMENT,
    SPAL_ZK_PUBLIC_INPUT,
    STRUCTURES,
    Structure,
)

__all__ = [
    "DID_SIGNED_REQUEST_ENVELOPE",
    "MAX_VARIABLE_FIELD_LENGTH",
    "PAYMENT_COMMITMENT",
    "SPAL_POLICY_COMMITMENT",
    "SPAL_ZK_PUBLIC_INPUT",
    "STRUCTURES",
    "DecodeError",
    "Field",
    "FieldKind",
    "FieldSpec",
    "FieldTooLongError",
    "FixedField",
    "FixedWidthError",
    "PreimageError",
    "Structure",
    "VariableField",
    "decode",
    "encode",
]
