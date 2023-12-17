# -*- coding: utf-8 -*-
import pytest
from Types import DataType
from HandleData import HandleData


class TestHandleData:

    @pytest.fixture()
    def data_content(self) -> tuple[str, DataType]:
        data = [
            {
                "Иванов Иван Иванович":
                {"математика": 91, "химия": 100}
            },
            {
                "Петров Петр Петрович":
                {"русский язык": 87, "литература": 78}
            },
            {
                "Иванов Петр Петрович":
                {"русский язык": 90, "литература": 90}
            }
        ]

        result = "Иванов Петр Петрович"

        return data, result

    def test_filter_by_mark(
            self,
            data_content: tuple[str, DataType, str]) -> None:
        result = HandleData().filterByMark(data_content[0])
        assert result == data_content[1]
