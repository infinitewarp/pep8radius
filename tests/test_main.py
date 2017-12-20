from tests.util import *


GLOBAL_CONFIG = os.path.join(TEMP_DIR, 'GLOBAL_CONFIG')
LOCAL_CONFIG = os.path.join(TEMP_DIR, '.style.yapf')


class TestMain(TestCase):

    def setUp(self):
        remove(LOCAL_CONFIG)
        remove(GLOBAL_CONFIG)

    def tearDown(self):
        remove(GLOBAL_CONFIG)
        remove(LOCAL_CONFIG)

    def test_version_number(self):
        version_ = pep8radius_main(['--version'])
        self.assertEqual(version_, version)

    def test_help(self):
        self.check_help()

    def test_help_outside_project(self):
        home = os.path.expanduser('~')
        try:
            VersionControl.which(cwd=home)
            raise SkipTest("Home directory is under version control ??")
        except NotImplementedError:
            pass
        self.check_help(cwd=home)

    def check_help(self, cwd=TEMP_DIR):
        help_message = pep8radius_main(['--help'], cwd=cwd)
        self.assertIn("--no-color", help_message)
        self.assertIn("PEP8 clean only the parts of the files", help_message)

if __name__ == '__main__':
    test_main()
