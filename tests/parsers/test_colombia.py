import pandas as pd
import pytest

from cpilatam.parsers.base import CPI_SCHEMA
from cpilatam.parsers.colombia import ColombiaCPIParser
from cpilatam.retrievers.colombia import ColombiaCPIRetriever


class TestColombiaParser:
    @pytest.fixture
    def setUp(self, monkeypatch):
        # crear instancia
        self.parser = ColombiaCPIParser()
        self.retriever = ColombiaCPIRetriever()

        # mock download using monkeypatch
        monkeypatch.setattr(self.parser, "download", self.mock_download_parser)
        monkeypatch.setattr(self.retriever, "download", self.mock_download_retrieval)

    def mock_download_parser(self):
        # Read the data and assign it to self.data
        self.parser.data = pd.read_excel("data/raw/colombia.xlsx")

    def mock_download_retrieval(self):
        return "cpilatam/retrievers/retrieved_files/colombia_cpi.xlsx", False

    def test_parse(self, setUp):
        # read data
        self.parser.download()

        # proceed to parse the data
        self.parser.parse()

        # assert that the schema is correct
        CPI_SCHEMA.validate(self.parser.data)

    def test_retrieval(self, setUp):
        # read data
        path, error = self.retriever.download()

        # parse and validate the data
        CPI_SCHEMA.validate(self.retriever.parse(path))
