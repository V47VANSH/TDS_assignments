# from PIL import Image
# import os

# def resize_and_compress_png(input_path, output_path, size=(10, 10), quality=50):
#     """
#     Resize PNG and compress it with adjustable quality via color quantization.

#     :param input_path: Path to input PNG
#     :param output_path: Path to save compressed PNG
#     :param size: Target resize dimensions (w, h)
#     :param quality: 1-100 (higher = more colors, better quality, larger file)
#     """
#     img = Image.open(input_path).convert("RGBA")
    
#     # Resize
#     img = img.resize(size, Image.LANCZOS)
    
#     # Map quality (1–100) to number of colors (2–256)
#     colors = max(2, min(256, int(quality * 2.55)))
    
#     # Quantize reduces colors (lossy but still PNG format)
#     img = img.quantize(colors=colors)
    
#     # Save optimized PNG
#     img.save(output_path, "PNG", optimize=True)
    
#     final_size = os.path.getsize(output_path)
#     print(f"Compressed PNG saved at {output_path}, size={final_size} bytes, colors={colors}")

# # Example usage
# # resize_and_compress_png("input.png", "output.png", size=(10, 10), quality=20)

# resize_and_compress_png("D:\\Downloads\\iitmimage.png", "D:\\Downloads\\output.png", size=(350,350), quality=2)

# # compress_to_extreme("D:\\Downloads\\iitmimage.png", "D:\\Downloads\\output.png")

# from PIL import Image
# import os

# def compress_simple_png(input_path, output_path, size=None, colors=4):
#     """
#     Compress a simple PNG (few colors) into a very small indexed PNG without distortion.
    
#     :param input_path: Path to input PNG
#     :param output_path: Path to save compressed PNG
#     :param size: Optional tuple (width, height) to resize
#     :param colors: Number of colors for palette (e.g. 4 for your case)
#     """
#     img = Image.open(input_path).convert("RGBA")
    
#     # Resize if needed
#     if size:
#         img = img.resize(size, Image.NEAREST)  # NEAREST keeps sharp edges for logos/icons
    
#     # Quantize to limited colors (palette mode, no dithering)
#     img = img.quantize(colors=colors, method=0, dither=Image.NONE)
    
#     # Save optimized PNG
#     img.save(output_path, format="PNG", optimize=True)
    
#     final_size = os.path.getsize(output_path)
#     print(f"Compressed PNG saved at {output_path}, size={final_size} bytes, colors={colors}")

# # Example usage
# compress_simple_png("D:\\Downloads\\iitmimage.png", "D:\\Downloads\\compressed.png", size=(20, 20), colors=4)


# from PIL import Image
# import os

# # Paths
input_path = "D:\\Downloads\\iitmimage.png"
output_path = "D:\\Downloads\\iitmimage_compressed.webp"

# def compress_simple_png(input_path, output_path, target_bytes=400, colors=6):
#     """
#     Compress PNG with few colors to get under target_bytes.
#     Will progressively reduce resolution until file size < target_bytes.
#     """
#     img = Image.open(input_path).convert("RGB")  # use RGB to avoid RGBA quantize issues

#     # Start with current size
#     width, height = img.size

#     # Loop until compressed file is under target_bytes
#     while True:
#         # Resize image
#         resized = img.resize((width, height), Image.Resampling.NEAREST)

#         # Quantize to limited colors (lossless for flat colors)
#         quantized = resized.quantize(colors=colors, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE)

#         # Save temporary PNG
#         quantized.save(output_path, format="PNG", optimize=True)

#         # Check file size
#         size_bytes = os.path.getsize(output_path)
#         if size_bytes <= target_bytes or width <= 1 or height <= 1:
#             return size_bytes, width, height

#         # Reduce resolution further
#         width = max(1, width // 2)
#         height = max(1, height // 2)


# # Run compression
# final_size, final_w, final_h = compress_simple_png(input_path, output_path)

# final_size, final_w, final_h, output_path




"""
PNG to WebP Lossless Compression Script
Provides maximum lossless compression for PNG images and converts them to WebP format.
"""

from PIL import Image
import os
import sys
from pathlib import Path


def compress_png_to_webp(input_path, output_path=None, quality=100, method=6):
    """
    Convert PNG to WebP with maximum lossless compression.
    
    Args:
        input_path (str): Path to the input PNG file
        output_path (str, optional): Path to save the WebP file. 
                                    If None, uses same name with .webp extension
        quality (int): Quality setting (0-100). For lossless, use 100
        method (int): Compression method (0-6). Higher = better compression but slower.
                     6 is maximum compression
    
    Returns:
        tuple: (output_path, original_size, compressed_size, compression_ratio)
    """
    try:
        # Open the PNG image
        img = Image.open(input_path)
        
        # Get original file size
        original_size = os.path.getsize(input_path)
        
        # Generate output path if not provided
        if output_path is None:
            output_path = Path(input_path).with_suffix('.webp')
        
        # Save as WebP with lossless compression
        # lossless=True ensures no quality loss
        # quality=100 with lossless=True provides maximum compression effort
        # method=6 uses the slowest but best compression algorithm
        img.save(
            output_path,
            'WEBP',
            lossless=True,
            quality=quality,
            method=method
        )
        
        # Get compressed file size
        compressed_size = os.path.getsize(output_path)
        
        # Calculate compression ratio
        compression_ratio = (1 - compressed_size / original_size) * 100
        
        print(f"✓ Conversion successful!")
        print(f"  Input:  {input_path}")
        print(f"  Output: {output_path}")
        print(f"  Original size:   {original_size:,} bytes ({original_size / 1024:.2f} KB)")
        print(f"  Compressed size: {compressed_size:,} bytes ({compressed_size / 1024:.2f} KB)")
        print(f"  Compression:     {compression_ratio:.2f}% reduction")
        
        return output_path, original_size, compressed_size, compression_ratio
        
    except FileNotFoundError:
        print(f"✗ Error: File '{input_path}' not found.")
        return None
    except Exception as e:
        print(f"✗ Error during conversion: {str(e)}")
        return None


def batch_compress_png_to_webp(input_dir, output_dir=None, quality=100, method=6):
    """
    Batch convert all PNG files in a directory to WebP format.
    
    Args:
        input_dir (str): Directory containing PNG files
        output_dir (str, optional): Directory to save WebP files. 
                                   If None, uses same directory as input
        quality (int): Quality setting (0-100)
        method (int): Compression method (0-6)
    
    Returns:
        list: List of tuples with conversion results
    """
    input_path = Path(input_dir)
    
    if not input_path.exists():
        print(f"✗ Error: Directory '{input_dir}' not found.")
        return []
    
    # Set output directory
    if output_dir is None:
        output_path = input_path
    else:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
    
    # Find all PNG files
    png_files = list(input_path.glob('*.png')) + list(input_path.glob('*.PNG'))
    
    if not png_files:
        print(f"✗ No PNG files found in '{input_dir}'")
        return []
    
    print(f"Found {len(png_files)} PNG file(s) to convert.\n")
    
    results = []
    total_original = 0
    total_compressed = 0
    
    for png_file in png_files:
        webp_file = output_path / (png_file.stem + '.webp')
        result = compress_png_to_webp(png_file, webp_file, quality, method)
        
        if result:
            results.append(result)
            total_original += result[1]
            total_compressed += result[2]
        
        print()  # Empty line between files
    
    # Print summary
    if results:
        total_reduction = (1 - total_compressed / total_original) * 100
        print("=" * 60)
        print(f"SUMMARY: Converted {len(results)} file(s)")
        print(f"Total original size:   {total_original:,} bytes ({total_original / 1024 / 1024:.2f} MB)")
        print(f"Total compressed size: {total_compressed:,} bytes ({total_compressed / 1024 / 1024:.2f} MB)")
        print(f"Total reduction:       {total_reduction:.2f}%")
        print("=" * 60)
    
    return results


def optimize_existing_png(input_path, output_path=None):
    """
    Optimize PNG file before converting to WebP for even better compression.
    Uses PIL's optimize feature.
    
    Args:
        input_path (str): Path to input PNG file
        output_path (str, optional): Path to save optimized PNG
    
    Returns:
        str: Path to optimized PNG file
    """
    try:
        img = Image.open(input_path)
        
        if output_path is None:
            output_path = Path(input_path).with_stem(Path(input_path).stem + '_optimized')
        
        # Save with PNG optimization
        img.save(output_path, 'PNG', optimize=True, compress_level=9)
        
        print(f"✓ PNG optimized: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"✗ Error optimizing PNG: {str(e)}")
        return None


# Example usage
if __name__ == "__main__":
    print("PNG to WebP Lossless Compression Tool")
    print("=" * 60)
    compress_png_to_webp(input_path, output_path)
    
    # # Example 1: Single file conversion
    # if len(sys.argv) > 1:
    #     # Command-line usage
    #     input_file = sys.argv[1]
    #     output_file = sys.argv[2] if len(sys.argv) > 2 else None
    #     compress_png_to_webp(input_file, output_file)
    # else:
    #     # Demo/interactive usage
    #     print("\nUsage Examples:")
    #     print("-" * 60)
    #     print("1. Single file conversion:")
    #     print("   python image_compressor.py input.png [output.webp]")
    #     print("\n2. In Python script:")
    #     print("   compress_png_to_webp('image.png')")
    #     print("   compress_png_to_webp('image.png', 'output.webp')")
    #     print("\n3. Batch conversion:")
    #     print("   batch_compress_png_to_webp('input_folder', 'output_folder')")
    #     print("\n4. With PNG optimization first:")
    #     print("   optimized = optimize_existing_png('image.png')")
    #     print("   compress_png_to_webp(optimized)")
    #     print("=" * 60)