import streamlit as st
from PIL import Image
import pytesseract
import io
import re
import time

# page configurations
st.set_page_config(
    page_title="Screenshot Calculator",
    page_icon="📈",
    layout="wide",

)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.title('Screenshot Calculator')

file_selector = st.file_uploader("Por favor, escolha um arquivo com a extensão .JPEG / .PNG / JPG",
                                 type=["jpeg", "png"])
process_file = st.button("Calcular")

# Remove the ‘#’ of the code below to add a loading bar!

# progress_text = "Calculando..."
# my_bar = st.progress(0, text=progress_text)


# for percent_complete in range(100):
#   time.sleep(0.01)
#   my_bar.progress(percent_complete + 1, text=progress_text)
# time.sleep(1)
# my_bar.empty()


st.divider()

if file_selector is not None:
    user_file = Image.open(io.BytesIO(file_selector.read()))

    if process_file:
        text = pytesseract.image_to_string(user_file)
        divided = text.splitlines()
        st.header("Texto extraído da imagem:")

        for line in divided:
            st.subheader(line)

        st.divider()

        num_separator = re.findall(r'\d+', text)

        num_converter = [int(num) for num in num_separator]

        # Remove duplicate numbers and preserve the order
        unique_nums = []
        seen = set()
        for num in num_converter:
            if num not in seen:
                unique_nums.append(num)
                seen.add(num)

        if not num_converter:
            st.header("Resultado do cálculo: ")
            st.subheader("Nenhum número foi identificado na imagem. Tente novamente")


        else:
            result = sum(unique_nums)
            st.header("Resultado do cálculo: ")
            st.subheader(result)
else:
    st.text("Por favor, insira uma imagem 📂")


