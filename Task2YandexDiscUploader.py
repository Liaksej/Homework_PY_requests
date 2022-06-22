import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, disk_file_path: str, filelist):
        for count, file in enumerate(filelist):
            url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
            headers = self.get_headers()
            params = {'path': disk_file_path + '/' + file, 'overwrite': 'true'}
            response_get_link = requests.get(url=url, headers=headers, params=params)
            request_for_url = response_get_link.json()
            url_for_upload = request_for_url.get('href', '')
            response_upload = requests.put(url_for_upload, data=open(file, 'rb'))
            response_upload.raise_for_status()
            if response_upload.status_code == 201:
                print(f'{count + 1} файл из списка с именем {file} загружен успешно')


if __name__ == '__main__':
    token = ''
    filelist = ('test1.txt', 'test2.txt')   # Указать один файл или кортеж
    disk_file_path = ''  # Указать путь без слеша в конце
    uploader = YaUploader(token)
    result = uploader.upload(disk_file_path, filelist)
