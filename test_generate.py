import generate_ref
import unittest


def generate(fname):
    header_len = 10
    content_len = 11
    with open(fname) as f:
        ref_table = generate_ref.generate_tbs_ref_table(
            f, header_len, content_len)
        check = generate_ref.check_length(ref_table, header_len *
                                          content_len)
    return ref_table, check


class TestGeneration(unittest.TestCase):

    def test_v1212(self):
        ref_table, check = generate("samples/ts_136213v121200p.txt")
        self.assertEqual(check, True, "Incorrect length")

    def test_v1213(self):
        ref_table, check = generate("samples/ts_136213v121300p.txt")
        self.assertEqual(check, True, "Incorrect length")


if __name__ == '__main__':
    unittest.main()
