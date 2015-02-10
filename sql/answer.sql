CREATE TABLE IF NOT EXISTS course(
    course_no VARCHAR(255) NOT NULL,
    semester ENUM('fall', 'spring') NOT NULL,
    name VARCHAR(255) NOT NULL,
    professor VARCHAR(255) NOT NULL,
    category ENUM('CORE_TECH', 'ELEC_TECH', 'POLICY', 'MANAGEMENT', 'HEALTH') NOT NULL,
    PRIMARY KEY (course_no)
    );
