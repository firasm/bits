---
substitutions:
  params:
    value: 23.5
---
# Substitutions in Markdown Files

## Trial 1 (ideal)

Here is a sentence that uses a subsitution value $ {{ params.value }} \textrm{mm} $ that does NOT show correctly.

## Trial 2 (workaround)

Here is a sentence that uses a subsitution value {{ params.value }} $\textrm{mm}$ that does show correctly.

## Trial 3 (Manual way ; what it should look like)

Here is a sentence that uses a subsitution value $23.5$ $\textrm{mm}$ that does show perfectly.