# Copyright (C) 2024 Reece H. Dunn. SPDX-License-Identifier: GPL-3

import torchaudio.functional as F


class MelScaleFilterBank:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"audio": ("AUDIO",)},
                "optional": {"n_freqs": ("INT", {"default": 400, "min": 1, "max": 2**32}),
                             "f_min": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 96000.0, "step": 1.0}),
                             "f_max": ("FLOAT", {"default": 44100.0, "min": 0.0, "max": 96000.0, "step": 1.0}),
                             "n_mels": ("INT", {"default": 128, "min": 1, "max": 2**32})}}

    CATEGORY = "AudioProcessing/filterbank"

    RETURN_TYPES = ("FILTER_BANK", )
    FUNCTION = "fbank"

    def fbank(self,
              audio,
              n_freqs=400,
              f_min=0.0,
              f_max=44100.0,
              n_mels=128):
        fbank = F.melscale_fbanks(n_freqs=n_freqs,
                                  f_min=f_min,
                                  f_max=f_max,
                                  n_mels=n_mels,
                                  sample_rate=audio["sample_rate"])
        return ({"fbank": fbank,
                 "sample_rate": audio["sample_rate"],
                 "n_freqs": n_freqs,
                 "f_min": f_min,
                 "f_max": f_max,
                 "n_mels": n_mels}, )
