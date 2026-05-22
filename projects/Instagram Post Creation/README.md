# Instagram Post Creation

Generates an Instagram post image by drawing centered text onto a template image using Pillow.

## Example

1. Run `python main.py`.
2. The script opens `templates/basic_template.jpg`, draws the text `"My Instagram Post"` centered near the bottom in white using the Poppins font at size 30.
3. The finished image is saved to `output/post.jpg` and the following is printed:
   ```
   Instagram post saved to output/post.jpg
   ```

## How to run on localhost

```
pip install pillow
python main.py
```

Requires the bundled `templates/` and `fonts/` assets.

## Dependencies

Pillow.
