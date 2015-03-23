__author__ = 'Steven Sarasin'

import unittest
import adts


class ListQueueTest(unittest.TestCase):
    def setUp(self):
        self.q = adts.ListQueue()

    def tearDown(self):
        self.q = None

    def test_queue_is_empty_on_creation(self):
        self.assertTrue(self.q.is_empty())

    def test_queue_has_size_zero_on_creation(self):
        self.assertEqual(0, self.q.size())

    def test_queue_has_size_one_after_one_enqueue(self):
        self.q.enqueue("first")
        self.assertEqual(1, self.q.size())

    def test_queue_is_not_empty_when_size_is_nonzero(self):
        self.q.enqueue("first")
        self.assertTrue(self.q.size() > 0, "q contains 'first' but has non-positive size()")
        self.assertFalse(self.q.is_empty(), "q has positive size but is_empty() returns true")

    def test_queue_size_increased_by_one_when_cargo_pushed_to_queue_of_size_k(self):
        # decreasing range(a, b) upper bound does not improve test speed appreciably
        for i in range(1, 1000):
            self.q.enqueue(i)
            self.assertEqual(i, self.q.size())

    def test_dequeue_on_empty_queue_returns_None(self):
        self.assertEqual(None, self.q.dequeue())

    def test_dequeue_preserves_enqueue_order(self):
        self.q.enqueue("first")
        self.q.enqueue("second")
        self.q.enqueue("third")
        self.assertEqual("first", self.q.dequeue(), "'first' not dequeued first")
        self.assertEqual("second", self.q.dequeue(), "'second' not dequeued second")
        self.assertEqual("third", self.q.dequeue(), "'third' not dequeued third")

    def test_queue_converts_to_string_equivalent_to_string_conversion_of_a_list_of_all_its_elements(self):
        elements = ['a', 'b', 1, 2]
        for cargo in elements:
            self.q.enqueue(cargo)
        self.assertEqual(str(elements), str(self.q))


class QueueTest(unittest.TestCase):
    def setUp(self):
        self.q = adts.Queue()

    def tearDown(self):
        self.q = None

    def test_queue_is_empty_on_creation(self):
        self.assertTrue(self.q.is_empty())

    def test_queue_has_size_zero_on_creation(self):
        self.assertEqual(0, self.q.size())

    def test_queue_has_size_one_after_one_enqueue(self):
        self.q.enqueue("first")
        self.assertEqual(1, self.q.size())

    def test_queue_is_not_empty_when_size_is_nonzero(self):
        self.q.enqueue("first")
        self.assertTrue(self.q.size() > 0, "q contains 'first' but has non-positive size()")
        self.assertFalse(self.q.is_empty(), "q has positive size but is_empty() returns true")

    def test_queue_size_increased_by_one_when_cargo_pushed_to_queue_of_size_k(self):
        # decreasing range(a, b) upper bound does not improve test speed appreciably
        for i in range(1, 1000):
            self.q.enqueue(i)
            self.assertEqual(i, self.q.size())

    def test_dequeue_on_empty_queue_returns_None(self):
        self.assertEqual(None, self.q.dequeue())

    def test_dequeue_preserves_enqueue_order(self):
        self.q.enqueue("first")
        self.q.enqueue("second")
        self.q.enqueue("third")
        self.assertEqual("first", self.q.dequeue(), "'first' not dequeued first")
        self.assertEqual("second", self.q.dequeue(), "'second' not dequeued second")
        self.assertEqual("third", self.q.dequeue(), "'third' not dequeued third")

    def test_queue_converts_to_string_equivalent_to_string_conversion_of_a_list_of_all_its_elements(self):
        elements = ['a', 'b', 1, 2]
        for cargo in elements:
            self.q.enqueue(cargo)
        self.assertEqual(str(elements), str(self.q))


class StackTest(unittest.TestCase):
    def setUp(self):
        self.s = adts.Stack()

    def tearDown(self):
        self.s = None

    def test_stack_is_empty_on_creation(self):
        self.assertTrue(self.s.is_empty())

    def test_stack_has_size_zero_on_creation(self):
        self.assertEqual(0, self.s.size())

    def test_stack_has_size_one_after_one_push(self):
        self.s.push("first")
        self.assertEqual(1, self.s.size())

    def test_stack_is_not_empty_when_size_is_nonzero(self):
        self.s.push("first")
        self.assertTrue(self.s.size() > 0, "q contains 'first' but has non-positive size()")
        self.assertFalse(self.s.is_empty(), "q has positive size but is_empty() returns true")

    def test_stack_size_increased_by_one_when_cargo_pushed_to_stack_of_size_k(self):
        # decreasing range(a, b) upper bound does not improve test speed appreciably
        for i in range(1, 1000):
            self.s.push(i)
            self.assertEqual(i, self.s.size())

    def test_pop_on_empty_stack_raises_RuntimeError(self):
        # required so error raising pop() isn't run before the assertRaises
        with self.assertRaises(RuntimeError):
            self.s.pop()
            
    def test_peek_on_empty_stack_raises_RuntimeError(self):
        # required so error raising peek() isn't run before the assertRaises
        with self.assertRaises(RuntimeError):
            self.s.peek()

    def test_pop_reverses_push_order(self):
        self.s.push("first")
        self.s.push("second")
        self.s.push("third")
        self.assertEqual("third", self.s.pop(), "'third' not popped first")
        self.assertEqual("second", self.s.pop(), "'second' not popped second")
        self.assertEqual("first", self.s.pop(), "'first' not popped third")
    def test_stack_converts_to_string_equivalent_to_string_conversion_of_a_list_of_all_its_elements(self):
        elements = ['a', 'b', 1, 2]
        for cargo in elements:
            self.s.push(cargo)
        self.assertEqual(str(elements), str(self.s))

    def test_peek_returns_last_item_pushed_but_stack_unchanged(self):
        elements = ['a', 'b', 1, 2]
        for cargo in elements:
            self.s.push(cargo)
        self.assertEqual(len(elements), self.s.size(), "size of stack doesn't match number of elements pushed")
        self.assertEqual(elements[-1], self.s.peek(), "not showing last element added")
        self.assertEqual(len(elements), self.s.size(), "size of  stack changed by peek")
        self.assertEqual(str(elements), str(self.s), "contents of stack changed by peek")


if __name__ == "__main__":
    unittest.main()
