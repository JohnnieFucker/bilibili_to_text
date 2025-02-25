import os
import subprocess
from config import AUDIO_DIR


class BilibiliDownloader:
    def __init__(self):
        if not os.path.exists(AUDIO_DIR):
            os.makedirs(AUDIO_DIR)

    def download_audio(self, url):
        """
        下载B站视频的音频
        """
        try:
            # 使用you-get下载音频
            output_path = AUDIO_DIR
            command = f"you-get -o {output_path} -F m4a {url}"
            subprocess.run(command, shell=True, check=True)

            # 获取下载的文件名
            files = os.listdir(AUDIO_DIR)
            audio_file = [f for f in files if f.endswith(".m4a")][-1]

            return os.path.join(AUDIO_DIR, audio_file)
        except Exception as e:
            print(f"下载音频时出错: {str(e)}")
            return None
