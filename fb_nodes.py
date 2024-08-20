# Copyright (C) 2024 Reece H. Dunn. SPDX-License-Identifier: GPL-3

import torch
import torchaudio.functional as F


class LinearFilterBank:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"spectrogram": ("SPECT",)},
                "optional": {"f_min": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 96000.0, "step": 1.0}),
                             "f_max": ("FLOAT", {"default": 44100.0, "min": 0.0, "max": 96000.0, "step": 1.0}),
                             "n_filter": ("INT", {"default": 128, "min": 1, "max": 2**32})}}

    CATEGORY = "audio processing/filter bank"

    RETURN_TYPES = ("FILTER_BANK", )
    FUNCTION = "fbank"

    def fbank(self,
              spectrogram,
              f_min=0.0,
              f_max=44100.0,
              n_filter=128):
        n_freqs = spectrogram["n_fft"] // 2 + 1
        fbank = F.linear_fbanks(n_freqs=n_freqs,
                                f_min=f_min,
                                f_max=f_max,
                                n_filter=n_filter,
                                sample_rate=spectrogram["sample_rate"])
        return ({"fbank": fbank,
                 "sample_rate": spectrogram["sample_rate"],
                 "n_freqs": n_freqs,
                 "f_min": f_min,
                 "f_max": f_max,
                 "n_bins": n_filter}, )


class MelScaleFilterBank:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"spectrogram": ("SPECT",)},
                "optional": {"f_min": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 96000.0, "step": 1.0}),
                             "f_max": ("FLOAT", {"default": 44100.0, "min": 0.0, "max": 96000.0, "step": 1.0}),
                             "n_mels": ("INT", {"default": 128, "min": 1, "max": 2**32})}}

    CATEGORY = "audio processing/filter bank"

    RETURN_TYPES = ("FILTER_BANK", )
    FUNCTION = "fbank"

    def fbank(self,
              spectrogram,
              f_min=0.0,
              f_max=44100.0,
              n_mels=128):
        n_freqs = spectrogram["n_fft"] // 2 + 1
        fbank = F.melscale_fbanks(n_freqs=n_freqs,
                                  f_min=f_min,
                                  f_max=f_max,
                                  n_mels=n_mels,
                                  sample_rate=spectrogram["sample_rate"])
        return ({"fbank": fbank,
                 "sample_rate": spectrogram["sample_rate"],
                 "n_freqs": n_freqs,
                 "f_min": f_min,
                 "f_max": f_max,
                 "n_bins": n_mels}, )


class ApplyFilterBank:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"spectrogram": ("SPECT",),
                             "fbank": ("FILTER_BANK",)}}

    CATEGORY = "audio processing/filter bank"

    RETURN_TYPES = ("SPECT", )
    FUNCTION = "filter"

    def filter(self, spectrogram, fbank):
        spect = spectrogram["spectrogram"]
        fb = fbank["fbank"]
        filtered = torch.matmul(spect.transpose(-1, -2), fb).transpose(-1, -2)
        return ({"spectrogram": filtered,
                 "sample_rate": spectrogram["sample_rate"],
                 "stype": spectrogram["stype"],
                 "n_fft": spectrogram["n_fft"],
                 "win_length": spectrogram["win_length"],
                 "hop_length": spectrogram["hop_length"]}, )
