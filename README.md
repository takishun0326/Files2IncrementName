# Files2IncrementName

指定したフォルダ内のファイル名を一括で変更するプログラム．

よく使うのに残していなかったから毎回書いてたけど，面倒になるから作った．

## 仕様
デフォルトではファイル名に5桁のゼロ埋めを行う．

Main.pyのZERO_PADDINGの値で変更可能

## 実行方法
~~~
cd Files2IncrementName
python Main.py
~~~

## 実行例

~~~
$ python Main.py
入力画像フォルダのパス
>> C:\hoge\test_imgs\
~~~
### 実行前
~~~
└─ test_imgs
      IMG_2438.png
      IMG_2439.png
      IMG_2450.jpg
      IMG_2514.png
      IMG_2518.png
~~~
### 実行後
~~~
└─ test_imgs
      00001.png
      00002.png
      00003.jpg
      00004.png
      00005.png
~~~
