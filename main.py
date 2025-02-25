from bilibili_downloader import BilibiliDownloader
from speech_to_text import SpeechToText


def main():
    url = input("请输入B站视频URL: ")

    # 下载音频
    downloader = BilibiliDownloader()
    audio_file = downloader.download_audio(url)

    if not audio_file:
        print("音频下载失败")
        return

    # 转换为文本
    converter = SpeechToText()
    text_file = converter.convert_to_text(audio_file)

    if text_file:
        print(f"转换完成！文本文件保存在: {text_file}")
    else:
        print("转换失败")


if __name__ == "__main__":
    main()
