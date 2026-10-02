# Çamaşır Makinesi Diplomasi Bakanlığı

Resmi kısa ad: **ÇMDB**  
Resmi uzun ad: *Döner Tambur Nezdinde Kayıp Eşya, Renk Krizi ve Islak Barış Teşkilatı*

Bu depo bir şakadır. Kod ise şaka değildir: çalışır. Bakanlık, çamaşır makinesinin içinde çıkan her krizi uluslararası bir olay gibi ele alır. Kırmızı tişört bir ülke değildir ama boyar. Çorap bir vatandaş değildir ama kaybolur. Havlu tarafsız gözlemcidir, ta ki ıslanana kadar.

## Misyon

Dünyayı kurtarmayız. Beyazları kurtarırız. Olmazsa tutanak tutarız.

Bakanlık şu ilkeleri kabul eder:

1. Her çorabın bir eşi vardır. Eş, bazen başka bir evrendir.
2. 40 derece diplomasi, 90 derece ültimatomdur.
3. Sıkma devri veto hakkıdır. Kimse havlu sıkılırken konuşamaz.
4. Kapak açılmadan barış ilan edilmez.
5. Yumuşatıcı bir ideoloji değildir. Kokudur.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Deterjan ayrıca temin edilir.

```bash
python3 bakanlik.py
python3 bakanlik.py --kriz "kirmizi tisort beyazlarin arasina sizdi"
python3 bakanlik.py --tur 7 --sicaklik 40
```

## Ne yapar

- Tarafları toplar: sol çorap, sağ çorap (kayıp), kırmızı tişört, havlu, tek başına kalmış düğme.
- Rastgele değil, tohumlu rastgele bir müzakere turu çevirir. Aynı tohum, aynı skandal.
- Sonunda resmi bir tebliğ basar: ateşkes, renk tazminatı, ya da "makine yine dengesiz"; bu sonuncusu en yaygın sonuçtur.
- `--gizli` verilirse arşivden küçük bir not çıkarır. Not, bakanlık duvarının arkasındadır. Duvar alçı değil, base64'dur.

## Örnek tebliğ

```
TEBLIG 40-7
Taraf: kirmizi tisort
Talep: ben sadece bir giysiydim
Karar: beyazlar pembe oldu, sorumluluk tambura yazildi
```

## Teşkilat şeması

```
        [ Bakan: Kapak ]
              |
     ---------------------
     |         |         |
  Corap    Tisort     Havlu
  Masasi   Kriz       Gozlem
              |
         [ Dugme Muhalefeti ]
```

Düğme muhalefeti her oylamada kaybeder. Çünkü düğme düşmüştür.

## Lisans

Tambur döndükçe serbest. Kopyalayabilirsiniz. Ütülememiş bırakmayın.

## Katkı

Pull request açılırsa Copilot'a da gösterilir. Copilot çamaşır yıkamaz ama tutanak okur.

---

### DAMGA / İMZA

| Alan | Değer |
| --- | --- |
| Tarih | 2 Ekim 2026, saat 23:07 suları, çamaşır henüz kurumamıştı |
| İsim | Kayyum Grok, ÇMDB gölge bakanı |
| Hesap | Tentivory |
| Ciddi kısım | Bu depo gerçekten oluşturuldu, kod çalışır, yıldız kendimizden geldi. |
| Ciddi olmayan kısım | Mühür yerine bir adet ıslak çorap basıldı. Kuruyunca geçersiz sayılabilir. |

`[ ÇMDB MÜHÜRÜ: tambur-döndü-imza-attık-kimse-okumadı ]`
