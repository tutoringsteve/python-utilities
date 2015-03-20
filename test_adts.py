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

if __name__ == "__main__":
    unittest.main()