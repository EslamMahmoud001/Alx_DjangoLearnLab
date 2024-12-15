# Django Blog - CRUD Features

## Features
- **Post Management**: Create, read, update, and delete blog posts.
- **Permissions**: Only authenticated users can create/edit posts. Only authors can edit/delete their own posts.
- **Views**: Class-based views for efficient development.
- **Templates**: User-friendly templates for each operation.

## URLs
- `/` - List all posts
- `/post/<pk>/` - View post details
- `/post/new/` - Create new post
- `/post/<pk>/edit/` - Edit post
- `/post/<pk>/delete/` - Delete post