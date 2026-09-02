'''
                                         SECTION = A
                                      
1) A column that references another table's primary key
2) ForeignKey()
3) Defines a relationship between two models
4) On the "many" side (child table)
5) Creates a bidirectional relationship
6) Automatically creates the reverse relationship
7) user_id = Column(Integer, ForeignKey('users.id'))
8) Post table
9) Relationship returns a list (one-to-many)
10) Deletes related objects when parent is deleted
11) One-to-many
12) user.posts (list of Post objects)
13) Both sides can navigate to each other
14) back_populates
15) Post is added to session and user_id is set
16) back_populates
17) Related objects loaded when accessed
18) Parent has relationship() to child, child has ForeignKey to parent
19) Enforce referential integrity
20) User has posts = relationship("Post"), Post has user_id = ForeignKey('users.id')
                                        Section B
                                        QUESTION = 1

Foreign key ek column hota hai jo doosri table ke primary key ko reference karta hai. Iska main purpose tables ke beech connection banana aur valid data maintain karna hai.

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

Yahan user_id foreign key hai jo users.id ko reference karta hai.

                                       QUESTION = 2

One-to-many ka matlab hai ek parent ke multiple child records ho sakte hain.

Example 

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    posts = relationship("Post")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

Foreign key many side, yani Post table mein hoti hai, kyunki multiple posts ek user se connected ho sakte hain.

                                     QUESTION =3

back_populates dono models mein relationship ko explicitly define karta hai.

class User(Base):
    posts = relationship("Post", back_populates="user")

class Post(Base):
    user = relationship("User", back_populates="posts")

backref automatically reverse relationship create karta hai.

class User(Base):
    posts = relationship("Post", backref="user")

Large applications mein back_populates zyada clear aur preferred hota hai, kyunki dono sides explicitly defined hoti hain.

                                         QUESTION = 4

Bidirectional relationship mein dono sides ek-doosre ko access kar sakti hain.

class User(Base):
    posts = relationship("Post", back_populates="user")


class Post(Base):
    user = relationship("User", back_populates="posts")

Parent se child:

user.posts

Child se parent:

post.user

Isliye User → Posts aur Post → User dono direction mein navigation possible hai. 


                                        SECTION = C 
                                        QUESTION = 1

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)

    posts = relationship("Post", back_populates="user")
    tasks = relationship("Task", back_populates="user")
                                             QUESTION =  2
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(500))
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="posts")
                                              QUESTION = 3
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500))
    status = Column(String(50))

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tasks")
                                             QUESTION = 4
user = User(name="Rahul", email="rahul@gmail.com")

post1 = Post(title="Python", content="Learning Python")
post2 = Post(title="SQL", content="Learning SQL")

task1 = Task(title="Practice Python", description="Solve questions", status="Pending")
task2 = Task(title="Practice SQL", description="Write queries", status="Completed")

user.posts.append(post1)
user.posts.append(post2)

user.tasks.append(task1)
user.tasks.append(task2)

session.add(user)
session.commit()

print(user.posts)
print(user.tasks)

print(post1.user)
print(task1.user)   


                                              SECTION = D
                                             QUESTION = 1
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
from datetime import datetime


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    posts = relationship(
        "Post",
        back_populates="author",
        cascade="all, delete-orphan"
    )

    comments = relationship(
        "Comment",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    author = relationship(
        "User",
        back_populates="posts"
    )

    comments = relationship(
        "Comment",
        back_populates="post",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Post(id={self.id}, title='{self.title}')>"


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)

    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    post = relationship(
        "Post",
        back_populates="comments"
    )

    user = relationship(
        "User",
        back_populates="comments"
    )

    def __repr__(self):
        return f"<Comment(id={self.id}, content='{self.content}')>"


engine = create_engine("sqlite:///blog.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user = User(name="Rahul", email="rahul@gmail.com")

post = Post(
    title="Python Basics",
    content="Learning Python"
)

comment = Comment(
    content="Very useful post"
)

user.posts.append(post)
post.comments.append(comment)
user.comments.append(comment)

session.add(user)
session.commit()

print(user)
print(user.posts)
print(post.author)
print(post.comments)
print(comment.user)
print(comment.post)

session.close()



                                               QUESTION = 2
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)

    tasks = relationship(
        "Task",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500))
    status = Column(String(50), default="Pending")
    due_date = Column(String(50))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship(
        "User",
        back_populates="tasks"
    )

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', status='{self.status}')>"


class CreateTaskService:

    def __init__(self, session):
        self.session = session

    def create_task(self, user_id, title, description, due_date):
        user = self.session.get(User, user_id)

        if not user:
            return None

        task = Task(
            title=title,
            description=description,
            due_date=due_date
        )

        user.tasks.append(task)

        self.session.commit()
        return task

    def get_user_tasks(self, user_id):
        user = self.session.get(User, user_id)

        if not user:
            return []

        return user.tasks

    def update_task(self, task_id, **kwargs):
        task = self.session.get(Task, task_id)

        if not task:
            return None

        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)

        self.session.commit()
        return task

    def delete_task(self, task_id):
        task = self.session.get(Task, task_id)

        if not task:
            return False

        self.session.delete(task)
        self.session.commit()
        return True


engine = create_engine("sqlite:///task_manager.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def demo():
    user1 = User(
        name="Rahul",
        email="rahul@gmail.com"
    )

    user2 = User(
        name="Aman",
        email="aman@gmail.com"
    )

    session.add_all([user1, user2])
    session.commit()

    task1 = Task(
        title="Learn Python",
        description="Practice Python basics",
        status="Pending",
        due_date="2026-09-01"
    )

    task2 = Task(
        title="Learn SQL",
        description="Practice SQL queries",
        status="Pending",
        due_date="2026-09-03"
    )

    task3 = Task(
        title="Learn SQLAlchemy",
        description="Practice ORM relationships",
        status="Pending",
        due_date="2026-09-05"
    )

    user1.tasks.append(task1)
    user1.tasks.append(task2)
    user1.tasks.append(task3)

    task4 = Task(
        title="Build Project",
        description="Create a small project",
        status="Pending",
        due_date="2026-09-07"
    )

    task5 = Task(
        title="Practice CRUD",
        description="Practice CRUD operations",
        status="Pending",
        due_date="2026-09-09"
    )

    user2.tasks.append(task4)
    user2.tasks.append(task5)

    session.commit()

    print("User 1 Tasks:")
    for task in user1.tasks:
        print(task)

    print()

    print("User 2 Tasks:")
    for task in user2.tasks:
        print(task)

    print()

    print("Task Owner:")
    print(task1.user)

    service = CreateTaskService(session)

    service.update_task(
        task1.id,
        title="Learn Advanced Python",
        status="Completed"
    )

    service.delete_task(task5.id)

    print()

    print("Final Task List:")

    for user in [user1, user2]:
        print(user.name)

        for task in user.tasks:
            print(task)


if __name__ == "__main__":
    demo()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     '''