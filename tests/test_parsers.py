# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    # ======
    parser = FastaParser("data/test.fa")
    records = list(parser)
    assert len(records) == 100
    assert records[0][0] == "seq0"
    # ======


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    # ======
    parser = FastaParser("data/test.fq")
    record = next(iter(parser))
    assert record[0] is None
    # ======


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    # ======
    parser = FastqParser("data/test.fq")
    records = list(parser)
    assert len(records) == 100
    assert records[0][0] == "seq0"
    assert len(records[0]) == 3
    # ======

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    # ======
    parser = FastqParser("data/test.fa")
    record = next(iter(parser))
    assert record[0] is None
    # ======