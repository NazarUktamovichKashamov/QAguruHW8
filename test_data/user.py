import dataclasses


@dataclasses.dataclass
class User:
    name: str
    surname: str
    mail: str
    gender: str
    user_number: str
    date_of_birth: str
    subject: str
    hobbies: str
    photo: str
    address: str
    state: str
    city: str

    def __init__(self, first_name, last_name, email, gender, phone, birthday, subject, photo, hobbies, address, state,
                 city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.phone = phone
        self.birthday = birthday
        self.subject = subject
        self.photo = photo
        self.hobbies = hobbies
        self.address = address
        self.state = state
        self.city = city

