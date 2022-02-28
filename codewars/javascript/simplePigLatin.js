# https://www.codewars.com/kata/520b9d2ad5c005041100000f

function pigIt(str){
  return str.replace(/(\w)(\w*)(\s|$)/g, '$2$1ay$3');
}
