from unittest import TestCase
from blog.blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test author', b.author)
        self.assertEqual(0, len(b.posts))
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['apple', 'shake']
        self.assertEqual(b.__repr__(), 'Test by Test Author (2 posts)')

    def test_json_no_posts(self):
        b = Blog('Test', 'Test author')

        self.assertDictEqual(b.json(), {
            'title': b.title,
            'author': b.author,
            'posts': [],
        })