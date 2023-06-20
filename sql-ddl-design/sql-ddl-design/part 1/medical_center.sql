CREATE TABLE patients(
    id SERIAL PRIMARY KEY,
    patient_name VARCHAR NOT NULL,
    birthday DATE NOT NULL,
    insurance_name VARCHAR ,
    insurance_number INTEGER
);

CREATE TABLE doctors(
    id SERIAL PRIMARY KEY,
    doctor_name VARCHAR NOT NULL,
    specialty VARCHAR
);

CREATE TABLE diseases(
    id SERIAL PRIMARY KEY,
    disease_name VARCHAR NOT NULL,
    descript TEXT
);

CREATE TABLE visits(
    id SERIAL PRIMARY KEY,
    date_of_visit DATE NOT NULL,
    notes TEXT NOT NULL,
    doctor_id INT REFERENCES doctors(id),
    disease_id INT REFERENCES diseases(id)
);

CREATE TABLE diagnosis(
    id SERIAL PRIMARY KEY,
    doctor_notes TEXT,
    visit_id INT REFERENCES visits(id),
    disease_id INT REFERENCES diseases(id)
);