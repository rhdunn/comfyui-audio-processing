# Copyright (C) 2024 Reece H. Dunn. SPDX-License-Identifier: GPL-3

from .io_nodes import LoadAudio
from .plot_nodes import PlotWaveform
from .spect_nodes import (
    Spectrogram, InverseSpectrogram,
    PowerSpectrogram, GriffinLim,
    MelSpectrogram
)

NODE_CLASS_MAPPINGS = {
    # I/O
    "ComfyAudio.LoadAudio": LoadAudio,
    # Plotting
    "ComfyAudio.PlotWaveform": PlotWaveform,
    # Spectrogram
    "ComfyAudio.Spectrogram": Spectrogram,
    "ComfyAudio.InverseSpectrogram": InverseSpectrogram,
    "ComfyAudio.PowerSpectrogram": PowerSpectrogram,
    "ComfyAudio.GriffinLim": GriffinLim,
    "ComfyAudio.MelSpectrogram": MelSpectrogram,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # I/O
    "ComfyAudio.LoadAudio": "Load Audio From Path",
    # Plotting
    "ComfyAudio.PlotWaveform": "Plot Waveform",
    # Spectrogram
    "ComfyAudio.Spectrogram": "Spectrogram",
    "ComfyAudio.InverseSpectrogram": "Inverse Spectrogram",
    "ComfyAudio.PowerSpectrogram": "Power Spectrogram",
    "ComfyAudio.GriffinLim": "Griffin Lim",
    "ComfyAudio.MelSpectrogram": "Mel-scale Spectrogram",
}
