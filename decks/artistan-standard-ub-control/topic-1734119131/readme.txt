[topic-1734119131] deck-1734108972 に関するキャッチアップ

deck-1734108972 (青黒増殖コントロール) のキャッチアップを行いました。
方法としては以下のノートを参考にしました。

    職工スタン サンプルデッキ紹介（〜FDN） 青黒増殖コントロール編
    https://note.com/gintensubaru/n/n10b4bb38398b

必要なコードを書きました。これは75枚の差分(diffall)とメインボードの差分(diffmain)を出力します。
結果は以下の通りでした。

    $ pip install -r requirements.txt
    $ python main.py

	diffall:
	                name  q_diff
	  Soul-Guide Lantern       3
	           Spellgyre       2
	   Withering Torment       2
	              Deduce       1
	Prologue to Phyresis      -1
	      Drown in Ichor      -2
	         Serum Snare      -2
	              Duress      -3

	diffmain:
	                name  q_diff
	           Spellgyre       2
	              Deduce       1
	Prologue to Phyresis      -1
	            Cut Down      -2
	      Drown in Ichor      -2
	         Serum Snare      -2
	              Duress      -3
	   Malicious Eclipse      -3
	              Negate      -3

diffmainより、全体的にやや重くなっていることがわかります。確かにマナが余り気味でした。
diffallより、増殖カードが大きくリストラされていることがわかります。10個ギリギリでしょうか。
増殖は Experimental Augury に頼る格好で、代わりに広く対応できるカードが増えているように思われます。

キャッチアップは以上です。
自分の現行レシピ [deck-1734108972] もアップデートが必要かもです。
