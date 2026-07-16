print("="*25)
print("Hospital Appointment Booking System")
print("="*25)

name = input("Enter patient name: ")
age = input("Enter patient age: ")
print("\nDoctors who have appointments today:\n1. Dr Tanya Williams\n2. Dr Arshad\n3. Dr Krishnan\n")
doctor = input("Enter name of doctor: ")
print(f"Patient {name} registered successfully")

def validate_patient_data(patient_name, age, phone):
    """Validate patient registration data"""
    if len(patient_name) < 2:
        return False, "Name too short"
    if age < 0 or age > 120:
        return False, "Invalid age"
    if len(str(phone)) != 10:
        return False, "Invalid phone number"
    return True, "Validation successful"