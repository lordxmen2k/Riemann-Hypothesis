# Proof as code — provenance and reproduction

This repository holds the submitted Lean development that is the subject of
*Is the Riemann Hypothesis Solved?* (DOI 10.5281/zenodo.23874214), extracted so
that it can be read, searched and checked.

## Where it came from

The author distributed the development as a fourteen-part tarball:

    https://alpo.ge/lean.tar.gz.part01  ...  https://alpo.ge/lean.tar.gz.part14

## How to reproduce the extraction

    curl -O https://alpo.ge/lean.tar.gz.part01   # ... through .part14
    cat lean.tar.gz.part* > lean.tar.gz
    tar -xzf lean.tar.gz

## Integrity

    sha256sum lean.tar.gz
    9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc

This is the hash published by the third-party mirror
(`github.com/CocoSgt/riemann-hypothesis-lean`, release `v2026-11-20`), and the
archive audited for the book hashes to it exactly.

## What is in it

| | |
|---|---|
| `.lean` files | 175,187 |
| Lines of Lean | ~17.4 million |
| Extracted size | ~1 GB |
| Toolchain | `leanprover/lean4:v4.33.1` (`lean-toolchain`) |
| Mathlib | pinned at `0df444a360eaa60ab8c11dca51a86af692955474` (`lakefile.toml`) |
| Axiom declarations | 0 |
| `sorry` occurrences | 0 |

## Layout

    src/Main.lean        the six exported theorems
    src/Statements.lean  the five propositions proved
    src/Development/     141,928 files — the theorems
    src/Formalism/        18,254 files — the general machinery
    src/GroundTheory/      8,507 files — geometric foundations
    src/ReciprocityTheory/ 3,845 files — reciprocity and automorphic forms
    src/CompanionTheory/   2,027 files
    src/PositivityTheory/    449 files — positivity and estimates
    src/Lemmata/             167 files
    src/BuildAid/              5 files
    src/Supplements/           3 files

## Where to start reading

The book maps each step of the method to a declaration in this tree; see
Chapter 16, *The Method in the Source: A Step-to-Declaration Map*, in the
published volume, and `../rh-book/research/source_ledger.md` for the ledger.

## A note on this repository

The development is the work of its author. This repository exists so that the
audit can cite exact paths and so that any local edit made while checking a
step is visible and reversible. It is not a redistribution of the author's
work and it is not the book's source repository.
