# Copyright (C) 2024 Reece H. Dunn. SPDX-License-Identifier: GPL-3

import io
import matplotlib.pyplot as plt
import numpy as np
import torch

from PIL import Image


def plot2image():
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image = Image.open(buffer)
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)


class PlotWaveform:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"audio": ("AUDIO",),
                             "title": ("STRING", {"default": "Waveform"})}}

    CATEGORY = "AudioProcessing/plot"

    RETURN_TYPES = ("IMAGE", )
    FUNCTION = "plot"

    def plot(self, audio, title="Waveform"):
        waveform = audio["waveform"].movedim(0, -1).numpy()
        num_channels, num_frames, _ = waveform.shape
        time_axis = torch.arange(0, num_frames) / audio["sample_rate"]
        figure, axes = plt.subplots(num_channels, 1)
        if num_channels == 1:
            axes = [axes]
        for c in range(num_channels):
            axes[c].plot(time_axis, waveform[c], linewidth=1)
            axes[c].grid(True)
            if num_channels > 1:
                axes[c].set_title(f"Channel {c+1}")
        figure.suptitle(title)
        return (plot2image(), )


class PlotSpectrogram:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"spectrogram": ("SPECT",),
                             "title": ("STRING", {"default": "Spectrogram"})}}

    CATEGORY = "AudioProcessing/plot"

    RETURN_TYPES = ("IMAGE", )
    FUNCTION = "plot"

    def plot(self, spectrogram, title="Spectrogram"):
        if len(spectrogram["spectrogram"].shape) == 2:
            num_channels = 1
        else:
            num_channels, _, _ = spectrogram["spectrogram"].shape
        figure, axes = plt.subplots(num_channels, 1)
        if num_channels == 1:
            axes = [axes]
        for c in range(num_channels):
            if num_channels == 1:
                spect = spectrogram["spectrogram"].numpy()
            else:
                spect = spectrogram["spectrogram"][c].numpy()
            axes[c].pcolormesh(spect, shading="gouraud")
            if num_channels > 1:
                axes[c].set_title(f"Channel {c+1}")
        figure.suptitle(title)
        return (plot2image(), )
