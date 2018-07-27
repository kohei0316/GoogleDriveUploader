# GoogleDriveUploader
PyDriveを用いてGoogleDriveに自動アップロードするコード

```
import GoogleDriveUpload
Upload = GoogleDriveUpload.Upload()

~~~

try:
    """
        filename : 保存するファイル名
        outpath : アップロードしたいファイルのパス（ローカル）
    """
    Upload.csv_uploader(filename, outpath)
    print("Google Drive にアップロードしました．")
except:
    sys.exit("Error : Google Drive にアップロードできませんでした．")

```
## クライアントIDとクライアントシークレットの取得方法
[PythonでGoogleドライブに画像をアップロード](https://qiita.com/akabei/items/f25e4f79dd7c2f754f0e)  