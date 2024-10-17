from datetime import datetime

import pymongo
from blog.database import mongo
from unidecode import unidecode


def get_all_posts(published: bool = True):
    posts = mongo.db.posts.find({"published": published})
    return posts.sort("date", pymongo.DESCENDING)


def get_post_by_slug(slug: str) -> dict:
    post = mongo.db.posts.find_one({"slug": slug})
    return post


def update_post_by_slug(slug: str, data: dict) -> dict:
    # Buscar o post atual para obter o título
    current_post = mongo.db.posts.find_one({"slug": slug})
    if not current_post:
        raise ValueError(f"Post with slug '{slug}' not found.")

    # Verificar se o título foi atualizado
    new_title = data.get("title")
    if new_title and new_title != current_post["title"]:
        # Gerar novo slug
        new_slug = unidecode(new_title).replace(" ", "-").lower()

        # Verificar se o novo slug já existe
        if mongo.db.posts.find_one({"slug": new_slug}):
            raise ValueError(f"Post with slug '{new_slug}' already exists.")

        # Adicionar o novo slug aos dados
        data["slug"] = new_slug

    # Atualizar o post
    return mongo.db.posts.find_one_and_update({"slug": slug}, {"$set": data})


def new_post(title: str, content: str, published: bool = True) -> str:
    slug = unidecode(title).replace(" ", "-").lower()
    if mongo.db.posts.find_one({"slug": slug}):
        raise ValueError(f"Post with slug '{slug}' already exists.")
    mongo.db.posts.insert_one(
        {
            "title": title,
            "content": content,
            "published": published,
            "slug": slug,
            "date": datetime.now(),
        }
    )
    return slug


def delete_post_by_slug(slug: str) -> bool:
    """Delete a post by its slug."""
    result = mongo.db.posts.delete_one({"slug": slug})
    if result.deleted_count > 0:
        return True
    else:
        return False
