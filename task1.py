import os
import numpy as np
import rasterio
from PIL import Image

def compress_data(data, old_min=0, old_max=10000, new_min=0, new_max=255):
    return ((data - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min

def tiff_to_rgb_image(tiff_path, output_path=None):
    try:
        with rasterio.open(tiff_path) as src:
            image_data = src.read()  # shape: (bands, height, width)
            bands, height, width = image_data.shape
    except Exception as e:
        raise IOError(f"无法加载文件 '{tiff_path}': {e}")

    if bands != 5:
        raise ValueError(f"期望5个波段，但实际读取到 {bands} 个波段")

    compressed_data = compress_data(image_data)

    rgb_data = compressed_data[:3, :, :].astype(np.uint8)
    rgb_data = np.transpose(rgb_data, (1, 2, 0))  # 转换为 (height, width, channels)

    rgb_image = Image.fromarray(rgb_data)

    if output_path is None:
        output_path = os.path.splitext(tiff_path)[0] + "_rgb.png"

    rgb_image.save(output_path)
    print(f"RGB图像已保存到: {output_path}")


