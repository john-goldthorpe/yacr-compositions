import unittest
import utils.legacy_db
from pathlib import Path


class TestLegacyDb(unittest.TestCase):
    def test_db_file_exists(self):
        p = Path(utils.LEGACY_DB_FILENAME)
        self.assertTrue(p.exists(), 'Database does not exist')

    def test_first_record(self):
        comp_record = utils.get_legacy_records()[0]
        self.assertEqual(comp_record['Method'], 'Grandsire Triples')
        self.assertEqual(comp_record['Composer Normal'], 'J Holt')
        self.assertEqual(comp_record['Changes'], 5040)


if __name__ == '__main__':
    unittest.main()
