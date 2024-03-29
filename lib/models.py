from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Table, Date
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import date

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)
# engine = create_engine('sqlite:///hospital.db')

# if __name__ == '__main__':
engine = create_engine('sqlite:///hospital.db')
Session = sessionmaker(bind=engine)
session = Session()

# Patient table
class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    contact_number = Column(String, nullable=False)

    # Relationship
    appointments = relationship("Appointment", backref=backref("patient"), cascade='all, delete-orphan')

    def __repr__(self):
        return f"{self.id}: {self.name}, DOB: {self.date_of_birth}, Gender: {self.gender}"
    
    #appointment filtering
    def get_upcoming_appointments(self):
        return [appointment for appointment in self.appointments if appointment.appointment_date >= date.today()]


# Medical staff table
class Staff(Base):
    __tablename__ = 'staffs'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    

    # Relationships
    appointments = relationship("Appointment", backref=backref("staff"), cascade='all, delete-orphan')

    def __repr__(self):
        return f"Name: {self.name}, Specialization: {self.specialization}"
    
    #Filter appointment
    def get_upcoming_appointments(self):
        return [appointment for appointment in self.appointments if appointment.appointment_date >= date.today()]

# Appointment table
class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    appointment_date = Column(Date, nullable=False)
    appointment_type= Column(String())

    # Relationship - Foreign keys
    patient_id = Column(Integer(), ForeignKey('patients.id'))
    staff_id = Column(Integer(), ForeignKey('staffs.id', name='fk_appointments_staff_id_staffs'), nullable=True)

    def __repr__(self):
        return f"Date of Appointment: {self.appointment_date}"
    
    #Staff details
    def staff_details(self):
        return f"Staff ID: {self.staff_id}, Staff Name: {self.staff.name}" if self.staff else "No Staff Assigned"
    
    #appointment details
    def appointment_details(self):
        return f"Appointment ID: {self.id}\n\tDate of Appointment: {self.appointment_date}\n\tType: {self.appointment_type}"

# engine = create_engine('sqlite:///hospital.db')




