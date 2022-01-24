# %% [markdown]
# #### Intall pytesseract on windows from
# #### https://github.com/UB-Mannheim/tesseract/wiki
# #### pip install pytesseract
# #### pip install opencv-python

# %%
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# %% [markdown]
# # Bengali Language

# %%
#Read Image
ben_img = cv2.imread('img/bengali.jpg')

# %%
#Extract Text from Image
text = pytesseract.image_to_string(ben_img,lang='ben')
print(text)

# %% [markdown]
# # English Language

# %%
# Read Image
eng_img = cv2.imread('img/english.jpg')

# %%
#Extract Text from Image
text = pytesseract.image_to_string(eng_img,lang='eng')
print(text)


