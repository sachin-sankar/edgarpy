import pytest

from edgarpy.exceptions import InvalidCIK
from edgarpy.models import Submission
from edgarpy.secapi import getSubmissionsByCik


def test_getSubmissionsByCik_fails_on_empty_cik():
    with pytest.raises(InvalidCIK) as e_info:
        getSubmissionsByCik("")


def test_getSubmissionsByCik():
    out = getSubmissionsByCik("0001018724")
    assert isinstance(out[0], Submission)
