import requests, os


class FishAPI:

    def download_file(self, url):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        local_filename = url.split('/')[-1]
        local_path = f"{dir_path}/downloads/{local_filename}"
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print("successfully downloaded to: ", local_path)
        return local_path