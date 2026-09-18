class Child:
  def __init__(name,age):
      name = name
      age = age

  def celebrate_birthday():
      age = age + 1
      return "Свядкуе день народження"


class Hobby:
    def __init__(self,hobby,hours):
        self.hobby = hobby
        self.hours = hours


    def practice(self):
        return "урок" + hooby


class Pupil(Child, Hobby):
    def __init__( name, age, hobby, phours, school_grade):
        super().__init__(name, age)
        school_grade = school_grade

    def study():
        return f"Учень {name} навчається у {school_grade} класі"


student = Pupil("Марійка", 10, "Малювання", 4, "5-А")

print(student.study())
print(student.celebrate_birthday())
print(student.practice())