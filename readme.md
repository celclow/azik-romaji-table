# なにこれ
AZIKのローマ字テーブルと、それを作るscript。
Google日本語入力に対応してます。

[拡張ローマ字入力『ＡＺＩＫ』・『ACT』で快適な日本語入力を！]
(http://hp.vector.co.jp/authors/VA002116/azik/azikindx.htm)
を参考にしてます。

ウェブにはAZIKローマ字テーブルを配布しているところは多いけれど、kyi(きぃ) や wi(うぃ) 等が入力できないものが多いので作成。

# 使い方
通常通り使う方は、**azik_romaji_table.txt**をGoogle日本語入力のローマ字テーブル設定からインポートしてください。

独自にカスタマイズしたい方は、data/unique.txtに単語を追加し、

```
% ./romaji_table_maker.py data/unique.txt > azik_romaji_table.txt
```

のように実行してください。