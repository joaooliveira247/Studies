from fastapi import (
    FastAPI, HTTPException, status, Response, Path, Query, Header, Depends,
    )
import uvicorn
from time import sleep

from models import Curso


app = FastAPI()


def fake_db():
    try:
        print("Open Connection.")
        sleep(1)
    finally:
        print("Close Connection.")
        sleep(2)


courses = {
    1: {
        "title": "Math I",
        "classes": 112,
        "time": 58
    },
    2: {
        "title": "Math II",
        "classes": 112,
        "time": 58
    }
}


@app.get("/v1/courses")
async def get_courses(
    user_agent: str | None = Header(default=None),
    db: str | None = Depends(fake_db)
    ):
    print(user_agent)
    return courses


@app.get("/v1/courses/{id}")
async def get_course_by_id(
    id: int = Path(
        default=None,
        title="Course ID",
        gt=0,
        lt=len(courses),
        description="Course ID between 1 and 2"
        )
        ):
    try:
        return courses[id]
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not Found."
            )


@app.post("/v1/courses", status_code=status.HTTP_201_CREATED)
async def post_course(course: Curso):
    courses[len(courses) + 1] = course.__dict__
    return course.__dict__
    # raise HTTPException(
    #     status_code=status.HTTP_409_CONFLICT,
    #     detail=f"Course {course.id} already exist."
    #     )


@app.put("/v1/courses/{id}")
async def put_course(id: int, course: Curso) -> Curso:
    if id in courses:
        courses[id] = course.__dict__
        return course.__dict__
    raise HTTPException(
        status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="id not valid."
    )


@app.delete("/v1/courses/{id}")
async def delete_course(id: int):
    if id not in courses:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Object not found."
        )
    courses.pop(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Query parameter
@app.get("/utils/sum")
async def sum_calc(
    a: int = Query(default=0, gt=0, lt=100),
    b: int = Query(default=0, gt=0, lt=100),
    c: int = Query(default=0, gt=0, lt=100)
        ):
    return sum([a, b, c])

# TODO: Make Header Parameter.


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="localhost", port=8000, reload=True, log_level="info"
        )
