import unittest
from todo import Task, TaskPool

class TestTaskPool(unittest.TestCase):

    def setUp(self):
        self.pool = TaskPool()

    def test_add_task(self):
        task = Task("New Task")
        self.pool.add_task(task)
        self.assertEqual(len(self.pool.tasks), 1)

    def test_get_open_tasks(self):
        self.pool.populate()
        open_tasks = self.pool.get_open_tasks()
        self.assertEqual(len(open_tasks), 3)
        self.assertTrue(all(task.status == "ToDo" for task in open_tasks))

    def test_get_done_tasks(self):
        self.pool.populate()
        done_tasks = self.pool.get_done_tasks()
        self.assertEqual(len(done_tasks), 3)
        self.assertTrue(all(task.status == "Done" for task in done_tasks))

if __name__ == "__main__":
    # Load tests from TestTaskPool
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTaskPool)

    # Capture printed output
    captured_output = StringIO()

    # Run tests (verbosity = 2 gives detailed method names)
    result = unittest.TextTestRunner(
        stream=captured_output, verbosity=2
    ).run(suite)

    # Extract text output lines
    output_lines = captured_output.getvalue().splitlines()

    # Display each successful test in a concise format
    for line in output_lines:
        if "ok" in line:
            # keep only the test-method name before the space
            print(line.split(" ")[0] + " ... ok")

    # Summarise totals
    total_tests = result.testsRun
    failed_tests = [t[0] for t in result.failures + result.errors]
    passed_tests = [t for t in suite if t not in failed_tests]

    print(f"\nTotal Tests: {total_tests}")
    print(f"Passed: {len(passed_tests)} ({(len(passed_tests)/total_tests)*100:.2f}%)")
    print(f"Failed: {len(failed_tests)} ({(len(failed_tests)/total_tests)*100:.2f}%)")
