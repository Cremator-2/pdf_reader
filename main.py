import ironpdf
import cv2
"""
cd venv/Scripts
activate

python -m ipykernel install --user --name=myenv --display-name "Python (myenv)"

jupyter kernelspec list
jupyter kernelspec remove <kernel_name>
jupyter kernelspec remove -f <path_to_kernel>

'''
import subprocess

command = f"python -V"
subprocess.run(command, shell=True)
'''

pip freeze > requirements.txt
"""


def pdf_to_img(path: str, dpi: int):
    pdf = ironpdf.PdfDocument.FromFile(path)
    pdf.RasterizeToImageFiles("images/*.png", DPI=dpi)


if __name__ == "__main__":
    pass


