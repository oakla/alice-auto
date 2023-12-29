CREATE TABLE time_slots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    start_datetime TEXT NOT NULL,
    end_datetime TEXT NOT NULL,
    role TEXT NOT NULL,
    duration REAL NOT NULL
);
