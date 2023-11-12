# MultiSensorPi3

<h4><<概要>></h4>
　ラズパイを手に入れて、Ｌチカとかやってみたけれど、さて次は何をしようと悩んでいたら、センサーをやってみましょう。<br>
　部品から揃えてやるのもいいですが、サクッと初めてpythonやnode-redをやりたいならこの基板が良いです。<br>
　センサーを個別に買うより、簡単に使えて、色々ノウハウが手に入ります。
 
  ・気象観測関係　気温、湿度、気圧センサー<br>
  ・距離測定　　　超音波による測距センサー<br>
  ・環境測定　　　明るさセンサー、傾きセンサー<br>
  ・その他　　　　LED 2個、SW 2個、赤外線センサー<br>
  
  以上のセンサー類をnode-redによりwebブラウザで表示制御できます。<br>
　すべてのソースプログラムを開示いたします。<br>

・LEDの色等指定はできません。<br>
・部品の仕様、有無等変わる場合があります。 <br>
・基板のバージョンが変わる場合がありますが、機能等に違いはありません。<br>
・回路に関しても随時変更しますが、機能等に違いはありません。<br>
・ラズパイは付属しません。<br>

<h4><<使用方法>></h4>
git clone https://github.com/momorara/MultiSensorPi3 sensorHAT<br>
でラズパイにダウンロードしてください。<br>
インストールについては、インストール文書に従いインストールを行ってください。<br>

<h4><<使用説明資料>></h4>
説明書類の中の資料を確認ください。
お問い合わせに関しては、サポート.txtを参照ください。><br>

<h4><<注意事項>></h4>
センサーの取り付け方法 SR04とAHT10の接続方向を確実に確認してください。<br>
間違った接続をしてしまうと、センサーが発熱し、触るとやけどをする可能性があります。<br>

<h4><<動作環境>>></h4>
2023/8/4 対応OS：Buster版、Bullseye版(11.6、11.7)(32bit)での動作を確認しています。<br>

<h4><<ライセンス>></h4>
使用しているライブラリについては、ライブラリ制作者のライセンス規定を参照ください。
オリジナル部分については、オープソースとさせていただきます。
Released under the MIT license です。
プログラム自体はサンプルプログラムです。

<h4><<アップデート>></h4>
2023/9/14 MultiSensorPi3を使う上で失敗しそうな点をまとめました。<br>
2023/9/23 今後BMP180をBMP280に置き換えていきます。<br>
簡略化のためソフトプルダウンにしてプルダウン抵抗を削除していきます。<br>
コンデンサについて機能上不要である確認が出来ましたので、削除します。<br>
そのため、回路図と実際の基板に違いが出ますが、機能的には同じです。<br>

