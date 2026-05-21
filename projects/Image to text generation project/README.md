# Image to Text Generation

A Jupyter notebook that generates a caption for an image. It loads a pretrained Vision Encoder-Decoder model (`bipin/image-caption-generator`) via Hugging Face Transformers and produces a text description of a given image.

## How to run

```
pip install transformers torch pillow
```

Open `Image_to_text_generation.ipynb` in Jupyter (or Google Colab) and run the cells.

## Dependencies

- transformers
- torch
- pillow

## Pyodide-runnable

No — it requires PyTorch and Hugging Face Transformers (large native ML libraries) and is delivered as a notebook, none of which run under Pyodide.
