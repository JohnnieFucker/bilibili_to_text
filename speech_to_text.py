import os
import azure.cognitiveservices.speech as speechsdk
from config import SPEECH_KEY, SPEECH_REGION, TEXT_DIR


class SpeechToText:
    def __init__(self):
        if not os.path.exists(TEXT_DIR):
            os.makedirs(TEXT_DIR)

        self.speech_config = speechsdk.SpeechConfig(
            subscription=SPEECH_KEY, region=SPEECH_REGION
        )
        self.speech_config.speech_recognition_language = "zh-CN"

    def convert_to_text(self, audio_file):
        """
        将音频文件转换为文本
        """
        try:
            audio_config = speechsdk.audio.AudioConfig(filename=audio_file)
            speech_recognizer = speechsdk.SpeechRecognizer(
                speech_config=self.speech_config, audio_config=audio_config
            )

            text_content = []

            def handle_result(evt):
                text_content.append(evt.result.text)

            speech_recognizer.recognized.connect(handle_result)
            speech_recognizer.recognized.connect(
                lambda evt: print("识别文本:", evt.result.text)
            )

            speech_recognizer.start_continuous_recognition()
            speech_recognizer.stop_continuous_recognition()

            # 保存文本文件
            base_name = os.path.splitext(os.path.basename(audio_file))[0]
            text_file = os.path.join(TEXT_DIR, f"{base_name}.txt")

            with open(text_file, "w", encoding="utf-8") as f:
                f.write("\n".join(text_content))

            return text_file

        except Exception as e:
            print(f"转换文本时出错: {str(e)}")
            return None
