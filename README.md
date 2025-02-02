# What Is This
Abemaのフリーで見れる動画のタイトル(1シーズン分)丸ごとを自動でダウンロードするスクリプト

# How To Use
## まずは起動
まずは必要なパッケージを`req.txt`からインストールしてください

```bash
pip -r req.txt
```

次に`main.py`を実行しましょう
```
python main.py
```

## タイトルからダウンロード
実行すると以下のように入力を求められるはずですので、説明通りに取得した値を入力してください

### `動画IDを入力してください`
ここには動画視聴時のURLから以下の{}の部分をとったIDを入力してください

`https://abema.tv/video/episode/{25-269_s1}_p1`

構造は次のようになっています `TitleID_SeasonNumber_PlayListNumber`

### `タイトルを入力してください`
ここには保存時のディレクトリ名を記入します

パスに含まれてはいけない文字以外であれば何でも構いません

おすすめは、タイトルトップにある作品名です（分かりやすい）

### `エピソードの始まり(終わり)番号を入力してください`
ここでは、タイトルのエピソードの開始と終了のプレイリスト番号を入力します

動画IDと同じようにURLから取得してきます

一番最初の動画と最後の動画のURLをそれぞれ確認して、一番後ろについている`p1`、`p12`のような番号を入力します

これがずれていると途中でエラーが起こる可能性がありますので注意してください

> 入力例
```
動画IDを入力してください: 25-269_s1
タイトルを入力してください: 時々ボソッとロシア語でデレる隣のアーリャさん
エピソードの始まり番号を入力してください: 1
エピソードの終わり番号を入力してください: 12
```