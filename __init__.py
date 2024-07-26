# Copyright (C) 2024 Reece H. Dunn. SPDX-License-Identifier: GPL-3

from .io_nodes import LoadAudio

NODE_CLASS_MAPPINGS = {
    "ComfyAudio.LoadAudio": LoadAudio,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyAudio.LoadAudio": "Load Audio From Path",
}
