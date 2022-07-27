CREATE TABLE IF NOT EXISTS courses
                 (course_id INT PRIMARY KEY     NOT NULL,
                 course_name           TEXT    NOT NULL,
                 course_timespan            TEXT,
                 course_fees        INT     NOT NULL,
                 course_description         TEXT);