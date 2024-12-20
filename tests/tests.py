import os
import unittest
from pathlib import Path
from chat_extractor import ChatExtractor


class TestChatExtractor(unittest.TestCase):
    def test_extract_from_chat(self):
        test_log_path = Path(__file__).cwd().joinpath("test_log_empty.log")
        output_file_path = Path(ChatExtractor.extract_from_file(test_log_path))

        self.assertTrue(output_file_path.exists(), "output_file_path does not exist.")
        os.remove(output_file_path)
        # TODO: Make this test check the contents as well if possible.


if __name__ == '__main__':
    unittest.main()
