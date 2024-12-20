import sys
from datetime import datetime
from pathlib import Path


class ChatExtractor:
    @staticmethod
    def extract_from_file(file_path) -> Path:
        """
        Assumes: 'file_path' is a string representing the path to the log file or a pathlib.Path.

        Writes out the chat messages from the referenced log to an output file if successful.
        :returns: A pathlib.Path representing the path to the output file.
        """
        assert isinstance(file_path, (str, Path)), "'path' is not a string or a pathlib.Path."

        if isinstance(file_path, str):
            file_path = Path(file_path)

        output_file_path = Path("%s %s-filtered.txt" % (file_path.stem, datetime.now()))

        try:
            log_file = open(file_path, "r")
        except IOError:
            print("Unable to open log file: '%s'." % file_path)
        else:
            try:
                output_file = open(output_file_path, "w")
            except IOError:
                print("Unable to open output file: '%s'." % output_file_path)
            else:
                for line in log_file:
                    if "[CHAT]" in line and "into the lobby!" not in line:
                        output_file.write(line)

                output_file.close()

            log_file.close()

        return output_file_path


def main() -> None:
    if len(sys.argv) != 2:
        print("Expected 1 argument, got %i instead." % (len(sys.argv) - 1))
        return

    ChatExtractor.extract_from_file(Path(sys.argv[1]))


if __name__ == "__main__":
    main()
