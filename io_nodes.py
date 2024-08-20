# Copyright (C) 2024 Reece H. Dunn. SPDX-License-Identifier: GPL-3

import torchaudio
import os


class LoadAudio:
    SUPPORTED_FORMATS = ('.wav', '.mp3', '.ogg', '.flac', '.aiff', '.aif')

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"audio": ("STRING",{"multiline":False})}}

    CATEGORY = "audio processing"

    RETURN_TYPES = ("AUDIO", )
    FUNCTION = "load"

    def load(self, audio):
        waveform, sample_rate = torchaudio.load(audio)
        audio = {"waveform": waveform.unsqueeze(0), "sample_rate": sample_rate}
        return (audio, )

    @classmethod
    def IS_CHANGED(s, audio):
        m = hashlib.sha256()
        with open(audio, 'rb') as f:
            m.update(f.read())
        return m.digest().hex()

    @classmethod
    def VALIDATE_INPUTS(s, audio):
        if not os.path.exists(audio) or not audio.endswith(LoadAudio.SUPPORTED_FORMATS):
            return "Invalid audio file: {}".format(audio)
        return True
