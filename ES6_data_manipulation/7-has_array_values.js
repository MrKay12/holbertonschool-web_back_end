/*eslint-disable*/
export default function hasArrayValues(array, values) {
  return values.every((value) => array.includes(value));
}
