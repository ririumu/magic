[topic-1734119131] deck-1734108972 に関するキャッチアップ

deck-1734108972 (青黒増殖コントロール) のキャッチアップを行いました。
方法としては以下のノートを参考にしました。

    職工スタン サンプルデッキ紹介（〜FDN） 青黒増殖コントロール編
    https://note.com/gintensubaru/n/n10b4bb38398b

デッキレシピのアップデートとサイドボードの復元を試みました。
分析用のコードを書き実行しました。

結果は以下の通りでした。

    $ pip install -r requirements.txt
    $ python main.py

    diffall:
                    name  q_diff
    0    Soul-Guide Lantern       3
    1             Spellgyre       2
    2     Withering Torment       2
    3                Deduce       1
    4  Prologue to Phyresis      -1
    5        Drown in Ichor      -2
    6           Serum Snare      -2
    7                Duress      -3

    diffmain:
                    name  q_diff
    0             Spellgyre       2
    1                Deduce       1
    2  Prologue to Phyresis      -1
    3              Cut Down      -2
    4        Drown in Ichor      -2
    5           Serum Snare      -2
    6                Duress      -3
    7     Malicious Eclipse      -3
    8                Negate      -3

最新のレシピではまず盤面を捌くこと優先しているように見受けられました。
なお、分析の詳細は https://github.com/ririumu/magic/issues/3 にメモがあります。

以上です。
