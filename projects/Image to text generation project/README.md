# Image to Text Generation

A Jupyter notebook that generates a caption for an image. It loads a pretrained Vision Encoder-Decoder model (`bipin/image-caption-generator`) via Hugging Face Transformers and produces a text description of a given image.

## Example

1. Open `Image_to_text_generation.ipynb` in Jupyter or Google Colab.
2. Set `img_name` to the path of your image, e.g. `img_name = "dog.jpg"`.
3. Run all cells. The notebook loads the `bipin/image-caption-generator` model and prints a generated caption such as:
   ```
   A woman in a white shirt and blue jeans is running on the sidewalk.
   ```

## How to run on localhost

```
pip install transformers torch pillow
```

Open `Image_to_text_generation.ipynb` in Jupyter (or Google Colab) and run the cells.

## Dependencies

- transformers
- torch
- pillow
