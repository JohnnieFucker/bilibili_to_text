import os
from dotenv import load_dotenv

load_dotenv()

# Azure Speech to Text 配置
SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY")
SPEECH_REGION = os.getenv("AZURE_SPEECH_REGION")

# 输出目录配置
OUTPUT_DIR = "output"
AUDIO_DIR = os.path.join(OUTPUT_DIR, "audio")
TEXT_DIR = os.path.join(OUTPUT_DIR, "text")
