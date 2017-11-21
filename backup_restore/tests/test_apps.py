from django.apps import apps
from django.test import TestCase

from backup_restore.apps import BackupRestoreConfig


class BackupRestoreConfigTests(TestCase):
    """
    Test case for ``BackupRestoreConfig``
    """

    def test_backup_restore_config(self):
        """
        Testing ``AuthyMeConfig`` class.
        """
        app = BackupRestoreConfig

        self.assertEqual(app.name, 'backup_restore')
        self.assertEqual(apps.get_app_config('backup_restore').name, 'backup_restore')
