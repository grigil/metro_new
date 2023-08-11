from sqlalchemy import and_, or_
from sqlalchemy.orm import Session
from app import models, schemas
import json
import hashlib
from collections import OrderedDict


def get_find(db: Session, hash: hash) -> schemas.FindBase:
    find_objects = db.query(models.Find).filter(
        and_(
            models.Find.hash == hash,
        )
    ).all()
    return find_objects


async def post_find(db: Session, request):
    body_values = await request.json()
    post = db.query(models.Find).filter(
        or_(
            models.Find.body == body_values,
            models.Find.header == body_values
        )
    ).all()
    return post


async def post_problems(db: Session, request):
    header_value = OrderedDict(sorted(request.headers.items()))
    body_values = await request.json()
    body_values = OrderedDict(sorted(body_values.items()))
    problem_hash = hashlib.md5(json.dumps({"body": body_values, "header": header_value}).encode('utf-8')).hexdigest()
    db_problems = models.Find(
        body=body_values,
        header=header_value,
        hash=problem_hash
    )
    db.add(db_problems)
    db.commit()
    return problem_hash
