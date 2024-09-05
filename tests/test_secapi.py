import pytest

from edgarpython.exceptions import InvalidCIK
from edgarpython.models import Submission
from edgarpython.secapi import getSubmissionsByCik, getXlsxUrl


def test_getSubmissionsByCik_fails_on_empty_cik():
    with pytest.raises(InvalidCIK) as _:
        getSubmissionsByCik("")


def test_getSubmissionsByCik():
    out = getSubmissionsByCik("0001018724")
    assert isinstance(out[0], Submission)


def test_getXlsxUrl_fails_on_invalid_cik():
    with pytest.raises(FileNotFoundError) as _:
        getXlsxUrl("", "")


def test_getXlsxUrl():
    out = getXlsxUrl("0001018724", "0001018724-24-000130")
    assert isinstance(out, str)
