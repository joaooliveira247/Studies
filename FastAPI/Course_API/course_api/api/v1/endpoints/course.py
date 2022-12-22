from fastapi import APIRouter, HTTPException, Response, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from course_api.models.course_model import CourseModel
from course_api.core.dependencies import get_session
from sqlmodel.sql.expression import Select, SelectOfScalar

# Bypassing warning of SQLModels select
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

router: APIRouter = APIRouter()


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=CourseModel
)
async def post_course(
    course: CourseModel, db: AsyncSession = Depends(get_session)
) -> CourseModel:
    new_course = CourseModel(
        title=course.title, classes=course.classes, time=course.time
    )

    db.add(new_course)
    await db.commit()
    return new_course


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=list[CourseModel]
)
async def get_courses(
    db: AsyncSession = Depends(get_session),
) -> list[CourseModel]:
    async with db as session:
        result = await session.execute(select(CourseModel))
        courses: list[CourseModel] = result.scalars().all()
        return courses


@router.get(
    "/{id}", status_code=status.HTTP_200_OK, response_model=CourseModel
)
async def get_course_by_id(
    id: int, db: AsyncSession = Depends(get_session)
) -> CourseModel:
    async with db as session:
        result = await session.execute(
            select(CourseModel).filter(CourseModel.id == id)
        )
        if course := result.scalar_one_or_none():
            return course
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Course not found."
        )


@router.put(
    "/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=CourseModel
)
async def att_course(
    id: int, course: CourseModel, db: AsyncSession = Depends(get_session)
) -> CourseModel:
    async with db as session:
        result = await session.execute(
            select(CourseModel).filter(CourseModel.id == id)
        )
        if update_course := result.scalar_one_or_none():
            update_course.title = course.title
            update_course.classes = course.classes
            update_course.time = course.time
            await session.commit()
            return course
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail="Course not found."
        )


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_course(
    id: int, db: AsyncSession = Depends(get_session)
) -> Response:
    async with db as session:
        result = await session.execute(
            select(CourseModel).filter(CourseModel.id == id)
        )
        if del_course := result.scalar_one_or_none():
            await session.delete(del_course)
            await session.commit()
            return Response(
                status_code=status.HTTP_204_NO_CONTENT,
                content="Course deleted.",
            )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Course not found."
        )
