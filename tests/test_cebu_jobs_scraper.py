#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_cebu_jobs_scraper
----------------------------------

Tests for `cebu_jobs_scraper` module.
"""

import pytest

from contextlib import contextmanager
from click.testing import CliRunner

from cebu_jobs_scraper import cebu_jobs_scraper
from cebu_jobs_scraper import cli


class TestCebu_jobs_scraper(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_something(self):
        pass
    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'cebu_jobs_scraper.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

    @classmethod
    def teardown_class(cls):
        pass

