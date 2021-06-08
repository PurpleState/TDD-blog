from blog.blog import Blog

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post and "q" to quit'
POST_TEMPLATE = '''
--- {} ---

{}

'''
blogs = dict() # blog name: blog object

def menu():
    # show the user the available blogs
    # let the user make a choice
    # do something with that choice
    # eventually exit
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))

def ask_create_blog():
    title = input("Enter your blog title")
    author = input("Enter you name: ")
    blogs[title] = Blog(title, author)
# i can test blog creation but that will be unit test, i need to test the selection
# and if this function is called, and then is it performing correctly
def ask_read_blog():
    title = input("Enter your blog title you want to read")
    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    blog_title = input("Enter your blog title you want to write your post in: ")
    post_title = input("Enter your post title: ")
    post_content = input("Enter your post content: ")
    blogs[blog_title].create_post(post_title, post_content)