# 2024-contest
2024年企画コンテストのリポジトリです

## 初期設定
### 仮想環境を作る

```
python3 -m venv venv
or
python -m venv venv
(末尾のvenvは任意の仮想環境名)
```

### 仮想環境を有効化

```
source ./venv/bin/activate
or
.\venv\Scripts\activate
```

### モジュールの一括インストール

```
pip install -r requirements.txt
```

### .envファイルの作成

- 2024-contest直下に`.env`ファイルを作成し、委員会内で配布されている内容を貼り付け後、保存する

### 動作確認をする

```
python3 manage.py makemigrations
or
python manage.py makemigrations
```

```
python3 manage.py migrate
or
python manage.py migrate
```

```
python3 manage.py runserver
or
python manage.py runserver
```

### 権限の必要なAPIについて

```
python3 manage.py createsuperuser
or
python manage.py createsuperuser
```

管理者として登録

```
開発環境であれば
http://127.0.0.1:8000/admin/
本番環境であれば
https://ドメイン/admin/
```

上記からログインすれば利用可能
