Fasta project
===========

Библиотека для работы с FASTA файлами.

Быстрый старт
-------------

.. code-block:: python

   from fasta import Seq, FastaReader

   seq = Seq("test", "ATCGTUAACG")
   print(seq)  # Seq('test', 10 nucl, nucleotide)

   reader = FastaReader("small_example.fasta")
   for sequence in reader:
       print(sequence)

Документация API
----------------

.. toctree::
   :maxdepth: 2
   
   api
