# Copyright (C) 2024 Reece H. Dunn. SPDX-License-Identifier: GPL-3

import torchaudio.transforms as T


SPECTROGRAM_TYPES = ("complex", "magnitude", "power")

SPECTROGRAM_TYPE_TO_POWER = {
    "complex": None,
    "magnitude": 1,
    "power": 2,
}


class Spectrogram:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"audio": ("AUDIO",)},
                "optional": {"stype": (SPECTROGRAM_TYPES, {"default": "power"}),
                             "n_fft": ("INT", {"default": 400, "min": 1, "max": 2**32}),
                             "win_length": ("INT", {"default": -1, "min": -1, "max": 2**32}),
                             "hop_length": ("INT", {"default": -1, "min": -1, "max": 2**32})}}

    CATEGORY = "audio processing/spectrogram"

    RETURN_TYPES = ("SPECT", )
    FUNCTION = "spectrogram"

    def spectrogram(self,
                    audio,
                    stype="power",
                    n_fft=400,
                    win_length=-1,
                    hop_length=-1):
        if win_length == -1: win_length = None
        if hop_length == -1: hop_length = None
        waveform = audio["waveform"].movedim(0, -1).squeeze()
        spectrogram = T.Spectrogram(n_fft=n_fft,
                                    win_length=win_length,
                                    hop_length=hop_length,
                                    power=SPECTROGRAM_TYPE_TO_POWER[stype])(waveform)
        return ({"spectrogram": spectrogram,
                 "sample_rate": audio["sample_rate"],
                 "stype": stype,
                 "n_fft": n_fft,
                 "win_length": win_length,
                 "hop_length": hop_length}, )


class InverseSpectrogram:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"spectrogram": ("SPECT",)}}

    CATEGORY = "audio processing/spectrogram"

    RETURN_TYPES = ("AUDIO", )
    FUNCTION = "inverse"

    def inverse(self, spectrogram):
        if spectrogram["stype"] != "complex":
            raise Exception(f"The spectrogram is not a complex-valued spectrogram: {spectrogram['stype']}")
        waveform = T.InverseSpectrogram(n_fft=spectrogram["n_fft"],
                                        win_length=spectrogram["win_length"],
                                        hop_length=spectrogram["hop_length"])(spectrogram["spectrogram"])
        if len(waveform.shape) == 1:
            waveform = waveform.unsqueeze(0)  # 1 channel (mono) audio
        return ({"waveform": waveform.unsqueeze(0),
                 "sample_rate": spectrogram["sample_rate"]}, )


class GriffinLim:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"spectrogram": ("SPECT",)},
                "optional": {"n_iter": ("INT", {"default": 32, "min": 1, "max": 2**32}),
                             "momentum": ("FLOAT", {"default": 0.99, "min": 0.0, "max": 1.0, "step": 0.01})}}

    CATEGORY = "audio processing/spectrogram"

    RETURN_TYPES = ("AUDIO", )
    FUNCTION = "griffin_lim"

    def griffin_lim(self, spectrogram, n_iter=32, momentum=0.99):
        if spectrogram["stype"] == "complex":
            raise Exception(f"The spectrogram is not a real-valued spectrogram: {spectrogram['stype']}")
        waveform = T.GriffinLim(n_fft=spectrogram["n_fft"],
                                n_iter=n_iter,
                                win_length=spectrogram["win_length"],
                                hop_length=spectrogram["hop_length"],
                                power=SPECTROGRAM_TYPE_TO_POWER[spectrogram["stype"]],
                                momentum=momentum)(spectrogram["spectrogram"])
        if len(waveform.shape) == 1:
            waveform = waveform.unsqueeze(0)  # 1 channel (mono) audio
        return ({"waveform": waveform.unsqueeze(0),
                 "sample_rate": spectrogram["sample_rate"]}, )
