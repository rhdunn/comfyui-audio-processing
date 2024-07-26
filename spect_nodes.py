# Copyright (C) 2024 Reece H. Dunn. SPDX-License-Identifier: GPL-3

import torchaudio.transforms as T


class Spectrogram:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"audio": ("AUDIO",)},
                "optional": {"n_fft": ("INT", {"default": 400, "min": 1, "max": 2**32}),
                             "win_length": ("INT", {"default": -1, "min": -1, "max": 2**32}),
                             "hop_length": ("INT", {"default": -1, "min": -1, "max": 2**32})}}

    CATEGORY = "AudioProcessing/features"

    RETURN_TYPES = ("SPECT", )
    FUNCTION = "spectrogram"

    def spectrogram(self,
                    audio,
                    n_fft=400,
                    win_length=-1,
                    hop_length=-1):
        if win_length == -1: win_length = None
        if hop_length == -1: hop_length = None
        waveform = audio["waveform"].movedim(1, -1).squeeze()
        spectrogram = T.Spectrogram(n_fft=n_fft,
                                    win_length=win_length,
                                    hop_length=hop_length,
                                    power=None)(waveform)
        return ({"spectrogram": spectrogram,
                 "sample_rate": audio["sample_rate"],
                 "n_fft": n_fft,
                 "win_length": win_length,
                 "hop_length": hop_length}, )


class PowerSpectrogram:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"audio": ("AUDIO",)},
                "optional": {"n_fft": ("INT", {"default": 400, "min": 1, "max": 2**32}),
                             "win_length": ("INT", {"default": -1, "min": -1, "max": 2**32}),
                             "hop_length": ("INT", {"default": -1, "min": -1, "max": 2**32})}}

    CATEGORY = "AudioProcessing/features"

    RETURN_TYPES = ("POWER_SPECT", )
    FUNCTION = "spectrogram"

    def spectrogram(self,
                    audio,
                    n_fft=400,
                    win_length=-1,
                    hop_length=-1):
        if win_length == -1: win_length = None
        if hop_length == -1: hop_length = None
        waveform = audio["waveform"].movedim(1, -1).squeeze()
        spectrogram = T.Spectrogram(n_fft=n_fft,
                                    win_length=win_length,
                                    hop_length=hop_length,
                                    power=2)(waveform)
        return ({"spectrogram": spectrogram,
                 "sample_rate": audio["sample_rate"],
                 "n_fft": n_fft,
                 "win_length": win_length,
                 "hop_length": hop_length}, )


class MelSpectrogram:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"audio": ("AUDIO",)},
                "optional": {"n_fft": ("INT", {"default": 400, "min": 1, "max": 2**32}),
                             "n_mels": ("INT", {"default": 128, "min": 1, "max": 2**32}),
                             "win_length": ("INT", {"default": -1, "min": -1, "max": 2**32}),
                             "hop_length": ("INT", {"default": -1, "min": -1, "max": 2**32})}}

    CATEGORY = "AudioProcessing/features"

    RETURN_TYPES = ("MEL_SPECT", )
    FUNCTION = "spectrogram"

    def spectrogram(self,
                    audio,
                    n_fft=400,
                    n_mels=128,
                    win_length=-1,
                    hop_length=-1):
        if win_length == -1: win_length = None
        if hop_length == -1: hop_length = None
        waveform = audio["waveform"].movedim(1, -1).squeeze()
        spectrogram = T.MelSpectrogram(sample_rate=audio["sample_rate"],
                                       n_fft=n_fft,
                                       n_mels=n_mels,
                                       win_length=win_length,
                                       hop_length=hop_length,
                                       power=2)(waveform)
        return ({"spectrogram": spectrogram,
                 "sample_rate": audio["sample_rate"],
                 "n_fft": n_fft,
                 "n_mels": n_mels,
                 "win_length": win_length,
                 "hop_length": hop_length}, )
