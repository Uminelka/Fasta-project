import os
from seq import Seq


class FastaReader:
    """
    Класс для чтения файла в формате fasta.

    Attributes:
        path_to_file (str): Путь к файлу fasta
    """

    def __init__(self, path_to_file):
        """
        Инициализирует объект FastaReader.

        Raises:
            FileNotFoundError: Если файл не существует
        """

        if not os.path.exists(path_to_file):
            raise FileNotFoundError(f"Файл не найден: {path_to_file}")

        self.path_to_file = path_to_file

    def _is_fasta(self):
        """
        Проверяет, имеет ли файл допустимый формат fasta.
        """

        try:
            with open(self.path_to_file, "r", encoding="utf-8") as file:
                first_line = file.readline().strip()
                return first_line.startswith(">")
        except:
            return False

    def __iter__(self):
        """
        Перебирает последовательности с помощью генератора.
        """

        title = None
        sequence_lines = []

        with open(self.path_to_file, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                if line.startswith(">"):
                    if title is not None:
                        yield Seq(title, "".join(sequence_lines))
                    title = line[1:]
                    sequence_lines = []
                else:
                    sequence_lines.append(line)

        if title is not None:
            yield Seq(title, "".join(sequence_lines))
