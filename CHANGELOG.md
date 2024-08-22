# Change Log
> Release notes for comfyui-audio-processing.

## [Unreleased]

### Added

### Changed

### Removed

## [1.0.0] - 2024-08-22

### Added

The following nodes have been added:

| Name                  | Description                                                                         |
|-----------------------|-------------------------------------------------------------------------------------|
| Load Audio From Path  | Same as "Load Audio" but loads from a local path instead of an uploaded audio file. |
| Plot Waveform         | Plots the waveform of an `AUDIO` object.                                            |
| Spectrogram           | Computes the spectrogram of a given `AUDIO` object.                                 |
| Inverse Spectrogram   | Converts a complex-valued spectrogram to `AUDIO`.                                   |
| Griffin Lim           | Converts a real-valued spectrogram to `AUDIO` using the Griffin-Lim algorithm.      |
| Plot Spectrogram      | Plots the spectrogram of a `SPECT` object.                                          |
| Linear Filter Bank    | Create a linear filter bank.                                                        |
| Mel-scale Filter Bank | Create a mel-scale filter bank.                                                     |
| Apply Filter Bank     | Apply the specified filter bank to the spectrogram.                                 |
| Plot Filter Bank      | Plots the `FILTER_BANK` object.                                                     |

[Unreleased]: https://github.com/rhdunn/comfyui-audio-processing/compare/1.0.0...HEAD
[1.0.0]: https://github.com/rhdunn/comfyui-audio-processing/releases/tag/1.0.0
