# Text-to-Image Generation Project

A Jupyter notebook (`Text_to_image.ipynb`) that demonstrates generating images from text prompts using a deep-learning text-to-image model.

## Example

1. Open `Text_to_image.ipynb` in Jupyter and run the setup cells to load the model.
2. Locate the cell that defines the text prompt and set it to a description such as `"a sunset over the ocean"`.
3. Run the generation cell — the model processes the prompt and produces an image.
4. The generated image is displayed inline in the notebook output below the cell.
5. Change the prompt to a different description and re-run the cell to generate a new image.

## How to run on localhost

Open the notebook in Jupyter:

```bash
jupyter notebook Text_to_image.ipynb
```

Install the deep-learning dependencies referenced inside the notebook (e.g. `diffusers`, `torch`, `transformers`).

## Dependencies

Deep-learning libraries such as `diffusers`, `torch`, and `transformers` (see the notebook cells).
