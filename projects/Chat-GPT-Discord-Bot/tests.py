import unittest
from unittest.mock import patch, MagicMock
from Chat_GPT_Function import gpt, dalle3, dalle2
from dotenv import load_dotenv
import os

load_dotenv(override=True)

gpt_api_key = os.getenv("GPT_API_KEY")


class TestGPT(unittest.TestCase):
    @patch("Chat_GPT_Function.OpenAI")
    def test_gpt_success(self, mock_openai):
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content="Test output"))]
        mock_client.chat.completions.create.return_value = mock_response

        result = gpt("gpt-3.5-turbo", "prompt", "sys_prompt", 0.5)

        self.assertIsInstance(result, str)
        self.assertTrue(result.strip())
        mock_openai.assert_called_once_with(api_key=gpt_api_key)
        mock_client.chat.completions.create.assert_called_once_with(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "sys_prompt"},
                {"role": "user", "content": "prompt"},
            ],
            temperature=0.5,
            top_p=1,
        )

    @patch("Chat_GPT_Function.OpenAI")
    def test_gpt_failure(self, mock_openai):
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_client.chat.completions.create.side_effect = Exception("API error")

        with self.assertRaises(Exception):
            gpt("model", "prompt", "sys_prompt", 0.5)


class TestDALLE3(unittest.TestCase):
    @patch("Chat_GPT_Function.OpenAI")
    def test_dalle3_success(self, mock_openai):
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.data = [MagicMock(url="https://example.com/image.png")]
        mock_client.images.generate.return_value = mock_response

        result = dalle3("prompt", "hd", "1792x1024", "vivid")

        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("https://"))
        mock_openai.assert_called_once_with(api_key=gpt_api_key)
        mock_client.images.generate.assert_called_once_with(
            model="dall-e-3",
            prompt="prompt",
            size="1792x1024",
            quality="hd",
            style="vivid",
            n=1,
        )

    @patch("Chat_GPT_Function.OpenAI")
    def test_dalle3_failure(self, mock_openai):
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_client.images.generate.side_effect = Exception("API error")

        with self.assertRaises(Exception):
            dalle3("prompt", "quality", "size", "style")


class TestDALLE2(unittest.TestCase):
    @patch("Chat_GPT_Function.OpenAI")
    def test_dalle2_success(self, mock_openai):
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.data = [MagicMock(url="https://example.com/image.png")]
        mock_client.images.generate.return_value = mock_response

        result = dalle2("prompt", "256x256")

        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("https://"))
        mock_openai.assert_called_once_with(api_key=gpt_api_key)
        mock_client.images.generate.assert_called_once_with(
            model="dall-e-2", prompt="prompt", size="256x256", n=1
        )

    @patch("Chat_GPT_Function.OpenAI")
    def test_dalle2_failure(self, mock_openai):
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_client.images.generate.side_effect = Exception("API error")

        with self.assertRaises(Exception):
            dalle2("prompt", "size")


if __name__ == "__main__":
    unittest.main()
