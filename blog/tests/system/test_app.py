from unittest import TestCase
from unittest.mock import patch
import blog.main
from blog.blog import Blog
from blog.post import Post


class AppTest(TestCase):
    def setUp(self):
        dummy_blog = Blog('Test', 'Test Author')
        blog.main.blogs = {'Test': dummy_blog}

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')
            blog.main.menu()
            self.assertIsNotNone(blog.main.blogs['Test Create Blog'])


    def test_menu_print_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            blog.main.menu()

            mocked_input.assert_called_with(blog.main.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('blog.main.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                blog.main.menu()

                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        dummy_blog = Blog('Test', 'Test Author')
        blog.main.blogs = {'Test': dummy_blog}
        with patch('builtins.print') as mocked_print:
            blog.main.print_blogs()

            mocked_print.assert_called_with('- Test by Test Author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            blog.main.ask_create_blog()

            self.assertIsNotNone(blog.main.blogs.get('Test'))

    def test_ask_read_blog(self):
        dummy_blog = blog.main.blogs['Test']
        with patch('builtins.input', return_value='Test'):
            with patch('blog.main.print_posts') as mocked_print_posts:
                blog.main.ask_read_blog()

                mocked_print_posts.assert_called_with(dummy_blog)
                #this function calls another function

    def test_print_posts(self):
        dummy_blog = blog.main.blogs['Test']
        dummy_blog.create_post('Test Post', 'Test Content')

        with patch('blog.main.print_post') as mocked_print_post:
            blog.main.print_posts(dummy_blog)

            mocked_print_post.assert_called_with(dummy_blog.posts[0])

    def test_print_post(self):
        dummy_post = Post('Post Title', 'Post Content')
        expected_print = '''
--- Post Title ---

Post Content

'''
        with patch('builtins.print') as mocked_print:
            blog.main.print_post(dummy_post)

            mocked_print.assert_called_with(expected_print)


    def test_ask_create_post(self):
        dummy_blog = blog.main.blogs['Test']
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Post Title', 'Post Content')
            blog.main.ask_create_post()

            self.assertIsNotNone(blog.main.blogs.get('Test'))
            self.assertEqual(dummy_blog.posts[0].title, 'Post Title')
            self.assertEqual(dummy_blog.posts[0].content, 'Post Content')


