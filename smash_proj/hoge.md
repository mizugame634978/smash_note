Username: admin
Password: 2WgJbpTgUpCNBVN
mailadd: ryouta1853@gmail.com

username: admin2
password:admin2
mailadd:  admin2@example.com
# 仮想環境
lsでmanage.pyが表示される階層で行った。

```
python -m venv venv
```

で仮想環境を作成し、
```
venv\Scripts\Activate.ps1
```
で仮想環境に入る。
```
pip install -r requirements.txt
```
でライブラリを一括インストール。
```
pip freeze > requirements.txt
```
で仮想環境にインストールしているライブラリが全てrequirements.txtに書き込まれる。