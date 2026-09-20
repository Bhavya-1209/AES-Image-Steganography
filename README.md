# AES Image Steganography

A Python-based image steganography project that encrypts a text message using **AES-128** and hides the encrypted bytes inside an image using pixel-channel manipulation with OpenCV.

## 📌 Project Overview

This project combines:

- **AES-128 encryption** for protecting messages
- **Key-based encryption and extraction**
- **Image steganography** for hiding encrypted data
- **OpenCV** for image processing

The project is intended for educational use in cryptography and information security.

## 🚀 Features

- Encrypts text using AES-128 in CBC mode
- Derives a 128-bit AES key using SHA-256
- Hides encrypted bytes inside image pixel channels
- Saves the modified image as `encrypted_img.jpg`
- Extracts and decrypts the hidden message
- Detects incorrect keys or corrupted data

## 🛠️ Technologies Used

- Python 3
- OpenCV (`cv2`)
- PyCryptodome
- SHA-256
- AES-128
- Image Steganography

## 📂 Project Structure

```text
steganography/
├── aes_stego.py
├── stego.jpg
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Bhavya-1209/AES-Image-Steganography.git
```

### 2. Navigate to the Project

```bash
cd AES-Image-Steganography
```

### 3. Install Dependencies

```bash
pip install opencv-python pycryptodome
```

## ▶️ Usage

### 1. Prepare the Image

Place the input image in the expected location and update the image path in the Python script if required.

The current script uses:

```python
x = cv2.imread('/content/stego.jpg')
```

For local Windows execution, change it to:

```python
x = cv2.imread('stego.jpg')
```

### 2. Run the Program

```bash
python aes_stego.py
```

### 3. Enter the Required Information

The program asks for:

```text
Enter Key to encrypt & hide:
Enter Text to hide:
```

The encrypted image is saved as:

```text
encrypted_img.jpg
```

The program then asks whether the user wants to extract the message.

## 🔄 Working Process

1. Read the input image using OpenCV.
2. Accept a key and plaintext message.
3. Derive an AES-128 key using SHA-256.
4. Encrypt the message using AES-CBC.
5. Hide encrypted bytes in image pixel channels.
6. Save the modified image.
7. Extract the encrypted bytes.
8. Decrypt the message using the key.

## 🔐 Security and Technical Notes

- Use this project only with images and systems you own or are authorized to test.
- The current implementation uses AES-CBC without authentication, so message integrity is not independently verified.
- JPEG compression is lossy and may damage hidden pixel data. PNG is more suitable for lossless steganography.
- The current implementation expects the extraction process to run within the same program flow and uses the original encrypted message length.
- Do not use real passwords, confidential information, or sensitive personal data during demonstrations.

## 🔮 Future Improvements

- Use PNG instead of JPEG for lossless storage
- Add authenticated encryption such as AES-GCM
- Add a separate extraction mode
- Store encrypted message length safely
- Add capacity validation for the input image
- Improve error handling and input validation
- Create a graphical user interface using Tkinter
- Add PSNR and image-quality analysis

## 👨‍💻 Author

**Bhavya Bhaskar Arora**

Cybersecurity | Python | Cryptography | Steganography
