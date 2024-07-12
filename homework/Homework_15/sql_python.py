import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# 1. Добавляем студента
cursor.execute("INSERT INTO students (name, second_name) VALUES (%s, %s)", ('Claus', 'Mouse'))
db.commit()
student_id = cursor.lastrowid
print(f"Добавлен студент с ID: {student_id}")

# 2. Добавляем группу
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
               ('Group for Bobby', '2024-07-01', '2024-09-11'))
db.commit()
group_id = cursor.lastrowid
print(f"Добавлена группа с ID: {group_id}")

# 3. Назначаем студента в группу
cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id))
db.commit()
print(f"Студент с ID {student_id} назначен в группу с ID {group_id}")

# 4. Добавляем книги
cursor.executemany("INSERT INTO books (title) VALUES (%s)", [('Cats',), ('Dogs',)])
db.commit()
cursor.execute("SELECT id, title FROM books WHERE title IN ('Cats', 'Dogs')")
books = cursor.fetchall()
print("Добавленные книги:")
for book in books:
    print(book)

# 5. Назначаем книги студенту
book_ids = [book['id'] for book in books]
cursor.executemany("UPDATE books SET taken_by_student_id = %s WHERE id = %s",
                   [(student_id, book_id) for book_id in book_ids])
db.commit()
print(f"Книги {book_ids} назначены студенту с ID {student_id}")

# 6. Добавляем предметы
cursor.executemany("INSERT INTO subjets (title) VALUES (%s)", [('Dog Science',), ('Cat Science',)])
db.commit()
cursor.execute("SELECT id, title FROM subjets WHERE title IN ('Dog Science', 'Cat Science')")
subjects = cursor.fetchall()
print("Добавленные предметы:")
for subject in subjects:
    print(subject)

# 7. Добавляем уроки
dog_subject_id = next(subject['id'] for subject in subjects if subject['title'] == 'Dog Science')
cat_subject_id = next(subject['id'] for subject in subjects if subject['title'] == 'Cat Science')
cursor.executemany("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", [
    ('INTRO to Dog Science', dog_subject_id),
    ('Advanced Dog Science', dog_subject_id),
    ('INTRO to Cat Science', cat_subject_id),
    ('Advanced Cat Science', cat_subject_id)
])
db.commit()
cursor.execute(
    "SELECT id, title FROM lessons WHERE title IN ('INTRO to Dog Science', 'Advanced Dog Science', "
    "'INTRO to Cat Science', 'Advanced Cat Science')")
lessons = cursor.fetchall()
print("Добавленные уроки:")
for lesson in lessons:
    print(lesson)

# 8. Добавляем оценки для студента
lesson_ids = [lesson['id'] for lesson in lessons]
cursor.executemany("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
                   [(10, lesson_id, student_id) for lesson_id in lesson_ids])
db.commit()
print(f"Добавлены оценки для уроков {lesson_ids} для студента с ID {student_id}")

# 9. Получаем и печатаем все данные, связанные со студентом
cursor.execute("""
        SELECT s.id as student_id, s.name, s.second_name, g.id as group_id, g.title as group_title, 
               b.id as book_id, b.title as book_title, m.id as mark_id, m.value as mark_value, 
               l.id as lesson_id, l.title as lesson_title, sub.id as subject_id, sub.title as subject_title
        FROM students s
        JOIN `groups` g ON s.group_id = g.id
        JOIN books b ON s.id = b.taken_by_student_id
        JOIN marks m ON s.id = m.student_id
        JOIN lessons l ON m.lesson_id = l.id
        JOIN subjets sub ON l.subject_id = sub.id
        WHERE s.id = %s
    """, (student_id,))
student_data = cursor.fetchall()
print("Все данные, связанные со студентом:")
for row in student_data:
    print(row)

# Закрываем курсор и соединение
cursor.close()
db.close()
print("Соединение закрыто")
