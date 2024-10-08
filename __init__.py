# Copyright (C) 2024 Reece H. Dunn. SPDX-License-Identifier: GPL-3

from .fb_nodes import (
    LinearFilterBank, MelScaleFilterBank,
    ApplyFilterBank
)
from .io_nodes import LoadAudio
from .plot_nodes import (PlotWaveform, PlotSpectrogram, PlotFilterBank)
from .spect_nodes import (
    Spectrogram, InverseSpectrogram,
    GriffinLim,
)

NODE_CLASS_MAPPINGS = {
    # Filter Banks
    "ComfyAudio.LinearFilterBank": LinearFilterBank,
    "ComfyAudio.MelScaleFilterBank": MelScaleFilterBank,
    "ComfyAudio.ApplyFilterBank": ApplyFilterBank,
    # I/O
    "ComfyAudio.LoadAudio": LoadAudio,
    # Plotting
    "ComfyAudio.PlotWaveform": PlotWaveform,
    "ComfyAudio.PlotSpectrogram": PlotSpectrogram,
    "ComfyAudio.PlotFilterBank": PlotFilterBank,
    # Spectrogram
    "ComfyAudio.Spectrogram": Spectrogram,
    "ComfyAudio.InverseSpectrogram": InverseSpectrogram,
    "ComfyAudio.GriffinLim": GriffinLim,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # Filter Banks
    "ComfyAudio.LinearFilterBank": "Linear Filter Bank",
    "ComfyAudio.MelScaleFilterBank": "Mel-scale Filter Bank",
    "ComfyAudio.ApplyFilterBank": "Apply Filter Bank",
    # I/O
    "ComfyAudio.LoadAudio": "Load Audio From Path",
    # Plotting
    "ComfyAudio.PlotWaveform": "Plot Waveform",
    "ComfyAudio.PlotSpectrogram": "Plot Spectrogram",
    "ComfyAudio.PlotFilterBank": "Plot Filter Bank",
    # Spectrogram
    "ComfyAudio.Spectrogram": "Spectrogram",
    "ComfyAudio.InverseSpectrogram": "Inverse Spectrogram",
    "ComfyAudio.GriffinLim": "Griffin Lim",
}
