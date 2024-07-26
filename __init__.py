# Copyright (C) 2024 Reece H. Dunn. SPDX-License-Identifier: GPL-3

from .io_nodes import LoadAudio
from .plot_nodes import PlotWaveform
from .spect_nodes import Spectrogram

NODE_CLASS_MAPPINGS = {
    "ComfyAudio.LoadAudio": LoadAudio,
    "ComfyAudio.PlotWaveform": PlotWaveform,
    "ComfyAudio.Spectrogram": Spectrogram,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyAudio.LoadAudio": "Load Audio From Path",
    "ComfyAudio.PlotWaveform": "Plot Waveform",
    "ComfyAudio.Spectrogram": "Spectrogram",
}
