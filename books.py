import os, csv
from booksdb import *
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://oupmdpbbloafkq:524dc2ab68ad1420bdb528f75b63e4c1f43af3d677d07e2dfe2e7ef3bda4c4eb@ec2-34-198-243-120.compute-1.amazonaws.com:5432/d6i86eicfinhqi")
dbscope = scoped_session(sessionmaker(bind=engine))

def main():
    Base.metadata.create_all(bind=engine)
    f = open("books.csv")
    # print(f)
    reader = csv.reader(f)
    next(reader)
    for isbn, title, author, year in reader:
        book = Books(isbn=isbn, title=title, author=author, year=int(year))
        dbscope.add(book)
    dbscope.commit()
    dbscope.close()

if __name__ == "__main__":
    main()