import streamlit as st
import os
from pydub import AudioSegment
from PIL import Image
import io

# Function to compress audio
def compress_audio(input_file, bitrate='64k'):
  audio = AudioSegment.from_file(input_file)
  compressed_audio = audio.set_frame_rate(44100).set_channels(1)
  output_buffer = io.BytesIO()
  compressed_audio.export(output_buffer, format='mp3', bitrate=bitrate)
  return output_buffer.getvalue()

# Function to compress image
def compress_image(input_file, quality=50):
  img = Image.open(input_file)
  output_buffer = io.BytesIO()
  img_format = input_file.name.split(".")[-1].lower()
  
  if img_format not in ["jpg", "jpeg"]:
    st.warning("Only JPEG format is supported for compression. Converting the image to JPEG...")
    img = img.convert("RGB")
  
  img.save(output_buffer, format='JPEG', quality=quality)
  return output_buffer.getvalue()

import streamlit as st
import os
from pydub import AudioSegment
from PIL import Image
import io

# Function to compress audio
def compress_audio(input_file, bitrate='64k'):
  audio = AudioSegment.from_file(input_file)
  compressed_audio = audio.set_frame_rate(44100).set_channels(1)
  output_buffer = io.BytesIO()
  compressed_audio.export(output_buffer, format='mp3', bitrate=bitrate)
  return output_buffer.getvalue()

# Function to compress image
def compress_image(input_file, quality=50):
  img = Image.open(input_file)
  output_buffer = io.BytesIO()
  img_format = input_file.name.split(".")[-1].lower()
  
  if img_format not in ["jpg", "jpeg"]:
    st.warning("Only JPEG format is supported for compression. Converting the image to JPEG...")
    img = img.convert("RGB")
  
  img.save(output_buffer, format='JPEG', quality=quality)
  return output_buffer.getvalue()

# Define page for audio compression
def audio_compression():
  st.title("Audio Compression")

  # Main content - upload area (left column)
  col1, col2 = st.columns(2)
  with col1:
    st.write("""
    ## Upload your audio file and compress it!
    """)
    audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

  # Settings section - navbar style (right column)
  with col2:
    st.header("Settings")
    audio_bitrate = st.selectbox("Select audio bitrate", ["64k", "128k", "192k", "256k", "320k"])

  if audio_file is not None:
    st.audio(audio_file, format='audio/mp3', start_time=0)
    st.write("Uploaded Audio File Details:")
    audio_details = {"Filename":audio_file.name,"FileType":audio_file.type,"FileSize":audio_file.size}
    st.write(audio_details)

    # Compress audio button
    if st.button("Compress Audio"):
      st.write("Compressing audio...")
      compressed_audio = compress_audio(audio_file, bitrate=audio_bitrate)
      st.success("Audio compression successful!")

      # Download button for compressed audio
      st.write("### Download Compressed Audio")
      audio_download_button_str = f"Download Compressed Audio File ({os.path.splitext(audio_file.name)[0]}_compressed.mp3)"
      st.download_button(label=audio_download_button_str, data=compressed_audio, file_name=f"{os.path.splitext(audio_file.name)[0]}_compressed.mp3", mime="audio/mpeg", key=None)

# Define page for image compression
def image_compression():
  st.title("Image Compression")

  # Main content - upload area (left column)
  col1, col2 = st.columns(2)
  with col1:
    st.write("""
    ## Upload your image file and compress it!
    """)
    image_file = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])

  # Settings section - navbar style (right column)
  with col2:
    st.header("Settings")
    image_quality = st.slider("Select image quality", min_value=1, max_value=100, value=50)

  if image_file is not None:
    st.image(image_file, caption="Uploaded Image", use_column_width=True)
    st.write("Uploaded Image File Details:")
    image_details = {"Filename":image_file.name,"FileType":image_file.type,"FileSize":image_file.size}
    st.write(image_details)

    # Compress image button
    if st.button("Compress Image"):
      st.write("Compressing image...")
      compressed_image = compress_image(image_file, quality=image_quality)
      st.success
# Multipage function
def multipage():
    pages = {
        "Audio Compression": audio_compression,
        "Image Compression": image_compression
    }
    
    st.sidebar.title("UTS - 1217050106")
    st.sidebar.write("Muhammad Zidan Fauzi")
    page_selection = st.sidebar.radio("Go to", list(pages.keys()))
    
    page = pages[page_selection]
    page()

# Run the app
if __name__ == '__main__':
    multipage()
