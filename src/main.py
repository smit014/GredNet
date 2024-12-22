from fastapi import FastAPI
# from src.resource.user.api import user_router
# from src.resource.post.api import post_router
from src.resource.auth.api import auth_router
# from src.resource.like.api import like_router
# from src.resource.comment.api import comment_router
app = FastAPI()

# app.include_router(user_router)
# app.include_router(post_router)
# app.include_router(like_router)
# app.include_router(comment_router)
app.include_router(auth_router)