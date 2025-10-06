from fasta import Seq, FastaReader

seq = Seq("test", "ATCGTUAACG")
print(f"Длина: {len(seq)}")
print(f"Тип: {seq.alphabet()}")

reader_one = FastaReader("small_example.fasta")
for sequence in reader_one:
    print(sequence)

reader_two = FastaReader("big_example.fasta")
for sequence in reader_two:
    print(sequence)
