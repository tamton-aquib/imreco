# Imreco

Image-Resizer-Converter.
A python cli program to perform basic operations on images using opencv. (WIP)

This project was made possible by: @[shana](https://github.com/Shanayasmin).
This project was done regarding [tinkerhub co-coder](https://tinkerhub.org/).

### Installation:
```python
pip install imreco
```

### Usage:
```sh
# Syntax:
imreco resize  -i <input_file> -o <output_file> -s 300x400
imreco convert -i <input_file> -o <output_file> 
```

### TODOS:
- [x] Resizer: To change dimension of the provided image, and save it to a new file.
- [x] Converter: To change file formats from png to jpg, etc.
- [ ] Compressor: To compress jpg files in file size.
- [x] Config: Add user config options. (maybe argparse or typer)
- [ ] Checks multiple files or a directory.
- [ ] Chain functions and/or operations
