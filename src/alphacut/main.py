from pathlib import Path
from rembg import remove

INPUT = Path("src/alphacut/input")
OUTPUT = Path("src/alphacut/output")
SUPPORTED_FORMATS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".bmp",
    ".tiff",
}

def main():
    for image in INPUT.iterdir():
        if image.suffix.lower() in SUPPORTED_FORMATS:
            process_image(image)

def process_image(input_image: Path):
    output_image = OUTPUT / f"{input_image.stem}.png"

    with input_image.open("rb") as file:
        input_data = file.read()

    output = remove(input_data)

    if not isinstance(output, bytes):
        raise TypeError("Expected rembg to return bytes")


    with output_image.open("wb") as file:
        _ = file.write(output)


if __name__ == "__main__":
    main()