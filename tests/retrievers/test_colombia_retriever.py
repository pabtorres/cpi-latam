import pytest

from cpilatam.parsers.base import CPI_SCHEMA
from cpilatam.retrievers.colombia import ColombiaCPIRetriever


class TestColombiaRetriever:
    @pytest.fixture
    def setUp(self, monkeypatch):
        # crear instancia
        self.retriever = ColombiaCPIRetriever()

        # mock download using monkeypatch
        monkeypatch.setattr(self.retriever, "download", self.mock_download)

    def mock_download(self):
        return "cpilatam/retrievers/retrieved_files/colombia_cpi.xlsx", False

    def test_retrieval(self, setUp):
        # read data
        path, error = self.retriever.download()

        # parse and validate the data
        CPI_SCHEMA.validate(self.retriever.parse(path))
