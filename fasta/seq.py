class Seq:
    """
    Класс для работы с последовательностями.

    Attributes:
        title (str): Строка заголовка без символа ">"
        sequence (str): Биологическая последовательность
    """

    def __init__(self, title, sequence):
        """
        Инициализирование объекта Seq.

        Args:
            title (str): Строка заголовка из файла FASTA
            sequence (str): Биологическая последовательность

        Raises:
            ValueError: Если последовательность пустая
        """

        self.title = title.lstrip(">").strip()
        self.sequence = "".join(sequence.split()).upper()

        if not self.sequence:
            raise ValueError("Последовательность пуста")

    def __len__(self):
        """
        Возвращает длину последовательности.

        Returns:
            int: Длина последовательности
        """

        return len(self.sequence)

    def alphabet(self):
        """
        Определяет алфавит последовательности.

        Returns:
            str: 'nucleotide' или 'protein'
        """

        protein_elements = set("ACDEFGHIKLMNPQRSTVWY")
        nucleotide_elements = set('ATGCUN')
        if all(element in nucleotide_elements for element in self.sequence):
            return "nucleotide"
        elif all(element in protein_elements for element in self.sequence):
            return "protein"
        else:
            return "unknown"

    def __str__(self):
        """
        Возвращает строковое представление в формате FASTA.

        Returns:
            str: Красиво оформленная строка с информацией о последовательности
        """

        sequence_type = self.alphabet()
        sequence_lenght = len(self)
        return f"Seq('{self.title}', {sequence_lenght}, {sequence_type})"

    def to_fasta(self):
        """
        Возвращает строку FASTA для записи в файл.
        """
        result = f">{self.title}\n"
        for i in range(0, len(self.sequence), 70):
            result += self.sequence[i : i + 70] + "\n"
        return result.rstrip()
