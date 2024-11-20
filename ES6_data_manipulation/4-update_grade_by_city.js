/*eslint-disable*/
export default function updateStudentGradeByCity(students, city, newGrade) {
  students.forEach((student) => {
    if (student.location === city) {
      student.grade = newGrade;
    }
  });
}
