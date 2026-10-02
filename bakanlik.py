#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Çamaşır Makinesi Diplomasi Bakanlığı — çalışan kriz masası."""

from __future__ import annotations

import argparse
import base64
import hashlib
import random
import sys
import textwrap

TARAFLAR = [
    "sol corap",
    "sag corap (kayip)",
    "kirmizi tisort",
    "beyaz havlu",
    "tek dugme",
    "ic etiket",
]

TALEPLER = [
    "ben masumum, renk benden cikmadi",
    "esim bir onceki yikamada kaldi",
    "40 derece insan hakki sayilir",
    "sikma devri isbirligi degil, baskidir",
    "cep unutuldu, kimlik icinde",
    "ben sadece dikisidim",
]

KARARLAR = [
    "ateşkes ilan edildi, pembe tonu kabul edildi",
    "tazminat: bir yemek kasigi yumusatici",
    "sorumluluk tambura yazildi, tambur konusmadi",
    "dosya kapaga iade edildi",
    "gozlemci havlu islak oldugu icin cekinser kaldi",
    "makine dengesiz, baris da dengesiz",
]

# Arsiv notu. Duvarda asili degil, kodun icinde.
_ARSIV = (
    "YnXDn2zEsWsgdGFtYnVyZGEgaGVyIGtleWZlIHDDtnJhIGbEsWthaW5pbiBhw7ğ
    "bmluYSBk8O3dlci4gS2F5eXVtIGR1cnVsbWEgYmFzbWF6OyB5dXJ0dGHDp2xhciBhaW5p"
    "IHRhbWJ1cmRhIGthbMSxciwga2ltc2Ugc2VjZW1lei4="
)


def tohum_uret(metin: str) -> int:
    ozet = hashlib.sha256(metin.encode("utf-8")).hexdigest()
    return int(ozet[:12], 16)


def oturum(kriz: str, tur: int, sicaklik: int) -> list[str]:
    rng = random.Random(tohum_uret(f"{kriz}|{tur}|{sicaklik}"))
    satirlar = [
        "ÇMDB KRIZ MASASI AÇILDI",
        f"Konu: {kriz}",
        f"Su: {sicaklik} derece ({'diplomasi' if sicaklik < 60 else 'ultimatom'})
        f"Tur sayisi: {tur}",
        "-" * 42,
    ]
    for n in range(1, tur + 1):
        taraf = rng.choice(TARAFLAR)
        talep = rng.choice(TALEPLER)
        karar = rng.choice(KARARLAR)
        if sicaklik >= 90 and rng.random() < 0.4:
            karar = "kumas çekti, anlaşma da çekti"
        satirlar.append(f"TUR {n} | {taraf}")
        satirlar.append(f"  talep: {talep}")
        satirlar.append(f"  karar: {karar}")
    kayip = rng.choice(["sol corap", "sag corap", "dugme", "kimse"])
    satirlar.append("-" * 42)
    satirlar.append(f"KAPANIS: bu yikamanin kaybi -> {kayip}")
    satirlar.append("Tebliğ yürürlüktedir. Kuruyunca da.")
    return satirlar


def gizli_not() -> str:
    try:
        ham = base64.b64decode(_ARSIV).decode("utf-8")
    except Exception:
        ham = "arsiv nemlendi, okunamadi"
    return textwrap.fill(ham, width=68)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Çamaşır Makinesi Diplomasi Bakanlığı kriz masası"
    )
    p.add_argument(
        "--kriz",
        default="beyazlar pembe oldu, kimse üstlenmiyor",
        help="gündem maddesi",
    )
    p.add_argument("--tur", type=int, default=4, help="müzakere turu")
    p.add_argument("--sicaklik", type=int, default=40, help="derece")
    p.add_argument(
        "--gizli",
        action="store_true",
        help="duvarın arkasındaki arşiv notunu bas",
    )
    args = p.parse_args(argv)
    if args.tur < 1:
        print("Tur sifir olamaz. Bakanlik bile bir tur ister.", file=sys.stderr)
        return 2
    if not 0 <= args.sicaklik <= 95:
        print("Bu makine o dereceyi tanimiyor.", file=sys.stderr)
        return 2
    print("\n".join(oturum(args.kriz, args.tur, args.sicaklik)))
    if args.gizli:
        print()
        print("ARSIV NOTU (gizli sandik, herkese acik depo)")
        print(gizli_not())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
