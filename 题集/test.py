import unittest
import io
import sys
from .work import func


def stub_stdin(testcase_inst, inputs):
    stdin = sys.stdin

    def cleanup():
        sys.stdin = stdin

    testcase_inst.addCleanup(cleanup)
    sys.stdin = io.StringIO(inputs)


def stub_stdout(testcase_inst):
    stderr = sys.stderr
    stdout = sys.stdout

    def cleanup():
        sys.stderr = stderr
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stderr = io.StringIO()
    sys.stdout = io.StringIO()


class UnitTest(unittest.TestCase):
    def test_fun(self):
        stub_stdin(self, '4 6\n')  # 依次输入2,4
        stub_stdout(self)
        func()
        self.assertEqual(str(sys.stdout.getvalue()), 'GRRGGG\r\nFFRGGG\r\nFFRGGF\r\nFFRRGF')

        # stub_stdout(self)  # 重置输出
        # main()
        # self.assertEqual(str(sys.stdout.getvalue()), '9\n')


if __name__ == '__main__':
    """
    input:  4 6
            GRRGGGGGGRFFFFRGGFFGRRFF
    output:
            GRRGGG
            FFRGGG
            FFRGGF
            FFRRGF
    ---------------------------------
    input:  2
            GRRR
    output:
            incorrect mesh size.
    ---------------------------------
    input:  ab
            GRRR
    output:
            incorrect mesh size.
    ---------------------------------
    input: 2 4
            GGGRFFGG
    output:     
            GGGR
            GGFF       
    ---------------------------------            
    input: 2 4
            GGGSFFGG
    output:     
        Incalid cell type
    ---------------------------------            
    input: 2 3
            GGGRFFGG
    output:     
            Data mismatch
    """
    unittest.main()
