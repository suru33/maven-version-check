from unittest import TestCase

from maven_version import MavenVersion


class TestMavenVersion(TestCase):
    def test_aliases(self):
        self.assertEqual(MavenVersion("1.0-alpha1"), MavenVersion("1.0-a1"))
        self.assertEqual(MavenVersion("1.0-beta1"), MavenVersion("1.0-b1"))
        self.assertEqual(MavenVersion("1.0-milestone1"), MavenVersion("1.0-m1"))
        self.assertEqual(MavenVersion("1.0-rc1"), MavenVersion("1.0-cr1"))

    def test_different_final_releases(self):
        self.assertEqual(MavenVersion("1.0-ga"), MavenVersion("1.0"))
        self.assertEqual(MavenVersion("1.0-final"), MavenVersion("1.0"))
        self.assertEqual(MavenVersion("1.0"), MavenVersion("1.0.0"))

    def test_case_insensitive(self):
        self.assertEqual(MavenVersion("1.0ALPHA1"), MavenVersion("1.0-a1"))
        self.assertEqual(MavenVersion("1.0Alpha1"), MavenVersion("1.0-a1"))
        self.assertEqual(MavenVersion("1.0AlphA1"), MavenVersion("1.0-a1"))
        self.assertEqual(MavenVersion("1.0BETA1"), MavenVersion("1.0-b1"))
        self.assertEqual(MavenVersion("1.0MILESTONE1"), MavenVersion("1.0-m1"))
        self.assertEqual(MavenVersion("1.0RC1"), MavenVersion("1.0-cr1"))
        self.assertEqual(MavenVersion("1.0GA"), MavenVersion("1.0"))
        self.assertEqual(MavenVersion("1.0FINAL"), MavenVersion("1.0"))
        self.assertEqual(MavenVersion("1.0-SNAPSHOT"), MavenVersion("1-snapshot"))

    def test_separators(self):
        self.assertEqual(MavenVersion("1.0alpha1"), MavenVersion("1.0-a1"))
        self.assertEqual(MavenVersion("1.0alpha-1"), MavenVersion("1.0-a1"))
        self.assertEqual(MavenVersion("1.0beta1"), MavenVersion("1.0-b1"))
        self.assertEqual(MavenVersion("1.0beta-1"), MavenVersion("1.0-b1"))
        self.assertEqual(MavenVersion("1.0milestone1"), MavenVersion("1.0-m1"))
        self.assertEqual(MavenVersion("1.0milestone-1"), MavenVersion("1.0-m1"))
        self.assertEqual(MavenVersion("1.0rc1"), MavenVersion("1.0-cr1"))
        self.assertEqual(MavenVersion("1.0rc-1"), MavenVersion("1.0-cr1"))
        self.assertEqual(MavenVersion("1.0ga"), MavenVersion("1.0"))
        # unequal separator
        self.assertEqual(MavenVersion("1.0alpha.1"), MavenVersion("1.0-a1"))

    def test_dash_and_period(self):
        self.assertEqual(MavenVersion("1-0.ga"), MavenVersion("1.0"))
        self.assertEqual(MavenVersion("1.0-final"), MavenVersion("1.0"))
        self.assertEqual(MavenVersion("1-0-ga"), MavenVersion("1.0"))
        self.assertEqual(MavenVersion("1-0-final"), MavenVersion("1-0"))
        self.assertEqual(MavenVersion("1-0"), MavenVersion("1.0"))

    def test_greater_than(self):
        self.assertGreater(MavenVersion("1.0alpha2"), MavenVersion("1.0-a1"))
        self.assertGreater(MavenVersion("1.0.1alpha-1"), MavenVersion("1.0-a1"))
        self.assertGreater(MavenVersion("1.0beta1"), MavenVersion("1.0.0-a1"))
        self.assertGreater(MavenVersion("1.0"), MavenVersion("1.0-b1"))
        self.assertGreater(MavenVersion("1.0.1"), MavenVersion("1.0"))
        self.assertGreater(MavenVersion("1.0milestone-1"), MavenVersion("1.0-a1"))
        self.assertGreater(MavenVersion("1.0rc1"), MavenVersion("1.0-b1"))
        self.assertGreater(MavenVersion("1.0sp"), MavenVersion("1.0"))
        self.assertGreater(MavenVersion("1.0ga"), MavenVersion("0.1"))

    def test_less_than(self):
        self.assertLess(MavenVersion("1.0-a1"), MavenVersion("1.0alpha2"))
        self.assertLess(MavenVersion("1.0-a1"), MavenVersion("1.0.1alpha-1"))
        self.assertLess(MavenVersion("1.0.0-a1"), MavenVersion("1.0beta1"))
        self.assertLess(MavenVersion("1.0-b1"), MavenVersion("1.0"))
        self.assertLess(MavenVersion("1.0"), MavenVersion("1.0.1"))
        self.assertLess(MavenVersion("1.0-a1"), MavenVersion("1.0milestone-1"))
        self.assertLess(MavenVersion("1.0-b1"), MavenVersion("1.0rc1"))
        self.assertLess(MavenVersion("1.0"), MavenVersion("1.0sp"))
        self.assertLess(MavenVersion("0.1"), MavenVersion("1.0ga"))
