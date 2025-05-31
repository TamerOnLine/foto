# 📸 tameronline-foto

A lightweight desktop tool to resize and compress images using Python and a simple GUI built with Tkinter.  
Designed to reduce image size without significant quality loss, with automatic compression and dimension adjustment.

## 🚀 Features

- Compress images to under 300KB (or any specified target).
- Resize images (default: 800x800 pixels).
- Supports common formats: JPG, PNG, WEBP, BMP.
- Simple graphical interface.
- User alerts for success or failure of the operation.

## 🖥️ Screenshot (optional)
> *(You can add a sample screenshot of the GUI or before/after results here later.)*

## 🧰 Requirements

```bash
pip install -r requirements.txt
```

- `pillow` – For image processing.
- `pyinstaller` – To optionally build an executable file.

## 🛠️ Usage

1. Run the script `myfoto.py`.
2. Select an image from your system.
3. The image will be resized and compressed to the same directory with a name like `image_compressed.jpg`.
4. A message box will confirm whether the compression was successful.

### From terminal (optional)
```bash
python myfoto.py
```

## 🧱 Project Structure

```
tameronline-foto/
├── README.md              ← This file
├── LICENSE                ← Apache 2.0 license
├── myfoto.py              ← Main script for GUI and image processing
└── requirements.txt       ← Required libraries
```

## 📦 Build Executable (Optional)

You can use `PyInstaller` to generate an executable:

```bash
pyinstaller --onefile myfoto.py
```

The executable will appear in the `dist/` folder.

## 📄 License

This project is licensed under the [Apache License 2.0](LICENSE).

## ✨ Author

- Tamer Hamad Faour – [GitHub: TamerOnLine](https://github.com/TamerOnLine)