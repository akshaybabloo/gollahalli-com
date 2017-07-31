from django.test import TestCase

from backup_restore.apps import BackupRestoreConfig


class BackupRestoreConfigTests(TestCase):
    """
    Test case for ``BackupRestoreConfig``
    """

    def test_authy_me_config(self):
        """
        Testing ``AuthyMeConfig`` class.
        """
        app = BackupRestoreConfig

        self.assertTrue(app.name, 'backup_restore')
