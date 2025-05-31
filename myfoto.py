import os
import io
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
            title="اختر صورة",
            filetypes=[("صور", "*.jpg *.jpeg *.png *.webp *.bmp")]
        )

        if input_path:
            filename = os.path.basename(input_path)
            name, _ = os.path.splitext(filename)
            output_path = os.path.join(os.path.dirname(input_path), f"{name}_compressed.jpg")

            success, size_kb = resize_and_compress_image(
                input_path=input_path,
                output_path=output_path
            )

            if success:
                messagebox.showinfo("تم", f"✅ تم ضغط الصورة ({size_kb} KB)")
            else:
                messagebox.showerror("فشل", "❌ لم يتم ضغط الصورة بالحجم المطلوب.")
        else:
            messagebox.showwarning("لا يوجد ملف", "❗ لم يتم اختيار صورة.")
    except Exception as e:
        import traceback
        messagebox.showerror("حدث خطأ", traceback.format_exc())
