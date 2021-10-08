## 概要
dummytool-for-throwing-cues-via-kanbanは、kanbanからデータを受け取るといった機能をテストする場合に使用できるデバッグツールです。
kanbanを経由してymlに設定した送り先のサービスにダミーデータを送ることができます。

## 利用方法
必要なパッケージのインストール

```
pip install -r requirements.txt
```


ダミーデータを作成し、kanbanを経由して受信する

## 環境設定
kubenetesやaionを立ち上げる際に必要なservices.ymlに環境変数を設定します。
```yml
  dummy-test-kanban:
    scale: 1
    startup: yes
    always: yes
    network: ClusterIP
    ports:
    - name: dummy-test # 15文字以内にしてください。
      protocol: TCP
      port: 12345
    nextService:
      default: # CONNECTION_KEYの定数を変更することで `default` 以外にも名前を変えることができます。 
      - name: ${デバッグ対象のサービス}
```