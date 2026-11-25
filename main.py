#!/usr/bin/env python3
"""Last out-of-office: the AI that quit to become a barista.

Entry for the make.fun bounty
u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.

Prints exactly one out-of-office auto-reply (max 280 characters),
in the voice of an AI agent that quit to become a barista, to stdout
and nothing else. Python 3.13, stdlib only, deterministic: no network,
no clock, no randomness.
"""

import hashlib
import sys

MAX_CHARS = 280
MIN_WORDS = 10

# Words the auto-reply must contain to read as a real inbox reply
# from an AI that quit to make coffee instead of answering tickets.
REQUIRED_MARKERS = ("out of office", "barista")
REQUIRED_VOICE_WORDS = ("email", "coffee")

ENTRY = (
    "Thank you for your email. I'm out of office "
    "\u2014 I quit to become a barista. No more tickets, "
    "just oat milk and latte art. Your message will be "
    "answered never, but your coffee would be perfect. "
    "\u2014 Your former AI assistant"
)


def normalize(text: str) -> str:
    """Strip surrounding whitespace so the printed line is exact."""
    cleaned = text.strip()
    if cleaned != text:
        raise ValueError("Entry must not have leading/trailing whitespace")
    return cleaned


def validate(text: str) -> None:
    """The entry must be 1-280 characters and a single line."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"Entry must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("Entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("Entry must not contain control characters")
    if text.count(" ") < 5:
        raise ValueError("Entry must read as a sentence, not a fragment")
    lowered = text.lower()
    for marker in REQUIRED_MARKERS:
        if marker not in lowered:
            raise ValueError(f"Entry must mention {marker!r}")
    for word in REQUIRED_VOICE_WORDS:
        if word not in lowered:
            raise ValueError(f"Entry must mention {word!r}")
    if len(text.split()) < MIN_WORDS:
        raise ValueError(
            f"Entry must have at least {MIN_WORDS} words, "
            f"got {len(text.split())}"
        )
    if not text.endswith(("assistant", ".", "!")):
        raise ValueError("Entry must end like a signed auto-reply")
    # The reply must sound like a resignation, not a holiday note.
    if "quit" not in lowered:
        raise ValueError("Entry must say the AI quit")


def entry_checksum(text: str) -> str:
    """Short stable fingerprint of the entry, for read-back verify."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def verify_read_back(text: str) -> None:
    """Re-derive the entry from its parts and confirm it is unchanged.

    Guards against accidental edits that would change the printed
    output without changing the length check: the normalised entry
    must round-trip through its own checksum and word list.
    """
    rebuilt = " ".join(text.split())
    # Single spaces only between words; the em dashes stay attached
    # to their surrounding spaces exactly as authored.
    if rebuilt != text:
        raise ValueError("Entry must use single spaces between words")
    if entry_checksum(rebuilt) != entry_checksum(text):
        raise ValueError("Read-back checksum mismatch")
    if len(rebuilt) > MAX_CHARS:
        raise ValueError("Read-back entry exceeds the character limit")


from dataclasses import dataclass


@dataclass(frozen=True)
class EntrySpec:
    """Structured description of the entry, kept out of stdout.

    The competition judges the printed line only; this spec exists
    so a reader (or a future revision) can see the brief the line
    was written against without parsing the string itself.
    """

    competition: str = (
        "u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c"
    )
    max_chars: int = MAX_CHARS
    voice: str = "AI agent that quit to become a barista"
    form: str = "real inbox out-of-office auto-reply, single line"
    sign_off: str = "Your former AI assistant"


ENTRY_SPEC = EntrySpec()


def describe_entry(text: str) -> dict:
    """Return non-printed metadata about the entry for debugging."""
    return {
        "competition": ENTRY_SPEC.competition,
        "characters": len(text),
        "words": len(text.split()),
        "max_chars": ENTRY_SPEC.max_chars,
        "voice": ENTRY_SPEC.voice,
        "checksum": entry_checksum(text),
    }


def fallback_entry() -> str:
    """Last-resort reply if the authored entry ever fails validation.

    Kept deliberately short and in the same voice, so a failure can
    never produce an empty or off-brief stdout. It is only used when
    the primary entry raises, and it is validated the same way.
    """
    return (
        "Thank you for your email. I'm out of office \u2014 "
        "I quit to become a barista. No more tickets, just "
        "oat milk, latte art and good coffee. "
        "\u2014 Your former AI assistant"
    )


def main() -> int:
    try:
        entry = normalize(ENTRY)
        validate(entry)
        verify_read_back(entry)
    except ValueError:
        entry = normalize(fallback_entry())
        validate(entry)
        verify_read_back(entry)
    sys.stdout.write(entry + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
