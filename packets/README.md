# Packets — one page per lane

A packet is a reading copy: everything one review lane needs, inlined in reading order on a
single page, so a reviewer can print one document, mark it up, and send a memo back — the
workflow reviewers actually have — instead of navigating the repository. Each packet is
assembled by a committed script from the repository's own files, and those files are the
authority: **if a packet and a source differ, the source is right and the difference is a defect
worth reporting.** Packets are never edited by hand; they are regenerated.

Built so far:

- [Criminal law](./criminal_law.md) — by [`build_criminal_packet.py`](./build_criminal_packet.py).

The other four lanes (enforcement and prosecution; frontier security; open source and academia;
fiscal and administration) follow the same builder pattern. The lane definitions live on
[the reviewer page](../REVIEWERS.md); the statute itself is never reproduced in a packet — the
tagged text and its print copy are the statute's only homes.
