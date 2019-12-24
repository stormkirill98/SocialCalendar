from unittest import TestCase

from server.entities.database_object import DatabaseObject


class TestDatabaseObject(TestCase):
    def setUp(self):
        self.db_object = DatabaseObject("id")

    def test_set_id(self):
        self.assertEqual(self.db_object.id, 'id')
        self.db_object.set_id("id123")
        self.assertEqual(self.db_object.id, 'id123')
