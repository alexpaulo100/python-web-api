from blog.database import mongo
from datetime import datetime



def get_all_posts(published: bool = True):
    posts = mongo.db.posts.find({"published": published})
    return posts.sort("date")


def get_post_by_slug(slug: str) -> dict:
    post = mongo.db.posts.find_one({"slug": slug})
    return post



def update_post_by_slug(slug: str, data: dict) -> dict:
    # TODO: Se o titulo muda, atualizar o slug  {falhar se ja existir}
    return mongo.db.posts.find_one_and_update({"slug": slug}, {"$set":data})



def new_post(title: str, content: str, published: bool = True) -> str:
    # TODO: Refatorar a criação do slug removendo acentos
    slug = title.replace(" ", "-").replace(" ", "-").lower()
    # TODO: Verificar se post com este slug já existe
    new = mongo.db.posts.insert_one(
        {
            "title": title,
            "content": content,
            "published": published,
            "slug": slug,
            "date": datetime.now(),
        }
    )
    return slug


