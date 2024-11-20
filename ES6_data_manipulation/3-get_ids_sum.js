/*eslint-disable*/
export default function getStudentIdsum(students) {
  return students.reduce((acc, student) => acc + student.id, 0);
}
