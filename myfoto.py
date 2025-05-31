import os
import io
import traceback
from tkinter import Tk, filedialog, messagebox
from PIL import Image

def resize_and_compress_image(
    input_path,
    output_path,
    target_width=800,
    target_height=800,
    max_size_kb=300,
    image_format='JPEG',
    min_quality=10,
    step=5
):
    """
    Resize and compress an image to fit within target dimensions and size.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path where the compressed image will be saved.
        target_width (int, optional): Desired image width. Defaults to 800.
        target_height (int, optional): Desired image height. Defaults to 800.
        max_size_kb (int, optional): Maximum file size in kilobytes. Defaults to 300.
        image_format (str, optional): Format to save the image. Defaults to 'JPEG'.
        min_quality (int, optional): Minimum JPEG quality to try. Defaults to 10.
        step (int, optional): Step decrement for quality. Defaults to 5.

    Returns:
        tuple: (success (bool), final_size_kb (int))
    """
    img = Image.open(input_path)
    img = img.convert("RGB")
    img = img.resize((target_width, target_height), Image.LANCZOS)

    quality = 95
    while quality >= min_quality:
        buffer = io.BytesIO()
        img.save(buffer, format=image_format, quality=quality)
        size_kb = buffer.tell() / 1024

        if size_kb <= max_size_kb:
            with open(output_path, 'wb') as f:
                f.write(buffer.getvalue())
            return True, int(size_kb)

        quality -= step

    return False, 0


if __name__ == "__main__":
    try:
        root = Tk()
        root.withdraw()

        input_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Images", "*.jpg *.jpeg *.png *.webp *.bmp")]
        )

        if input_path:
            filename = os.path.basename(input_path)
            name, _ = os.path.splitext(filename)
            output_path = os.path.join(
                os.path.dirname(input_path), f"{name}_compressed.jpg"
            )

            success, size_kb = resize_and_compress_image(
                input_path=input_path,
                output_path=output_path
            )

            if success:
                messagebox.showinfo("Success", f"Image compressed successfully ({size_kb} KB)")
            else:
                messagebox.showerror("Failure", "Image could not be compressed to the desired size.")
        else:
            messagebox.showwarning("No File Selected", "No image file was selected.")

    except Exception:
        messagebox.showerror("Error", traceback.format_exc())
