# Captcha Genrator 
A simple image captcha genrator

## Example

1. Run `Captcha_Genrator.py`. A Tkinter window opens displaying a randomly generated 6-digit image CAPTCHA (e.g. an image of `482931`), a text area, a **Submit** button, and a **Refresh** button.
2. Type the digits shown in the CAPTCHA image into the text area and click **Submit**. If the entry matches, a dialog shows "verified"; otherwise it shows "Not verified" and generates a new CAPTCHA automatically.
3. Click **Refresh** at any time to replace the current CAPTCHA image with a new one.

### Prerequisites
1. Install the dependencies by executing the following command 
   ```pip install -r requirements.txt```

2. Update the path of font in code (if required)
    ```image = ImageCaptcha(fonts=['<path>/ChelseaMarketsr.ttf', '<path>/DejaVuSanssr.ttf'])```

### Screenshot
![image](https://user-images.githubusercontent.com/39544459/137623915-1e837ada-f199-4513-a15d-ecbb969fd53e.png)

## *Mayur Singal*  
