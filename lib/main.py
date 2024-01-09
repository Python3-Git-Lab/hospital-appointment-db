import click
from models import Patient, Staff, Appointment, Base, create_engine, Session
from datetime import datetime

def add_patient():
    """Add a new patient."""
    name = input('Enter patient name: ')
    dob_str = input("Enter date of birth (YYYY-MM-DD): ")
    dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
    gender = input('Enter gender: ')
    contact = input('Enter contact number: ')

    new_patient = Patient(name=name, date_of_birth=dob, gender=gender, contact_number=contact)
    session.add(new_patient)
    session.commit()
    session.close()
    click.echo(f"Patient '{name}' added successfully.")

if __name__ == "__main__":
    DATABASE_URL = "sqlite:///hospital.db"

    # Create engine and session
    engine = create_engine(DATABASE_URL)
    Session.configure(bind=engine)
    session = Session()

    # Uncomment the line below if you want to clear the patients table before adding a new patient
    # session.query(Patient).delete()

    # Create the tables if they do not exist
    Base.metadata.create_all(bind=engine)

    add_patient()


# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# import click
# from models import Base, Patient, Appointment, Staff
# from datetime import datetime

# # def create_database(base):
# #     base.metadata.create_all(bind=engine)

# def add_patient():
#     """Add a new patient."""
#     name = input('Enter patient name: ')
#     dob_str = input("Enter date of birth (YYYY-MM-DD): ")
#     dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
#     gender = input('Enter gender: ')
#     contact = input('Enter contact number: ')

#     new_patient = Patient(name=name, date_of_birth=dob, gender=gender, contact_number=contact)
#     session.add(new_patient)
#     session.commit()
#     session.close()
#     click.echo(f"Patient '{name}' added successfully.")

# if __name__ == "__main__":
#     DATABASE_URL = "sqlite:///hospital.db"
#     engine = create_engine(DATABASE_URL)
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     session.query(Patient).delete()
#     add_patient()
