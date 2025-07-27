from common import run_importer_test

from uabean.importers.privatbank_xls import get_test_importer


def test_privatbank_xls_importer(capsys):
    run_importer_test(get_test_importer(), capsys)