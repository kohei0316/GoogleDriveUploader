from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class Upload():
    gauth = GoogleAuth()
    gauth.CommandLineAuth()
    drive = GoogleDrive(gauth)

    folder_id = '' # 保存先フォルダのID（URLの末尾）
    max_results = 100
    query = "'{}' in parents and trashed=false".format(folder_id)

    def overwrite(self, name):
        """
            保存するファイル名と同じ title のファイルを検索し id をリストに格納
            id を指定して削除することで同じ名前の古いファイルを削除
        """
        id_list = []
        for file_list in (self.drive).ListFile({'q': self.query, 'maxResults': self.max_results}):
            for l in file_list:
                if not l['mimeType'] == 'application/vnd.google-apps.folder':
                    #print('title: %s, id: %s' % (l['title'], l['id']))
                    if l['title'] == name:
                        id_list.append(l['id'])
        
        for m in id_list:
            delete_file = (self.drive).CreateFile({'id': m})
            delete_file.Delete()

    def csv_uploader(self, name, path):

        self.overwrite(name)
        
        f = (self.drive).CreateFile({'title': name,
                            'parents': [{'kind': 'drive#fileLink', 'id': self.folder_id}]})
        f.SetContentFile(path)
        f.Upload()

