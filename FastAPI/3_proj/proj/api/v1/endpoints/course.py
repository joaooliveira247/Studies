from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.course_model import CourseModel
from schemas.course_schema import CourseSchema
from core.dependecies import get_session


router: APIRouter = APIRouter()


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=CourseSchema
)
async def post_course(
    course: CourseSchema, db: AsyncSession = Depends(get_session)
) -> CourseSchema:
    new_course = CourseModel(
        title=course.title, classes=course.classes, time=course.time
    )
    db.add(new_course)
    await db.commit()
    return new_course


@router.get("/", response_model=list[CourseSchema])
async def get_courses(
    db: AsyncSession = Depends(get_session),
) -> list[CourseSchema]:
    async with db as session:
        result = await session.execute(select(CourseModel))
        courses: list[CourseModel] = result.scalars().all()
        return courses


@router.get(
    "/{id}", response_model=CourseSchema, status_code=status.HTTP_200_OK
)
async def get_course(
    id: int, db: AsyncSession = Depends(get_session)
) -> CourseSchema:
    async with db as session:
        query = select(CourseModel).filter(CourseModel.id == id)
        result = await session.execute(query)
        course = result.scalar_one_or_none()
        if course:
            return course
        raise HTTPException(
            detail="Course not found.", status_code=status.HTTP_404_NOT_FOUND
        )


@router.put(
    "/{id}", response_model=CourseSchema, status_code=status.HTTP_202_ACCEPTED
)
async def att_course(
    id: int, course: CourseSchema, db: AsyncSession = Depends(get_session)
) -> CourseSchema:
    async with db as session:
        query = select(CourseModel).filter(CourseModel.id == id)
        result = await session.execute(query)
        course_up = result.scalar_one_or_none()
        if course_up:
            course_up.title = course.title
            course_up.classes = course.classes
            course_up.time = course.time
            await session.commit()
            return course_up
        raise HTTPException(
            detail="Course not found.", status_code=status.HTTP_404_NOT_FOUND
        )


@router.delete("/{id}", response_model=CourseSchema)
async def delete_course(
    id: int, db: AsyncSession = Depends(get_session)
) -> None:
    async with db as session:
        query = select(CourseModel).filter(CourseModel.id == id)
        result = await session.execute(query)
        course_del = result.scalar_one_or_none()
        if course_del:
            await session.delete(course_del)
            await session.commit()
            return Response(
                status_code=status.HTTP_204_NO_CONTENT
            )
        raise HTTPException(
            detail="Course not found.", status_code=status.HTTP_404_NOT_FOUND
        )
