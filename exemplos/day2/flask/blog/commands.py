import click
from blog.posts import (
    delete_post_by_slug,
    get_all_posts,
    get_post_by_slug,
    new_post,
    update_post_by_slug,
)


@click.group()
def post():
    """Manage blog posts."""


@post.command()
@click.option("--title")
@click.option("--content")
def new(title, content):
    """Add new post to database."""
    new = new_post(title, content)
    click.echo(f"New post created {new}")


@post.command("list")
def _list():
    """Lists all posts"""
    for post in get_all_posts():
        click.echo(post)
        click.echo("-" * 174)


@post.command()
@click.argument("slug")
def get(slug):
    """Get post by slug"""
    post = get_post_by_slug(slug)
    click.echo(post or "post not found")


@post.command()
@click.argument("slug")
@click.option("--content", default=None, type=str)
@click.option("--published", default=None, type=str)
def update(slug, content, published):
    """Update post by slug"""
    data = {}
    if content is not None:
        data["content"] = content
    if published is not None:
        data["published"] = published.lower() == "true"
    update_post_by_slug(slug, data)
    click.echo("Post updated")


@post.command()
@click.argument("slug")
def delete(slug):
    """Delete post by slug

    Usage: flask post delete <slug>

    Example: flask post delete meu-primeiro-post

    """
    if delete_post_by_slug(slug):
        click.echo(f"Post with slug '{slug}' deleted.")
    else:
        click.echo(f"Post with slug '{slug}' not found.")


def configure(app):
    app.cli.add_command(post)
