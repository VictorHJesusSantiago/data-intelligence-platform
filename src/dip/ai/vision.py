from __future__ import annotations

import math
from collections import deque
from typing import Any


class Vision:
    """Portable graymap computer vision: statistics, thresholding and objects."""

    def analyze_pgm(self, payload: bytes, threshold: int | None = None) -> dict[str, Any]:
        width, height, maximum, pixels = self._read_pgm(payload)
        normalized = [value * 255 / maximum for value in pixels]
        brightness = sum(normalized) / len(normalized)
        contrast = math.sqrt(sum((value - brightness) ** 2 for value in normalized) / len(normalized))
        cutoff = threshold if threshold is not None else int(brightness)
        foreground = {index for index, value in enumerate(normalized) if value < cutoff}
        objects = self._components(foreground, width, height)
        histogram = [0] * 16
        for value in normalized:
            histogram[min(15, int(value) // 16)] += 1
        return {"width": width, "height": height, "brightness": round(brightness, 4),
                "contrast": round(contrast, 4), "threshold": cutoff,
                "objects": objects, "histogram": histogram}

    @staticmethod
    def _read_pgm(payload: bytes) -> tuple[int, int, int, list[int]]:
        tokens = []
        for line in payload.splitlines():
            line = line.split(b"#", 1)[0]
            tokens.extend(line.split())
        if len(tokens) < 4 or tokens[0] != b"P2":
            raise ValueError("only ASCII PGM (P2) images are supported")
        width, height, maximum = map(int, tokens[1:4])
        pixels = list(map(int, tokens[4:]))
        if width < 1 or height < 1 or maximum < 1 or len(pixels) != width * height:
            raise ValueError("invalid PGM dimensions or pixel count")
        if any(value < 0 or value > maximum for value in pixels):
            raise ValueError("PGM pixel is outside its declared range")
        return width, height, maximum, pixels

    @staticmethod
    def _components(foreground: set[int], width: int, height: int) -> list[dict[str, int]]:
        remaining, objects = set(foreground), []
        while remaining:
            start, queue, points = remaining.pop(), deque(), []
            queue.append(start)
            while queue:
                current = queue.popleft()
                x, y = current % width, current // width
                points.append((x, y))
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    index = ny * width + nx
                    if 0 <= nx < width and 0 <= ny < height and index in remaining:
                        remaining.remove(index)
                        queue.append(index)
            xs, ys = zip(*points)
            objects.append({"x": min(xs), "y": min(ys), "width": max(xs) - min(xs) + 1,
                            "height": max(ys) - min(ys) + 1, "area": len(points)})
        return sorted(objects, key=lambda item: (-item["area"], item["y"], item["x"]))
