//ES5 Global Constants to ES2015 Global Constants
const PI = 3.14;
PI = 42; //SyntaxError expected because const variables cannot be reassigned or redeclared

//Quiz
//What is the difference between var and let?
//  var works in function scope, can be reassigned, and can be redeclared wheereas let works in block scope, can be reassigned, but cannot be redeclared.
//  Variables made with var can be hoisted.
//What is the difference between var and const?
//  var works in function scope, can be reassigned, and can be redeclared wheereas const works in block scope, cannot be reassigned, and cannot be redeclared.
//  Variables made with var can be hoisted.
//What is the difference between let and const?
//  let works in block scope, can be reassigned, but cannot be redeclared whereas const works in block scope, cannot be reassigned, and cannot be redeclared.
//What is hoisting?
//  Certain variables are able to be accessed before they are declared in the code because of the way that JavaScript works.
//  These variable names are only able to used if they are assigned by var and they will have an undefined value until the variable is mentioned in the code.