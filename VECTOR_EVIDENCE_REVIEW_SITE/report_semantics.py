"""Data loading and source metadata for the separate dossier renderer."""

import ast
import hashlib
import json
import os
from pathlib import Path


def load_counts(path):
    tree = ast.parse(Path(path).read_text(encoding="utf-8"), filename=str(path))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "counts" for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise ValueError("counts assignment not found")


def load_manifest(path):
    manifest = json.loads(Path(path).read_text(encoding="utf-8"))
    if manifest.get("schema_version") != "digital-evidence.dossier.v1":
        raise ValueError("Unsupported evidence manifest schema_version")
    counts = manifest.get("counts")
    if not isinstance(counts, list) or not counts:
        raise ValueError("Evidence manifest must contain counts")
    event_ids = [event.get("event_id") for event in counts]
    if any(not value for value in event_ids) or len(event_ids) != len(set(event_ids)):
        raise ValueError("Evidence manifest event_id is missing or duplicated")
    return counts


def display_amount(value):
    return str(value or "").strip() or "—"


def display_title(value):
    return str(value or "").strip()


def display_datetime(value):
    return str(value or "").strip() or "—"


def display_slip(value):
    return str(value or "").strip() or "—"


def review_text(value, field):
    return str(value or "").strip() or "—"


def candidate_laws(values):
    return list(values or [])


def source_identity(ref):
    root = os.environ.get("VECTOR_SOURCE_ROOT")
    if not root:
        return str(ref)
    base = Path(root).resolve()
    candidate = (base / ref).resolve()
    if not candidate.is_relative_to(base) or not candidate.is_file():
        return str(ref)
    digest = hashlib.sha256()
    with candidate.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return f"{ref} • SHA-256: {digest.hexdigest()}"
