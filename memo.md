### venvのアクティブを作る
```
uv venv
```
### 何かしら作るやつ（空のディレクトリ）
```
uv init
```
### パッケージのインストール
```
uv add
```
### 依存関係を解決
```
uv sync
```
### ディレクトリごと別のPCに送る
```
scp -r (元のディレクトリ)./ (送り先)akari-2026-05-21@(ipアドレス):(ディレクトリ)
```
### 変更点のみ
```
rsync -avz --dry--run --exclude .venv/ --exclude .git (変更元)./ (変更先)akari-2026-05-21@(ipアドレス):(ディレクトリ)
```
```
rsync -avz --exclude .venv/ --exclude .git/  akari-2026-05-21@172.31.14.21:/home/akari-2026-05-21/AKARI-HANDOREMI/ ./
```

### ipアドレス確認(mac)
```
ifconfig |grep inet
```
### ipアドレス確認(ubuntu)
```
ip a | grep inet
```
### 環境設定
```
uv sync
```
### アクティブ
```
source .venv/bin/activate
```