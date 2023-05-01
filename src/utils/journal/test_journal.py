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
        
        self.journal_content = "Today, I made a conscious effort to " + \
            "prioritize my well-being. I started the day with meditation " + \
            "and a mindful breakfast, and then went for a long walk in " + \
            "nature. I attended a yoga class and spent some time " + \
            "journaling and reflecting on my goals. Finally, I treated " + \
            "myself to a massage. I feel refreshed and energized, and I " + \
            "realize the importance of making self-care a regular priority."
        self.journal_date = datetime.date(2023, 4, 18)
        self.journal_id = 70
        self.journal_title = "A Day Focused on Self-Care"
        self.user_id = 3

        
        self.journal = Journal(self.journal_content, self.journal_date,
                               self.journal_id, self.journal_title,
                               self.user_id)

        
        self.db_connection = MagicMock(spec=DBConnection)
        self.db_connection.cursor = MagicMock()
        self.db_connection.cursor.fetchone = MagicMock()
        self.db_connection.cursor.close = MagicMock()
        self.db_connection.cnx = MagicMock()
        self.db_connection.cnx.close = MagicMock()

    def test_create_journal(self):
        """Test create_journal method."""
        
        self.db_connection.cursor.execute = MagicMock()
        
        self.journal.create_journal(self.journal_content, self.journal_date,
                                    self.journal_title, self.user_id,
                                    self.journal_id)
        
        
        self.db_connection.cursor.execute.assert_called_with(
            "INSERT INTO Journal (journal_id, user_id, journal_title, " +
            "journal_content, journal_date) VALUES (%s, %s, %s, %s, %s)",
            (self.journal_id, self.user_id, self.journal_title,
             self.journal_content, self.journal_date))
        
        
        self.db_connection.cnx.commit.assert_called()
        self.db_connection.cursor.close.assert_called()
        self.db_connection.cnx.close.assert_called()

    if __name__ == "__main__":
        unittest.main()