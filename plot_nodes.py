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
        return {"required": {"audio": ("AUDIO",)},
                "optional": {"title": ("STRING", {"default": "Waveform"}),
                             "xlabel": ("STRING", {"default": "Time (s)"}),
                             "ylabel": ("STRING", {"default": "Amplitude"}),
                             "show_grid": ("BOOLEAN", {"default": True}),}}

    CATEGORY = "AudioProcessing/plot"

    RETURN_TYPES = ("IMAGE", )
    FUNCTION = "plot"

    def plot(self, audio, title="Waveform", xlabel="Time (s)", ylabel="Amplitude", show_grid=True):
        waveform = audio["waveform"].movedim(0, -1).numpy()
        num_channels, num_frames, _ = waveform.shape
        time_axis = torch.arange(0, num_frames) / audio["sample_rate"]
        figure, axes = plt.subplots(num_channels, 1)
        if num_channels == 1:
            axes = [axes]
        for c in range(num_channels):
            axes[c].plot(time_axis, waveform[c], linewidth=1)
            axes[c].grid(show_grid)
            axes[c].set_ylabel(ylabel)
            axes[c].set_xlabel(xlabel)
            if num_channels > 1:
                axes[c].set_title(f"Channel {c+1}")
        figure.suptitle(title)
        figure.tight_layout()
        return (plot2image(), )


class PlotSpectrogram:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"spectrogram": ("SPECT",)},
                "optional": {"title": ("STRING", {"default": "Spectrogram"}),
                             "xlabel": ("STRING", {"default": "Time (s)"}),
                             "ylabel": ("STRING", {"default": "Frequency (Hz)"}),
                             "show_grid": ("BOOLEAN", {"default": False}),}}

    CATEGORY = "AudioProcessing/plot"

    RETURN_TYPES = ("IMAGE", )
    FUNCTION = "plot"

    def plot(self, spectrogram, title="Spectrogram", xlabel="Time (s)", ylabel="Frequency (Hz)", show_grid=False):
        if spectrogram["stype"] == "complex":
            raise Exception(f"The spectrogram is not a real-valued spectrogram: {spectrogram['stype']}")
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
            axes[c].imshow(spect, origin="lower",aspect="auto", interpolation="nearest")
            axes[c].grid(show_grid)
            axes[c].set_ylabel(ylabel)
            axes[c].set_xlabel(xlabel)
            if num_channels > 1:
                axes[c].set_title(f"Channel {c+1}")
        figure.suptitle(title)
        figure.tight_layout()
        return (plot2image(), )
