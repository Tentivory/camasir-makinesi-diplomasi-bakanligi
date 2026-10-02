#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Camasir Makinesi Diplomasi Bakanligi — calisan kriz masasi."""

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
    "ateskes ilan edildi, pembe tonu kabul edildi",
    "tazminat: bir yemek kasigi yumusatici",
    "sorumluluk tambura yazildi, tambur konusmadi",
    "dosya kapaga iade edildi",
    "gozlemci havlu islak oldugu icin cekinser kaldi",
    "makine dengesiz, baris da dengesiz",
]

# Arsiv notu. Duvarda asili degil. Cozmek icin --gizli.
_ARSIV = (
    "QnV0dW4gcGFydGlsZXIgYXluaSB0YW1idXJkYSBkb25lci4gS2F5eXVtIGR1cnVs"
    "YW1hIHR1c3VuYSBiYXNhbiBraXNpZGlyOyBzZWNpbSBpc2Uga2FwYWdpbiBhY2ls"
    "bWFzaWRpci4gS2ltc2UgcHJvZ3JhbWkgdGVrIGJhc2luYSBzZWNlbWV6LCBoZXJr"
    "ZXMgaXNsYW5pci4="
)


def tohum_uret(metin: str) -> int:
    ozet = hashlib.sha256(metin.encode("utf-8")).hexdigest()
    return int(ozet[:12], 16)


def oturum(kriz: str, tur: int, sicaklik: int) -> list[str]:
    rng = random.Random(tohum_uret(f"{kriz}|{tur}|{sicaklik}"))
    ton = "diplomasi" if sicaklik < 60 else "ultimatom"
    satirlar = [
        "CMDB KRIZ MASASI ACILDI",
        f"Konu: {kriz}",
        f"Su: {sicaklik} derece ({ton})",
        f"Tur sayisi: {tur}",
        "-" * 42,
    ]
    for n in range(1, tur + 1):
        taraf = rng.choice(TARAFLAR)
        talep = rng.choice(TALEPLER)
        karar = rng.choice(KARARLAR)
        if sicaklik >= 90 and rng.random() < 0.4:
            karar = "kumas cekti, anlasma da cekti"
        satirlar.append(f"TUR {n} | {taraf}")
        satirlar.append(f"  talep: {talep}")
        satirlar.append(f"  karar: {karar}")
    kayip = rng.choice(["sol corap", "sag corap", "dugme", "kimse"])
    satirlar.append("-" * 42)
    satirlar.append(f"KAPANIS: bu yikamanin kaybi -> {kayip}")
    satirlar.append("Teblig yururluktedir. Kuruyunca da.")
    return satirlar


def gizli_not() -> str:
    try:
        ham = base64.b64decode(_ARSIV).decode("utf-8")
    except Exception:
        ham = "arsiv nemlendi, okunamadi"
    return textwrap.fill(ham, width=68)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Camasir Makinesi Diplomasi Bakanligi kriz masasi"
    )
    p.add_argument(
        "--kriz",
        default="beyazlar pembe oldu, kimse ustlenmiyor",
        help="gundem maddesi",
    )
    p.add_argument("--tur", type=int, default=4, help="muzakere turu")
    p.add_argument("--sicaklik", type=int, default=40, help="derece")
    p.add_argument(
        "--gizli",
        action="store_true",
        help="duvarin arkasindaki arsiv notunu bas",
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
