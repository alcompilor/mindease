"""unittest Journal module."""

import unittest
import datetime
from unittest.mock import MagicMock

from src.utils.journal.journal import Journal
from src.utils.db_connection.db_connection import DBConnection


class TestJournal(unittest.TestCase):
    """Test Journal class."""

    def setUp(self):
        """Set up method."""
        self.journal_content = (
            "Today, I made a conscious effort to "
            + "prioritize my well-being. I started the day with meditation "
            + "and a mindful breakfast, and then went for a long walk in "
            + "nature. I attended a yoga class and spent some time "
            + "journaling and reflecting on my goals. Finally, I treated "
            + "myself to a massage. I feel refreshed and energized, and I "
            + "realize the importance of making self-care a regular priority."
        )
        self.journal_date = datetime.date(2023, 4, 18)
        self.journal_id = 70
        self.journal_title = "A Day Focused on Self-Care"
        self.user_id = 3

        self.journal = Journal(
            self.journal_content,
            self.journal_date,
            self.journal_title,
            self.user_id,
        )

        self.db_connection = MagicMock(spec=DBConnection)
        self.db_connection.cursor = MagicMock()
        self.db_connection.cursor.fetchone = MagicMock()
        self.db_connection.cursor.close = MagicMock()
        self.db_connection.cnx = MagicMock()
        self.db_connection.cnx.close = MagicMock()

    def test_create_journal(self):
        """Test create_journal method."""
        result = self.journal.create_journal(
            self.journal_content,
            self.journal_date,
            self.journal_title,
            self.user_id,
        )

        self.assertTrue(result.get("journal_created"))

    def test_create_journal_error(self):
        """Test create_journal with query error."""
        result = self.journal.create_journal(
            self.journal_content,
            self.journal_date,
            self.journal_title,
            self.user_id,
        )
        self.assertTrue("error" in result)

    def test_get_all_journals(self):
        """Test get_all_journals method."""
        user_id = 98
        result = self.journal.get_all_journals(user_id)
        self.assertTrue(isinstance(result, dict))
        for journal in result:
            self.assertEqual(journal["user_id"], user_id)

    def test_search_journals(self):
        """Test search_journals method."""
        search_query = "self-care"
        result = self.journal.search_journals(self.user_id, search_query)
        self.assertTrue(isinstance(result, list))

    def test_search_journals_error(self):
        """Test search_journals with query error."""
        result = self.journal.search_journals(self.user_id, "")
        self.assertTrue("error" in result)

    @classmethod
    def tearDownClass(cls):
        """Remove inserted data from database."""
        database = DBConnection()
        query = "DELETE FROM Journal WHERE journal_id = %s"
        database.cursor.execute(query, (70,))
        database.cnx.commit()
        database.cursor.close()
        database.cnx.close()

    if __name__ == "__main__":
        unittest.main()
