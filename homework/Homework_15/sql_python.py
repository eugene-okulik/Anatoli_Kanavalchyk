import mysql.connector as mysql

# Подключение к базе данных
db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

try:
    # Начало транзакции
    db.start_transaction()

    # 1. Добавляем студента
    cursor.execute("INSERT INTO students (name, second_name) VALUES (%s, %s)", ('Claus', 'Mouse'))
    student_id = cursor.lastrowid
    print(f"Добавлен студент с ID: {student_id}")

    # 2. Добавляем группу
    cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
                   ('Group for Bobby', '2024-07-01', '2024-09-11'))
    group_id = cursor.lastrowid
    print(f"Добавлена группа с ID: {group_id}")

    # 3. Назначаем студента в группу
    cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id))
    print(f"Студент с ID {student_id} назначен в группу с ID {group_id}")

    # 4. Добавляем книги и получаем их ID
    books_to_add = ['Cats', 'Dogs']
    book_ids = []
    for book_title in books_to_add:
        cursor.execute("INSERT INTO books (title) VALUES (%s)", (book_title,))
        book_ids.append(cursor.lastrowid)
    print("Добавленные книги:")
    print(book_ids)

    # 5. Назначаем книги студенту
    for book_id in book_ids:
        cursor.execute("UPDATE books SET taken_by_student_id = %s WHERE id = %s", (student_id, book_id))
    print(f"Книги {book_ids} назначены студенту с ID {student_id}")

    # 6. Добавляем предметы и получаем их ID
    subjects_to_add = ['Dog Science', 'Cat Science']
    subject_ids = []
    for subject_title in subjects_to_add:
        cursor.execute("INSERT INTO subjets (title) VALUES (%s)", (subject_title,))
        subject_ids.append(cursor.lastrowid)
    print("Добавленные предметы:")
    print(subject_ids)

    # 7. Добавляем уроки и получаем их ID
    lessons_to_add = [
        ('INTRO to Dog Science', subject_ids[0]),
        ('Advanced Dog Science', subject_ids[0]),
        ('INTRO to Cat Science', subject_ids[1]),
        ('Advanced Cat Science', subject_ids[1])
    ]
    lesson_ids = []
    for lesson_title, subject_id in lessons_to_add:
        cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", (lesson_title, subject_id))
        lesson_ids.append(cursor.lastrowid)
    print("Добавленные уроки:")
    print(lesson_ids)

    # 8. Добавляем оценки для студента
    for lesson_id in lesson_ids:
        cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
                       (10, lesson_id, student_id))
    print(f"Добавлены оценки для уроков {lesson_ids} для студента с ID {student_id}")

    # Коммит транзакции
    db.commit()

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

finally:
    # Закрываем курсор и соединение
    cursor.close()
    db.close()
    print("Соединение закрыто")
