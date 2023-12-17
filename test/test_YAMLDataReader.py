# -*- coding: utf-8 -*-
import pytest
import yaml
from Types import DataType
from YAMLDataReader import YAMLDataReader


class TestTextDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
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
        text = '''
                - Иванов Иван Иванович:
                    математика: 91
                    химия: 100
                - Петров Петр Петрович:
                    русский язык: 87
                    литература: 78
                - Иванов Петр Петрович:
                    русский язык: 90
                    литература: 90
                '''

        result = "Иванов Петр Петрович"

        return text, data, result

    @pytest.fixture()
    def filepath_and_data(
            self,
            file_and_data_content: tuple[str, DataType],
            tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.yml")

        yamlFormatText = yaml.safe_load(file_and_data_content[0])

        with open(str(p), 'w', encoding='utf-8') as file:
            yaml.dump(yamlFormatText, file)

        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = YAMLDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]

    def test_filter_by_mark(
            self,
            file_and_data_content: tuple[str, DataType, str]) -> None:
        result = YAMLDataReader().filterByMark(file_and_data_content[1])
        assert result == file_and_data_content[2]
